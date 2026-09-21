# Research journal — 2026-09-21_check_1200-research

Companion to the generated journal entry for `2026-09-21_check_1200_paper`. The generated API journal and
evidence exports were not edited; corrections live here.

- **Timestamp and task id:** written 2026-09-21T11:40Z (19:40 Asia/Kuala_Lumpur), slot `2026-09-21_check_1200`.
- **What was done:** Read AGENTS.md (both languages present), TRADING-STRATEGY.md, schedule.json, CONTINUITY.md,
  readiness.json, current-state.json, the latest journal and reviews/LESSONS.md. Ran the read-only observation for
  the due slot, researched all five watchlist contracts from the demo host's public endpoints, checked news, and
  submitted a `no_trade` decision through `paper_engine.py`.
- **Why it was done:** The 12:00 slot was due (`due_slot: 2026-09-21_check_1200`, 180 planned slots) and no
  position was open, so a new entry was permitted if and only if two independent evidence categories agreed.
- **Order proposed:** No.
- **Order placed:** No. No demo order was sent; the engine returned `status: no_trade`, `live_order_sent: false`,
  `demo_order_sent: false`.
- **Order filled:** No.
- **Current holdings:** None. Flat.
- **Current cash:** 5000 USDT.
- **Current risk:** 0 USDT open risk; 0 USDT realized today.
- **Evidence captured:** `05-交易记录-data/evidence/2026-09-21_check_1200.json` (read-only run),
  `05-交易记录-data/evidence/2026-09-21_check_1200_paper.json` (engine), and
  `05-交易记录-data/evidence/2026-09-21_check_1200-research.json` (research and correction).

## Decision

`no_trade`. Trend and market context pointed up; price action and volume pointed down. No two independent
categories agreed on a single direction, so the two-category entry condition was not met. The best long candidate
(BNBUSDT, strongest 24h move and tightest spread) also failed the 1.5 net reward/risk floor once the stop was
placed on real structure below the 764.61 higher low, because the resulting target sat above the 785 high that had
just rejected the whole complex on expanding volume. Tightening the stop to 772.78 would have been choosing a stop
to fit a position size, which the strategy prohibits. A short was rejected because it would have traded against a
clear daily uptrend with only price action behind it.

## Two issues the 22:00 review should see

**1. The run stalled across slots.** The observation ran at 04:10Z (12:10 MYT, inside the 30-minute grace), but the
session then paused for about 7.5 hours and the decision was only submitted at 11:37Z (19:37 MYT) — roughly 7 hours
after the 12:00 slot's grace expired. Host clock and demo exchange server clock agree independently, so the timing
is not in doubt. No position was open at any point, the decision was `no_trade`, no order was sent and no historical
trade was backfilled, so there is no position or accounting consequence. The open process question — whether a
stalled run should still submit a decision once the slot grace has passed, or abort and leave the slot unrecorded —
belongs in `reviews/PROPOSALS.md` and is the user's call.

**2. A factual correction to the decision thesis.** The thesis claimed the demo host diverged materially from
third-party reporting (demo BTC 81,427 against reported ~85,000). That is wrong: the gap was time, not venue. At
11:37Z the demo host itself quoted BTC 84,696 and ETH 2,721, matching the reporting. The decision's market data was
simply stale by the time it was submitted. The `no_trade` action stands and remains correct — stale and conflicting
data is precisely a no-trade case — but the thesis should not be read as a valid assessment of the 19:37 MYT market.

For the record, the conflict resolved upward: by 11:37Z every one of the five had broken through the level that
rejected it (BTC through 81,981; ETH through 2,700 to a 2,850 high; BNB through 785 to 791.7; SOL through 113.17 to
116.55; XRP through 1.4359 to 1.4969). The long was there in hindsight. It was not takeable under the rules at
12:10 MYT, and this note is not an argument for loosening them.

## Data quality flag

The demo host's BTCUSDT 1h bar opening 09:00Z prints a high of 95,804.10 against an open of 83,753.50 and a close
of 84,625.90 — an approximately 14% wick with no counterpart in the other four contracts, which also contaminates
the 24h high field. It looks like a thin simulated-book print. This matters beyond cosmetics: exchange-side stop and
take-profit orders on this account trigger on the mark price in the same environment, so a structural stop placed
near such an extreme could be triggered by an artifact.

## Next task focus

The 20:00 Asia/Kuala_Lumpur check was not yet due when this was written and was deliberately left to its own
scheduled run; no decision was made on the 11:37Z data. Account is flat, so that check may open a new position if
two independent categories agree. Note that the complex is now extended after a 5-8% day across all five, which
argues for more selectivity, not less, on a long at these levels.

## Human confirmations needed

None for demo paper trading; live trading remains disabled. Two items for Edward's awareness, neither requiring
action before the next check: the scheduled-run stall described above, and the demo-host price artifact.
