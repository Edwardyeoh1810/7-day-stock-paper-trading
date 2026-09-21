import json
import sys
import tempfile
import unittest
from contextlib import ExitStack
from datetime import datetime, timezone
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
    SYMBOL = {"symbol": "BTCUSDT", "status": "TRADING", "isSpotTradingAllowed": True, "filters": [
        {"filterType": "LOT_SIZE", "stepSize": "0.00001", "minQty": "0.00001", "maxQty": "9000"},
        {"filterType": "MARKET_LOT_SIZE", "stepSize": "0", "minQty": "0", "maxQty": "100"},
        {"filterType": "NOTIONAL", "minNotional": "5", "maxNotional": "9000000"},
        {"filterType": "PRICE_FILTER", "tickSize": "0.01"}]}

    def test_fetch_snapshot_rejects_missing_sizes(self):
        # The quote endpoint supplies sizes; a paper fill must not invent them.
        responses = iter((
            ({"symbols": [self.SYMBOL]}, None),
            ({"symbol": "BTCUSDT", "bidPrice": "100", "askPrice": "100.01"}, None),
        ))
        with patch("paper_engine.get_json", side_effect=lambda *args: next(responses)):
            with self.assertRaises(PaperEngineError):
                fetch_snapshot("BTCUSDT", datetime.now(timezone.utc))

    def test_fetch_snapshot_maps_spot_filters_and_uses_demo_host_without_key(self):
        responses = iter((
            ({"symbols": [self.SYMBOL]}, None),
            ({"symbol": "BTCUSDT", "bidPrice": "100", "bidQty": "2", "askPrice": "100.01", "askQty": "3"}, None),
        ))
        with patch("paper_engine.get_json", side_effect=lambda *args: next(responses)) as request:
            snapshot = fetch_snapshot("BTCUSDT", datetime.now(timezone.utc))
        self.assertEqual(snapshot["rules"], {
            "symbol": "BTCUSDT", "tradability": "BUY_SELL", "fractionable": True, "stepSize": "0.00001",
            "minQty": "0.00001", "maxQty": "100", "minNotional": "5", "maxNotional": "9000000", "tickSize": "0.01"})
        self.assertEqual(snapshot["quote"]["ask_size"], "3")
        for call in request.call_args_list:
            self.assertTrue(call.args[0].startswith("https://demo-api.binance.com/api/v3/"))
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
                               "demo_order_execution_enabled": True, "max_position_size_percent": 10,
                               "max_daily_loss_percent": 2, "max_single_trade_loss_percent": 0.5,
                               "binance_demo_api": {"checked_at": now.isoformat(), "demo_market_access_verified": True}},
            "config.json": {"fee_bps_per_side": "10", "slippage_bps_per_side": "2", "max_spread_bps": "25",
                            "quote_max_age_seconds": "10", "readiness_max_age_hours": "24",
                            "minimum_evidence_categories": 2, "minimum_reward_risk": "1.5",
                            "timezone": "Asia/Kuala_Lumpur", "entry_window_open": "00:00",
                            "entry_window_close": "23:59", "max_hold_hours": "24"},
            "ledger.json": {"version": 1, "next_sequence": 1, "events": []},
        }
        for name, payload in files.items():
            (root / name).write_text(json.dumps(payload), encoding="utf-8")
        self.build = lambda: PaperLedger(root / "state.json", root / "readiness.json", root / "config.json", root / "ledger.json")
        self.calls = []
        self.exit_result = None
        self.oco_fails = False
        self.decision = {"paper_trading_only": True, "action": "open_long", "symbol": "BTCUSDT",
                         "stop_price": "78000.004", "target_price": "90000.009", "thesis": "test",
                         "evidence": [{"category": "price_action", "source": "a"}, {"category": "market_context", "source": "b"}]}

    def snapshot(self, symbol, now):
        return {"rules": {"symbol": symbol, "tradability": "BUY_SELL", "fractionable": True, "stepSize": "0.00001",
                          "minQty": "0.00001", "maxQty": "100", "minNotional": "5", "maxNotional": "9000000", "tickSize": "0.01"},
                "quote": {"symbol": symbol, "bid": "81999.99", "ask": "82000", "bid_size": "5", "ask_size": "5",
                          "received_at": datetime.now(timezone.utc).isoformat()}}

    def market(self, config, symbol, side, quantity):
        self.calls.append(("market", side))
        quantity = Decimal(str(quantity))
        gross = quantity * Decimal("82000")
        return {"demo_order_id": "1", "status": "FILLED", "side": side, "executed_qty": str(quantity), "net_qty": str(quantity),
                "avg_price": "82000", "gross_usdt": str(gross), "net_usdt": str(gross), "fee_usdt": "0"}

    def oco(self, config, symbol, quantity, stop, target):
        self.calls.append(("oco", str(stop), str(target)))
        if self.oco_fails:
            raise DemoOrderError("rejected")
        return {"order_list_id": "11", "stop_order_id": "21", "target_order_id": "22"}

    def run_engine(self, decision, run_id):
        patches = {"build_ledger": self.build, "load_config": lambda path: {"BINANCE_ENV": "demo"},
                   "check_demo_spot": lambda config, symbol: {"demo_market_access_verified": True},
                   "update_readiness": lambda result: None, "fetch_snapshot": self.snapshot,
                   "market_order": self.market, "place_exit_oco": self.oco,
                   "cancel_exit_oco": lambda config, symbol, protection: self.calls.append(("cancel", protection["order_list_id"])),
                   "exit_status": lambda config, symbol, protection: self.exit_result}
        with ExitStack() as stack:
            for name, replacement in patches.items():
                stack.enter_context(patch("paper_engine." + name, replacement))
            return execute(decision, run_id)

    def test_entry_is_protected_on_the_exchange_with_tick_rounded_prices(self):
        self.run_engine(self.decision, "r1")
        self.assertEqual(self.calls, [("market", "BUY"), ("oco", "78000.00", "90000.00")])
        self.assertEqual(self.build().state["positions"][0]["demo_exit_orders"]["order_list_id"], "11")

    def test_unprotectable_entry_is_closed_immediately(self):
        self.oco_fails = True
        with self.assertRaises(PaperEngineError):
            self.run_engine(self.decision, "r1")
        self.assertEqual([call[0] for call in self.calls], ["market", "oco", "market"])
        ledger = self.build()
        self.assertEqual(ledger.state["positions"], [])
        self.assertEqual(ledger.ledger["events"][-1]["reason"], "protection_failed")

    def test_exchange_stop_is_booked_and_manual_close_cancels_exit_orders_first(self):
        self.run_engine(self.decision, "r1")
        self.calls.clear()
        result = self.run_engine({"paper_trading_only": True, "action": "close", "reason": "thesis_invalid"}, "r2")
        self.assertEqual(self.calls, [("cancel", "11"), ("market", "SELL")])
        self.assertEqual(result["event"]["reason"], "thesis_invalid")
        self.run_engine(self.decision, "r3")
        self.calls.clear()
        self.exit_result = {"reason": "stop", "fill": self.market(None, "BTCUSDT", "SELL", "0.006")}
        self.calls.clear()
        result = self.run_engine({"paper_trading_only": True, "action": "manage"}, "r4")
        self.assertEqual((result["status"], result["event"]["reason"], self.calls), ("exchange_exit_reconciled", "stop", []))
        self.assertEqual(self.build().state["positions"], [])


if __name__ == "__main__":
    unittest.main()
