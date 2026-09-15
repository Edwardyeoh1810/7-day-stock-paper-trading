# Seven-Day Stock Trading Experiment

Project directory: `/Users/a123/Desktop/7天股票交易实验`.

This is a Binance Stocks research and paper experiment. Read-only integration and execution journaling are implemented. Actual account authentication has not passed, the stop/fill proposal is pending review, and the seven-session experiment has not started.

## Navigation

| Topic | File |
| --- | --- |
| Decisions, status and next steps | [Project handoff](docs/PROJECT-HANDOFF.md) |
| Local setup and commands | [Getting started, Chinese](开始使用.md) |
| Binance endpoints | [API integration](docs/BINANCE-API.md) |
| Stop/fill proposal | [Draft v0.1](docs/STOP-AND-FILL-DRAFT.md) |
| Existing strategy | [Trading strategy](docs/TRADING-STRATEGY.md) |
| Agent operating rules | [AGENTS](AGENTS.md) |
| Recovery and scheduling | [Continuity](routines/CONTINUITY.md), [Automation prompt](routines/AUTOMATION-PROMPT.md) |
| Validation | [Validation record](data/evidence/2026-09-14-validation.md) |
| Chinese overview | [README Chinese](README.md) |

## Saved Status as of 2026-09-14

Credentials are locally configured. The most recent public connectivity check passed, but signed account and Stocks reads returned -2015. Sixteen automated tests passed; this does not establish authenticated access. SQLite records, concurrency protection and export recovery are implemented. The six-times-per-day schedule has 42 provisional occurrences; an app configuration card was rendered, but saving or activation has not been verified. The stop/fill draft is unapproved. There is no fill engine, continuous risk monitor or live order implementation. Paper cash is 20 USDT, with no positions.

Current authority: [readiness](state/readiness.json), [portfolio state](data/current-state.json), [automation status](routines/automation-status.json) and the latest evidence. This documentation organization did not call Binance again.

## Layout and Ownership

`docs/` contains strategy, integration, review and draft documents. `routines/` contains schedules and continuity. `scripts/` and `tests/` contain implementation and tests. `state/` tracks readiness; `data/` holds the paper portfolio, SQLite execution records, journals and evidence. Existing paths are preserved.

The original Alpaca PDF remains reference material, not the Binance implementation's instructions. Earlier work in the Documents project was not merged into the Desktop experiment. All subsequent project changes belong here. Both Chinese and English documents remain available.

Real credentials stay only in `binance-api.env`. Share `binance-api.env.example`, not the completed file, editor swap files or backups. Git ignore rules do not filter Finder copies or archives.
