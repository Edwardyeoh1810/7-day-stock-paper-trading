#!/usr/bin/env python3
"""Deterministic local paper ledger for USDT-perpetual futures, long or short. This module has no
broker write path of its own; the engine may inject a demo-account executor so recorded fills
are the actual demo fills."""

import copy
import json
import os
import tempfile
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_DOWN
from pathlib import Path
from zoneinfo import ZoneInfo


class PaperLedgerError(ValueError):
    pass


def decimal_value(value, name):
    try:
        result = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError):
        raise PaperLedgerError("Invalid decimal: " + name) from None
    if not result.is_finite():
        raise PaperLedgerError("Non-finite decimal: " + name)
    return result


def json_number(value):
    rounded = value.quantize(Decimal("0.00000001"))
    return int(rounded) if rounded == rounded.to_integral() else float(rounded)


def floor_step(value, step):
    if step <= 0:
        raise PaperLedgerError("stepSize must be positive")
    return (value / step).to_integral_value(rounding=ROUND_DOWN) * step


def parse_time(value, name):
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        raise PaperLedgerError("Invalid timestamp: " + name) from None
    if parsed.tzinfo is None:
        raise PaperLedgerError("Timestamp must include timezone: " + name)
    return parsed.astimezone(timezone.utc)


def atomic_json(path, payload):
    temporary = None
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as file:
            temporary = Path(file.name)
            json.dump(payload, file, ensure_ascii=False, indent=2)
            file.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


class PaperLedger:
    def __init__(self, state_path, readiness_path, config_path, ledger_path):
        self.state_path = Path(state_path)
        self.readiness_path = Path(readiness_path)
        self.config_path = Path(config_path)
        self.ledger_path = Path(ledger_path)
        self.state = json.loads(self.state_path.read_text(encoding="utf-8"))
        self.readiness = json.loads(self.readiness_path.read_text(encoding="utf-8"))
        self.config = json.loads(self.config_path.read_text(encoding="utf-8"))
        self.ledger = json.loads(self.ledger_path.read_text(encoding="utf-8"))

    def validate_readiness(self, now=None):
        now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
        required = {
            "paper_trading_only": True,
            "live_trading_enabled": False,
            "broker_connected": True,
            "human_confirmation_required_for_live_orders": True,
            "binance_demo_api_read_access_verified": True,
            "local_paper_ledger_initialized": True,
            "autonomous_paper_execution_enabled": True,
            "orders_allowed": False,
        }
        for key, expected in required.items():
            if self.readiness.get(key) is not expected:
                raise PaperLedgerError("Unsafe or missing readiness field: " + key)
        check = self.readiness.get("binance_demo_api")
        if not isinstance(check, dict) or check.get("demo_market_access_verified") is not True:
            raise PaperLedgerError("Fresh Binance demo read verification is required")
        checked_at = parse_time(check.get("checked_at"), "readiness.checked_at")
        max_age = decimal_value(self.config["readiness_max_age_hours"], "readiness_max_age_hours")
        age_hours = Decimal(str((now - checked_at).total_seconds())) / Decimal("3600")
        if age_hours < 0 or age_hours > max_age:
            raise PaperLedgerError("Binance demo readiness is stale")
        for key in ("max_position_size_percent", "max_daily_loss_percent", "max_single_trade_loss_percent"):
            if key not in self.readiness:
                raise PaperLedgerError("Missing risk limit: " + key)

    def _zone(self):
        return ZoneInfo(self.config["timezone"])

    def roll_day(self, now):
        """Start a new local day: the daily loss counter resets and the experiment day index moves on."""
        today = now.astimezone(self._zone()).date().isoformat()
        dates = self.state.get("planned_trading_dates", [])
        if today not in dates or self.state.get("ledger_date") == today:
            return
        self.state["ledger_date"] = today
        self.state["trading_day_index"] = dates.index(today) + 1
        self.state["daily_realized_pnl_usdt"] = 0
        atomic_json(self.state_path, self.state)

    def _limits(self):
        capital = decimal_value(self.state["starting_capital_usdt"], "starting_capital_usdt")
        return {
            "capital": capital,
            "position": capital * decimal_value(self.readiness["max_position_size_percent"], "position percent") / 100,
            "daily": capital * decimal_value(self.readiness["max_daily_loss_percent"], "daily percent") / 100,
            "trade": capital * decimal_value(self.readiness["max_single_trade_loss_percent"], "trade percent") / 100,
        }

    def _assert_entry_window(self, now):
        local = now.astimezone(self._zone())
        if local.date().isoformat() not in self.state.get("planned_trading_dates", []):
            raise PaperLedgerError("Not a planned trading date")
        open_hour, open_minute = map(int, self.config["entry_window_open"].split(":"))
        cut_hour, cut_minute = map(int, self.config["entry_window_close"].split(":"))
        minute = local.hour * 60 + local.minute
        if not (open_hour * 60 + open_minute <= minute <= cut_hour * 60 + cut_minute):
            raise PaperLedgerError("New paper entries are outside the allowed window")

    def _validate_quote(self, symbol, quote, now, side):
        if not isinstance(quote, dict) or str(quote.get("symbol", "")).upper() != symbol:
            raise PaperLedgerError("Quote symbol mismatch")
        bid = decimal_value(quote.get("bid"), "bid")
        ask = decimal_value(quote.get("ask"), "ask")
        bid_size = decimal_value(quote.get("bid_size"), "bid_size")
        ask_size = decimal_value(quote.get("ask_size"), "ask_size")
        if not (0 < bid <= ask and bid_size > 0 and ask_size > 0):
            raise PaperLedgerError("Quote is not executable")
        mid = (bid + ask) / 2
        spread_bps = (ask - bid) / mid * 10000
        if spread_bps > decimal_value(self.config["max_spread_bps"], "max_spread_bps"):
            raise PaperLedgerError("Spread exceeds paper limit")
        received_at = parse_time(quote.get("received_at"), "quote.received_at")
        age = Decimal(str((now - received_at).total_seconds()))
        if age < Decimal("-2") or age > decimal_value(self.config["quote_max_age_seconds"], "quote_max_age_seconds"):
            raise PaperLedgerError("Quote is stale")
        return {
            "bid": bid,
            "ask": ask,
            "bid_size": bid_size,
            "ask_size": ask_size,
            "received_at": received_at.isoformat(),
            "executable_size": ask_size if side == "buy" else bid_size,
            "spread_bps": spread_bps,
        }

    def _validate_evidence(self, evidence):
        if not isinstance(evidence, list):
            raise PaperLedgerError("Evidence must be a list")
        categories = set()
        for item in evidence:
            if not isinstance(item, dict) or not item.get("category") or not item.get("source"):
                raise PaperLedgerError("Each evidence item needs category and source")
            categories.add(str(item["category"]).strip().lower())
        if len(categories) < int(self.config["minimum_evidence_categories"]):
            raise PaperLedgerError("At least two independent evidence categories are required")

    def _validate_rules(self, symbol, rules, side):
        if not isinstance(rules, dict) or str(rules.get("symbol", "")).upper() != symbol:
            raise PaperLedgerError("Trading rules symbol mismatch")
        allowed = {"BUY_SELL", "BUY"} if side == "buy" else {"BUY_SELL", "SELL"}
        if rules.get("tradability") not in allowed:
            raise PaperLedgerError("Symbol is not tradable for requested side")
        return {
            "step": decimal_value(rules.get("stepSize"), "stepSize"),
            "min_qty": decimal_value(rules.get("minQty") or "0", "minQty"),
            "max_qty": decimal_value(rules.get("maxQty") or "1E18", "maxQty"),
            "min_notional": decimal_value(rules.get("minNotional") or "0", "minNotional"),
            "max_notional": decimal_value(rules.get("maxNotional") or "1E18", "maxNotional"),
        }

    def _cost_rates(self):
        return (
            decimal_value(self.config["fee_bps_per_side"], "fee_bps_per_side") / 10000,
            decimal_value(self.config["slippage_bps_per_side"], "slippage_bps_per_side") / 10000,
        )

    def _next_id(self, now):
        sequence = int(self.ledger.get("next_sequence", 1))
        self.ledger["next_sequence"] = sequence + 1
        return "PAPER-%s-%04d" % (now.astimezone(self._zone()).strftime("%Y%m%d"), sequence)

    def _unrealized(self, position, mark):
        """Futures accounting: cash is the wallet balance and a position contributes only its P&L."""
        quantity = decimal_value(position["quantity"], "position.quantity")
        direction = 1 if position["side"] == "long" else -1
        fee_rate, _ = self._cost_rates()
        gross = direction * (mark - decimal_value(position["entry_price"], "entry_price")) * quantity
        return gross - quantity * mark * fee_rate

    def _save_event(self, event):
        event["state_after"] = copy.deepcopy(self.state)
        self.ledger.setdefault("events", []).append(event)
        atomic_json(self.ledger_path, self.ledger)
        atomic_json(self.state_path, self.state)

    def open_position(self, request, now=None, execute=None):
        now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
        self.validate_readiness(now)
        self._assert_entry_window(now)
        if self.state.get("positions"):
            raise PaperLedgerError("Only one active paper position is allowed")
        symbol = str(request.get("symbol", "")).upper()
        if symbol not in self.state.get("watchlist", []):
            raise PaperLedgerError("Symbol is outside the approved watchlist")
        side = request.get("side")
        if side not in {"long", "short"}:
            raise PaperLedgerError("Position side must be long or short")
        direction = 1 if side == "long" else -1
        order_side = "buy" if side == "long" else "sell"
        self._validate_evidence(request.get("evidence"))
        quote = self._validate_quote(symbol, request.get("quote"), now, order_side)
        rules = self._validate_rules(symbol, request.get("rules"), order_side)
        stop = decimal_value(request.get("stop_price"), "stop_price")
        target = decimal_value(request.get("target_price"), "target_price")
        fee_rate, slip_rate = self._cost_rates()
        # A long buys the ask and exits lower on a stop; a short sells the bid and exits higher.
        entry = (quote["ask"] if side == "long" else quote["bid"]) * (1 + direction * slip_rate)
        stop_fill = stop * (1 - direction * slip_rate)
        target_fill = target * (1 - direction * slip_rate)
        if not (stop > 0 and target > 0 and direction * (entry - stop) > 0 and direction * (target - entry) > 0):
            raise PaperLedgerError("Stop and target are on the wrong sides of the entry")
        if abs(entry - stop) / entry * 100 > decimal_value(self.config["max_stop_distance_percent"], "max_stop_distance_percent"):
            raise PaperLedgerError("Stop is too far from the entry for the configured leverage")
        loss_per_unit = direction * (entry - stop_fill) + (entry + stop_fill) * fee_rate
        reward_per_unit = direction * (target_fill - entry) - (entry + target_fill) * fee_rate
        if loss_per_unit <= 0 or reward_per_unit / loss_per_unit < decimal_value(
                self.config["minimum_reward_risk"], "minimum_reward_risk"):
            raise PaperLedgerError("Net reward/risk is below the configured minimum")
        limits = self._limits()
        cash = decimal_value(self.state["cash_usdt"], "cash_usdt")
        leverage = decimal_value(self.config["leverage"], "leverage")
        daily_loss = max(Decimal("0"), -decimal_value(self.state.get("daily_realized_pnl_usdt", 0), "daily pnl"))
        remaining_daily = limits["daily"] - daily_loss
        if remaining_daily <= 0:
            raise PaperLedgerError("Daily loss limit has been reached")
        quantity = min(
            limits["position"] / entry,
            limits["trade"] / loss_per_unit,
            remaining_daily / loss_per_unit,
            cash / (entry * (1 / leverage + fee_rate)),
            rules["max_qty"],
            rules["max_notional"] / entry,
        )
        if execute is None:
            # A simulated fill must not exceed the quoted size; a demo order reports its real fill.
            quantity = min(quantity, quote["executable_size"])
        quantity = floor_step(quantity, rules["step"])
        notional = quantity * entry
        entry_fee = notional * fee_rate
        planned_loss = quantity * loss_per_unit
        if quantity <= 0 or quantity < rules["min_qty"] or notional < rules["min_notional"]:
            raise PaperLedgerError("Rounded paper quantity does not meet exchange limits")
        if notional > limits["position"] or planned_loss > limits["trade"]:
            raise PaperLedgerError("Paper order exceeds a risk limit")
        if notional / leverage + entry_fee > cash:
            raise PaperLedgerError("Insufficient paper margin")
        local_date = now.astimezone(self._zone()).date().isoformat()
        recent_closes = [event for event in self.ledger.get("events", [])
                         if event.get("action") == "close" and event.get("trading_date") == local_date]
        if len(recent_closes) >= 2 and all(event.get("reason") == "stop" for event in recent_closes[-2:]):
            raise PaperLedgerError("Two consecutive stops block new entries")
        fill = None
        if execute is not None:
            # Every check has passed; from here the demo account's actual fill is authoritative.
            fill = execute(symbol, "BUY" if side == "long" else "SELL", quantity, False)
            quantity = decimal_value(fill["executed_qty"], "fill.executed_qty")
            entry = decimal_value(fill["avg_price"], "fill.avg_price")
            entry_fee = decimal_value(fill["fee_usdt"], "fill.fee_usdt")
            notional = quantity * entry
            planned_loss = quantity * (direction * (entry - stop_fill) + stop_fill * fee_rate) + entry_fee
        order_id = self._next_id(now)
        mark = quote["bid"] if side == "long" else quote["ask"]
        position = {
            "symbol": symbol,
            "side": side,
            "quantity": str(quantity),
            "entry_price": str(entry),
            "mark_price": str(mark),
            "stop_price": str(stop),
            "target_price": str(target),
            "entry_time": now.isoformat(),
            "notional_usdt": str(notional),
            "leverage": str(leverage),
            "margin_usdt": str(notional / leverage),
            "entry_fee_usdt": str(entry_fee),
            "planned_loss_usdt": str(planned_loss),
            "thesis": str(request.get("thesis", "")).strip(),
            "evidence": copy.deepcopy(request["evidence"]),
            "order_id": order_id,
        }
        unrealized = self._unrealized(position, mark)
        self.state["cash_usdt"] = json_number(cash - entry_fee)
        self.state["positions"] = [position]
        self.state["open_orders"] = []
        self.state["equity_usdt"] = json_number(cash - entry_fee + unrealized)
        self.state["unrealized_pnl_usdt"] = json_number(unrealized)
        self.state["daily_open_risk_usdt"] = json_number(planned_loss)
        self.state["paper_fees_paid_usdt"] = json_number(
            decimal_value(self.state.get("paper_fees_paid_usdt", 0), "fees") + entry_fee)
        event = {
            "event_id": order_id + "-OPEN",
            "order_id": order_id,
            "action": "open_" + side,
            "trading_date": local_date,
            "timestamp": now.isoformat(),
            "symbol": symbol,
            "quantity": str(quantity),
            "fill_price": str(entry),
            "fee_usdt": str(entry_fee),
            "planned_loss_usdt": str(planned_loss),
            "quote": request["quote"],
            "reason": "strategy_entry",
        }
        if fill is not None:
            event["demo_order"] = fill
        if request.get("run_id"):
            event["run_id"] = str(request["run_id"])
        self._save_event(event)
        return event

    def mark(self, request, now=None, evaluate=False, execute=None):
        now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
        self.validate_readiness(now)
        positions = self.state.get("positions", [])
        if len(positions) != 1:
            raise PaperLedgerError("Exactly one active paper position is required")
        position = positions[0]
        symbol = position["symbol"]
        direction = 1 if position["side"] == "long" else -1
        quote = self._validate_quote(symbol, request.get("quote"), now, "sell" if direction == 1 else "buy")
        mark = quote["bid"] if direction == 1 else quote["ask"]
        position["mark_price"] = str(mark)
        quantity = decimal_value(position["quantity"], "quantity")
        stop = decimal_value(position["stop_price"], "stop")
        fee_rate, slip_rate = self._cost_rates()
        stop_exit = stop * (1 - direction * slip_rate)
        entry = decimal_value(position["entry_price"], "entry_price")
        open_risk = max(Decimal("0"), quantity * (direction * (entry - stop_exit) + stop_exit * fee_rate))
        unrealized = self._unrealized(position, mark)
        self.state["equity_usdt"] = json_number(decimal_value(self.state["cash_usdt"], "cash_usdt") + unrealized)
        self.state["unrealized_pnl_usdt"] = json_number(unrealized)
        self.state["daily_open_risk_usdt"] = json_number(open_risk)
        # Exit orders resting on the demo exchange own the stop and target; evaluating them here too
        # would race the exchange for the same position.
        protected = bool(position.get("demo_exit_orders"))
        if evaluate and not protected and direction * (mark - stop) <= 0:
            return self.close({"quote": request["quote"], "reason": "stop", "run_id": request.get("run_id")}, now, execute)
        if evaluate and not protected and direction * (mark - decimal_value(position["target_price"], "target")) >= 0:
            return self.close({"quote": request["quote"], "reason": "target", "run_id": request.get("run_id")}, now, execute)
        held_hours = Decimal(str((now - parse_time(position["entry_time"], "entry_time")).total_seconds())) / 3600
        if evaluate and held_hours >= decimal_value(self.config["max_hold_hours"], "max_hold_hours"):
            return self.close({"quote": request["quote"], "reason": "time_exit", "run_id": request.get("run_id")}, now, execute)
        event = {
            "event_id": self._next_id(now) + "-MARK",
            "action": "mark",
            "trading_date": now.astimezone(self._zone()).date().isoformat(),
            "timestamp": now.isoformat(),
            "symbol": symbol,
            "mark_price": str(mark),
            "quote": request["quote"],
            "reason": "risk_refresh",
        }
        if request.get("run_id"):
            event["run_id"] = str(request["run_id"])
        self._save_event(event)
        return event

    EXIT_REASONS = {"stop", "target", "thesis_invalid", "time_exit", "end_of_day", "manual_exit", "protection_failed"}

    def close(self, request, now=None, execute=None):
        now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
        self.validate_readiness(now)
        positions = self.state.get("positions", [])
        if len(positions) != 1:
            raise PaperLedgerError("Exactly one active paper position is required")
        position = positions[0]
        symbol = position["symbol"]
        direction = 1 if position["side"] == "long" else -1
        quote = self._validate_quote(symbol, request.get("quote"), now, "sell" if direction == 1 else "buy")
        quantity = decimal_value(position["quantity"], "quantity")
        fee_rate, slip_rate = self._cost_rates()
        fill = (quote["bid"] if direction == 1 else quote["ask"]) * (1 - direction * slip_rate)
        if execute is None and quote["executable_size"] < quantity:
            raise PaperLedgerError("Quoted size cannot support the paper exit")
        reason = str(request.get("reason", "manual_exit"))
        if reason not in self.EXIT_REASONS:
            raise PaperLedgerError("Unsupported paper exit reason")
        exit_fee = quantity * fill * fee_rate
        demo_fill = None
        if execute is not None:
            demo_fill = execute(symbol, "SELL" if direction == 1 else "BUY", quantity, True)
        return self._settle(position, fill, exit_fee, reason, now, request["quote"], demo_fill, request.get("run_id"))

    def record_exit(self, demo_fill, reason, now=None, run_id=None):
        """Book an exit the demo exchange already executed (a triggered stop or target order)."""
        now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
        positions = self.state.get("positions", [])
        if len(positions) != 1:
            raise PaperLedgerError("Exactly one active paper position is required")
        if reason not in self.EXIT_REASONS:
            raise PaperLedgerError("Unsupported paper exit reason")
        return self._settle(positions[0], None, None, reason, now, None, demo_fill, run_id)

    def set_protection(self, protection, now=None, run_id=None):
        """Remember (or, with None, forget) the exit orders resting on the demo exchange."""
        now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
        positions = self.state.get("positions", [])
        if len(positions) != 1:
            raise PaperLedgerError("Exactly one active paper position is required")
        if protection is None:
            positions[0].pop("demo_exit_orders", None)
        else:
            positions[0]["demo_exit_orders"] = protection
        event = {
            "event_id": self._next_id(now) + "-PROTECT",
            "action": "protect",
            "trading_date": now.astimezone(self._zone()).date().isoformat(),
            "timestamp": now.isoformat(),
            "symbol": positions[0]["symbol"],
            "demo_exit_orders": protection,
        }
        if run_id:
            event["run_id"] = str(run_id)
        self._save_event(event)
        return event

    def _settle(self, position, fill, exit_fee, reason, now, quote, demo_fill, run_id):
        funding = Decimal("0")
        if demo_fill is not None:
            fill = decimal_value(demo_fill["avg_price"], "fill.avg_price")
            exit_fee = decimal_value(demo_fill["fee_usdt"], "fill.fee_usdt")
            funding = decimal_value(demo_fill.get("funding_usdt", 0), "fill.funding_usdt")
        symbol = position["symbol"]
        direction = 1 if position["side"] == "long" else -1
        quantity = decimal_value(position["quantity"], "quantity")
        gross = direction * (fill - decimal_value(position["entry_price"], "entry_price")) * quantity
        # The entry fee left the wallet when the position opened; it still belongs to this trade's result.
        net_pnl = gross - exit_fee - decimal_value(position["entry_fee_usdt"], "entry_fee") + funding
        cash = decimal_value(self.state["cash_usdt"], "cash") + gross - exit_fee + funding
        self.state["cash_usdt"] = json_number(cash)
        self.state["equity_usdt"] = json_number(cash)
        self.state["realized_pnl_usdt"] = json_number(
            decimal_value(self.state.get("realized_pnl_usdt", 0), "realized pnl") + net_pnl)
        self.state["daily_realized_pnl_usdt"] = json_number(
            decimal_value(self.state.get("daily_realized_pnl_usdt", 0), "daily pnl") + net_pnl)
        self.state["unrealized_pnl_usdt"] = 0
        self.state["daily_open_risk_usdt"] = 0
        self.state["positions"] = []
        self.state["open_orders"] = []
        self.state["paper_fees_paid_usdt"] = json_number(
            decimal_value(self.state.get("paper_fees_paid_usdt", 0), "fees") + exit_fee)
        order_id = self._next_id(now)
        event = {
            "event_id": order_id + "-CLOSE",
            "order_id": order_id,
            "action": "close",
            "trading_date": now.astimezone(self._zone()).date().isoformat(),
            "timestamp": now.isoformat(),
            "symbol": symbol,
            "side": position["side"],
            "quantity": str(quantity),
            "fill_price": str(fill),
            "fee_usdt": str(exit_fee),
            "funding_usdt": str(funding),
            "net_pnl_usdt": str(net_pnl),
            "quote": quote,
            "reason": reason,
        }
        if demo_fill is not None:
            event["demo_order"] = demo_fill
        if run_id:
            event["run_id"] = str(run_id)
        self._save_event(event)
        return event

    def reconcile(self):
        events = self.ledger.get("events", [])
        if not events or "state_after" not in events[-1]:
            raise PaperLedgerError("No paper event snapshot is available for reconciliation")
        self.state = copy.deepcopy(events[-1]["state_after"])
        atomic_json(self.state_path, self.state)
        return self.state
