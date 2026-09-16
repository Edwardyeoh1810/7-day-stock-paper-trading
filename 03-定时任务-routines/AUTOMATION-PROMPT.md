# Automation Description and Saved Prompt

This is the checked-in companion to the active GPT heartbeat. See [automation-status.json](automation-status.json) for the current deployment status.

## Active Schedule

Use `/Users/a123/Desktop/7天股票交易实验` and return to the existing experiment conversation. Six America/Chicago checks: 07:45, 08:35, 11:00, 13:00, 14:15 and 14:45. Dates are in [schedule.json](schedule.json) and its [Chinese companion](schedule.zh-CN.json): 42 occurrences and a 30-minute late-start tolerance. GPT heartbeat automation 7 is active; the GitHub-hosted runner remains blocked by Binance HTTP 451.

## Saved Prompt

Perform all project operations only in the Desktop experiment directory. Read both languages of AGENTS, strategy, schedule and CONTINUITY, plus readiness, current-state and the latest journal.

Run `python3 -B 06-程序脚本-scripts/run_observation.py --dry-run` first. Outside the planned sessions or slot tolerance, finish quietly. For a due slot, run `python3 -B 06-程序脚本-scripts/run_observation.py`. Stop on duplicate_skipped or another_run_active. Reconcile interrupted read-only runs using recovery before continuing.

Research the slot's topic with official calendars, news and verifiable data. Save research in separate journal/evidence files using the same run_id with a `-research` suffix, and update next-task focus. Do not edit generated API journals.

After research, independently decide whether the local paper ledger should open, manage, close, or record no trade. The user authorized autonomous paper decisions only. Never submit a real Binance order, transfer, tokenization request, or account-setting change.

For every decision, create a non-secret JSON file under `05-交易记录-data/decisions/` with `paper_trading_only: true`, an `action` of `open_long`, `manage`, `close`, or `no_trade`, and the evidence, thesis, stop, and target required for an entry. Then run `python3 -B 06-程序脚本-scripts/paper_engine.py --decision <file> --run-id <date_slot>_paper`; the `_paper` suffix prevents overwriting the read-only runner's evidence file. The engine refreshes read-only Stocks data, rejects stale or unsafe state, and writes only to the local paper ledger. Do not create an entry before 08:30 Central or after 11:30 Central. At 14:15 Central, close any remaining paper position because overnight holds are disabled.

Keep 10000 USDT paper capital and existing limits; record no trade when actual fees, liquidity, data quality, or evidence make trading infeasible. This is not a continuous stop monitor. Read credentials locally through the script; never display them.

Stay quiet for unchanged or non-actionable state. Notify on scheduled reports, meaningful changes, completion, failure or required user action. Revalidate seven sessions and synchronize schedules if the start is delayed. Pause after the seventh session.

## Verification Boundary

All 42 times and bilingual schedules were checked offline. GPT heartbeat automation 7 is active and has executed against the Desktop project. One delayed wake-up was recorded on 2026-09-15, so every run must compare the actual host time with the intended Central-time slot and must never backfill a historical trade.
