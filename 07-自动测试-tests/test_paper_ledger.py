import json
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "06-程序脚本-scripts"))

from paper_ledger import PaperLedger, PaperLedgerError


class PaperLedgerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "05-交易记录-data").mkdir()
        (self.root / "04-运行状态-state").mkdir()
        self.now = datetime(2026, 9, 15, 14, 0, tzinfo=timezone.utc)
        self.state = {
            "planned_trading_dates": ["2026-09-15"],
            "starting_capital_usdt": 10000,
            "cash_usdt": 10000,
            "equity_usdt": 10000,
            "realized_pnl_usdt": 0,
            "unrealized_pnl_usdt": 0,
            "daily_realized_pnl_usdt": 0,
            "daily_open_risk_usdt": 0,
            "positions": [],
            "open_orders": [],
            "watchlist": ["AAPL", "SPY"],
        }
        self.readiness = {
            "paper_trading_only": True,
            "live_trading_enabled": False,
            "broker_connected": True,
            "human_confirmation_required_for_live_orders": True,
            "binance_demo_api_read_access_verified": True,
            "local_paper_ledger_initialized": True,
            "autonomous_paper_execution_enabled": True,
            "orders_allowed": False,
            "max_position_size_percent": 10,
            "max_daily_loss_percent": 2,
            "max_single_trade_loss_percent": 0.5,
            "binance_demo_api": {
                "checked_at": self.now.isoformat(),
                "demo_market_access_verified": True,
            },
        }
        self.config = {
            "fee_bps_per_side": "10",
            "slippage_bps_per_side": "2",
            "max_spread_bps": "25",
            "quote_max_age_seconds": "10",
            "readiness_max_age_hours": "24",
            "minimum_evidence_categories": 2,
            "minimum_reward_risk": "1.5",
            "timezone": "America/Chicago",
            "entry_window_open": "08:30",
            "entry_window_close": "11:30",
            "max_hold_hours": "24",
            "leverage": "5",
            "max_stop_distance_percent": "10",
        }
        self.ledger_data = {"version": 1, "next_sequence": 1, "events": []}
        self._write_all()

    def _write_all(self):
        for path, payload in (
            (self.root / "05-交易记录-data/current-state.json", self.state),
            (self.root / "04-运行状态-state/readiness.json", self.readiness),
            (self.root / "04-运行状态-state/paper-config.json", self.config),
            (self.root / "05-交易记录-data/paper-ledger.json", self.ledger_data),
        ):
            path.write_text(json.dumps(payload), encoding="utf-8")

    def make_ledger(self):
        return PaperLedger(
            self.root / "05-交易记录-data/current-state.json",
            self.root / "04-运行状态-state/readiness.json",
            self.root / "04-运行状态-state/paper-config.json",
            self.root / "05-交易记录-data/paper-ledger.json",
        )

    def quote(self, bid="99.98", ask="100.00", bid_size="100", ask_size="100", received_at=None):
        return {
            "symbol": "AAPL",
            "bid": bid,
            "ask": ask,
            "bid_size": bid_size,
            "ask_size": ask_size,
            "received_at": (received_at or self.now).isoformat(),
        }

    def rules(self):
        return {
            "symbol": "AAPL",
            "tradability": "BUY_SELL",
            "fractionable": True,
            "stepSize": "0.0001",
            "minQty": "0.0001",
            "maxQty": "1000",
            "minNotional": "5",
            "maxNotional": "1000000",
        }

    def request(self):
        return {
            "symbol": "AAPL",
            "side": "long",
            "quote": self.quote(),
            "rules": self.rules(),
            "stop_price": "95",
            "target_price": "109",
            "thesis": "Liquid large-cap trend continuation with defined invalidation.",
            "evidence": [
                {"category": "price_action", "source": "market snapshot"},
                {"category": "market_context", "source": "index context"},
            ],
        }

    def test_open_respects_position_and_trade_limits(self):
        ledger = self.make_ledger()
        event = ledger.open_position(self.request(), self.now)
        state = json.loads((self.root / "05-交易记录-data/current-state.json").read_text())
        position = state["positions"][0]
        self.assertEqual(event["action"], "open_long")
        self.assertLessEqual(Decimal(position["entry_price"]) * Decimal(position["quantity"]), Decimal("1000"))
        self.assertLessEqual(Decimal(position["planned_loss_usdt"]), Decimal("50"))
        self.assertLess(state["cash_usdt"], 10000)
        self.assertFalse(event.get("live_order_sent", False))

    def test_rejects_single_evidence_category(self):
        request = self.request()
        request["evidence"] = [{"category": "price_action", "source": "one source"}]
        with self.assertRaisesRegex(PaperLedgerError, "two independent"):
            self.make_ledger().open_position(request, self.now)

    def test_rejects_stale_quote(self):
        request = self.request()
        request["quote"] = self.quote(received_at=self.now - timedelta(seconds=11))
        with self.assertRaisesRegex(PaperLedgerError, "stale"):
            self.make_ledger().open_position(request, self.now)

    def test_rejects_wide_spread(self):
        request = self.request()
        request["quote"] = self.quote(bid="99", ask="100")
        with self.assertRaisesRegex(PaperLedgerError, "Spread"):
            self.make_ledger().open_position(request, self.now)

    def test_live_enabled_blocks_paper_action(self):
        self.readiness["live_trading_enabled"] = True
        self._write_all()
        with self.assertRaisesRegex(PaperLedgerError, "live_trading_enabled"):
            self.make_ledger().open_position(self.request(), self.now)

    def test_after_cutoff_blocks_new_entry(self):
        late = datetime(2026, 9, 15, 18, 0, tzinfo=timezone.utc)
        self.readiness["binance_demo_api"]["checked_at"] = late.isoformat()
        self._write_all()
        request = self.request()
        request["quote"]["received_at"] = late.isoformat()
        with self.assertRaisesRegex(PaperLedgerError, "outside"):
            self.make_ledger().open_position(request, late)

    def test_stop_exit_updates_realized_pnl(self):
        ledger = self.make_ledger()
        ledger.open_position(self.request(), self.now)
        stop_time = self.now + timedelta(minutes=5)
        ledger.readiness["binance_demo_api"]["checked_at"] = stop_time.isoformat()
        stop_quote = self.quote(bid="94.90", ask="95.00", received_at=stop_time)
        event = ledger.mark({"quote": stop_quote}, stop_time, evaluate=True)
        state = json.loads((self.root / "05-交易记录-data/current-state.json").read_text())
        self.assertEqual(event["action"], "close")
        self.assertEqual(event["reason"], "stop")
        self.assertEqual(state["positions"], [])
        self.assertLess(state["realized_pnl_usdt"], 0)
        self.assertEqual(state["daily_open_risk_usdt"], 0)

    def test_quote_size_caps_entry_and_blocks_unsupported_exit(self):
        request = self.request()
        request["quote"] = self.quote(ask_size="1")
        ledger = self.make_ledger()
        ledger.open_position(request, self.now)
        position = ledger.state["positions"][0]
        self.assertLessEqual(Decimal(position["quantity"]), Decimal("1"))
        exit_time = self.now + timedelta(minutes=1)
        ledger.readiness["binance_demo_api"]["checked_at"] = exit_time.isoformat()
        with self.assertRaisesRegex(PaperLedgerError, "Quoted size"):
            ledger.close({
                "quote": self.quote(bid_size="0.5", received_at=exit_time),
                "reason": "manual_exit",
            }, exit_time)

    def demo_fill(self, side, quantity, price, fee="0", funding=None):
        quantity, price = Decimal(str(quantity)), Decimal(price)
        fill = {"demo_order_id": "42", "side": side, "executed_qty": str(quantity), "avg_price": str(price),
                "gross_usdt": str(quantity * price), "fee_usdt": fee}
        if funding is not None:
            fill["funding_usdt"] = funding
        return fill

    def test_demo_executor_fills_replace_simulated_fills(self):
        orders = []

        def execute(symbol, side, quantity, closing):
            orders.append((symbol, side, quantity, closing))
            if not closing:
                return self.demo_fill(side, quantity, "100.05", fee="0.4")
            return self.demo_fill(side, quantity, "104", fee="0.5", funding="-0.25")

        ledger = self.make_ledger()
        opened = ledger.open_position(self.request(), self.now, execute)
        position = ledger.state["positions"][0]
        self.assertEqual((position["entry_price"], Decimal(position["quantity"])), ("100.05", orders[0][2]))
        # Futures accounting: only the fee leaves the wallet at entry, not the notional.
        self.assertEqual(Decimal(str(ledger.state["cash_usdt"])), Decimal("9999.6"))
        self.assertEqual(opened["demo_order"]["demo_order_id"], "42")
        later = self.now + timedelta(minutes=5)
        ledger.readiness["binance_demo_api"]["checked_at"] = later.isoformat()
        closed = ledger.close({"quote": self.quote(bid="104", ask="104.02", received_at=later), "reason": "target"}, later, execute)
        self.assertEqual(orders[1], ("AAPL", "SELL", Decimal(position["quantity"]), True))
        gross = orders[1][2] * (Decimal("104") - Decimal("100.05"))
        self.assertEqual(Decimal(closed["net_pnl_usdt"]), gross - Decimal("0.5") - Decimal("0.4") - Decimal("0.25"))
        self.assertEqual(Decimal(str(ledger.state["cash_usdt"])), (Decimal("9999.6") + gross - Decimal("0.75")).quantize(Decimal("0.00000001")))
        self.assertEqual(ledger.state["positions"], [])

    def short_request(self):
        request = self.request()
        request.update({"side": "short", "stop_price": "105", "target_price": "91"})
        return request

    def test_short_profits_when_price_falls_and_stops_out_above_entry(self):
        ledger = self.make_ledger()
        event = ledger.open_position(self.short_request(), self.now)
        self.assertEqual(event["action"], "open_short")
        position = ledger.state["positions"][0]
        self.assertLess(Decimal(position["entry_price"]), Decimal("99.98"))
        self.assertLessEqual(Decimal(position["planned_loss_usdt"]), Decimal("50"))
        later = self.now + timedelta(minutes=5)
        ledger.readiness["binance_demo_api"]["checked_at"] = later.isoformat()
        ledger.mark({"quote": self.quote(bid="96.98", ask="97.00", received_at=later)}, later, evaluate=True)
        self.assertGreater(ledger.state["unrealized_pnl_usdt"], 0)
        event = ledger.mark({"quote": self.quote(bid="105.00", ask="105.02", received_at=later)}, later, evaluate=True)
        self.assertEqual((event["action"], event["reason"], event["side"]), ("close", "stop", "short"))
        self.assertLess(ledger.state["realized_pnl_usdt"], 0)
        self.assertGreaterEqual(ledger.state["realized_pnl_usdt"], -51)

    def test_rejects_wrong_sided_or_too_distant_stops(self):
        for changes, message in (({"side": "short"}, "wrong sides"), ({"side": "flat"}, "long or short"),
                                 ({"stop_price": "89", "target_price": "125"}, "too far")):
            request = self.request()
            request.update(changes)
            with self.assertRaisesRegex(PaperLedgerError, message):
                self.make_ledger().open_position(request, self.now)

    def test_margin_limits_size_when_cash_is_short(self):
        self.state["cash_usdt"] = 100
        self._write_all()
        ledger = self.make_ledger()
        ledger.open_position(self.request(), self.now)
        position = ledger.state["positions"][0]
        self.assertLessEqual(Decimal(position["margin_usdt"]) + Decimal(position["entry_fee_usdt"]), Decimal("100"))
        self.assertGreater(Decimal(position["notional_usdt"]), Decimal("400"))

    def test_failed_demo_order_records_nothing(self):
        def execute(symbol, side, quantity, closing):
            raise ValueError("Demo order rejected")

        ledger = self.make_ledger()
        with self.assertRaises(ValueError):
            ledger.open_position(self.request(), self.now, execute)
        state = json.loads((self.root / "05-交易记录-data/current-state.json").read_text())
        self.assertEqual(state["positions"], [])
        self.assertEqual(state["cash_usdt"], 10000)

    def test_rejected_request_never_reaches_executor(self):
        calls = []
        request = self.request()
        request["evidence"] = [{"category": "price_action", "source": "one source"}]
        with self.assertRaises(PaperLedgerError):
            self.make_ledger().open_position(request, self.now, lambda *args: calls.append(args))
        ledger = self.make_ledger()
        ledger.open_position(self.request(), self.now)
        with self.assertRaisesRegex(PaperLedgerError, "exit reason"):
            ledger.close({"quote": self.quote(), "reason": "because"}, self.now, lambda *args: calls.append(args))
        self.assertEqual(calls, [])

    def test_protected_position_leaves_stop_to_exchange_but_enforces_max_hold(self):
        ledger = self.make_ledger()
        ledger.open_position(self.request(), self.now)
        ledger.set_protection({"order_list_id": "1", "stop_order_id": "2", "target_order_id": "3"}, self.now)
        later = self.now + timedelta(minutes=5)
        ledger.readiness["binance_demo_api"]["checked_at"] = later.isoformat()
        event = ledger.mark({"quote": self.quote(bid="94.90", ask="95.00", received_at=later)}, later, evaluate=True)
        self.assertEqual(event["action"], "mark")
        self.assertEqual(len(ledger.state["positions"]), 1)
        expired = self.now + timedelta(hours=24)
        ledger.readiness["binance_demo_api"]["checked_at"] = expired.isoformat()
        event = ledger.mark({"quote": self.quote(received_at=expired)}, expired, evaluate=True)
        self.assertEqual((event["action"], event["reason"]), ("close", "time_exit"))

    def test_record_exit_books_exchange_fill_without_a_quote(self):
        ledger = self.make_ledger()
        ledger.open_position(self.request(), self.now)
        position = ledger.state["positions"][0]
        cash_after_entry = Decimal(str(ledger.state["cash_usdt"]))
        fill = self.demo_fill("SELL", position["quantity"], "95", fee="0.5", funding="0.1")
        event = ledger.record_exit(fill, "stop", self.now + timedelta(hours=3), "run-1")
        gross = Decimal(position["quantity"]) * (Decimal("95") - Decimal(position["entry_price"]))
        self.assertEqual(Decimal(event["net_pnl_usdt"]), gross - Decimal("0.5") - Decimal(position["entry_fee_usdt"]) + Decimal("0.1"))
        self.assertEqual((event["reason"], event["run_id"], event["quote"]), ("stop", "run-1", None))
        state = json.loads((self.root / "05-交易记录-data/current-state.json").read_text())
        self.assertEqual(state["positions"], [])
        self.assertAlmostEqual(state["cash_usdt"], float(cash_after_entry + gross - Decimal("0.4")), places=6)
        self.assertLess(state["daily_realized_pnl_usdt"], 0)

    def test_roll_day_resets_daily_loss_once_per_planned_day(self):
        self.state["daily_realized_pnl_usdt"] = -80
        self._write_all()
        ledger = self.make_ledger()
        ledger.roll_day(self.now)
        self.assertEqual((ledger.state["daily_realized_pnl_usdt"], ledger.state["trading_day_index"]), (0, 1))
        ledger.state["daily_realized_pnl_usdt"] = -30
        ledger.roll_day(self.now + timedelta(hours=1))
        self.assertEqual(ledger.state["daily_realized_pnl_usdt"], -30)
        ledger.roll_day(self.now + timedelta(days=30))
        self.assertEqual(ledger.state["daily_realized_pnl_usdt"], -30)

    def test_reconcile_restores_last_event_snapshot(self):
        self.make_ledger().open_position(self.request(), self.now)
        damaged = json.loads((self.root / "05-交易记录-data/current-state.json").read_text())
        damaged["cash_usdt"] = 1
        (self.root / "05-交易记录-data/current-state.json").write_text(json.dumps(damaged), encoding="utf-8")
        restored = self.make_ledger().reconcile()
        self.assertGreater(restored["cash_usdt"], 1)
        self.assertEqual(len(restored["positions"]), 1)


if __name__ == "__main__":
    unittest.main()
