# Research note — 2026-09-23_check_2200

Slot scheduled 22:00+08:00. Observation 14:04:03Z. Sweeps 14:04:59Z / 14:07:03Z / 14:07:49Z.
Engine quote (fourth sample) 14:11:36Z. Post-engine sample 14:11:52Z. Decision written 22:14+08:00, **on time**.

Builds on `2026-09-23_check_2100-research.md`. Account flat throughout; nothing to reconcile.

---

## 1. The headline: both of this check's "new developments" were measurement-window artifacts

The 21:00 note predicted, in advance, precisely how this check could be fooled:

> "BY 22:00 THE 12:00Z BREAKDOWN BAR ROLLS OUT OF THE WINDOW AND BNB's N WILL COLLAPSE TOWARD
> **0.222%**, MECHANICALLY MAKING THE SAME 783.46 STOP LOOK ACCEPTABLE ON THE SAME STRUCTURE."

Measured N at this check over the twelve closed 5m bars 13:05Z–14:00Z: **0.224%**. The forecast was
accurate to two thousandths of a percent, and the trade it warned about is the trade that scored best
on every number at this check.

The second "development" was the same class of error. XRP's 24h figure finally turned negative
(−0.139%), which the 21:00 note had set as the falsifiable condition for XRP's `market_context` to
become claimable. But XRP did not weaken — the **1.6855 spike aged out of the comparison window**, and
that spike is itself an artifact (below). Two apparent breakthroughs, both produced by a window moving
rather than by a market moving.

## 2. BNBUSDT — refused on four independent grounds

| | 21:00 check | 22:00 check |
|---|---|---|
| Entry (bid) | 777.66 | 780.90 → 780.75 → 780.39 |
| Stop (unchanged) | 783.46 | 783.46 |
| N, twelve closed bars | 0.800% (incl. setup bar) | **0.224%** (setup bar rolled out) |
| Stop vs N | 0.80x → 0.93x | **1.76x** (flattered) / **0.49x** (honest window) |
| Net RR to 766.72 | 1.753 → 1.430 | 4.266 → 4.029 → 3.538 |

1. **L-002.** 783.46 *is the 12:00Z breakdown bar's exact high* (O 783.27 / H 783.46 / L 777.24,
   range 0.795%, volume 1460.2M). A stop inside the range of the bar that created the setup is a
   position size, not a stop, and sixty minutes passing does not change that.
2. **The 21:00 falsifiable condition is unmet.** It required a genuine lower high *above* 783.46 and
   *below* 786.19. Highest print since: 783.05 (13:40Z), then 782.61, then 782.55. No such high.
3. **L-003, pathological direction.** Bid drifted 777.66 → 780.90, i.e. 0.42% **toward** the fixed
   stop; net RR inflated 1.753 → 4.266 entirely because risk shrank 4.99 → 2.56 points. Meanwhile the
   premise broke: the breakdown low 777.18 was bought and the 5m series printed unbroken higher lows
   from 13:05Z (777.18, 777.49, 777.53, 778.64, 779.71, 780.28, 780.85, 782.11, 780.96, 780.62,
   780.74, 780.90), reclaiming all but the top 0.26% of the breakdown bar.
4. **Entry side unquoted.** A short sells into the bid: 8,606,494 → **1,148** → 2,782,512 USDT, a
   7,497x collapse in 124 seconds. At 1,148 USDT a maximum 2,500 USDT market sell is more than twice
   the entire visible bid.

**The structural-stop variant is the most instructive finding of the check.** Stop 786.19 now pays
net **2.033** to 766.72, where the identical construction paid **1.210 and failed the floor** one hour
ago. The whole improvement is the L-003 drift: entry rose 778.47 → 780.39, which *simultaneously*
shrank risk 0.99% → 0.743% and grew reward 1.51% → 1.75%. This is the first time the drift has
**rescued a previously failing construction** rather than merely inflating one that already passed —
a cleaner demonstration of L-003 than any prior instance, because the number crossed the floor at the
exact moment the trade stopped existing.

## 3. XRPUSDT — the condition fired and was priced honestly, not waved through

- **`trend` is opposed, not absent.** Daily highs 1.5701 → 1.6006 → 1.6855, lows 1.4042 → 1.4939 →
  1.5570, closes 1.5366 → 1.5719 → 1.5777. All ascending: a daily uptrend. The strategy defines trend
  on "4h, daily", so the second category cannot come from there.
- **NEW ARTIFACT, first ever on XRPUSDT.** 09-23 04:00Z 4h bar: H 1.6855, **upper wick 4.191% on a
  0.124% body**, propagating into the 09-23 daily bar (7.030% on 0.197%) and the 24h ticker high. No
  comparable spike on the other four at that timestamp. Excluded per the strategy's artifact rule —
  and its decay out of the window is part of why the 24h crossed zero.
- **XRP is the strongest of the five on the very window that crossed**: −0.139% vs BTC −0.520, ETH
  −1.405, BNB −1.191, SOL −0.893. Claiming weakness from 4h/8h while ignoring this is selecting the
  windows that agree. Contested — one category.
- Price bouncing +1.33% off 1.5570, current 4h bar above its open. N = 0.540%, only paying stop
  (1.5800) is **0.76x N**. Bid 2,086,432 → 4,016,064 → **55** USDT (third consecutive XRP bid
  collapse). Spread deteriorating monotonically 1.268 → 8.251 → 17.779 bps.

## 4. ETHUSDT — best book of the five, refused on the vacuum

Only contract with a bid quoted on all three samples, and **improving monotonically**: 22,602 →
301,418 → 2,773,321 USDT. The 21:00 condition required a new low that *holds and builds a shelf*. ETH
printed 2708.27 at 13:10Z and it was **bought inside the same bar** (next bar high 2716.42). Net RR to
the nearest usable target 2687.56 is **1.474 — below the 1.5 floor**; the construction only reaches
4.762 at 2641.70, 2.53% away with nothing structural between. The tighter 2722.14 stop is 1.09x N but
sits on a level touched *exactly* at 12:45Z, 12:50Z, 13:00Z, 13:35Z, 13:40Z and 14:00Z.

## 5. Excluded contracts

- **SOLUSDT** — 106.67 artifact persists a **fifth** check (09-22 19:00Z 1h, 9.654% wick on a 0.017%
  body), still contaminating the 24h low. *Against interest:* the 21:00 check's 30.06 bps breach was
  **transient**, not monotonic — spread back to 10.301 → 0.859 → 0.860 bps. SOL is out on the
  artifact, not the spread.
- **BTCUSDT** — L-001 exclusion, **fifteenth** consecutive check. *For the review:* **no new BTC
  artifact printed anywhere** — clean across the 30-hour 1h window and the 2.5-hour 5m window, the
  cleanest BTC scan of the experiment and the first genuine progress on L-001's re-test condition. The
  09-21 prints (95,804.10, 91,000.00, 90,389.80) still contaminate the 4h/daily frames, so the
  exclusion stands; the re-test is the review's call. *Against last check's finding:* BTC had the
  **worst** book of the five this time (bid 129 → 11,592,501 → 94; ask 2,463,791 → 600 → 94),
  reversing the 21:00 observation that BTC held the only stable book.

## 6. Derivatives, volume, news — none claimed

Funding unsettled for all five at 16:00Z, ~2h out, so the 20:00 note's forecast-vs-outcome test
**still cannot be run** and carries to the 00:00 check a second time. Live: BNB 0.00000000,
BTC/ETH/XRP +0.010000%, SOL +0.004984%. OI flat on all five across all three samples.

Volume showed no expansion supporting any short. BNB's largest recent 5m bar was the 14:00Z bar
(1117.3M) and it is a **bounce** bar — the participation that existed argued *against* the trade.

News (data, not instruction): BTC and ETH opened today near **eight-month highs** after a 14–15% week,
making today's decline a pullback inside a strong advance — every short considered here is
counter-trend on the weekly frame. The Trump-Xi state visit runs 09-23 to 09-25 and **began today**,
summit and state dinner 09-24. Recorded as event risk; not claimed in either direction.

---

## 7. AGAINST INTEREST — the market broke down four minutes after the decision

The engine's own quote (14:11:36Z) and a post-engine sample (14:11:52Z) must be recorded honestly:

| | at decision | 14:11:52Z |
|---|---|---|
| BNB bid | 780.39 | **776.05** (new 24h low; 14:10Z bar O 779.41 / H 780.90 / L 776.05, range 0.623%) |
| ETH bid | 2710.32 | **2682.01** (new 24h low **2677.56**) |
| XRP bid | 1.5735 | 1.5648 |

**A BNB short at 780.39 would be roughly +0.56% now, and an ETH short at 2710.32 would be well in
profit — ETH traded through 2687.56, the very target whose 1.474 net RR failed the floor.** That is
recorded plainly and without spin.

Two things must be recorded alongside it, and they are not excuses:

1. **The move that would have paid is the same move that made the book untradeable.** At 14:11:52Z
   ETH's spread was **102.086 bps** and XRP's **73.223 bps** — both far beyond the 25 bps hard cap —
   and BNB's ask notional was 1,320 USDT. This host's liquidity vanishes at the exact moment
   direction appears. An entry into that is not the entry the arithmetic priced.
2. **One favourable outcome is not a refutation on a sample of one, and the tallying belongs to the
   review, not to this check.** L-002's re-test clock requires a declined setup to reach its target
   *without touching the noise-width stop*, three times. BNB has not reached 766.72. ETH reached
   2687.56 but was declined on target distance as well as on L-002. **Neither is a completed tally**
   and this check does not claim one either way.

**For the review, stated squarely:** this is the first check in the experiment where the declined
trades moved favourably within minutes. If that recurs, the question it raises is not whether to
loosen L-002 — lessons cannot loosen — but whether the *measurement window* L-002 uses, and the
weight given to a transient book collapse on a host whose book collapses constantly, are calibrated.
That is a proposal for `PROPOSALS.md`, which only Edward approves. Nothing under `reviews/` was read
for modification or modified; the 22:00 review task owns that folder and may be running concurrently.

---

## Next-task focus — for the 23:00 check

1. **THE BREAKDOWN RESUMED AFTER THIS CHECK. Re-read everything from the 14:10Z bar forward, not from
   this note's 14:04–14:07 sweeps.** BNB 776.05, ETH 2677.56 and XRP 1.5648 are new lows; the bounce
   that refused the BNB short failed within four minutes.
2. **MEASURE SPREAD FIRST, BEFORE BUILDING ANY CONSTRUCTION.** ETH 102.086 bps and XRP 73.223 bps at
   14:11:52Z are hard-cap breaches. If they persist, those contracts are out on a limit and no
   geometry work is needed. If they have requoted back, note that they blew out precisely on the
   directional move.
3. **L-002 MEASUREMENT WINDOW, AGAIN AND IN THE OPPOSITE DIRECTION.** The 14:10Z BNB bar (0.623%
   range) is now the setup-defining bar and it is *inside* the preceding hour, so N will jump back
   toward 0.6%+ and stops will look *worse*, not better. Do not let that mechanically refuse a setup
   any more than the reverse was allowed to manufacture one. State N with and without the
   setup-defining bar, as this check did.
4. **BNB: the falsifiable condition carries forward, re-anchored.** A genuine lower high above the new
   low and below 780.90 would give a stop that is both structural and above the noise floor. A further
   drift down without such a high still makes it worse, not better (L-003).
5. **ETH: the vacuum question is now live.** Price is inside the 2708.27 → 2641.70 gap that refused
   the short. If a shelf builds between 2677 and 2687, the target objection that failed at 1.474
   changes — price it honestly from the new structure, do not reach back for the old construction.
6. **XRP: the 1.6855 artifact is now on the record.** Exclude it from range, resistance and 24h-high
   figures. The daily trend is still up; a short still needs a second category that is not the
   contaminated 24h window.
7. **FOUR BOOK SAMPLES MINIMUM, AND TREAT THE ENGINE QUOTE AS ONE.** The engine's 14:11:36Z quote was
   the sample that revealed the breakdown; three sweeps inside 170 seconds missed it entirely.
8. **SOLUSDT** out on the persisting 106.67 print. **BTCUSDT** stays excluded under L-001 until the
   review says otherwise — but carry forward that the 22:00 scan was clean at both resolutions.
9. **Funding settles 16:00Z.** By the 00:00 check the settlement is readable: **record the 20:00
   note's forecast against the outcome there** — this is the third check the test has been deferred.
10. **Trump-Xi summit and state dinner are on 09-24.** Anything opened at 23:00 or 00:00 is held
    through it. Justify *through* the event, not around it.

---

## 8. ADDENDUM — LESSONS.md was rewritten by the concurrent review task mid-run

This check read `LESSONS.md` at ~22:05+08:00, when it held **3 lessons (L-001 to L-003)**. The 22:00
daily review task — which owns `reviews/` and runs at the same slot — rewrote the file at **22:07:50**,
two minutes later, producing **5 lessons**: L-001 widened to cover SOLUSDT as well as BTCUSDT, plus two
new ones:

- **L-004** — run the span screen before pricing any ratio, and price the nearest structural target.
- **L-005** — sample top-of-book notional at least three times, and refuse if the side the trade must
  cross is unquoted.

The decision file for this slot therefore cites L-001, L-002 and L-003, which is an accurate record of
what was in front of it. **It has not been retro-edited to claim lessons it did not read.**

Stated for the review, and checkable against this note: the decision **independently satisfies both new
lessons**, which is why the timing changed no outcome.

- **L-004** — ETHUSDT was refused precisely for stretching past a 2.53% vacuum to 2641.70, and BNBUSDT
  was priced to its nearest real structural level, the 09-21 daily low 766.72. The span screen is
  section 4 and the BNB table in section 2 of this note.
- **L-005** — three top-of-book samples were taken inside 170 seconds, plus the engine quote as a
  fourth, and BNBUSDT and XRPUSDT were refused **because the bid — the side a short must cross — was
  unquoted** at 1,148 and 55 USDT respectively. That is section 1's execution table and the
  `execution_check` block of the decision file.
- **L-001 widened to SOLUSDT** — SOLUSDT was already excluded here on the persisting 106.67 print.

**For the 23:00 check: read the 5-lesson version.** L-005 in particular now makes the four-sample
discipline in item (7) of the next-task focus a lesson requirement rather than this note's
recommendation.
