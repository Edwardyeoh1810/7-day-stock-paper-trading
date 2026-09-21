#!/usr/bin/env python3
"""Deterministic statistics for the review process, computed from the paper ledger. Read-only
apart from writing 05-交易记录-data/reviews/stats.json; it never contacts Binance."""

import json
from collections import Counter
from datetime import datetime
from zoneinfo import ZoneInfo
from decimal import Decimal
from pathlib import Path

from paper_ledger import atomic_json

ROOT = Path(__file__).resolve().parents[1]


def closed_trades(events):
    """Pair every close with the entry before it; the ledger holds one position at a time."""
    trades, entry = [], None
    for event in events:
        if event.get("action") in {"open_long", "open_short"}:
            entry = event
        elif event.get("action") == "close" and entry is not None:
            position = entry["state_after"]["positions"][0]
            pnl = Decimal(event["net_pnl_usdt"])
            planned = Decimal(entry["planned_loss_usdt"])
            held = datetime.fromisoformat(event["timestamp"]) - datetime.fromisoformat(entry["timestamp"])
            trades.append({
                "symbol": entry["symbol"],
                "side": position.get("side", "long"),
                "opened": entry["timestamp"],
                "closed": event["timestamp"],
                "hours_held": round(held.total_seconds() / 3600, 2),
                "exit_reason": event.get("reason"),
                "net_pnl_usdt": float(pnl),
                # R = result measured in units of the loss that was planned at entry.
                "r_multiple": round(float(pnl / planned), 3) if planned > 0 else None,
                "fees_usdt": float(Decimal(entry["fee_usdt"]) + Decimal(event["fee_usdt"])),
                "funding_usdt": float(Decimal(event.get("funding_usdt", "0"))),
                "evidence_categories": sorted({str(item["category"]).strip().lower() for item in position.get("evidence", [])}),
                "thesis": position.get("thesis", ""),
            })
            entry = None
    return trades


def summarize(trades):
    if not trades:
        return {"trades": 0}
    pnls = [trade["net_pnl_usdt"] for trade in trades]
    wins = [pnl for pnl in pnls if pnl > 0]
    losses = [pnl for pnl in pnls if pnl <= 0]
    multiples = [trade["r_multiple"] for trade in trades if trade["r_multiple"] is not None]
    peak = running = drawdown = 0.0
    for pnl in pnls:
        running += pnl
        peak = max(peak, running)
        drawdown = max(drawdown, peak - running)
    return {
        "trades": len(trades),
        "win_rate_percent": round(100 * len(wins) / len(trades), 1),
        "net_pnl_usdt": round(sum(pnls), 4),
        "average_win_usdt": round(sum(wins) / len(wins), 4) if wins else None,
        "average_loss_usdt": round(sum(losses) / len(losses), 4) if losses else None,
        "average_r": round(sum(multiples) / len(multiples), 3) if multiples else None,
        "max_drawdown_usdt": round(drawdown, 4),
        "fees_usdt": round(sum(trade["fees_usdt"] for trade in trades), 4),
        "funding_usdt": round(sum(trade["funding_usdt"] for trade in trades), 4),
    }


def grouped(trades, key):
    groups = {}
    for trade in trades:
        values = trade[key] if isinstance(trade[key], list) else [trade[key]]
        for value in values:
            groups.setdefault(str(value), []).append(trade)
    return {name: summarize(members) for name, members in sorted(groups.items())}


def slot_coverage(schedule, decision_dir, now):
    """Slots that were due so far against slots that have a recorded decision (proposal P-002)."""
    zone = ZoneInfo(schedule["timezone"])
    start = datetime.fromisoformat(schedule["coverage_from"])
    due = []
    for day in schedule["planned_trading_dates"]:
        for task in schedule["tasks"]:
            when = datetime.fromisoformat(day + "T" + task["time"]).replace(tzinfo=zone)
            if start <= when <= now:
                due.append(day + "_" + task["id"])
    decided = {slot for slot in due if any(decision_dir.glob(slot + "*.json"))}
    return {"slots_due": len(due), "slots_decided": len(decided),
            "coverage_percent": round(100 * len(decided) / len(due), 1) if due else None,
            "missed_slots": [slot for slot in due if slot not in decided]}


def build_report(ledger, state, decision_dir, schedule=None, now=None):
    trades = closed_trades(ledger.get("events", []))
    decisions = Counter()
    for path in sorted(decision_dir.glob("*.json")):
        try:
            decisions[str(json.loads(path.read_text(encoding="utf-8")).get("action"))] += 1
        except (OSError, ValueError):
            decisions["unreadable"] += 1
    return {
        "generated_at": datetime.now().astimezone().isoformat(),
        "sample_warning": "Fewer than 30 closed trades: treat every pattern as a hypothesis, not a finding." if len(trades) < 30 else None,
        "account": {key: state.get(key) for key in ("starting_capital_usdt", "cash_usdt", "equity_usdt", "realized_pnl_usdt",
                                                     "trading_day_index", "positions")},
        "decisions_by_action": dict(decisions),
        "slot_coverage": slot_coverage(schedule, decision_dir, now or datetime.now().astimezone()) if schedule else None,
        "overall": summarize(trades),
        "by_symbol": grouped(trades, "symbol"),
        "by_side": grouped(trades, "side"),
        "by_exit_reason": grouped(trades, "exit_reason"),
        "by_evidence_category": grouped(trades, "evidence_categories"),
        "trades": trades,
    }


def main():
    data = ROOT / "05-交易记录-data"
    report = build_report(json.loads((data / "paper-ledger.json").read_text(encoding="utf-8")),
                          json.loads((data / "current-state.json").read_text(encoding="utf-8")), data / "decisions",
                          json.loads((ROOT / "03-定时任务-routines" / "schedule.json").read_text(encoding="utf-8")))
    atomic_json(data / "reviews" / "stats.json", report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
