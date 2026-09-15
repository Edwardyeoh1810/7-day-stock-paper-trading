import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from paper_engine import PaperEngineError, fetch_snapshot, load_decision


class PaperEngineTests(unittest.TestCase):
    def test_fetch_snapshot_rejects_missing_sizes(self):
        # The live quote endpoint supplies sizes; a local paper fill must not invent them.
        responses = iter((
            ({"symbols": [{"symbol": "AAPL", "tradability": "BUY_SELL", "fractionable": True,
                            "stepSize": "0.0001", "minQty": "0.0001", "maxQty": "1000",
                            "minNotional": "5", "maxNotional": "1000000"}]}, None),
            ({"symbol": "AAPL", "bidPrice": "100", "askPrice": "100.01"}, None),
        ))
        with patch("paper_engine.get_json", side_effect=lambda *args: next(responses)):
            with self.assertRaises(PaperEngineError):
                fetch_snapshot({"BINANCE_API_KEY": "not-used"}, "AAPL", datetime.now(timezone.utc))

    def test_open_decision_requires_paper_mode(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "decision.json"
            path.write_text('{"action":"open_long"}', encoding="utf-8")
            with self.assertRaises(PaperEngineError):
                load_decision(path)


if __name__ == "__main__":
    unittest.main()
