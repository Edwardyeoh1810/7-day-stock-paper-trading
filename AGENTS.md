# AI Trading Experiment Operating Rules

This project is a 7 trading day stock/ETF research and paper trading experiment.
It is not a live trading system and must not be described as a profitable system.

## Safety Defaults

- Default mode is paper trading only.
- Live trading is disabled unless the user explicitly authorizes a specific live order in chat.
- Never place a real-money order without human confirmation.
- If any readiness check is missing, false, stale, or ambiguous, do not place orders.
- If market conditions are unclear, choose observation over trading.
- Risk control has priority over returns.

## Platform Scope

- Target platform: Binance stock/ETF trading capability.
- Before any execution path is used, verify whether Binance account permissions, region eligibility, API support, and any paper/sandbox capability are available.
- If Binance does not expose paper trading for stocks/ETFs, use the local paper ledger in this project.
- Binance API keys must stay local in the root `binance-api.env`; never ask the user to paste keys in chat. The read-only checker reads only this file. Share `binance-api.env.example`, never the completed credential file.

## Permitted Work

- Read strategy, schedules, state, journal, and evidence.
- Perform read-only account, position, order, and market-data checks when credentials are locally available.
- Produce watchlists, risk notes, and paper trade records.
- In paper trading only, autonomously decide whether to buy, sell, reduce, stop out, flatten, hold, or stay in cash according to the strategy and risk limits.
- Record no-trade decisions with evidence and reasons.

## Prohibited Work

- No live orders without explicit user confirmation.
- No options, futures, margin, leveraged products, crypto perpetuals, low-liquidity stocks, penny stocks, or unclear tokenized securities.
- No orders based on a single news item or a single indicator.
- No full-account or heavy-position trades.
- No credential leakage into journal, evidence files, logs, or chat.
- Paper trading autonomy does not authorize live trading, live order submission, transfers, account setting changes, or enabling trading permissions.

## Required Startup Reads

Every scheduled run must read these files before taking action:

- `AGENTS.md`
- `AGENTS.zh-CN.md`
- `docs/TRADING-STRATEGY.md`
- `docs/TRADING-STRATEGY.zh-CN.md`
- `routines/schedule.json`
- `routines/schedule.zh-CN.json`
- `routines/CONTINUITY.md`
- `routines/CONTINUITY.zh-CN.md`
- `state/readiness.json`
- `data/current-state.json`
- Latest file in `data/journal/`, if present

## Required End-of-Run Writes

Every scheduled run must update:

- `data/current-state.json`
- The current trading day's journal file in `data/journal/`
- Evidence notes in `data/evidence/`

Each journal entry must state:

- What was done
- Why it was done
- Whether an order was proposed
- Whether an order was placed
- Whether an order filled
- Current holdings
- Current cash
- Current risk
- Next task focus
- Human confirmations needed

## Binance Runtime

- Use `docs/BINANCE-API.md` and its Chinese companion for the Stocks endpoint mapping. The default checker uses `/sapi/v1/equity/`, not Spot symbol probes.
- `scripts/run_observation.py` is read-only; its SQLite database records executions, not a completed trading engine. No POST endpoint is implemented.
- `docs/STOP-AND-FILL-DRAFT.md` and its Chinese companion remain drafts. They do not authorize fills, continuous monitoring or changed risk limits.
- Preserve both languages. Dates in the schedule are provisional until authentication and review pass; do not count setup days as experiment sessions.
