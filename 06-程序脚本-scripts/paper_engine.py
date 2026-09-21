#!/usr/bin/env python3
"""Execute one autonomous paper-trading decision on the Binance demo account (virtual funds).

Never sends a production order: market data and orders use the demo host only."""

import argparse
import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from binance_readiness_check import HOSTS, check_demo_spot, get_json, load_config, update_readiness
from demo_orders import DemoOrderError, cancel_exit_oco, exit_status, market_order, place_exit_oco
from paper_ledger import PaperLedger, PaperLedgerError, atomic_json, decimal_value, floor_step

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "09-API密钥-仅本地" / "binance-api.env"


class PaperEngineError(ValueError):
    pass


def build_ledger():
    return PaperLedger(
        ROOT / "05-交易记录-data" / "current-state.json",
        ROOT / "04-运行状态-state" / "readiness.json",
        ROOT / "04-运行状态-state" / "paper-config.json",
        ROOT / "05-交易记录-data" / "paper-ledger.json",
    )


def load_decision(path):
    decision = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(decision, dict):
        raise PaperEngineError("Decision must be a JSON object")
    if decision.get("paper_trading_only") is not True:
        raise PaperEngineError("Decision must explicitly confirm paper_trading_only")
    action = decision.get("action")
    if action not in {"open_long", "manage", "close", "no_trade"}:
        raise PaperEngineError("Unsupported paper decision action")
    return decision


def fetch_snapshot(symbol, now):
    """Read current Spot rules and top-of-book from the demo host using public GET endpoints."""
    symbol = str(symbol).upper()
    base = HOSTS["demo"]
    rules_data, error = get_json(base + "/api/v3/exchangeInfo?symbol=" + symbol)
    symbols = rules_data.get("symbols") if isinstance(rules_data, dict) else None
    matches = [item for item in symbols if isinstance(item, dict) and item.get("symbol") == symbol] if isinstance(symbols, list) else []
    if not matches:
        raise PaperEngineError("No tradable paper rules for the selected symbol")
    quote_data, error = get_json(base + "/api/v3/ticker/bookTicker?symbol=" + symbol)
    if not isinstance(quote_data, dict) or quote_data.get("symbol") != symbol:
        raise PaperEngineError("No current paper quote for the selected symbol")
    try:
        bid = decimal_value(quote_data["bidPrice"], "bidPrice")
        ask = decimal_value(quote_data["askPrice"], "askPrice")
        bid_size = decimal_value(quote_data["bidQty"], "bidQty")
        ask_size = decimal_value(quote_data["askQty"], "askQty")
    except (KeyError, PaperLedgerError) as exc:
        raise PaperEngineError("Invalid paper quote shape") from exc
    if not (0 < bid <= ask and bid_size > 0 and ask_size > 0):
        raise PaperEngineError("Paper quote is not executable")
    rule = matches[0]
    filters = {item.get("filterType"): item for item in rule.get("filters", []) if isinstance(item, dict)}
    lot, notional = filters.get("LOT_SIZE", {}), filters.get("NOTIONAL", {})
    tick = filters.get("PRICE_FILTER", {}).get("tickSize")
    tradable = rule.get("status") == "TRADING" and rule.get("isSpotTradingAllowed") is True
    return {
        # Spot rules mapped onto the rule shape the ledger validates.
        "rules": {
            "symbol": symbol,
            "tradability": "BUY_SELL" if tradable else "NONE",
            "fractionable": True,
            "stepSize": lot.get("stepSize"),
            "minQty": lot.get("minQty"),
            "maxQty": filters.get("MARKET_LOT_SIZE", {}).get("maxQty") or lot.get("maxQty"),
            "minNotional": notional.get("minNotional"),
            "maxNotional": notional.get("maxNotional"),
            "tickSize": tick,
        },
        "quote": {
            "symbol": symbol,
            "bid": str(bid),
            "ask": str(ask),
            "bid_size": str(bid_size),
            "ask_size": str(ask_size),
            "received_at": now.isoformat(),
        },
    }


def prior_event(ledger, run_id):
    return next((event for event in ledger.ledger.get("events", []) if event.get("run_id") == run_id), None)


def decision_symbol(decision, ledger):
    if decision["action"] == "open_long":
        return str(decision.get("symbol", "")).upper()
    positions = ledger.state.get("positions", [])
    if positions:
        return positions[0]["symbol"]
    return str(decision.get("symbol", "BTCUSDT")).upper()


def execute(decision, run_id, now=None):
    now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    ledger = build_ledger()
    duplicate = prior_event(ledger, run_id)
    if duplicate:
        return {"status": "duplicate_skipped", "event": duplicate, "snapshot": None}

    symbol = decision_symbol(decision, ledger)
    if not symbol:
        raise PaperEngineError("A symbol is required")
    config = load_config(CONFIG)
    if config["BINANCE_ENV"] != "demo":
        raise PaperEngineError("BINANCE_ENV must be demo")
    readiness = check_demo_spot(config, symbol=symbol)
    update_readiness(readiness)
    if readiness.get("demo_market_access_verified") is not True:
        raise PaperEngineError("Fresh demo read verification failed")

    # The API check itself takes time; use a post-refresh timestamp for freshness validation.
    now = datetime.now(timezone.utc)
    ledger = build_ledger()
    ledger.validate_readiness(now)
    ledger.roll_day(now)
    snapshot = fetch_snapshot(symbol, now)
    action = decision["action"]
    # Without this readiness switch fills are simulated locally and nothing is sent to the demo account.
    demo = ledger.readiness.get("demo_order_execution_enabled") is True

    positions = ledger.state.get("positions", [])
    protection = positions[0].get("demo_exit_orders") if positions else None
    if demo and protection:
        # The exchange may have triggered the stop or target since the last check: book that first.
        done = exit_status(config, positions[0]["symbol"], protection)
        if done and done["fill"]:
            event = ledger.record_exit(done["fill"], done["reason"], now, run_id)
            if action != "open_long":
                return {"status": "exchange_exit_reconciled", "event": event, "snapshot": snapshot}
            protection = None
        elif done:
            ledger.set_protection(None, now)
            protection = None

    def executor(order_symbol, side, quantity):
        if side == "SELL" and protection:
            cancel_exit_oco(config, order_symbol, protection)
        return market_order(config, order_symbol, side, quantity)

    execute_order = executor if demo else None
    if action == "no_trade":
        return {"status": "no_trade", "event": None, "snapshot": snapshot}
    if action == "open_long":
        # Exchange trigger prices must sit on the symbol's price tick.
        tick = decimal_value(snapshot["rules"]["tickSize"], "tickSize")
        request = {
            "run_id": run_id,
            "symbol": symbol,
            "quote": snapshot["quote"],
            "rules": snapshot["rules"],
            "stop_price": str(floor_step(decimal_value(decision.get("stop_price"), "stop_price"), tick)),
            "target_price": str(floor_step(decimal_value(decision.get("target_price"), "target_price"), tick)),
            "thesis": decision.get("thesis", ""),
            "evidence": decision.get("evidence"),
        }
        event = ledger.open_long(request, now, execute_order)
        if demo:
            position = ledger.state["positions"][0]
            try:
                orders = place_exit_oco(config, symbol, position["quantity"], position["stop_price"], position["target_price"])
            except DemoOrderError:
                # Never hold a position the exchange is not protecting: leave at market straight away.
                later = datetime.now(timezone.utc)
                ledger.close({"run_id": run_id, "quote": fetch_snapshot(symbol, later)["quote"],
                              "reason": "protection_failed"}, later, execute_order)
                raise PaperEngineError("Exit orders could not be placed; the position was closed at market") from None
            ledger.set_protection(orders, datetime.now(timezone.utc), run_id)
    elif action == "manage":
        event = ledger.mark({"run_id": run_id, "quote": snapshot["quote"]}, now, evaluate=True, execute=execute_order)
    else:
        event = ledger.close({"run_id": run_id, "quote": snapshot["quote"],
                              "reason": decision.get("reason", "end_of_day")}, now, execute_order)
    return {"status": "executed", "event": event, "snapshot": snapshot}


def write_records(run_id, decision, result, now):
    ledger = build_ledger()
    local = now.astimezone(ZoneInfo(ledger.config["timezone"]))
    state = ledger.state
    event = result.get("event") or {}
    demo_order = event.get("demo_order")
    state["last_run"] = {
        "run_id": run_id,
        "timestamp": now.isoformat(),
        "mode": "autonomous_demo_paper",
        "demo_api_verified": True,
        "orders_placed": False,
        "demo_order_sent": bool(demo_order),
        "paper_action": decision["action"],
        "paper_result": result["status"],
    }
    state["next_task_focus"] = (
        "Refresh market evidence and reassess the demo paper position at the next scheduled check. "
        "Live trading remains disabled."
    )
    atomic_json(ROOT / "05-交易记录-data" / "current-state.json", state)
    evidence = {
        "run_id": run_id,
        "timestamp": now.isoformat(),
        "mode": "binance_demo_paper",
        "live_order_sent": False,
        "demo_order_sent": bool(demo_order),
        "decision": decision,
        "result": result,
        "state": {key: state.get(key) for key in ("cash_usdt", "equity_usdt", "positions", "daily_open_risk_usdt")},
    }
    atomic_json(ROOT / "05-交易记录-data" / "evidence" / (run_id + ".json"), evidence)
    journal_path = ROOT / "05-交易记录-data" / "journal" / (local.date().isoformat() + ".md")
    action = decision["action"]
    lines = [
        "", "## autonomous_paper_" + run_id + " - " + now.isoformat(), "",
        "- What was done: Autonomous local paper decision processed: " + action + ".",
        "- Why it was done: The user authorized autonomous paper-trading decisions within the documented risk limits.",
        "- Order proposed: " + ("Yes" if action == "open_long" else "No") + ".",
        "- Order placed: " + ("Demo account order " + demo_order["demo_order_id"] + " (virtual funds); no real order."
                              if demo_order else "No real order; local paper ledger only."),
        "- Order filled: " + ("Yes, on the demo account." if demo_order else "Yes, simulated locally." if event else "No."),
        "- Current holdings: " + json.dumps(state.get("positions", []), ensure_ascii=False) + ".",
        "- Current cash: " + str(state.get("cash_usdt")) + " USDT paper cash.",
        "- Current risk: " + str(state.get("daily_open_risk_usdt")) + " USDT open risk.",
        "- Evidence captured: `05-交易记录-data/evidence/" + run_id + ".json`.",
        "- Next task focus: Refresh read-only quote and reassess the paper position or no-trade state.",
        "- Human confirmations needed: None for demo paper trading; live trading remains disabled.",
    ]
    with journal_path.open("a", encoding="utf-8") as file:
        file.write("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--decision", required=True, type=Path, help="Non-secret JSON paper decision")
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    now = datetime.now(timezone.utc)
    try:
        decision = load_decision(args.decision)
        result = execute(decision, args.run_id, now)
        write_records(args.run_id, decision, result, now)
        print(json.dumps({"paper_trading": True, "live_order_sent": False, **result}, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, PaperLedgerError, PaperEngineError, DemoOrderError) as exc:
        print(json.dumps({"paper_trading": True, "live_order_sent": False,
                          "error": "Paper decision rejected; no production order was sent.",
                          "reason": str(exc)}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
