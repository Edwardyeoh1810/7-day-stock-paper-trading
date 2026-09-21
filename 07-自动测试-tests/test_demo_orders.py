import sys
import unittest
from decimal import Decimal
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "06-程序脚本-scripts"))

import demo_orders
from demo_orders import DemoOrderError, market_order


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

    def test_rejection_and_unfilled_orders_raise(self):
        for reply in ((None, "HTTP 400 / Binance -2010"), ({"orderId": 9, "status": "EXPIRED", "executedQty": "0", "cummulativeQuoteQty": "0"}, None)):
            with patch.object(demo_orders, "get_json", return_value=({"serverTime": 1000}, None)), \
                    patch.object(demo_orders, "post_json", return_value=reply):
                with self.assertRaises(DemoOrderError):
                    market_order(self.config, "BTCUSDT", "BUY", "0.01")


if __name__ == "__main__":
    unittest.main()
