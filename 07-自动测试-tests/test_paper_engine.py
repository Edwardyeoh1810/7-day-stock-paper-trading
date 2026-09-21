import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "06-程序脚本-scripts"))

from paper_engine import PaperEngineError, fetch_snapshot, load_decision


class PaperEngineTests(unittest.TestCase):
    SYMBOL = {"symbol": "BTCUSDT", "status": "TRADING", "isSpotTradingAllowed": True, "filters": [
        {"filterType": "LOT_SIZE", "stepSize": "0.00001", "minQty": "0.00001", "maxQty": "9000"},
        {"filterType": "MARKET_LOT_SIZE", "stepSize": "0", "minQty": "0", "maxQty": "100"},
        {"filterType": "NOTIONAL", "minNotional": "5", "maxNotional": "9000000"}]}

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
            "minQty": "0.00001", "maxQty": "100", "minNotional": "5", "maxNotional": "9000000"})
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


if __name__ == "__main__":
    unittest.main()
