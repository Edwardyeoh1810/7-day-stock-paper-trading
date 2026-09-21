import json
import sys
import tempfile
import unittest
from contextlib import ExitStack
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from unittest.mock import patch
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "06-程序脚本-scripts"))

from demo_orders import DemoOrderError
from paper_engine import PaperEngineError, execute, fetch_snapshot, load_decision
from paper_ledger import PaperLedger


class PaperEngineTests(unittest.TestCase):
    SYMBOL = {"symbol": "BTCUSDT", "status": "TRADING", "contractType": "PERPETUAL", "filters": [
        {"filterType": "LOT_SIZE", "stepSize": "0.001", "minQty": "0.001", "maxQty": "1000"},
        {"filterType": "MARKET_LOT_SIZE", "stepSize": "0.0001", "minQty": "0.0001", "maxQty": "120"},
        {"filterType": "MIN_NOTIONAL", "notional": "50"},
        {"filterType": "PRICE_FILTER", "tickSize": "0.10"}]}

    def test_fetch_snapshot_rejects_missing_sizes(self):
        # The quote endpoint supplies sizes; a paper fill must not invent them.
        responses = iter((
            ({"symbols": [self.SYMBOL]}, None),
            ({"symbol": "BTCUSDT", "bidPrice": "100", "askPrice": "100.01"}, None),
        ))
        with patch("paper_engine.get_json", side_effect=lambda *args: next(responses)):
            with self.assertRaises(PaperEngineError):
                fetch_snapshot("BTCUSDT", datetime.now(timezone.utc))

    def test_fetch_snapshot_maps_futures_filters_and_uses_demo_host_without_key(self):
        responses = iter((
            ({"symbols": [self.SYMBOL]}, None),
            ({"symbol": "BTCUSDT", "bidPrice": "100", "bidQty": "2", "askPrice": "100.01", "askQty": "3"}, None),
        ))
        with patch("paper_engine.get_json", side_effect=lambda *args: next(responses)) as request:
            snapshot = fetch_snapshot("BTCUSDT", datetime.now(timezone.utc))
        self.assertEqual(snapshot["rules"], {
            "symbol": "BTCUSDT", "tradability": "BUY_SELL", "stepSize": "0.0001", "minQty": "0.0001",
            "maxQty": "120", "minNotional": "50", "maxNotional": None, "tickSize": "0.10"})
        self.assertEqual(snapshot["quote"]["ask_size"], "3")
        for call in request.call_args_list:
            self.assertTrue(call.args[0].startswith("https://demo-fapi.binance.com/fapi/v1/"))
            self.assertEqual(len(call.args), 1)

    def test_open_decision_requires_paper_mode(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "decision.json"
            path.write_text('{"action":"open_long"}', encoding="utf-8")
            with self.assertRaises(PaperEngineError):
                load_decision(path)


class ProtectionFlowTests(unittest.TestCase):
    """execute() with every network call replaced: what reaches the demo order functions, and when."""

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        now = datetime.now(timezone.utc)
        local = now.astimezone(ZoneInfo("Asia/Kuala_Lumpur"))
        files = {
            "state.json": {"planned_trading_dates": [local.date().isoformat()], "starting_capital_usdt": 5000,
                           "cash_usdt": 5000, "equity_usdt": 5000, "realized_pnl_usdt": 0, "unrealized_pnl_usdt": 0,
                           "daily_realized_pnl_usdt": 0, "daily_open_risk_usdt": 0, "positions": [], "open_orders": [],
                           "watchlist": ["BTCUSDT"]},
            "readiness.json": {"paper_trading_only": True, "live_trading_enabled": False, "broker_connected": True,
                               "human_confirmation_required_for_live_orders": True,
                               "binance_demo_api_read_access_verified": True, "local_paper_ledger_initialized": True,
                               "autonomous_paper_execution_enabled": True, "orders_allowed": False,
                               "demo_order_execution_enabled": True, "max_position_size_percent": 50,
                               "max_daily_loss_percent": 2, "max_single_trade_loss_percent": 0.5,
                               "binance_demo_api": {"checked_at": now.isoformat(), "demo_market_access_verified": True}},
            "config.json": {"fee_bps_per_side": "10", "slippage_bps_per_side": "2", "max_spread_bps": "25",
                            "quote_max_age_seconds": "10", "readiness_max_age_hours": "24",
                            "minimum_evidence_categories": 2, "minimum_reward_risk": "1.5",
                            "timezone": "Asia/Kuala_Lumpur", "entry_window_open": "00:00",
                            "entry_window_close": "23:59", "max_hold_hours": "24", "leverage": "5",
                            "decision_max_age_minutes": "45",
                            "max_stop_distance_percent": "10"},
            "ledger.json": {"version": 1, "next_sequence": 1, "events": []},
        }
        for name, payload in files.items():
            (root / name).write_text(json.dumps(payload), encoding="utf-8")
        self.build = lambda: PaperLedger(root / "state.json", root / "readiness.json", root / "config.json", root / "ledger.json")
        self.slot = local.strftime("%Y-%m-%d_check_%H%M_paper")
        self.calls = []
        self.exit_result = None
        self.oco_fails = False
        self.decision = {"paper_trading_only": True, "action": "open_long", "symbol": "BTCUSDT",
                         "stop_price": "78000.004", "target_price": "90000.009", "thesis": "test",
                         "evidence": [{"category": "price_action", "source": "a"}, {"category": "market_context", "source": "b"}]}

    def snapshot(self, symbol, now):
        return {"rules": {"symbol": symbol, "tradability": "BUY_SELL", "stepSize": "0.0001", "minQty": "0.0001",
                          "maxQty": "120", "minNotional": "50", "maxNotional": None, "tickSize": "0.10"},
                "quote": {"symbol": symbol, "bid": "81999.99", "ask": "82000", "bid_size": "5", "ask_size": "5",
                          "received_at": datetime.now(timezone.utc).isoformat()}}

    def market(self, config, symbol, side, quantity, reduce_only=False):
        self.calls.append(("market", side, reduce_only))
        quantity = Decimal(str(quantity))
        return {"demo_order_id": "1", "side": side, "executed_qty": str(quantity), "avg_price": "82000",
                "gross_usdt": str(quantity * Decimal("82000")), "fee_usdt": "0.5"}

    def oco(self, config, symbol, side, quantity, stop, target):
        self.calls.append(("exits", side, float(stop), float(target)))
        if self.oco_fails:
            raise DemoOrderError("rejected")
        return {"stop_algo_id": "21", "target_algo_id": "22"}

    def run_engine(self, decision, run_id):
        patches = {"build_ledger": self.build, "load_config": lambda path: {"BINANCE_ENV": "demo"},
                   "check_demo_futures": lambda config, symbol: {"demo_market_access_verified": True},
                   "update_readiness": lambda result: None, "fetch_snapshot": self.snapshot,
                   "market_order": self.market, "place_exit_orders": self.oco,
                   "prepare_symbol": lambda config, symbol, leverage: self.calls.append(("prepare", str(leverage))),
                   "funding_since": lambda config, symbol, start_ms: "-0.2",
                   "cancel_exit_orders": lambda config, symbol, protection: self.calls.append(("cancel", protection["stop_algo_id"])),
                   "exit_status": lambda config, symbol, side, protection: self.exit_result}
        with ExitStack() as stack:
            for name, replacement in patches.items():
                stack.enter_context(patch("paper_engine." + name, replacement))
            return execute(decision, run_id)

    def test_entry_is_protected_on_the_exchange_with_tick_rounded_prices(self):
        self.run_engine(self.decision, self.slot)
        self.assertEqual(self.calls, [("prepare", "5"), ("market", "BUY", False), ("exits", "long", 78000.0, 90000.0)])
        position = self.build().state["positions"][0]
        self.assertEqual(position["demo_exit_orders"]["stop_algo_id"], "21")
        # 50% position cap, but the 25 USDT risk budget is the binding limit with a ~4.9% stop.
        self.assertLessEqual(Decimal(position["planned_loss_usdt"]), Decimal("25.6"))
        self.assertLessEqual(Decimal(position["notional_usdt"]), Decimal("2500"))

    def test_short_entry_sells_first_and_buys_back_reduce_only(self):
        decision = {**self.decision, "action": "open_short", "stop_price": "86000", "target_price": "74000"}
        self.run_engine(decision, self.slot)
        self.assertEqual(self.calls[1:], [("market", "SELL", False), ("exits", "short", 86000.0, 74000.0)])
        self.calls.clear()
        result = self.run_engine({"paper_trading_only": True, "action": "close", "reason": "manual_exit"}, "r2")
        self.assertEqual(self.calls, [("cancel", "21"), ("market", "BUY", True)])
        self.assertEqual(result["event"]["funding_usdt"], "-0.2")

    def test_stale_or_unscheduled_entries_are_rejected_before_any_order(self):
        old = (datetime.now(timezone.utc).astimezone(ZoneInfo("Asia/Kuala_Lumpur")) - timedelta(minutes=46))
        for run_id in (old.strftime("%Y-%m-%d_check_%H%M_paper"), "2026-09-21_check_1200_paper", "manual_entry"):
            with self.assertRaisesRegex(PaperEngineError, "stale|scheduled check"):
                self.run_engine(self.decision, run_id)
        self.assertEqual(self.calls, [])
        self.assertEqual(self.build().state["positions"], [])

    def test_late_runs_may_still_manage_and_close(self):
        self.run_engine(self.decision, self.slot)
        self.calls.clear()
        self.assertEqual(self.run_engine({"paper_trading_only": True, "action": "manage"}, "2026-09-21_check_1200_paper")["status"], "executed")
        result = self.run_engine({"paper_trading_only": True, "action": "close", "reason": "manual_exit"}, "2026-09-21_check_1600_paper")
        self.assertEqual(self.calls[-1], ("market", "SELL", True))
        self.assertEqual(result["event"]["reason"], "manual_exit")

    def test_unprotectable_entry_is_closed_immediately(self):
        self.oco_fails = True
        with self.assertRaises(PaperEngineError):
            self.run_engine(self.decision, self.slot)
        self.assertEqual([call[0] for call in self.calls], ["prepare", "market", "exits", "market"])
        self.assertEqual(self.calls[-1], ("market", "SELL", True))
        ledger = self.build()
        self.assertEqual(ledger.state["positions"], [])
        self.assertEqual(ledger.ledger["events"][-1]["reason"], "protection_failed")

    def test_exchange_stop_is_booked_and_manual_close_cancels_exit_orders_first(self):
        self.run_engine(self.decision, self.slot)
        self.calls.clear()
        result = self.run_engine({"paper_trading_only": True, "action": "close", "reason": "thesis_invalid"}, "r2")
        self.assertEqual(self.calls, [("cancel", "21"), ("market", "SELL", True)])
        self.assertEqual(result["event"]["reason"], "thesis_invalid")
        self.run_engine(self.decision, self.slot + "_again")
        self.calls.clear()
        self.exit_result = {"reason": "stop", "fill": self.market(None, "BTCUSDT", "SELL", "0.006", True)}
        self.calls.clear()
        result = self.run_engine({"paper_trading_only": True, "action": "manage"}, "r4")
        self.assertEqual((result["status"], result["event"]["reason"], self.calls), ("exchange_exit_reconciled", "stop", []))
        self.assertEqual(self.build().state["positions"], [])


if __name__ == "__main__":
    unittest.main()
