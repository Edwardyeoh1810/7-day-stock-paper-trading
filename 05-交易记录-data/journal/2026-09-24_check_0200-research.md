# Research note / 研究记录 — 2026-09-24 02:00 (slot 2026-09-24_check_0200)

- Run: `2026-09-24_check_0200-research`
- Slot scheduled: 2026-09-24T02:00+08:00 — run started 02:03:47+08:00, decision ~02:14, engine 02:13:50. **On time, not a late run.** Twelfth consecutive on-time check since the 09:00 stall on 09-22.
- Account: **flat**, 5000 USDT cash and equity, no positions, no open orders, nothing to reconcile. No exit order has ever been placed in this experiment.
- Decision: **no_trade**. Best candidate BNBUSDT **long** — the first check of the experiment whose best candidate is a long.

## Headline

The 00:00 note asked a falsifiable question of the 16:05Z bounce. **The answer is "reclaimed, then lost again" —
766.72 was taken back at 17:15Z–17:25Z, held entirely for two bars, printed 767.92, and was lost on the 18:00Z
bar.** Per that note's own instruction the BNB short's premise is therefore **gone**, and it is stated explicitly
below. The long that replaces it failed four times over, and **the level is now a magnet touched eleven times in
165 minutes**, so no stop can be anchored there in either direction.

## Answering the 00:00 note's question

It asked: did the 16:05Z bounce build a higher low above 760.09 and **reclaim 766.72**, or fail underneath it and
roll over? Both branches partly fired, and the reclaim branch is the one that binds.

- **760.09 held.** Higher lows since: 762.63 (17:05Z) → 765.33 (17:35Z) → 767.09 (17:50Z).
- **The failure branch fired first.** 16:20Z–17:10Z made lower highs under the level — 766.65 → 766.03 → 766.08 →
  766.07 → 765.17 → 765.94 → 764.31 → 763.79 — bottoming at 762.63. That is exactly the re-armed short the 00:00
  note was hoping for.
- **Then the reclaim branch cancelled it.** 17:15Z went 763.74 → 766.44, a 0.354% body on **998,020 volume,
  ~2.5x its neighbours**. 17:25Z closed 766.89, the first close above. **17:45Z (L767.11) and 17:50Z (L767.09)
  traded entirely above the level**, and 17:50Z printed **767.92, the highest since 15:15Z**.
- **And then it was lost again.** 18:00Z: L765.63, C765.98. Price is 766.00–766.66 now — **pinned on the level.**

**Stated explicitly, as the 00:00 note required: the BNB short's premise is gone.** The lower-high sequence
769.49→769.03→768.27→766.70→764.05→762.97→761.64 that was the short's only premise ended at 16:05Z, briefly
re-formed, and has been **replaced by a higher-high sequence 766.44 → 766.92 → 767.26 → 767.30 → 767.57 →
767.92**. No short was priced this check.

**766.72 is now a magnet, which L-002 addresses directly.** Touched or crossed at 15:20Z L766.74, 15:25Z O766.74,
15:30Z H766.69, 15:35Z H766.70, 16:20Z H766.65, 17:20Z H766.92, 17:25Z C766.89, 17:30Z O766.89, 17:55Z L766.18,
18:00Z C765.98 and the live quote — **eleven touches in 165 minutes.** The honest read is chop on the level, not
a reclaim and not a failure.

## The noise floor, stated four ways (L-002)

Full preceding hour 17:05Z–18:05Z, twelve closed 5m bars: 0.234, 0.056, **0.403**, 0.064, 0.085, 0.163, 0.106,
0.244, 0.060, 0.108, 0.129, 0.207.

| measurement | N |
|---|---|
| full preceding hour | **0.403%** |
| setup-defining bar (17:15Z reclaim) | **0.403%** |
| excluding the setup bar | 0.244% |
| wider window incl. the 16:05Z bounce | 0.541% |

**This is the honest case where the first two coincide.** The largest bar of the preceding hour *is* the bar that
created the setup. L-002 warns that the setup bar is usually the largest and that a short window flatters exactly
the setups most likely to be taken; here no flattery is arithmetically possible. Everything below is priced
against **0.403%**, not the 0.244% that dropping the setup bar would give.

## L-006 — the first re-measurement that did NOT dissolve

The 00:00 note forecast in writing that both of its defining bars (15:35Z 0.415%; 16:05Z, which closed at
0.541%) would age out of the preceding hour by ~17:05Z and that **if nothing new printed** N would fall toward
0.20–0.27%, mechanically flattering tight stops.

**They did age out. N measured 0.403%, not 0.20–0.27%** — because something new *did* print: the 17:15Z reclaim
bar, a genuine 0.403% directional move on 2.5x volume. The forecast's arithmetic and, importantly, **its
conditional** were both correct.

**This is the first non-dissolving re-measurement examined under L-006.** It is recorded as a factual contrast
case only. **Whether it advances the lesson's clock is the review's call, not this check's**; the lesson bound in
full here and every window-derived figure was re-measured against the setup-containing window.

## Why the long was refused — four independent grounds

**1. L-004 target validity — the primary refusal, run before any ratio.** The only target that pays 1.5 net from
a noise-safe stop is **777.18** (the 12:00Z/13:00Z 1h lows, broken support turned resistance). It is reached
**only by jumping two levels that both rejected today**: 767.92, which rejected **twenty minutes before this
check**, and 769.03, which rejected three hours before it en route to the 760.09 low. This is the cleanest
instance of the rule yet, because one of the jumped levels rejected *inside the decision's own hour*.

**2. L-004 span screen on the honest tight stop — refused by 0.283pp.** Stop 762.40 (below the 17:05Z low from
which the reclaim leg launched) to the nearest structural target 769.03 = 6.63 points on a 766.51 entry =
**0.865%**. Required = 2.5N + 0.14% = 2.5(0.403) + 0.14 = **1.148%**. A **fourteen-fold wider miss** than the
0.020pp of the 00:00 check. Priced out, that construction pays **net 0.35**.

**3. L-003 requote — tenth consecutive material check, this time in the legitimate direction.** On the fixed
honest wide construction (stop 759.90 below the 24h low, target 777.18):

| quote (UTC) | ask | risk | reward | net RR |
|---|---|---|---|---|
| 18:04:48 | 765.98 | 6.08 | 11.20 | **1.666 — passes** |
| 18:07:14 | 766.51 | 6.61 | 10.67 | 1.452 |
| 18:08:33 | 766.70 | 6.80 | 10.48 | 1.383 |
| 18:09:51 | 766.50 | 6.60 | 10.68 | 1.455 |
| 18:13:50 (engine) | 766.19 | 6.29 | 10.99 | **1.577 — passes** |

**Only the first quote cleared the floor, by 0.166; had this check acted on it, its next three quotes all refuse
the trade.** This is the *legitimate* form — price advanced **away** from the stop, so risk grew 6.08 → 6.80
points while reward shrank — and chasing it means widening risk to hold the same target, which is equally a
refusal. **And then the engine's own sixth quote crossed back above the floor at 1.577.** The ratio oscillated
across the 1.5 floor **three times in 545 seconds on unchanged structure**, which is the lesson's whole point:
the number is not stable and is not information. The refusals in (1) and (4) are independent of it. Clock stays
at **zero**.

**4. L-005 execution — ninth consecutive check, refusing independently of all geometry.** Five sweeps in 303
seconds; top-of-book notional in USDT:

| | s1 18:04:48 | s2 18:06:46 | s3 18:07:14 | s4 18:08:33 | s5 18:09:51 |
|---|---|---|---|---|---|
| BTC bid | 45.42M | 44.89M | 44.80M | 24.07M | **244,485** |
| BTC ask | 2.56M | **84.20** | 35.52M | **70,831** | **33.70** |
| ETH bid | 4.80M | 1.08M | 342,355 | 3.21M | 98,598 |
| ETH ask | 13.00M | **29.31** | 4.96M | 29.96M | 1.00M |
| BNB bid | 851,314 | 554,693 | 4.97M | 2.33M | 39,979 |
| BNB ask | 1.50M | 28.31M | 9.00M | **7.67** | 1.20M |
| SOL bid | 2,904 | 255,713 | 26,272 | 2,205 | **19.42** |
| SOL ask | **17.14** | **11.41** | 116,028 | 115,040 | **51.42** |
| XRP bid | 4.24M | **267.47** | **247.07** | **247.17** | **22.29** |
| XRP ask | 1.40M | 1.39M | 1.39M | 22.36M | 1.49M |

**Not one of the five held both sides quoted across all five samples.** BNB is the **binding** one, because a
long **buys into the ask**: its ask printed **7.67 USDT (0.01 BNB) at sample 4**, so a maximum 2,500 USDT market
buy is **326x the entire visible ask** — and it printed that at 0.522 bps. **BNB had held both sides across
samples 1–3 and was the only contract to do so; it failed at sample 4**, so three healthy samples again meant
nothing. Its bid then fell 4,973,531 → 39,979 USDT, 124x.

- **XRPUSDT is the strongest persistence instance of the experiment**: bid unquoted on **four consecutive
  samples** (267.47 / 247.07 / 247.17 / 22.29 USDT) — a book that never returned inside the check, not a
  collapse-and-recover.
- **BTCUSDT gone on the ask at three of five** (84.20 / 70,831 / 33.70 USDT) while quoting **0.012 bps at sample
  4 — the tightest spread of the check, on a 70k then 34 dollar ask** — with its bid collapsing 24,070,823 →
  244,485 USDT in 78 seconds.
- **SOLUSDT unquoted on both sides at sample 5** (bid 19.42, ask 51.42).
- **ETHUSDT's ask printed 29.31 USDT at 0.60 bps** at sample 2 — the same pathology as 00:00 but on the opposite
  side. ETH has now been caught unquoted on the **bid** (00:00, five of five) and on the **ask** (this check).

**No contract breached the 25 bps cap this check. The cap was blind to all of it.**

**Recorded against interest:** the engine's own sixth quote at 18:13:50Z showed BNB healthy on *both* sides —
bid 14.1M, ask 52.4M USDT. That is the opposite of the 00:00 check, where the engine quote was among the worst
samples. It does not change the refusal (L-005 requires every sample to hold, and sample 4 did not), but it is a
sample that runs the other way and is recorded as such.

## Why no tighter stop rescues the ratio (L-002)

The only stop that would lift the tight construction over the floor is **765.20**, below the 17:35Z low: that is
**0.171% = 0.42x N — sub-noise** — and it sits *inside the 18:00Z bar's own range* (L765.63). **Both ends of
L-004's predicted trade-off observed again in one check**: the noise-safe stop kills the ratio, the
ratio-passing stop is a position size.

## Artifact scan — 5m, 1h, 4h and daily on all five (L-001)

- **BTCUSDT excluded, 18th consecutive check, and the contamination has not moved at all.** The 09-21 20:00Z 4h
  bar still reads O86,588.90 H**90,389.80** C86,523.40 — a 4.390% upper wick on a 0.076% body = **58.0x**, range
  4.717% = **4.5x** its frame median, both legs passing. The 09-21 daily bar still reads H**95,804.10** on an
  81,144.10 open — an **11.437% wick on an 18.147% range**, ~12x the daily median.
- **SOLUSDT excluded, 8th.** 106.67 is **still the live `low24h`** against a 114.13 last and a real session floor
  of 113.03 (09-23 14:00Z 1h low). SOL's 24h quote volume is 477,336,640 USDT against **102–137 billion** for the
  other four — ~250x smaller.
- **XRPUSDT excluded.** The 09-23 04:00Z 4h bar still carries a 4.191% upper wick on a 0.124% body = **33.9x**,
  and **`high24h` still reads 1.6855 against a 1.4951 last**. *Correction to the 00:00 note for the record:* it
  said the print exits the 24h window at 09-24 04:00Z, "between the 02:00 and 09:00 checks". **04:00Z on 09-24 is
  12:00 local, which is after the 09:00 local check (01:00Z), not between them.** The print is still in the
  window now and will still be there at 09:00.
- **ETHUSDT and BNBUSDT clean on all four frames** — the two readable contracts, as at 23:00 and 00:00. ETH's
  highest 4h wick/body is 9.2x on a 1.24x-median range and its highest 1h is 23.2x on a ~1.1x-median range: both
  fail the range leg. BNB's 19.4x daily doji sits on a *below-median* range, and the 17:10Z 5m bar reads 9999x
  only because its body is zero on a 0.056% range with 3,570 volume — a dead bar, not an artifact.

## Evidence gate — NOT passed, which breaks a run of two

For the long I can claim **`price_action`** (760.09 held; 766.72 reclaimed and held 17:25Z–17:55Z) and
**`volume`** (the 17:15Z reclaim bar at ~2.5x neighbouring volume; 16:05Z at 883,150).

But **`trend` runs firmly against the long** — daily closes 799.71 → 788.70 → 766.29, 24h −2.861%, lower highs
and lower lows on 4h since 09-21 — and **`market_context` runs against it too**: all five contracts are down
2.677% to 4.958% on the day and all five made fresh 24h lows about four hours before this check.

**Two categories support the direction and two contradict it.** The rule requires two *independent* categories
supporting the *same* direction; this check will not claim a gate passed on a bare count while the two strongest
categories point the other way. `derivatives` not claimed (funding clamped at +0.010000% on four and
0.00000000 on BNB; OI sampled once). `news` recorded not claimed: **the Trump-Xi summit and state dinner are
today, 2026-09-24**, so under the 24-hour hold anything opened here would be held *through* the event and would
have to be justified through it, not around it.

**This breaks the run of two consecutive checks in which evidence passed and geometry refused** — worth
reporting to the review alongside that earlier pattern.

## Against interest — the 00:00 declined short would have STOPPED OUT

The 00:00 check declined a BNB short with **stop 766.72**, target 757.90, at entries 761.52 and (drifted) 764.89.
Since that decision the high is **767.92** (17:50Z), and 766.72 was exceeded at 17:20Z (H766.92) and four more
times after; the low is 762.63, so **757.90 was never approached. Both constructions stop out.** This runs in
favour of the 00:00 refusal.

**L-002's re-test tally is NOT advanced** — it counts declined setups that would have *won*. It stands at **one
of three.** Both 23:00 constructions remain live: the declined short (766.74 / 780.90 / 757.90) saw a high of
767.92 and a low of 760.09, neither level; the declined long (766.85 / 758.55 / 780.90) saw the same extremes,
neither level, its stop again missed by 0.20%.

## Next task focus

Re-run the 766.72 question at 09:00 (01:00Z) from whatever structure exists then — **eleven touches in 165
minutes makes it a magnet, so the honest read is chop, not a reclaim and not a failure**, and no stop can be
anchored there in either direction. BNB and ETH stay the only two readable contracts; BTC, SOL and XRP stay
excluded. **XRP's 1.6855 will still be in the 24h window at 09:00** (it leaves at 12:00 local, not before) — and
when `high24h` does stop reading it, that is the window moving, not XRP becoming readable (L-006). Funding
settles 00:00Z = 08:00 local, an hour *before* the 09:00 check, and no check sits on it; the forecast test is
answered and must not be repeated. The summit is today — justify any entry **through** it. **Sample the book
five times minimum and read quantity before spread: BNB's ask printed 7.67 USDT this check at 0.522 bps.**
