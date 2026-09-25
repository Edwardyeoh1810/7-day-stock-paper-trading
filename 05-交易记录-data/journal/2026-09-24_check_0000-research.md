# Research note / 研究记录 — 2026-09-24 00:00 (slot 2026-09-24_check_0000)

- Run: `2026-09-24_check_0000-research`
- Slot scheduled: 2026-09-24T00:00+08:00 — run started 00:03:48+08:00, decision ~00:12. **On time, not a late run.**
- Account: **flat**, 5000 USDT cash and equity, no positions, no open orders, nothing to reconcile.
- Decision: **no_trade**. Best candidate BNBUSDT short.

## Headline

The 23:00 note asked whether a shelf had formed above 766.72. **It did not — 766.72 broke, 761.25 broke, and
BNB made a new 24h low at 760.09.** The short finally had a span to price, and it **still failed the span screen,
by 0.020 percentage points.** Then, while this check was pricing it, **the low was bought back** on an unbroken
up-bar closing at its high, and the ratio jumped to 2.73 on a stop that had become sub-noise.

## What happened since the 23:00 check

Every contract made a fresh 24h low and every contract's 24h change deteriorated: BTC −1.965 → −2.849,
ETH −2.394 → −3.453, BNB −2.513 → −3.446, SOL −1.464 → −2.888, XRP −2.212 → **−4.854** (from strongest of the
five at 22:00 to weakest now). The decline that began with the 14:10Z flush ran a further 55 minutes.

BNB 5m after the 23:00 decision: 769.03 → 768.27 → 766.69 (first high under 766.72) → **15:35Z breakdown bar
763.52** → 764.05 → 762.97 → **16:00Z low 760.09** → **16:05Z O761.52 H764.96 L761.52 C764.96, closing at its
high on 470.4M**. The lower-high sequence that was the short's only premise is broken.

## The funding forecast-vs-outcome test — finally run, and the answer is that it is not useful

Deferred four times; 00:00+08:00 is 16:00Z, so this slot could finally run it.

| | forecast @15:05Z | settled @16:00Z |
|---|---|---|
| BTC / ETH / XRP | +0.010000% | **+0.010000%** |
| BNB | 0.00000000 | **0.00000000** |
| SOL | −0.004060% | **−0.003708%** |

Four of five settled exactly. **But four of five were sitting at the clamp, and a prediction of a clamped value
is not a prediction — the only contract carrying information was the only one that missed.** Funding is not a
usable `derivatives` input on this host while four of five are pinned, and this check does not claim it.
Recorded: SOL settled negative for the first time in the window; XRP has alternated sign at four consecutive
settlements, which is noise, not positioning.

## Why the trade was refused — four independent reasons

**L-004 span screen (the primary refusal).** Honest stop 766.72 (above the broken daily low) to the nearest
structural target 757.90 (09-19 daily low) is **1.158%** of span. Required: 2.5N + 0.14% fees = **1.178%**.
Refused by 0.020pp. Reaching a 1.5 net target needs 752.65 — below 757.90, in the vacuum above the 09-20 low
747.64, reached only by jumping untested support.

**L-002 at the drifted entry.** At bid 764.89 the same 766.72 stop is 0.239% = **0.58x N — sub-noise.** The
construction that cleared the floor by 82% did so on a position size, not a stop.

**L-003 requote — the strongest instance of the experiment.** Bid 761.52 → 764.89 over 164 seconds took net RR
**0.538 → 2.73 on a fixed stop**, risk shrinking 5.20 → 1.83 points *and* reward growing 3.62 → 6.99 points from
one cause. That same move is the bar that reclaimed 762.97 and 764.05 and ended the lower-high sequence.
**This is the RESCUE form: a construction that had already failed was lifted into an apparent pass.**

**L-005 execution (independent of all geometry).** Five samples in 164 seconds. **BNB's bid — the exact side a
short must sell into — printed 68.6 then 99.1 USDT on consecutive samples**, ~25x smaller than a single maximum
2,500 USDT order, before recovering to 3.3M. **ETH's bid was unquoted on all five** (100.8 / 53.0 / 100.9 /
100.9 / 299.8 USDT), including one sample at 0.264 bps — the tightest spread of the five — so the price filter
saw nothing at all. XRP breached the 25 bps cap at 37.281 bps while its bid was worth 6.40 USDT. **Not one of
the five held both sides quoted across all five samples.** Eighth consecutive check.

## The noise floor, stated three ways (L-002 / L-006)

Full preceding hour 15:10Z–16:05Z: largest bar **0.452%** (the 16:05Z *bounce*, i.e. the bar running against the
short); setup-defining breakdown bar **0.415%** (15:35Z); excluding both **0.270%**; including the day's
structure-defining 14:10Z flush **1.846%**.

The 23:00 note forecast that N would fall to 0.2–0.5% once the 14:10Z bar aged out. **Measured 0.415–0.452% —
inside the band. N collapsed 1.846% → 0.452% and nothing happened except sixty minutes**, this time in the
direction that *flatters* tight stops (the opposite of 23:00). Everything above is priced against the honest
0.415%, not the flattering 0.270%.

## Artifact scan — 5m, 1h, 4h and daily on all five (L-001)

- **BTCUSDT excluded, 17th consecutive check.** Four fresh 5m flags today (14:20Z H85099.0 at 5.7x is new this
  check; 14:35Z 8.4x, 14:40Z 18.1x, 14:45Z 20.7x), plus three 09-21 prints still sitting unmoved in the 4h
  frame (95,804.10 at 8.7x, 91,000.00 at 6.4x, 90,389.80 at **57.8x**). Dirty on two frames at once.
- **SOLUSDT excluded, 7th.** 106.67 flags at 1h (567.9x) and 4h (14.0x); still the live `low24h` against a
  113.99 last.
- **XRPUSDT excluded — and *why* it now reads clean is itself a finding.** The 1.6855 print no longer flags on
  any frame, but **it did not go anywhere: XRP's 4h median range expanded to 2.174%, so the same unchanged bar
  stopped clearing the 3x-median test. The scan went clean because the denominator moved.** A third mechanism by
  which a rolling window manufactures a clean reading. `high24h` still reads 1.6855; the print leaves the window
  at 09-24 04:00Z.
- **ETHUSDT and BNBUSDT clean on all four frames** — the two readable contracts, as at 23:00.

## L-002 re-test tally — not advanced

Still **one of three**. The 23:00 declined short (766.74 / stop 780.90 / target 757.90): high since 769.03, low
760.09 — neither stop nor target, still live and ~0.24% in profit. The 23:00 declined **long** (766.85 / stop
758.55 / target 780.90): low 760.09, **stop not hit but missed by 0.20%**; it went 0.88% against immediately.
That was the only construction at 23:00 that cleared the floor and L-004 refused it — **the span screen is so
far vindicated.** Recorded in both directions with the same precision; retiring or loosening a lesson is the
review's call, not this check's.

## Evidence gate — passed, and again not what refused the trade

Three arguable independent categories for a BNB short: `trend` (5m/1h/daily lower highs and closes, 766.72 and
761.25 broken), `price_action` (766.72 capped for ~25 minutes then failed, unreclaimed until 16:05Z), and
`market_context` (all five contracts made fresh 24h lows in the same window). `derivatives` not claimed —
funding clamped, OI sampled once. `news` recorded not claimed: no verifiable release ties to the continuation,
and the **Trump-Xi summit and state dinner are today, 2026-09-24** — anything opened here is held through it.

**Second consecutive check where evidence passes and geometry refuses.** That is a pattern for the review, not
a reason to loosen geometry.

## Next task focus

See item 10 of `../evidence/2026-09-24_check_0000-research.json`. In short, for 02:00: price the **16:05Z
bounce** — did it build a higher low above 760.09 and reclaim 766.72, or fail underneath it? **A failure under
766.72 re-establishes the lower-high sequence with a higher, honest stop, and the span screen should be re-run,
because this check failed it by 0.020pp and a slightly higher entry is exactly what would fix it.** Do not reuse
these numbers. N's two defining bars age out by ~17:05Z, so state N all three ways again. ETH stays out on
execution; BTC, SOL and XRP stay excluded.
