# Automation Description and Saved Prompt

This is the checked-in prompt for the local Claude scheduled tasks. See [automation-status.json](automation-status.json) for the current deployment status.

## Active Schedule

Project directory: `/Users/edwardmacmini/Projects/7-day-stock-paper-trading`. Six America/Chicago checks: 07:45, 08:35, 11:00, 13:00, 14:15 and 14:45. Dates are in [schedule.json](schedule.json) and its [Chinese companion](schedule.zh-CN.json): 42 occurrences and a 30-minute late-start tolerance. The tasks fire in the host's local time (UTC+8): 20:45, 21:35, 00:00, 02:00, 03:15 and 03:45; the four after-midnight runs belong to the previous Central-time date. GitHub-hosted runners are blocked by Binance HTTP 451, so all runs are local.

## Saved Prompt

Perform all project operations only in the project directory. Read both languages of AGENTS, strategy, schedule and CONTINUITY, plus readiness, current-state and the latest journal. The strategy documents were written for stocks; apply their evidence, risk and no-trade discipline to the crypto Spot watchlist, and where they conflict with `AGENTS.md`, `AGENTS.md` wins.

Run `python3 -B 06-程序脚本-scripts/run_observation.py --dry-run` first. If `due_slot` is null (outside the planned sessions or slot tolerance), finish quietly and change nothing. For a due slot, run `python3 -B 06-程序脚本-scripts/run_observation.py`. Stop on duplicate_skipped or another_run_active. Reconcile interrupted read-only runs using `--recover` before continuing.

At the 07:45 slot only, before any decision: confirm there is no open position, then set `daily_realized_pnl_usdt` to 0 and `trading_day_index` to the 1-based position of today's Central date in `planned_trading_dates` in `05-交易记录-data/current-state.json`.

Research the slot's topic with official calendars, news and verifiable market data for the watchlist pairs only. Save research in separate journal/evidence files using the same run_id with a `-research` suffix, and update next-task focus. Do not edit generated API journals.

After research, independently decide whether to open, manage, close, or record no trade. The user authorized autonomous paper decisions on the Binance demo account (virtual funds) only. Never submit a production Binance order, transfer, or account-setting change, never change `BINANCE_ENV`, readiness safety switches, risk limits, the watchlist or any script, and never call the order API except through `paper_engine.py`.

For every decision, create a non-secret JSON file under `05-交易记录-data/decisions/` with `paper_trading_only: true`, an `action` of `open_long`, `manage`, `close`, or `no_trade`, and for an entry the `symbol`, `thesis`, `stop_price`, `target_price` and an `evidence` list of at least two categories (each item with `category` and `source`). Then run `python3 -B 06-程序脚本-scripts/paper_engine.py --decision <file> --run-id <date_slot>_paper`; the `_paper` suffix prevents overwriting the read-only runner's evidence file. The engine refreshes the demo readiness check, rejects stale or unsafe state, sizes the order from the risk limits, sends one MARKET order to the demo account and records the actual fill in the local ledger. If the engine rejects a decision, record the reason and do not retry with loosened parameters. Do not create an entry before 08:30 Central or after 11:30 Central. At 14:15 Central, close any remaining position because overnight holds are disabled; at 14:45 confirm the account is flat.

Keep 5000 USDT paper capital and existing limits; record no trade when fees, liquidity, data quality, or evidence make trading infeasible. This is not a continuous stop monitor: stops and targets are only evaluated at the scheduled checks. Read credentials locally through the scripts; never display, print or copy them.

Stay quiet for unchanged or non-actionable state. Report on scheduled runs, meaningful changes, completion, failure or required user action. After the seventh session's 14:45 check, write a final summary to the journal and do nothing on later runs.

## Verification Boundary

All 42 times and bilingual schedules are checked offline by the test suite. The demo readiness check, market snapshots for all five pairs, validate-only test orders and a no-trade engine pass were verified on 2026-09-21. Scheduled tasks only run while the Claude desktop app is open; every run must compare the actual host time with the intended Central-time slot and must never backfill a historical trade.
