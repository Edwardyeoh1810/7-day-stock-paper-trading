# Continuity Protocol

The experiment must survive context loss, delayed scheduled starts, and incomplete prior runs. The local project files are the source of truth.

## Startup Sequence

Every scheduled task must begin by reading:

- `AGENTS.md`
- `AGENTS.zh-CN.md`
- `02-项目文档-docs/TRADING-STRATEGY.md`
- `02-项目文档-docs/TRADING-STRATEGY.zh-CN.md`
- `03-定时任务-routines/schedule.json`
- `03-定时任务-routines/schedule.zh-CN.json`
- `03-定时任务-routines/CONTINUITY.md`
- `03-定时任务-routines/CONTINUITY.zh-CN.md`
- `04-运行状态-state/readiness.json`
- `05-交易记录-data/current-state.json`
- Latest `05-交易记录-data/journal/` record, if present

Before any trade decision, check:

- Paper trading is enabled.
- Live trading is disabled.
- Broker/API status is read-only or explicitly verified for paper trading.
- Position size, daily loss, and single-trade loss limits are present.
- No unfinished previous run requires reconciliation.

If any item is missing, malformed, stale, contradictory, or unsafe, switch to observation only.

## End-of-Run Sequence

Every scheduled task must update:

- `05-交易记录-data/current-state.json`
- The current trading day's journal file in `05-交易记录-data/journal/`
- Evidence notes in `05-交易记录-data/evidence/`

## Required Journal Content

Each entry must include:

- Timestamp and scheduled task id
- What was done
- Why it was done
- Whether an order was proposed
- Whether an order was placed
- Whether an order filled
- Current holdings
- Current cash
- Current risk
- Evidence captured
- Next task focus
- Human confirmations needed

## Evidence Rules

Evidence files must not contain credentials or secrets. Evidence should include links, source names, timestamps, market data snapshots, and brief notes explaining how the evidence affected the decision.

## Duplicate Or Interrupted Runs

If a previous run appears unfinished:

- Do not open new risk.
- Reconcile current-state, journal, and any broker/account reads.
- Record the interruption.
- Resume only after the state is consistent.

## Live Trading Boundary

Even if credentials exist, live orders remain prohibited unless the user explicitly confirms a specific live order in chat. General permission, API access, or funding is not enough.

## Implemented Read-Only Recovery

Run `python3 -B 06-程序脚本-scripts/run_observation.py` from the project for a due slot, or use `--manual` for an explicit check. The process lock serializes runs; SQLite uses unique date/slot IDs and prevents a new run while an earlier run is unfinished. `--recover` acquires the same lock, restores completed exports and marks interrupted read-only executions. It never retries orders or rolls portfolio values backwards.

API-check journals and evidence are deterministic exports from `05-交易记录-data/runs.sqlite3`; do not manually edit them. Put research in separate files with a `-research` suffix. `05-交易记录-data/current-state.json` remains the current paper portfolio record, while `05-交易记录-data/paper-ledger.json` records simulated fill events. Latest read-only run metadata can be recovered from the database.

Each Stocks check has its own timestamp. A fresh API test does not refresh eligibility, market-data freshness or trading authorization. The proposed 5-second sampling and 15-second gap rule remain in the unapproved stop/fill draft.
