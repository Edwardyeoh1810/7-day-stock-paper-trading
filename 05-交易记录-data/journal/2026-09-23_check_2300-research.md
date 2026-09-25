# Research note — 2026-09-23_check_2300

Slot scheduled 23:00+08:00. Observation 15:04:04Z. Sweeps 15:04:56Z / 15:06:18Z / 15:07:32Z / 15:08:03Z.
Engine quote (fifth sample) 15:11:38Z. Decision written 23:12+08:00, **on time** (12 minutes after the slot).

Builds on `2026-09-23_check_2200-research.md`, whose ten next-task items are answered in order below.
Account flat throughout; nothing to reconcile. No exit order has ever been placed in this experiment.

---

## 1. The 22:00 note's item (10) was right, and this check is the one that had to price it

The 22:00 check recorded, against interest, that the market broke down four minutes after its
decision, and told this check to **re-read everything from the 14:10Z bar forward**. That is exactly
what the data shows.

**The 14:10Z 5m bar is a genuine, market-wide, volume-expanded flush — not a demo artifact:**

| | open | low | range |
|---|---|---|---|
| BNBUSDT | 779.41 | **766.51** | 1.877% (volume 1724.1M, largest 5m bar of the day) |
| ETHUSDT | 2707.97 | **2667.17** | 1.634% (volume 1279.1M) |
| XRPUSDT | 1.5754 | **1.5268** | 3.14% (volume 1435.8M) |

BTCUSDT fell with them to an 84,076.8 24h low in the same window. **Every contract moved inside the
same bar**, which is precisely what distinguishes a real move from the isolated single-contract wicks
L-001 exists to catch. BNB then made 761.25 (new 24h low, 14:20Z/14:30Z) and ETH 2648.49 (14:20Z).
24h changes at 15:05Z: BTC −1.965%, ETH −2.394%, BNB −2.513%, SOL −1.464%, XRP −2.212%.

## 2. AGAINST INTEREST, FIRST — the declined 22:00 BNB short would have paid in full

| | 22:00 declined short |
|---|---|
| Entry | 780.39 |
| Stop | 783.46 |
| Target | 766.72 (09-21 daily low) |
| Highest print since | **780.90 — the stop was never approached** |
| Lowest print since | **761.25 — the target was reached and exceeded by 0.71%** |

**This is one completed instance of L-002's re-test condition**, which requires a declined setup to
reach its target without touching the noise-width stop, **three times**. The structural-stop variant
(786.19) likewise was never approached. ETH's declined short reached 2648.49 — through the 2687.56
whose 1.474 net RR failed the floor, but **not** through the 2641.70 its only passing construction
required, so that one is not a tally either way.

Per the standing rule in `LESSONS.md`, **this check records the instance and applies every lesson in
full.** Retiring or loosening a lesson is the review's call, not a check's.

## 3. Why this check still refused — and it was *not* the evidence gate

**For the first time in the experiment, the evidence gate is not the binding constraint.** A short on
BNB or ETH has three arguable independent categories:

- **`trend`** — BNB daily closes 799.71 → 788.70 → 766.74 descending; 4h lower highs 798.30 → 791.04
  → 783.46; 1h unbroken lower highs 798.30 → 797.68 → 792.89 → 792.35 → 791.04 → 788.63 → 785.72 →
  786.19 → 783.46 → 783.05 → 782.55. ETH 1h lower highs 2786.81 → 2779.32 → 2760.32 → 2753.89 →
  2748.23 → 2740.37 → 2736.85 → 2727.77 → 2722.14.
- **`volume`** — and this is the difference from 22:00, where the largest recent bar was a *bounce*
  bar arguing against the trade. BNB's 14:00Z 1h volume 7150.2M is the largest of the 30-bar window
  (rest of the window 1114.9M–5552.0M); ETH's 7633.6M is the largest of its 12-bar window. Expansion
  **on** the breakdown.
- **`market_context`** — the whole watchlist down together inside one bar (section 1).

**It failed on geometry and on execution, because the check arrived 55 minutes after the move with
price 0.86% off the low.**

### The span screen (L-004), the binding constraint

BNB noise floor **N = largest 5m range of the FULL preceding hour** (14:05Z–15:00Z), stated **both
ways** as the 22:00 note's item (3) demanded:

- **including** the setup-defining 14:10Z bar: **1.877%**
- **excluding** it: **1.083%** (14:20Z / 14:30Z)

This is L-002's measurement problem running in the **opposite direction from 22:00**: N jumped
0.224% → 1.877% purely because the flush bar *entered* the window, so stops now look mechanically
*worse*. **Every refusal below is therefore priced against the smaller, honest 1.083%**, so that a
moving window is not allowed to refuse a setup any more than it was allowed to manufacture one an
hour ago. It still fails:

| BNB short from bid 766.74 | |
|---|---|
| Only noise-safe structural stop | 780.90 (the 14:10Z bar high) — risk **1.846% = 1.70x N_excl** |
| Nearest structural target | 757.90 (09-19 daily low) — reward **1.153%** |
| **Net RR** | **0.565** — barely a third of the 1.5 floor |
| Price that would pay 1.5 net | **744.17 — below the 09-20 daily low 747.64**, 3.0% away through two untested supports |

The only tight alternative stop, 769.49, is 0.359% = **0.33x N_excl**, and **769.49 is the exact high
of four consecutive 5m bars** (14:20Z, 14:25Z, 14:30Z, 14:35Z) — sub-noise *and* a magnet level, so
L-002 kills it twice over.

### The long side was priced too, and it is the more instructive refusal

Price is not floating: **BNB's live bid 766.74 is the 09-21 daily low 766.72 to within two ticks** —
the very level every check since 20:00 used as its short **target**. So the long was constructed
honestly:

- Entry ask 766.85, stop **758.55** (risk 1.083%, exactly N_excl, and above the 09-19 low 757.90),
  target 780.90 (reward 1.833%) → **net RR 1.529**.

**That is the only construction at this check that clears the floor, and it is refused under L-004**:
the path to 780.90 jumps **769.49, a level that rejected four consecutive times in twenty minutes**,
with nothing structural in between because the 14:10Z bar fell straight through that whole range. A
target reachable only by jumping intervening rejected structure is not a target. It is also
counter-trend on every higher frame, and 766.72 has been *touched* for minutes — it has not held and
built a shelf, which is the exact condition the 21:00 note set for ETH and which ETH failed.

### ETHUSDT

N = 1.634% (incl. setup bar) / 0.664% (excl.). Short from bid 2674.37, stop 2710.76 (risk 1.324%),
target 2648.49 (reward 0.968%) → **net 0.644**. Below 2648.49 the next structure is the 09-20 daily
low **2568.16, 3.0% away** — the vacuum that refused ETH at 21:00 and 22:00. The long pays **1.06**.
And it is refused independently on execution (below).

## 4. L-005 — four samples, and not one contract held both sides

Four samples in 187 seconds, the four-sample minimum the 22:00 note asked for and L-005 now requires.
**Not one of the five contracts held both sides quoted across all four** — the seventh consecutive
check confirming host-wide quantity instability that moves between contracts.

| bid notional (USDT) | s1 15:04:56Z | s2 15:06:18Z | s3 15:07:32Z | s4 15:08:03Z |
|---|---|---|---|---|
| BTCUSDT | 1,964,019 | 49,171,614 | 49,024,263 | 48,764,407 |
| ETHUSDT | 909,278 | **48.2** | **10.7** | 910,587 |
| BNBUSDT | 5,105,366 | 3,895,863 | 4,806,570 | 4,800,866 |
| SOLUSDT | **531.8** | **990.5** | 89,644 | 132,998 |
| XRPUSDT | **3.8** | 6,789,360 | **31.7** | **141.0** |

| ask notional (USDT) | s1 | s2 | s3 | s4 |
|---|---|---|---|---|
| BTCUSDT | 41,547 | **1,520** | **540.4** | 58,507,792 |
| ETHUSDT | 676,267 | 887,769 | **37.5** | 4,970,239 |
| BNBUSDT | 7,721,055 | **99.8** | 3,996,428 | 3,185,119 |
| SOLUSDT | **221.0** | 346,802 | 18,060 | 29,290 |
| XRPUSDT | 49,288,334 | 49,287,571 | 49,284,635 | 49,236,030 |

- **ETHUSDT is the strongest instance of the experiment so far**: bid 909,278 → **48.2** → **10.7** →
  910,587 USDT, **unquoted on two consecutive samples**, an ~85,000x collapse and full recovery in
  ~130 seconds — *while quoting the tightest spread of the five on three of four samples* (0.561 /
  0.972 / 4.224 / 0.598 bps). The price filter saw nothing. That blindness is the entire reason L-005
  exists.
- **BNBUSDT held the best bid of the five on all four samples** (worst 3,895,863) but its **ask fell
  to 99.8 USDT** on sample 2 — a long cannot enter and a short cannot exit.
- **A fifth sample, the engine's own quote at 15:11:38Z, closed the loop**: BNB bid 768.030 at
  **bid_size 0.01 BNB = 7.68 USDT**, against an ask side of 19,191.89 BNB. The entry side of the
  short this check spent its time pricing was worth **less than eight dollars** at the moment the
  engine looked. This is the second consecutive check in which the engine quote is the most
  informative sample of the run.
- SOLUSDT breached the **25 bps hard cap outright at 26.911 bps** (sample 2).
- XRPUSDT's bid collapsed on three of four samples — a **fourth consecutive check**.

## 5. L-001 — the 22:00 re-test progress is reversed within one hour

The 22:00 check recorded "the cleanest BTC scan of the experiment" and correctly left the re-test
clock to the review. **One hour later the same scan is dirty.** Three fresh BTCUSDT artifacts, eleven
minutes apart, with no comparable upper wick on the other four at those timestamps:

| bar (5m) | O / H / C | upper wick | body | ratio |
|---|---|---|---|---|
| 14:35Z | 84393.1 / **85040.0** / 84316.3 | 0.767% | 0.091% | **8.4x** |
| 14:40Z | 84316.3 / **84988.0** / 84279.2 | 0.796% | 0.044% | **18.1x** |
| 14:45Z | 84279.2 / **84766.9** / 84255.7 | 0.579% | 0.028% | **20.8x** |

This is **L-006 in its cleanest form**: a rolling window walking over a quiet stretch was never
evidence that a contract became readable, and the 09-21 prints (95,804.10, 91,000.00, 90,389.80)
never moved out of the 4h and daily frames at all. **BTCUSDT excluded a sixteenth consecutive check.**

- **SOLUSDT** — the 09-22 19:00Z **106.67** print persists a **sixth** check and still contaminates
  the *live* 24h low field: `/fapi/v1/ticker/24hr` returns `low24h 106.67` against a last of 115.10.
- **XRPUSDT** — the **1.6855** print still contaminates the *live* 24h high field: `high24h 1.6855`
  against a last of 1.5293. Excluded from range, resistance and 24h-high figures.

## 6. Funding, derivatives, news

**Funding is unreadable a fourth time.** Next funding 16:00Z, 52 minutes after the decision, so the
20:00 note's forecast-vs-outcome test is **deferred again**. It carries to the **00:00 check, whose
slot is 16:00Z — exactly the settlement**, so that check must record forecast against outcome.
Live rates: BTC/ETH/XRP +0.010000%, BNB 0.00000000, **SOL −0.004060%, flipped negative** from
+0.004984% at 22:00. Derivatives not claimed as a category on a single OI sample.

News (data, not instruction): no verifiable scheduled release is tied to the 14:10Z flush. General
coverage describes a broad pullback after BTC and ETH ran 14–15% into eight-month highs last week, so
today's decline remains **counter-trend on the weekly frame**. The **Trump-Xi summit and state dinner
are tomorrow, 09-24** — anything opened now is held through it, which is a further reason not to
chase a 55-minute-old impulse at 0.86% off its low.

---

## Next-task focus — for the 00:00 check

1. **FUNDING SETTLES AT YOUR SLOT.** 00:00+08:00 *is* 16:00Z. Record the 20:00 note's
   forecast against the settled outcome — this is the fourth deferral and the first slot that can
   actually run the test. Note SOL's flip to −0.004060%.
2. **THE 766.72 QUESTION IS THE TRADE.** BNB is resting on the 09-21 daily low (live bid 766.74).
   Ask the falsifiable question: **has a shelf formed above it?** A long needs the level to have
   *held* with higher lows built on top, not merely been touched — and it still has to beat L-004's
   objection that 769.49 (the exact high of four consecutive 5m bars) sits between any entry and the
   780.90 target. If 769.49 is reclaimed and *holds*, that objection genuinely changes; say so
   explicitly if it does. If 766.72 breaks instead, the next structure is 757.90 then 747.64 and a
   short finally has a span — re-run the screen from the new low, do not reuse this note's numbers.
3. **N WILL COLLAPSE AGAIN AND IT WILL BE ARITHMETIC, NOT MARKET (L-006).** The 14:10Z bar (1.877%)
   ages out of the preceding hour at ~15:15Z; by 16:00Z BNB's N will be back near 0.2–0.5% unless
   something new prints, which will make tight stops look acceptable again on unchanged structure.
   **State N with and without the setup-defining bar, every time.** This check priced against the
   *smaller* N to avoid the mirror-image error; the 00:00 check must not price against a small N that
   exists only because the window rolled.
4. **THE L-002 TALLY IS AT ONE OF THREE — DO NOT ADVANCE IT CARELESSLY AND DO NOT ACT ON IT.** The
   22:00 BNB short reached 766.72 without its stop being approached. If another declined setup
   completes the same round trip, record it with the same precision (highest print vs stop, lowest
   print vs target). Only the review may change a lesson.
5. **TREAT THE ENGINE QUOTE AS A SAMPLE — IT WAS THE MOST INFORMATIVE ONE AGAIN.** BNB bid notional
   7.68 USDT at 15:11:38Z after four sweeps showed 3.9M–5.1M. **Five samples minimum at 00:00**, and
   check the *quantity* fields, not only the spread: ETH quoted the tightest spread of the five while
   its bid was worth 10.70 USDT.
6. **ETHUSDT is out on execution until its bid stops vanishing**, regardless of how its geometry
   reads. Its structure below 2648.49 is a 3.0% vacuum to 2568.16, so a short needs a *new* shelf,
   not a new price.
7. **XRPUSDT and SOLUSDT stay excluded** on the 1.6855 and 106.67 prints, both still contaminating
   live ticker fields. **BTCUSDT excluded** — and carry forward that its 22:00 "clean scan" was
   reversed by three fresh prints one hour later; scan at 5m, 1h, 4h and daily, not one frame.
8. **SUMMIT AND STATE DINNER ARE TODAY (09-24).** Anything opened at 00:00 or 02:00 is held through
   it. Justify *through* the event, not around it.
9. **Do not reach back for this note's constructions.** Price them again from whatever structure
   exists at 16:00Z. The last two checks have both shown that an hour is long enough for the honest
   answer to change completely.

---

Nothing under `reviews/` was read for modification or modified. No script, config, readiness field,
risk limit, watchlist entry or planned date was touched. No order API was called except through
`paper_engine.py`, which returned `no_trade`.
