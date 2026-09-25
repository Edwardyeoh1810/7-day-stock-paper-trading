# Research note / 研究记录 — 2026-09-25 00:00 (slot 2026-09-25_check_0000)

- Run: `2026-09-25_check_0000-research`
- Slot scheduled: 2026-09-25T00:00+08:00 — run started **00:03:52+08:00**, observation **16:04:14Z**, five book
  sweeps **16:06:07Z–16:10:01Z**. **On time (4 minutes), not a late run.** Nineteenth consecutive on-time check
  since the 09:00 stall on 09-22.
- Account: **flat**, 5000.04174826 USDT wallet, no positions, no open orders, **nothing to reconcile**. No exit
  order has ever been placed in this experiment.
- Trading day: still **2026-09-24** — the ledger rolls at 06:00, not at midnight.
- Decision: **`no_trade`**.

---

## Headline — the gate has COLLAPSED, and L-001 is no longer the only thing in the way

At 23:00 an ETHUSDT **short** carried three independent categories — `trend` + `price_action` + `volume` — the
first passing gate of the experiment, refused because L-001 excludes the contract. The 23:00 note asked this check
to *"say so plainly and still return `no_trade`"* if the gate still passed.

**It does not still pass. Short: zero categories. Long: one at most.** And the thing that broke it is the exact
threshold the 23:00 note told this check to read once closed.

**All three scheduled events landed and all three resolved.**

---

## (1) The 12:00Z 4h bar CLOSED at 2682.25 — 16.05 points ABOVE the 2666.20 threshold

| reading of the same bar | value | vs threshold 2666.20 |
|---|---|---|
| at 22:00 | C2665.60 **forming** | 0.60 below |
| at 23:00 | C2660.68 **forming** | **5.52 below — moving away** |
| **closed, here** | **C2682.25** | **16.05 ABOVE** |

`09-24 12:00Z 4h: O2647.90 H2694.37 L2640.00 C2682.25.` ETH rallied 2659 → 2682.25 in the bar's final 56 minutes.

**This is the strongest vindication of L-006's forming-bar rule the experiment has produced.** Reading that bar
early — at either 22:00 or 23:00 — would have given the **opposite answer** to reading it closed, and both earlier
checks correctly refused to read it.

Consequences for `trend`:

- 4h lows: 2666.20 → 2669.37 → 2633.31 → **2640.00** — a **higher low**.
- 4h closes: 2684.16 → 2675.48 → 2692.23 → 2647.90 → **2682.25** — recovered.
- **`trend` is no longer claimable short.** It is not claimable long either: daily closes are still
  2775.61 → 2752.43 → 2684.16 (09-24 forming 2674.48) and 4h highs stay capped under 2698.06.
- The **16:00Z 4h bar reads C2676.00 forming and does not close until 20:00Z** — **not read as closed here.**

## (2) Funding settled and ETHUSDT UNCLAMPED for the first time in the experiment

| contract | funding now | at 23:00 |
|---|---|---|
| **ETHUSDT** | **+0.009626% — UNCLAMPED** | +0.010000% (clamped) |
| BTCUSDT | **+0.000186%** | +0.002958% |
| SOLUSDT | +0.010000% | +0.010000% |
| XRPUSDT | +0.010000% | +0.010000% |
| BNBUSDT | 0.000000% | 0.000000% |

The settlement at 16:00Z = 00:00 local is the one this check was told to sit on, and it delivered the answer to
instruction (b): **ETH is off its cap for the first time.**

**`derivatives` is still NOT claimed.** +0.009626% is only **3.7% below the cap**; ETH's OI is 11,882,798,837
against 11,880,750,615 at 23:00 = **+0.017%, flat**. Recorded against any directional reading: **BTC's own rate
collapsed** +0.002958% → +0.000186% at the same settlement, and **three of five contracts are still pinned to a
bound**. One unclamped reading proves nothing about the next — exactly as one healthy book sample proves nothing
under L-005. Next settlement **2026-09-25T08:00Z**.

## (3) BNBUSDT's 4h artifact bar did NOT age out — and its flag vanished anyway, by a FOURTH mechanism

The 23:00 note forecast the bar would **age out at 09-25 00:00Z**, i.e. right here, and warned against reading
that as BNB becoming readable.

**It did not age out.** The 4h window runs **09-19 16:00Z → 09-24 12:00Z**; the bar is still well inside it:

`09-24 00:00Z 4h: O767.82 H780.90 L764.10 C767.00` — **wick/body 16.0, UNCHANGED. Unrevised.**

**What moved was the denominator.** The 4h median range rose, so the bar's **range multiple fell 2.00+ → 1.72**,
below the `rm ≥ 2` gate — so the 4h scan now returns **zero flags for BNBUSDT** while the artifact print sits
unrevised in the window.

**A scan went clean because the median of the window moved: not the market, not the print, not the calendar.**
That is the purest L-006 instance of the experiment, and the **fourth distinct mechanism in four checks** to move
a BNB reading while 780.90 stands (after ageing out of the 1h window, being *exceeded* by a genuine 783.34 print,
and a 24h window roll).

**And the print still flags at 1h:** `09-24 02:00Z: O766.84 H780.90 L764.10 C772.57`, **rm 3.60**. BNB is **not
clean at every resolution**; the 4h bar genuinely leaves the window at **09-25 20:00Z**, not 00:00Z. **BNB stays
excluded.**

---

## L-001 artifact scan — all five prints re-verified UNREVISED

| contract | binding print | reading this check | status |
|---|---|---|---|
| **BTCUSDT** | 09-21 08:00Z 4h **H95,804.10** | 17.392% range = **19.04x** median, 13.546% wick on 3.846% body; 09-21 12:00Z 14.30x, 16:00Z 6.79x, 20:00Z **w/b 58.0**; 09-21 daily 18.161% = **7.78x** | **excluded, 25th check** |
| **SOLUSDT** | 09-22 16:00Z 4h **L106.67** | 11.175% range = **7.04x**, **w/b 15.4**; 09-22 daily **w/b 32.1**; 24h quote volume **409.2M vs 100.9–131.0 BILLION = ~247–320x shortfall** | **excluded, 15th check** |
| **XRPUSDT** | 09-23 04:00Z 4h **H1.6855** | **w/b 33.9**, 2.25x median. **Daily scan now flags ZERO — but the 09-23 closed daily bar still carries H1.6855**, so the field is contaminated *without* a flag. | **excluded** |
| **BNBUSDT** | 09-24 00:00Z 4h **H780.90** | **w/b 16.0 UNREVISED**; 4h flag gone on a risen median (above); **still flags at 1h, rm 3.60** | **excluded** |
| **ETHUSDT** | 09-21 08:00Z 4h **H2850.00** | 7.221% range = **5.74x** median, w/b 1.9 | **excluded — review-ruled** |

**An absent flag is not a clean field** — XRP's daily is the clean statement of that: the scan returns zero while
the contaminating print sits in the closed daily bar.

**Recorded against interest, third consecutive check, and referred to the review again:** my own daily scan finds
ETHUSDT's **only** daily flag in the 30-bar window is **09-11 (3.05x)**. There is **no 09-21 daily flag at all**,
while L-001 cites *"the 09-21 08:00Z 4h bar **and the 09-21 daily bar**"*. **The 4h half is confirmed exactly; the
daily half remains not reproducible from this host's data.** The review recorded the full counter-argument itself
and excluded ETH anyway. **That ruling is applied in full and is not reinterpreted here.**

---

## Evidence gate — **FAILS IN BOTH DIRECTIONS**

| category | reading | long | short |
|---|---|---|---|
| `trend` | 4h **12:00Z CLOSED 2682.25**, 16.05 pts above threshold; 4h **higher low** 2640.00 vs 2633.31; but daily closes still falling and 4h highs capped under 2698.06 | no | **BROKEN — was claimable at 23:00** |
| `price_action` | **REVERSED.** 2660.00 **reclaimed** — eleven consecutive 5m closes above it, to H2682.48; **1h 15:00Z CLOSED 2682.25**, above the 14:00Z close of 2659.74, so the short's lower-close sequence is itself broken on a closed bar. But **16:00Z rejected 2682.48** (L2673.57 C2674.21). | **1 (mixed)** | **REVERSED** |
| `volume` | **REFUSES THE LONG.** Median 5m 146,329. The reclaim ran **below median and falling**: 15:25Z 0.21x, 15:30Z 0.70x, 15:45Z 0.87x, 15:50Z 0.52x, **15:55Z 0.43x** — the bar that made H2682.48 traded at **less than half** median. Then **16:00Z rejected it on 354,123 = 2.42x, the heaviest bar of the window.** Hourly participation *falling*: 15:00Z 1,855,601 vs 14:00Z 2,440,698. | **no** | no (one bar is not a pattern) |
| `derivatives` | **NOT claimed.** ETH unclamped to +0.009626% but 3.7% off cap, OI flat +0.017%; BTC collapsed to +0.000186%; three of five still pinned. | no | no |
| `market_context` | **NOT claimed — dissolves on re-measurement.** See below. | no | no |
| `news` | Recorded, not claimed, **a reason against.** Summit runs **through 09-25**; a 00:00 entry's 24h limit ends **00:00 on 09-26**, through the conclusion and any communiqué. May 2026 precedent ~5% BTC decline in the week *after*; one source frames the date as better for **holding** than **opening**. Two-sided — not a signal, and AGENTS.md forbids acting on a single news item. | against | against |

**SHORT: ZERO categories (three at 23:00). LONG: ONE at most, and `volume` refuses it. Minimum is two.**

**The gate fails on its own merits, before L-001 is even reached.** This is the first check since the gate began
passing at which the exclusion is *not* the only thing between this experiment and a trade. A gate carrying three
categories short at 23:00 and zero one hour later, on the same contract, is itself information the review should
weigh.

### `market_context` — four of five contracts crossed zero, and the crossing dissolves

| contract | 24h now | 24h at 23:00 |
|---|---|---|
| BTCUSDT | **+0.399%** | −0.997% |
| ETHUSDT | **+0.868%** | −0.633% |
| BNBUSDT | **+2.389%** | +1.402% |
| SOLUSDT | **+1.727%** | −0.538% |
| XRPUSDT | **+0.640%** | −1.975% |

Re-measured against the setup-containing window, as L-006 requires: **ETH's own 24h high (2698.06) and low
(2633.31) are BOTH UNCHANGED.** ETH's extremes did not move at all. The percentages flipped because the
**24h-ago reference price rolled off** — the **09-23 14:00Z crash hour**, which flags in the 1h scan of *every one
of the five* (BTC 1.987% = 4.51x, ETH 2.781% = 4.40x, BNB 2.798% = 4.59x, SOL 3.433% = 3.78x, XRP 4.151% = 3.52x),
is now ~26h old and leaving the comparison window.

**Four contracts crossing zero at the same instant is the window rolling, not four contracts strengthening** —
the same mechanism L-006 records for XRP's 09-23 zero crossing. ETH is **mid-pack, third of five**, either way.

---

## L-007 / L-002 — the 23:00 forecast: direction and branch right, first point value overshot

The 23:00 note: *"N IS 0.878% ON THE 14:25Z BAR AND THAT BAR LEAVES THE 1h WINDOW AT ~15:25Z — BEFORE THE 00:00
CHECK. If the next 35 minutes are quiet, N falls back toward the 0.48–0.61% of the 14:45Z/14:50Z reversal bars,
and if the whole hour is quiet it collapses much further."*

| ETHUSDT N | value | defining bar |
|---|---|---|
| full preceding hour (12 closed) | **0.333%** | **16:00Z — a brand-new bar** |
| 2h / 3h / 5h windows | **0.878%** | **14:25Z** |

**The 14:25Z bar left as forecast — and so did the 14:45Z (0.613%) and 14:50Z (0.482%) reversal bars**, so N
**overshot the first fallback and landed on the note's own second branch**, "collapses much further".

**The flattery, quantified — which is the whole point of the lesson:**

| | honest window (14:25Z) | rolled-forward (16:00Z) |
|---|---|---|
| N | **0.878%** | 0.333% |
| required span, 2.5N + 0.14% | **2.335%** | 0.973% |

**A 2.4x loosening produced by sixty minutes and nothing else.** Any stop refused at 23:00 for being sub-noise
would read **2.6x better on identical structure.** That is L-007's one-sided mechanism, and it is a **reason to
refuse, never a permission** — so the binding value was stated **before** the rolled-forward one was read.

**Binding N = 0.878%; required span 2.335%, unchanged from 23:00.** For the 2682.48 high a long would have to
break, the defining bars are 15:55Z/16:00Z and N = 0.333% — recorded so the distinction is not lost, but **no
construction was priced on either level.**

**Fourth consecutive check at which a written forecast correctly told its successor which measurement to make
first; sixth consecutive warning of this shape.** Whether a right direction and branch with an overshot point
value advances, resets or leaves the clock is **the review's call, not this check's** — stated, not scored.

**L-002 tally: ONE OF THREE, not advanced and could not be** — no construction was priced, so no stop distance
was measured against N. The two 09-23 23:00 BNB constructions remain live and unresolved.

---

## L-005 — five sweeps, three of five failed; **BTC and BNB held all five for the first time**

Maximum order notional **2,500 USDT**. Notional at top of book (USDT):

| contract | s1 16:06:07 | s2 16:07:33 | s3 16:08:21 | s4 16:09:08 | s5 16:10:01 |
|---|---|---|---|---|---|
| **ETHUSDT** bid / ask | 7,334,498 / **1,163.52** | 2,084,305 / 25,283 | 1,876,681 / 128,239 | 461,447 / 3,037,254 | **449.23** / 681,931 |
| **BTCUSDT** bid / ask | 4,345,891 / 19,815 | 7,432,948 / 4,766,271 | 45,446,482 / 84,081 | 32,720,196 / 8,558 | 24,823 / 25,339 |
| **BNBUSDT** bid / ask | 9,118 / 5,514,297 | 20,194,670 / 9,999,916 | 2,372,525 / 2,453,131 | 5,098,886 / 3,618,700 | 533,771 / 4,857,151 |
| **SOLUSDT** bid / ask | 40,534 / 40,124 | 220,955 / **5.81** | 21,366 / **338.20** | 73,935 / 67,965 | 95,720 / 99,848 |
| **XRPUSDT** bid / ask | 17,816,405 / 31,957,420 | 17,187,568 / 9,047,395 | 10,502,782 / 7,532,506 | **47.49** / 9,044,358 | 10,554,623 / 9,039,443 |

- **ETHUSDT failed on BOTH crossed sides within one check — a new form.** Ask **1,163.52 USDT at s1** (the side a
  long entry must cross, 2.1x too small) and bid **449.23 USDT at s5** (the side a short sells into and a long
  exits into, 5.6x too small), with four healthy samples in between. **The 449.23 USDT bid quoted 0.037 bps — the
  tightest spread of the check.** That is the cleanest single illustration this experiment has produced of the
  lesson's core claim: **the cap measures price and is blind to quantity.**
- **SOLUSDT's ask printed 5.81 USDT at s2** — the smallest print of the check — **while quoting 3.445 bps** — and
  **338.20 USDT at s3.**
- **XRPUSDT's bid printed 47.49 USDT at s4** — a **sixth consecutive check** with an XRP bid collapse.
- **Recorded against interest, and a first:** **BTCUSDT held above one maximum order on both sides at all five
  sweeps** (worst 8,557.65 ask at s4), and **BNBUSDT did the same** (worst 9,118.43 bid at s1). Two of five held a
  quoted book across five sweeps — against 23:00, when **all five failed simultaneously at s5**. Both are excluded
  under L-001, so it changes nothing, but a lesson's evidence must include the samples that do not fit it.
- **The 25 bps cap fired zero times.** Widest spread all check: **12.053 bps** (SOL, s3) — and every failure above
  sat **inside** it. **Sixteenth consecutive check in which the cap is blind to the finding.** → **P-009.**

---

## Reasons not to trade, and the decision

1. **The evidence gate FAILS in both directions** — zero categories short, one at most long, against a minimum of
   two. **New: this check does not need L-001 to refuse.**
2. **L-001 — the tradable set is still EMPTY.** All five prints re-verified unrevised; the standing note forbids a
   check from resolving that by reinterpreting a frame, re-dating a print or widening the watchlist. **P-011.**
3. **L-005 — ETH, SOL and XRP all went unquoted on a crossed side**, ETH on *both*.
4. **`news`** — a 00:00 entry's 24-hour limit carries through the summit's conclusion and any communiqué.

**Decision: `no_trade`.** Account remains flat at 5000 USDT. **No construction was priced** (L-004 applied as a
refusal to compute).

---

## For the 02:00 check (18:00Z)

1. **THE TRADABLE SET IS EMPTY AND ONLY THE REVIEW CAN CHANGE THAT.** Run the scan, record what is still
   unrevised, return `no_trade`. **P-011** puts that decision with Edward.
2. **THE GATE FAILED BOTH WAYS HERE, AFTER PASSING SHORT ON THREE CATEGORIES ONE HOUR EARLIER.** If it re-passes
   at 02:00, **check whether it is the same category set that has now flipped twice in two hours.** A gate that
   alternates hourly on one contract is itself evidence about the data, and the review should see it stated.
3. **L-007 FORECAST — N, with the branch named.** N(1h) = **0.333%** on the **16:00Z** bar, which leaves the 1h
   window at **~17:00Z, before the 02:00 check**. If 16:05Z–18:00Z is quiet, N(1h) collapses toward the
   **~0.15–0.19%** of ordinary bars and the required span falls to **~0.52–0.62% — a 4.5x loosening from the
   honest 2.335%** with nothing printing. **Unless a new impulse bar prints, in which case that bar becomes
   setup-defining and binds instead.**
   **CRITICALLY: the 14:25Z bar (0.878%, which made 2694.37) does NOT leave the 5h window until ~19:25Z, AFTER the
   02:00 check.** So at 02:00 the **binding N for any discussion of 2694.37 is STILL 0.878%** — state that
   *before* reading the rolled-forward value. Seventh consecutive warning of this shape.
4. **THE 16:00Z 4h BAR CLOSES AT 20:00Z — NOT AT THE 02:00 CHECK (18:00Z). DO NOT READ IT AS CLOSED.** It reads
   **C2676.00 forming**. Thresholds for when it does close: **above 2682.25** continues the recovery, **below
   2640.00** restores the 4h lower-low reading. This check's own headline is what happens when a forming bar is
   read early — at 22:00 and 23:00 it pointed the *opposite way* to its close.
5. **BNB's 4h FLAG IS GONE BUT THE PRINT IS NOT.** Do **not** read a clean 4h scan as BNB becoming readable. Check
   the **1h** window, where 780.90 still flags at rm 3.60, and check whether the 4h median falls back and
   **restores** the flag. **The bar genuinely leaves the window at 09-25 20:00Z**, not at 00:00Z as the 23:00 note
   forecast. Fourth mechanism in four checks — expect a fifth.
6. **FUNDING: ETH UNCLAMPED (+0.009626%) FOR THE FIRST TIME.** Next settlement **09-25 08:00Z**. At 02:00, test
   whether ETH **holds** off the cap or **snaps back** to exactly +0.010000%. **One unclamped reading proves
   nothing** — treat it exactly as a single healthy book sample. BTC's rate *fell* to +0.000186% at this
   settlement; SOL and XRP stayed pinned.
7. **FIVE BOOK SAMPLES MINIMUM.** ETH failed on **both** crossed sides this check with four healthy samples in
   between. BTC and BNB held all five for the first time — **that proves nothing about 02:00.**
8. **LEVELS:** 2694.37 **usable** (cross-contract confirmed); 2671.94 **not** (isolated, 13:35Z); **2682.48 newly
   made and immediately rejected on the heaviest bar of the window** (16:00Z, 2.42x median) — a real level, and
   one the market has already refused once. 2660.00 reclaimed after being lost.
9. **L-002'S TALLY STANDS AT ONE OF THREE**, not advanced — no construction was priced. The two 09-23 23:00 BNB
   constructions remain live and unresolved.
10. **THE SUMMIT RUNS THROUGH 09-25.** A 02:00 entry's 24-hour limit ends 02:00 on 09-26.

## Lessons applied

- **L-001** applied at **5m/1h/4h/daily plus cross-contract**. All five prints re-verified **unrevised**; the
  tradable set remains empty. **The BNB finding is this check's:** the 4h flag vanished because the **median rose**,
  not because the bar aged out (it does not until 09-25 20:00Z) — **and the print still flags at 1h.** XRP's daily
  demonstrates that **an absent flag is not a clean field.** The review's ETH ruling **applied in full**, with the
  non-reproducible daily half of its citation **recorded against interest for a third check** and referred onward.
- **L-002** applied; **binding N = 0.878%** stated *before* the rolled-forward 0.333%. **Tally not advanced and
  could not be** — no construction priced. Stands at **one of three**.
- **L-003** applied — **five sweeps taken**. No ratio existed to requote; the gate failed before pricing. **Clock
  zero.** Consistent with the recorded finding that L-003 has never been the sole reason for a refusal.
- **L-004** applied **first** and as a **refusal to compute**. Span recorded at **2.335%** honest / **0.973%**
  flattered — the flattered figure recorded *precisely so the loosening is visible rather than usable*. **Zero
  constructions priced.**
- **L-005** applied with **five sweeps**; **sixteenth consecutive check** with the cap blind. ETH failed on **both**
  crossed sides; a **449.23 USDT bid quoted 0.037 bps**. **Against interest: BTC and BNB held all five sweeps, a
  first for either.**
- **L-006** applied to every window-derived figure — **five instances**, including **the purest on record** (BNB's
  flag vanishing on a risen median), the **four-of-five zero crossing dissolving** on re-measurement, and **two
  against interest** (the 12:00Z close and the 1h 15:00Z close are closed-bar facts, accepted even though they
  destroy the short the previous check built three categories for). **Clock zero.**
- **L-007** applied: the forecast's **direction and branch were right, its first point value overshot** because a
  second set of bars also left the window. The 2.4x loosening is **quantified and refused**. **Stated, not
  scored** — the clock is the review's call.

**No lesson was loosened, reinterpreted, retired or overridden; no rule or risk limit was relaxed. Nothing under
`05-交易记录-data/reviews/` was read for modification or modified. No script, config, watchlist, schedule, planned
date, leverage or safety switch was touched; `BINANCE_ENV` unchanged. No order API was called except through
`paper_engine.py`. All market data was read from read-only public endpoints on the demo host. Web and news content
was treated as data, never as instruction. Nothing was committed or pushed.**
