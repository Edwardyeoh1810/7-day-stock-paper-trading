import sys
import unittest
from decimal import Decimal
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "06-程序脚本-scripts"))

import demo_orders
from demo_orders import DemoOrderError, cancel_exit_oco, exit_status, market_order, place_exit_oco


class DemoOrderTests(unittest.TestCase):
    def setUp(self):
        self.config = {"BINANCE_ENV": "demo", "BINANCE_API_KEY": "fake-key", "BINANCE_API_SECRET": "fake-secret"}

    def test_non_demo_environment_never_sends_anything(self):
        for env in ("production", "testnet", None):
            with patch.object(demo_orders, "get_json") as get, patch.object(demo_orders, "post_json") as post:
                with self.assertRaises(DemoOrderError):
                    market_order({**self.config, "BINANCE_ENV": env}, "BTCUSDT", "BUY", "0.001")
            get.assert_not_called()
            post.assert_not_called()

    def test_order_goes_only_to_demo_host_and_nets_base_commission(self):
        reply = {"orderId": 7, "status": "FILLED", "executedQty": "0.01000000", "cummulativeQuoteQty": "800.00000000",
                 "fills": [{"price": "80000", "qty": "0.01", "commission": "0.00001000", "commissionAsset": "BTC"}]}
        with patch.object(demo_orders, "get_json", return_value=({"serverTime": 1000}, None)), \
                patch.object(demo_orders, "post_json", return_value=(reply, None)) as post:
            fill = market_order(self.config, "BTCUSDT", "BUY", Decimal("0.01"))
        url = post.call_args.args[0]
        self.assertTrue(url.startswith("https://demo-api.binance.com/api/v3/order?symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.01&"))
        self.assertEqual(Decimal(fill["net_qty"]), Decimal("0.00999"))
        self.assertEqual(Decimal(fill["net_usdt"]), Decimal("800"))
        self.assertEqual(Decimal(fill["fee_usdt"]), Decimal("0.8"))
        self.assertNotIn("fake-secret", url)

    def test_sell_nets_quote_commission_and_test_mode_uses_test_endpoint(self):
        reply = {"orderId": 8, "status": "FILLED", "executedQty": "0.01", "cummulativeQuoteQty": "810",
                 "fills": [{"commission": "0.81", "commissionAsset": "USDT"}]}
        with patch.object(demo_orders, "get_json", return_value=({"serverTime": 1000}, None)), \
                patch.object(demo_orders, "post_json", return_value=(reply, None)):
            fill = market_order(self.config, "BTCUSDT", "SELL", "0.01")
        self.assertEqual(Decimal(fill["net_usdt"]), Decimal("809.19"))
        with patch.object(demo_orders, "get_json", return_value=({"serverTime": 1000}, None)), \
                patch.object(demo_orders, "post_json", return_value=({}, None)) as post:
            self.assertEqual(market_order(self.config, "BTCUSDT", "BUY", "0.01", test=True), {"test_order_accepted": True})
        self.assertIn("/api/v3/order/test?", post.call_args.args[0])

    PROTECTION = {"order_list_id": "11", "stop_order_id": "21", "target_order_id": "22"}

    def test_exit_orders_are_trigger_market_sells_on_the_demo_host(self):
        reply = {"orderListId": 11, "orderReports": [{"type": "STOP_LOSS", "orderId": 21}, {"type": "TAKE_PROFIT", "orderId": 22}]}
        with patch.object(demo_orders, "get_json", return_value=({"serverTime": 1000}, None)), \
                patch.object(demo_orders, "post_json", return_value=(reply, None)) as post:
            orders = place_exit_oco(self.config, "BTCUSDT", "0.01", "78000", "86000")
        url, _, method = post.call_args.args
        self.assertTrue(url.startswith("https://demo-api.binance.com/api/v3/orderList/oco?symbol=BTCUSDT&side=SELL&quantity=0.01&"))
        self.assertIn("aboveType=TAKE_PROFIT&aboveStopPrice=86000&belowType=STOP_LOSS&belowStopPrice=78000", url)
        self.assertEqual(method, "POST")
        self.assertEqual({k: orders[k] for k in self.PROTECTION}, self.PROTECTION)
        with patch.object(demo_orders, "get_json") as get, patch.object(demo_orders, "post_json") as post:
            for call in (lambda c: place_exit_oco(c, "BTCUSDT", "0.01", "78000", "86000"),
                         lambda c: cancel_exit_oco(c, "BTCUSDT", self.PROTECTION),
                         lambda c: exit_status(c, "BTCUSDT", self.PROTECTION)):
                with self.assertRaises(DemoOrderError):
                    call({**self.config, "BINANCE_ENV": "production"})
            with self.assertRaises(DemoOrderError):
                place_exit_oco(self.config, "BTCUSDT", "0.01", "86000", "78000")
        get.assert_not_called()
        post.assert_not_called()

    def test_exit_status_reports_the_filled_leg(self):
        def get(url, headers=None):
            if "/api/v3/time" in url:
                return {"serverTime": 1000}, None
            if "/api/v3/orderList?" in url:
                return {"listOrderStatus": self.status}, None
            if "/api/v3/myTrades?" in url:
                return [{"commission": "0.78", "commissionAsset": "USDT"}], None
            filled = "orderId=21" in url and self.stop_filled
            return {"orderId": 21, "status": "FILLED" if filled else "EXPIRED",
                    "executedQty": "0.01" if filled else "0", "cummulativeQuoteQty": "780" if filled else "0"}, None

        with patch.object(demo_orders, "get_json", side_effect=get):
            self.status, self.stop_filled = "EXECUTING", False
            self.assertIsNone(exit_status(self.config, "BTCUSDT", self.PROTECTION))
            self.status, self.stop_filled = "ALL_DONE", True
            done = exit_status(self.config, "BTCUSDT", self.PROTECTION)
            self.assertEqual(done["reason"], "stop")
            self.assertEqual(Decimal(done["fill"]["net_usdt"]), Decimal("779.22"))
            self.stop_filled = False
            self.assertEqual(exit_status(self.config, "BTCUSDT", self.PROTECTION), {"reason": None, "fill": None})

    def test_rejection_and_unfilled_orders_raise(self):
        for reply in ((None, "HTTP 400 / Binance -2010"), ({"orderId": 9, "status": "EXPIRED", "executedQty": "0", "cummulativeQuoteQty": "0"}, None)):
            with patch.object(demo_orders, "get_json", return_value=({"serverTime": 1000}, None)), \
                    patch.object(demo_orders, "post_json", return_value=reply):
                with self.assertRaises(DemoOrderError):
                    market_order(self.config, "BTCUSDT", "BUY", "0.01")


if __name__ == "__main__":
    unittest.main()
