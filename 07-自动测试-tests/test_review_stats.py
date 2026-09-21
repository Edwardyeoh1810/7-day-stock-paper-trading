import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "06-程序脚本-scripts"))

from review_stats import build_report


def entry(action, symbol, side, time, planned, evidence):
    position = {"side": side, "thesis": "t", "evidence": [{"category": c, "source": "s"} for c in evidence]}
    return {"action": action, "symbol": symbol, "timestamp": time, "planned_loss_usdt": planned, "fee_usdt": "0.5",
            "state_after": {"positions": [position]}}


def close(time, reason, pnl, funding="0"):
    return {"action": "close", "timestamp": time, "reason": reason, "net_pnl_usdt": pnl, "fee_usdt": "0.5", "funding_usdt": funding}


class ReviewStatsTests(unittest.TestCase):
    def test_report_pairs_trades_and_groups_results(self):
        events = [
            entry("open_long", "BTCUSDT", "long", "2026-09-21T04:00:00+00:00", "25", ["price_action", "news"]),
            {"action": "protect"}, {"action": "mark"},
            close("2026-09-21T10:00:00+00:00", "target", "40"),
            entry("open_short", "ETHUSDT", "short", "2026-09-22T00:00:00+00:00", "20", ["price_action", "Volume "]),
            close("2026-09-22T12:00:00+00:00", "stop", "-22", "-0.3"),
            entry("open_long", "BTCUSDT", "long", "2026-09-23T00:00:00+00:00", "25", ["news"]),
        ]
        with tempfile.TemporaryDirectory() as temp:
            decisions = Path(temp)
            for index, action in enumerate(("no_trade", "no_trade", "open_long")):
                (decisions / ("%d.json" % index)).write_text(json.dumps({"action": action}))
            report = build_report({"events": events}, {"cash_usdt": 5018, "positions": []}, decisions)
        self.assertEqual(report["decisions_by_action"], {"no_trade": 2, "open_long": 1})
        self.assertEqual(report["overall"]["trades"], 2)  # the still-open third entry is not a closed trade
        self.assertEqual((report["overall"]["win_rate_percent"], report["overall"]["net_pnl_usdt"]), (50.0, 18.0))
        self.assertEqual(report["overall"]["average_r"], round((40 / 25 - 22 / 20) / 2, 3))
        self.assertEqual(report["overall"]["max_drawdown_usdt"], 22.0)
        self.assertEqual(report["trades"][0]["hours_held"], 6.0)
        self.assertEqual(report["by_side"]["short"]["net_pnl_usdt"], -22.0)
        self.assertEqual(report["by_exit_reason"]["target"]["trades"], 1)
        self.assertEqual(sorted(report["by_evidence_category"]), ["news", "price_action", "volume"])
        self.assertEqual(report["by_evidence_category"]["price_action"]["trades"], 2)
        self.assertIsNotNone(report["sample_warning"])

    def test_empty_ledger_reports_zero_trades(self):
        with tempfile.TemporaryDirectory() as temp:
            report = build_report({"events": []}, {}, Path(temp))
        self.assertEqual(report["overall"], {"trades": 0})


if __name__ == "__main__":
    unittest.main()
