# Research journal — 2026-09-21_check_2200-research

Companion to the generated journal entry for `2026-09-21_check_2200_paper`. The generated API journal and
evidence exports were not edited; research and corrections live here.

- **Timestamp and task id:** written 2026-09-21T14:20Z (22:20 Asia/Kuala_Lumpur), slot `2026-09-21_check_2200`.
- **What was done:** Read AGENTS.md, TRADING-STRATEGY.md, CONTINUITY.md, AUTOMATION-PROMPT.md, readiness.json,
  current-state.json, the 21:00 slot's research note and reviews/LESSONS.md. Ran the read-only observation for the
  due slot, re-researched all five watchlist contracts from the demo host's public endpoints (5m, 1h and 60 daily
  bars, book, 24h ticker, funding), tested the two price conditions the 21:00 note named in advance for XRPUSDT,
  re-tested ETHUSDT now that its required pullback has occurred, re-verified the 60-day overhead scan for all five,
  and submitted a `no_trade` decision through `paper_engine.py`.
- **Why it was done:** The 22:00 slot was due (`due_slot: 2026-09-21_check_2200`, 240 planned slots) and no position
  was open, so a new entry was permitted if and only if every entry condition was met.
- **Timing:** Observation ran at 14:10Z (22:10 MYT), decision submitted at 14:14Z (22:14 MYT) — 14 minutes after the
  slot, well inside the 45-minute entry window. This run was **not** late; an entry would have been accepted had one
  qualified. The `no_trade` is a judgement on the setups, not a timing artefact.
- **Order proposed:** No.
- **Order placed:** No. No demo order was sent; the engine returned `status: no_trade`, `live_order_sent: false`.
- **Order filled:** No.
- **Current holdings:** None. Flat.
- **Current cash:** 5000 USDT. Demo wallet balance 5000.04174826 USDT.
- **Current risk:** 0 USDT open risk; 0 USDT realized today. No daily-limit or consecutive-stop constraint is near.
- **Evidence captured:** `05-交易记录-data/evidence/2026-09-21_check_2200.json` (read-only run),
  `05-交易记录-data/evidence/2026-09-21_check_2200_paper.json` (engine),
  `05-交易记录-data/evidence/2026-09-21_check_2200-research.json` (research).

## XRPUSDT: the breakout failed

The 21:00 note did something useful — it wrote down in advance exactly what would change the answer, so this hour
is a test rather than a re-argument. It named two triggers, and a warning:

> The two prices that would change the answer are **1.4969** (today's high — a break *and hold* above it, on
> expanding volume) and **1.4847/1.4894** (a retest that holds would give a better entry). A break on contracting
> volume is not a trigger.

Neither happened. 1.4969 was never revisited and still stands as today's high from the 11:00Z hour. The retest did
not hold — it broke. The 14:05Z 5m bar took out the 1.4847 floor of the four-hour range and printed **1.4765**, and
price is back **below the 1.4894 swing high of 09-14** that the 21:00 note had recorded XRP as clearing. The level
it broke above one hour ago is overhead again. By the time the engine sampled the book at 14:14Z it was 1.4804/1.4805,
lower still.

The third possibility the note did not enumerate is the one that occurred: a failed breakout.

**The arithmetic improved, and that is not a reason to buy.** On the same structural stop and the same target:

| | 21:00 | 22:00 |
|---|---|---|
| Entry (ask) | 1.4900 | 1.4824 |
| Stop (unchanged, structural) | 1.4700 | 1.4700 |
| Target (unchanged, 08-24 daily high) | 1.5270 | 1.5270 |
| Gross risk / reward | 0.0200 / 0.0370 | 0.0124 / 0.0446 |
| **Net reward/risk** | **1.58** | **3.43** |

The ratio more than doubled for exactly one reason: price fell 0.51% toward a fixed stop and compressed the risk
leg. The number improved *because the market moved against the thesis*. Reading that as a green light is the mirror
image of choosing a stop to fit a desired size, which the strategy prohibits.

**The evidence test, which is what rejected XRP at 21:00, now fails by more.**

- `price_action` has flipped from neutral to **against**. At 21:00 the complaint was that 1.4900 was mid-range with
  no trigger. Now there is a trigger and it points down.
- `volume` has flipped the same way. The 21:00 note's complaint was contraction through the whole advance
  (3,834,343,687 on the breakout hour, declining to 3,445,568,944). Participation finally expanded this hour —
  4,089,988,720 in the 13:00Z hour — but the largest 5m bar of the last seventy minutes, **519,907,895 at 14:05Z**,
  is the down bar that broke the range. Expansion on the break of the range low confirms the failure.
- `trend` and `market_context` remain one observation, not two, and `market_context` has itself weakened (below).
- `derivatives` is permissive, not supportive, and reduces to funding on this host.

One supporting category at most, against a requirement of two independent ones.

**A separate and sufficient reason to decline even if the categories had been there.** The 1.4700 stop is now only
0.84% below the entry, while the 14:05Z 5m bar alone spanned 1.4765–1.4891, a 0.85% range. The stop sits inside one
five-minute bar of the current tape, and it would rest on an exchange that has printed four artifacts today,
triggered on the mark price.

## ETHUSDT: the pullback happened, and it still fails at 1.40

This is the one candidate that genuinely improved and the closest call of the day. The 21:00 note said ETH only
works on a pullback toward 2694–2700 and that it had moved the other way. It has now partly come back.

| | 20:00 | 21:00 | 22:00 |
|---|---|---|---|
| Entry (ask) | 2722.55 | 2739.52 | 2723.87 |
| Stop (unchanged, structural) | 2693.00 | 2693.00 | 2693.00 |
| Target (unchanged, 08-21 daily high) | 2771.00 | 2771.00 | 2771.00 |
| Gross risk / reward | 29.55 / 48.45 | 46.52 / 31.48 | 30.87 / 47.13 |
| **Net reward/risk** | **1.34** | **0.55** | **1.40** |

**Rejected on the 1.50 floor.** 1.40 is not rounded up, and the stop is not moved to 2700.00 to manufacture the
difference — that would place it inside the very level whose break defines the setup. The margin is also far too
fine to stretch for: the entry that produces exactly 1.50 is **2722.68**, just 1.19 below the current ask, which is
less than one 5m bar of ETH noise and comparable to what the 9.29 bps spread implies in slippage. Volume does not
support it either, contracting to 2,106,222 from 2,218,225.

ETH has now failed on the same arithmetic at three consecutive checks: 1.34, 0.55, 1.40.

## BTCUSDT: a fourth artifact, and the book is deteriorating

The **13:50Z 5m bar** opened 85377.20, closed 85448.00 and printed an 86769.40 high on 4,072 of volume — a 1.55%
upper wick with no counterpart anywhere in that window (ETH +0.16%, SOL and XRP similar). It carries into the
13:00Z 1h bar as a 1.66% upper wick against a 0.06% body. Fourth confirmed artifact of the day, third on BTC.

Independently, **BTC's spread has widened from 0.43 bps at 21:00 to 15.37 bps** — 61% of the 25 bps limit, while
the other four sit between 0.85 and 9.83 bps. Two separate signs that this contract's book is not behaving.

A scan of the last fourteen 1h bars on the other four contracts found **no new artifact**; no wick exceeds 1.5%.
XRPUSDT, the contract worked through this check, has produced no artifact at any point today.

## The 60-day overhead scan, re-verified

Re-run from daily bars rather than carried forward, because it is the single fact that eliminates three of five
contracts:

| | Spot | Daily highs above spot in 60 days |
|---|---|---|
| BTCUSDT | 85450.00 | only today's 95804.10 — which is the artifact itself |
| BNBUSDT | 793.54 | only today's 797.64 |
| SOLUSDT | 117.98 | only today's 118.52 |
| ETHUSDT | 2723.87 | 2771.00 (08-21), then today's 2850.00 artifact |
| XRPUSDT | 1.4824 | 1.4894 (09-14), 1.4969 (today), 1.5270 (08-24), 1.5441, 1.5444, 1.7000 |

BNB and SOL both printed new 24h and 60-day highs at 14:05Z (797.64 and 118.52) and gave them back inside the same
bar. A target has to exist before reward/risk means anything.

## The complex turned lower

For the first time today the complex gave back ground rather than extending. Four of five fell against the 21:00
readings: XRP +7.18% (was +8.16%), ETH +5.67% (6.08%), BTC +5.67% (5.87%), BNB +5.04% (5.15%). SOL alone extended,
+8.82% (8.25%). **XRP went from the second strongest of the five to the weakest in one hour**, which is exactly the
relative-strength reading the strategy asks for, and it is negative for the contract under consideration.

Funding is at or below the 0.0100% baseline on all five with the next settlement at 16:00Z, about 1.8 hours out;
BTC has turned positive (0.0021%) from negative at 21:00, so a BTC long would now pay rather than receive.

## A short was reconsidered, and rejected

XRP's failed breakout is the first genuinely bearish price-action item this experiment has seen, so it was worked
through rather than dismissed. Best-constructed version: short 1.4819, stop 1.4920 above the 14:00Z hourly high,
target 1.4717 at the post-breakout low — risk 0.0101 against reward 0.0102, **net 0.80**, failing the floor
outright. Stretching the target to 1.4383 would clear the ratio but would require the whole day's impulse to
reverse inside the 24-hour limit, and is a target invented to satisfy arithmetic.

It fails the evidence test regardless. Only `price_action` points down; `trend` and `market_context` both argue
against; funding at or below baseline on all five means there is no crowded long positioning to squeeze. The
strategy says shorting is not a reaction to a red candle, and one failed breakout in a complex still up 5–9% on the
day is exactly that.

## Next task focus

Account is flat, so the 23:00 check may open a new position if the conditions are met. Three things to carry
forward.

1. **ETHUSDT is now the contract to re-check first**, replacing XRP in that role. It is the only one that both has
   real overhead structure and is close to the floor: it needs an ask of **2722.68 or lower** to reach 1.50 net on
   the unchanged 2693.00 stop and 2771.00 target, and roughly **2710** to have any real margin. It is 1.19 away.
   Two cautions. Because the ratio is so sensitive to the entry, a pass must not be claimed on a price that has
   drifted by the time the decision is submitted — quote it at decision time. And a *fall* that clears the floor by
   pushing the entry down is worth less than one where the evidence also arrives; ETH volume is contracting.
2. **XRPUSDT is now the failed-breakout case, not the long candidate.** Do not re-open it as a long until price is
   back above **1.4894** *and holding*, with volume on the up bars rather than the down ones. If instead it keeps
   losing ground, the level that matters below is **1.4710/1.4717**; a break of that would put the 08:00Z impulse
   itself in question and would be worth re-examining as a short — but only with a second category, which does not
   exist today.
3. **BTC remains excluded** — four artifacts now, and a spread that widened 36-fold in an hour. **BNB and SOL remain
   untradeable** for lack of any overhead reference; both made and immediately lost new highs this hour, which does
   not change the structural point.

The complex turning lower for the first time today is the single most important change to watch at 23:00: if it
continues, the question shifts from which long qualifies to whether the 08:00Z impulse is being given back, and a
long is then harder to justify, not easier.

## Human confirmations needed

None for demo paper trading; live trading remains disabled. Three items for Edward's awareness, none requiring
action before the next check: the recurring BTCUSDT demo price artifacts, now four for the day, together with the
36-fold spread widening on that contract; the standing open-interest endpoint limitation, which keeps the
`derivatives` category reduced to funding alone; and the missed 16:00 slot recorded by the 20:00 note, which
remains a coverage question for the review rather than something to fix here. The 22:00 daily review owns
`reviews/` and may be running concurrently; nothing in that folder was modified.
