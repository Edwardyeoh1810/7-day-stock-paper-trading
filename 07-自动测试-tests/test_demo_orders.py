import sys
import unittest
from decimal import Decimal
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "06-程序脚本-scripts"))

import demo_orders
from demo_orders import (DemoOrderError, cancel_exit_orders, exit_status, funding_since, market_order,
                         place_exit_orders, prepare_symbol)

HOST = "https://demo-fapi.binance.com"
PROTECTION = {"stop_algo_id": "21", "target_algo_id": "22"}


class DemoOrderTests(unittest.TestCase):
    def setUp(self):
        self.config = {"BINANCE_ENV": "demo", "BINANCE_API_KEY": "fake-key", "BINANCE_API_SECRET": "fake-secret"}
        self.posts = []
        self.algo = {"21": {"algoStatus": "NEW"}, "22": {"algoStatus": "NEW"}}
        self.post_error = {}

    def get(self, url, headers=None):
        if "/fapi/v1/time" in url:
            return {"serverTime": 1000}, None
        if "/fapi/v1/userTrades?" in url:
            return [{"qty": "0.004", "quoteQty": "326.4", "commission": "0.08", "commissionAsset": "USDT"},
                    {"qty": "0.006", "quoteQty": "489.6", "commission": "0.12", "commissionAsset": "USDT"}], None
        if "/fapi/v1/algoOrder?" in url:
            return self.algo[url.split("algoId=")[1].split("&")[0]], None
        if "/fapi/v1/income?" in url:
            return [{"income": "-0.31"}, {"income": "0.11"}], None
        raise AssertionError(url)

    def post(self, url, headers, method="POST"):
        self.posts.append((method, url))
        for fragment, error in self.post_error.items():
            if fragment in url:
                return None, error
        if "/fapi/v1/algoOrder?" in url and method == "POST":
            return {"algoId": 21 if "type=STOP_MARKET" in url else 22}, None
        if "/fapi/v1/leverage?" in url:
            return {"leverage": 5}, None
        return {"orderId": 7}, None

    def patched(self):
        return patch.multiple(demo_orders, get_json=self.get, post_json=self.post)

    def test_non_demo_environment_never_sends_anything(self):
        calls = (lambda c: market_order(c, "BTCUSDT", "BUY", "0.001"), lambda c: prepare_symbol(c, "BTCUSDT", 5),
                 lambda c: place_exit_orders(c, "BTCUSDT", "long", "0.01", "78000", "86000"),
                 lambda c: cancel_exit_orders(c, "BTCUSDT", PROTECTION), lambda c: exit_status(c, "BTCUSDT", "long", PROTECTION),
                 lambda c: funding_since(c, "BTCUSDT", 0))
        for env in ("production", "testnet", None):
            with patch.object(demo_orders, "get_json") as get, patch.object(demo_orders, "post_json") as post:
                for call in calls:
                    with self.assertRaises(DemoOrderError):
                        call({**self.config, "BINANCE_ENV": env})
            get.assert_not_called()
            post.assert_not_called()

    def test_market_order_reads_the_real_fill_from_the_trade_list(self):
        with self.patched():
            fill = market_order(self.config, "BTCUSDT", "SELL", Decimal("0.01"), reduce_only=True)
        method, url = self.posts[0]
        self.assertTrue(url.startswith(HOST + "/fapi/v1/order?symbol=BTCUSDT&side=SELL&type=MARKET&quantity=0.01&reduceOnly=true&"))
        self.assertNotIn("fake-secret", url)
        self.assertEqual((Decimal(fill["executed_qty"]), Decimal(fill["avg_price"]), Decimal(fill["fee_usdt"])),
                         (Decimal("0.01"), Decimal("81600"), Decimal("0.2")))
        with self.patched():
            self.assertEqual(market_order(self.config, "BTCUSDT", "BUY", "0.01", test=True), {"test_order_accepted": True})
        self.assertIn("/fapi/v1/order/test?", self.posts[-1][1])
        self.assertNotIn("reduceOnly", self.posts[-1][1])

    def test_prepare_symbol_sets_isolated_margin_and_tolerates_already_isolated(self):
        self.post_error = {"/fapi/v1/marginType?": "HTTP 400 / Binance -4046"}
        with self.patched():
            prepare_symbol(self.config, "BTCUSDT", "5")
        self.assertIn("marginType=ISOLATED", self.posts[0][1])
        self.assertIn("/fapi/v1/leverage?symbol=BTCUSDT&leverage=5&", self.posts[1][1])
        self.post_error = {"/fapi/v1/marginType?": "HTTP 400 / Binance -4047"}
        with self.patched(), self.assertRaises(DemoOrderError):
            prepare_symbol(self.config, "BTCUSDT", "5")

    def test_exit_orders_are_reduce_only_triggers_on_the_correct_sides(self):
        with self.patched():
            orders = place_exit_orders(self.config, "BTCUSDT", "short", "0.01", "86000", "78000")
        self.assertEqual({k: orders[k] for k in PROTECTION}, PROTECTION)
        for (method, url), kind, trigger in zip(self.posts, ("STOP_MARKET", "TAKE_PROFIT_MARKET"), ("86000", "78000")):
            self.assertTrue(url.startswith(HOST + "/fapi/v1/algoOrder?algoType=CONDITIONAL&symbol=BTCUSDT&side=BUY&"))
            self.assertIn("type=%s&triggerPrice=%s&quantity=0.01&reduceOnly=true&workingType=MARK_PRICE" % (kind, trigger), url)
        for side, stop, target in (("long", "86000", "78000"), ("short", "78000", "86000"), ("flat", "1", "2")):
            with self.patched(), self.assertRaises(DemoOrderError):
                place_exit_orders(self.config, "BTCUSDT", side, "0.01", stop, target)
        self.assertEqual(len(self.posts), 2)

    def test_second_exit_order_failure_cancels_the_first(self):
        self.post_error = {"type=TAKE_PROFIT_MARKET": "HTTP 400 / Binance -2021"}
        with self.patched(), self.assertRaises(DemoOrderError):
            place_exit_orders(self.config, "BTCUSDT", "long", "0.01", "78000", "86000")
        self.assertEqual(self.posts[-1][0], "DELETE")
        self.assertIn("algoId=21", self.posts[-1][1])

    def test_exit_status_reports_the_filled_leg_and_cancels_the_other(self):
        with self.patched():
            self.assertIsNone(exit_status(self.config, "BTCUSDT", "long", PROTECTION))
            self.assertEqual(self.posts, [])
            self.algo["22"] = {"algoStatus": "FINISHED", "actualOrderId": "99"}
            self.post_error = {"algoId=22": "HTTP 400 / Binance -2011"}
            done = exit_status(self.config, "BTCUSDT", "long", PROTECTION)
        self.assertEqual((done["reason"], done["fill"]["side"], done["fill"]["demo_order_id"]), ("target", "SELL", "99"))
        self.assertEqual([method for method, url in self.posts], ["DELETE", "DELETE"])
        self.algo = {"21": {"algoStatus": "CANCELED"}, "22": {"algoStatus": "NEW"}}
        with self.patched():
            self.assertEqual(exit_status(self.config, "BTCUSDT", "long", PROTECTION), {"reason": None, "fill": None})

    def test_funding_is_netted_and_rejections_raise(self):
        with self.patched():
            self.assertEqual(Decimal(funding_since(self.config, "BTCUSDT", 123)), Decimal("-0.20"))
        self.post_error = {"/fapi/v1/order?": "HTTP 400 / Binance -2019"}
        with self.patched(), self.assertRaises(DemoOrderError):
            market_order(self.config, "BTCUSDT", "BUY", "0.01")
        with patch.object(demo_orders, "post_json", self.post), self.assertRaises(DemoOrderError), \
                patch.object(demo_orders, "get_json", lambda url, headers=None: ({"serverTime": 1}, None) if "time" in url else ([], None)):
            market_order(self.config, "BTCUSDT", "BUY", "0.01")


if __name__ == "__main__":
    unittest.main()
