# Research journal — 2026-09-21_check_2100-research

Companion to the generated journal entry for `2026-09-21_check_2100_paper`. The generated API journal and
evidence exports were not edited; research and corrections live here.

- **Timestamp and task id:** written 2026-09-21T13:18Z (21:18 Asia/Kuala_Lumpur), slot `2026-09-21_check_2100`.
- **What was done:** Read AGENTS.md, TRADING-STRATEGY.md, CONTINUITY.md, AUTOMATION-PROMPT.md, readiness.json,
  current-state.json, the 20:00 slot's research note and reviews/LESSONS.md. Ran the read-only observation for the
  due slot, re-researched all five watchlist contracts from the demo host's public endpoints (5m, 1h, 4h and 60
  daily bars, book, funding, open interest), re-tested the 20:00 note's two carried-forward items, worked through
  the one new candidate, and submitted a `no_trade` decision through `paper_engine.py`.
- **Why it was done:** The 21:00 slot was due (`due_slot: 2026-09-21_check_2100`, 240 planned slots) and no position
  was open, so a new entry was permitted if and only if every entry condition was met.
- **Timing:** Observation ran at 13:10Z (21:10 MYT), decision submitted at 13:14Z (21:14 MYT) — 14 minutes after the
  slot, well inside the 45-minute entry window. This run was **not** late; an entry would have been accepted had one
  qualified. The `no_trade` is a judgement on the setups, not a timing artefact.
- **Order proposed:** No.
- **Order placed:** No. No demo order was sent; the engine returned `status: no_trade`, `live_order_sent: false`.
- **Order filled:** No.
- **Current holdings:** None. Flat.
- **Current cash:** 5000 USDT. Demo wallet balance 5000.04174826 USDT.
- **Current risk:** 0 USDT open risk; 0 USDT realized today. No daily-limit or consecutive-stop constraint is near.
- **Evidence captured:** `05-交易记录-data/evidence/2026-09-21_check_2100.json` (read-only run),
  `05-交易记录-data/evidence/2026-09-21_check_2100_paper.json` (engine),
  `05-交易记录-data/evidence/2026-09-21_check_2100-research.json` (research).

## The two items the 20:00 note carried forward, both resolved

**ETHUSDT has deteriorated, not improved.** The 20:00 note named ETH as the contract to re-check first, because it
was the only one with a real level overhead (2771.00) and failed only on the 1.5 net reward/risk floor at 1.34. It
also said what would fix it: *a pullback toward the 2694-2700 area would make the same trade work on an honest
stop.* Price went the other way.

| | 20:00 | 21:00 |
|---|---|---|
| Entry (ask) | 2722.55 | 2739.52 |
| Stop (unchanged, structural) | 2693.00 | 2693.00 |
| Target (unchanged, 60d high) | 2771.00 | 2771.00 |
| Gross risk / reward | 29.55 / 48.45 | 46.52 / 31.48 |
| **Net reward/risk** | **1.34** | **0.55** |

One hour of advance moved the candidate further from qualifying. The condition that would have rescued it has not
occurred, and nothing about the stop or the target was adjusted to compensate.

**BTCUSDT's second artifact is now confirmed.** The 20:00 note flagged the 12:00Z BTC bar as an artifact *in
progress*. That bar has closed with its wick intact — 2.97% upper wick against a 0.73% body, open 84738.40, close
85353.30, no counterpart on any other contract in that hour. It is a confirmed third artifact for the day. BTC is
excluded again as structurally unreadable, quite apart from having no overhead daily reference.

A fresh scan of the last twelve 1h bars on all five contracts found **no new artifact this hour**. No bar other
than the three already on record shows a wick exceeding 1.5%.

## What is new: XRPUSDT finally has structure overhead

At 20:00 XRP was trading at 1.4886 *into* the 1.4894 swing high of 09-14 and failed at 0.89 net. It has since
cleared that level and trades at 1.4900. For the first time today, one contract in this complex sits below genuine
overhead daily structure — 1.5270 (08-24), 1.5441 (08-25), 1.5444 (08-23), 1.7000 (08-22). XRP is the laggard that
never recovered to its August prices, which is exactly why it has levels above it while BTC, BNB and SOL sit at
60-day highs with nothing there at all.

The arithmetic works, and this is the first time it has all day:

| | |
|---|---|
| Entry (ask) | 1.4900, spread 0.67 bps |
| Stop | 1.4700, below the 1.4710/1.4717 post-breakout lows and the broken 1.4894 |
| Target | 1.5270, the 2026-08-24 daily high |
| Gross risk / reward | 0.0200 / 0.0370 |
| Round-trip cost estimate | 0.002086 (14 bps) |
| **Net reward/risk** | **1.58 — clears the 1.5 floor** |

**It was still rejected, on the evidence requirement rather than the reward/risk.** The entry conditions need at
least two *independent* categories supporting the direction, and XRP has one observation counted twice:

- `trend` (XRP's uptrend) and `market_context` (the complex-wide move) are the same 08:00Z impulse. The strategy
  says these five contracts are five ways to express one view, and that evidence drawn over the same candles is one
  observation and not two. On a day when all five rose 5.1-8.3% together, they do not separate.
- `volume` **argues against**. XRP's breakout hour traded 3,834,343,687 against 3,979,635,555 the hour before —
  participation *contracted* on the move — and every hour since has been lower, down to 3,445,568,944.
- `price_action` gives no trigger. 1.4900 is the middle of a four-hour 1.4847-1.4969 range, not a break and retest
  or a rejection at a level. The 20:00 note refused an ETH stop chosen for size rather than for invalidation; the
  same discipline refuses an entry price chosen for convenience rather than for structure.
- `derivatives` is permissive, not supportive: funding at the 0.0100% baseline says only that longs are not
  crowded. See the data-quality note below on why it cannot be counted here at all.

Two secondary concerns, recorded but not the basis of the rejection. The 1.58 survives only at the tightest
defensible stop — 1.51 at a 1.4690 stop, 1.29 at 1.4650 — so there is no room for worse slippage than assumed. And
the check sits eighteen minutes before the 21:30 MYT US open, which the strategy names as erratic, with an
exchange-side stop 1.34% away triggering on the mark price in an environment that has printed three multi-percent
wicks today.

A footnote that supports the mid-range read: by the time the engine sampled the book at 13:15Z, three minutes
later, XRP had already traded back to 1.4872/1.4878 — toward the low of the same range.

## Data quality note: open interest is unmeasurable on the demo host

`/futures/data/openInterestHist` returns an empty response for every symbol on `demo-fapi.binance.com`. Only the
absolute snapshot at `/fapi/v1/openInterest` is available, and its magnitudes are not usable as a series
(XRPUSDT reads 15,600,795,069,537.4). The `derivatives` category on this project therefore reduces in practice to
funding rate and next funding time; the open-interest *change* that the strategy lists as part of that category
cannot be observed here. This is a standing limitation, not a condition of today. Worth the 22:00 review's
attention for `PROPOSALS.md` — it is not something to change here.

## Market state at the check

The complex extended a further 0.2-1.0% in the hour, still moving as one: SOL +8.25% (was +7.21%), XRP +8.16%
(+7.57%), ETH +6.08% (+5.57%), BTC +5.87% (+5.74%), BNB +5.15% (+4.93%). SOL printed a new 24h and 60-day high at
117.31 in the 13:05Z 5m bar on 45,994 against 1,904 and 2,051 in the two bars before it — the cleanest volume
signature on the board for a second consecutive check, and still with nowhere to aim. Funding is at or below the
0.010% baseline on all five with the next funding at 16:00Z; BTC remains negative at -0.0038%. Spreads are tight
everywhere: BNB 0.38, BTC 0.43, XRP 0.67, SOL 1.71, ETH 1.93 bps. No scheduled macro, regulatory or exchange event
was identified in the next 24 hours.

## Next task focus

Account is flat, so the 22:00 check may open a new position if the conditions are met. Three things to carry
forward.

1. **XRPUSDT is the contract to re-check first**, replacing ETH in that role. It is the only one with real overhead
   structure and it already clears the reward/risk floor; what it lacks is a price-action trigger and volume. The
   two prices that would change the answer are **1.4969** (today's high — a break *and hold* above it, on expanding
   volume, would supply the trigger that mid-range does not) and **1.4847/1.4894** (a retest that holds would give a
   better entry and a wider margin over the floor). A break on contracting volume is not a trigger.
2. **ETHUSDT only works on a pullback** toward 2694-2700, and moved away from it this hour. Do not re-test it at a
   higher price without re-deriving the stop from structure.
3. **BTC remains excluded** while artifacts print; three confirmed today. BNB and SOL remain untradeable for lack of
   any overhead reference, however good SOL's volume looks — a target has to exist before reward/risk means
   anything.

The 22:00 check is also the daily review slot; that task owns `reviews/` and may run concurrently.

## Human confirmations needed

None for demo paper trading; live trading remains disabled. Three items for Edward's awareness, none requiring
action before the next check: the open-interest endpoint limitation described above; the recurring BTCUSDT demo
price artifacts, now three for the day; and the missed 16:00 slot that the 20:00 note recorded, which remains a
coverage question for the review rather than something to fix here.
