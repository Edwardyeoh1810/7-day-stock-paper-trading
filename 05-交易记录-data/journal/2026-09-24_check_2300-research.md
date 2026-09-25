# Research note / 研究记录 — 2026-09-24 23:00 (slot 2026-09-24_check_2300)

- Run: `2026-09-24_check_2300-research`
- Slot scheduled: 2026-09-24T23:00+08:00 — run started **23:03:49+08:00**, observation **15:04:15Z**, five book
  sweeps **15:05:08Z–15:07:49Z**. **On time (4 minutes), not a late run.** Eighteenth consecutive on-time check
  since the 09:00 stall on 09-22.
- Account: **flat**, 5000.04174826 USDT wallet, no positions, no open orders, **nothing to reconcile**. No exit
  order has ever been placed in this experiment.
- Decision: **`no_trade`** — **the tradable set is empty.**

---

## Headline — the first check at which the evidence gate WOULD PASS and the trade is refused anyway

The daily review ran after the 22:00 check and **ruled on the question the last two checks referred to it**:
`LESSONS.md` now carries a standing note that **all five watchlist contracts are excluded under L-001** and that
*"the tradable set is empty … A check may not resolve it by reinterpreting a frame, re-dating a print or widening
the watchlist; it records the state and returns `no_trade`."* ETHUSDT was caught by the third amendment on its
2850.00 print.

**That ruling binds here, and it binds against a setup that would otherwise have cleared the evidence gate for the
first time in the experiment.** ETHUSDT this check offers `trend` + `price_action` + `volume`, three independent
categories all pointing **short** (detail below). Under any earlier state of the watchlist this would have been the
first check to reach the pricing stage with the gate satisfied.

**It is refused, and it is refused twice over:**

1. **L-001 — ETHUSDT is excluded.** A check may never retire or loosen a lesson, "even when a re-test condition is
   met". The exclusion is applied in full.
2. **L-005 — independently, every contract including ETHUSDT went unquoted at sweep 5** (below). Even without
   L-001 this check refuses.

**No construction was priced on ETHUSDT.** Pricing a stop and target on an excluded contract is exactly the
"looking for a construction" the 22:00 note warned against, and L-004 requires the span screen *before* any ratio —
but a screen run on an excluded contract is work done to make an impossible trade look close. The required span is
recorded below as a fact; no entry, stop or target was constructed.

---

## L-001 artifact scan — 5m / 1h / 4h / daily, plus cross-contract. **All five prints re-verified UNREVISED.**

| contract | binding print | reading this check | status |
|---|---|---|---|
| **BTCUSDT** | 09-21 08:00Z 4h **H95,804.10** | **17.392% range = 18.19x** the 4h median, 13.546% wick on a 3.846% body; 09-21 12:00Z 13.66x; 09-21 16:00Z 6.48x; 09-21 20:00Z **w/b 58.0**; 09-21 daily 18.161% = **7.93x** | **excluded, 24th check** |
| **SOLUSDT** | 09-22 16:00Z 4h **L106.67** | **11.175% range = 6.82x**, 9.975% lower wick on a 0.712% body = **14.0x**; 09-22 daily **w/b 28.8**; 24h quote volume **409.18M against 102–131 BILLION** (~270x shortfall, worse than the ~250x at 22:00) | **excluded, 14th check** |
| **XRPUSDT** | 09-23 04:00Z 4h **H1.6855** | **4.226% wick on a 0.125% body = 33.9x**, 2.24x median range; 1h flags **130.0x, 51.3x, 28.3x, 27.9x, 20.3x** | **excluded** |
| **BNBUSDT** | 09-24 00:00Z 4h **H780.90** | **1.712% wick on a 0.107% body = 16.0x — UNREVISED**, unchanged from 20:00, 21:00 and 22:00. Ages out 09-25 00:00Z. | **excluded** |
| **ETHUSDT** | 09-21 08:00Z 4h **H2850.00** | **7.221% range = 5.51x** the 4h median, 4.772% wick on a 2.421% body = **w/b 2.0**. Still inside the 30-bar 4h window. | **excluded — review-ruled** |

**Recorded against interest, as the 22:00 note left it:** my own daily scan again finds **ETHUSDT has no flag on
the 09-21 daily bar at all** — ETH's only daily flags in the 30-bar window are 09-11 (3.15x), 08-27, 09-20 and
09-08. `LESSONS` L-001 cites "the 09-21 08:00Z 4h bar **and the 09-21 daily bar**". **The 4h half of that citation
is confirmed exactly; the daily half is not reproducible from this host's data.** The review recorded the full
counter-argument itself (w/b only 2.0, an order of magnitude below every other caught print; 7.2% above the market;
contaminates no field priced here) and excluded ETH anyway, on the grounds that ruling the other way would be a
loosening made on four days of data and zero trades. **That ruling is applied in full and is not reinterpreted
here.** The discrepancy is recorded for the review, which is the only body that may act on it.

### The 14:25Z spike is cross-contract CONFIRMED — the opposite of the 13:35Z finding

The 22:00 note's instruction #2 asked for the 13:35Z cross-contract comparison to be re-run. A **new and larger**
move has since printed, and it must be judged on its own:

| contract | 14:25–14:30Z impulse | x own 5m median | 14:45–14:50Z reversal | x median |
|---|---|---|---|---|
| **ETHUSDT** | 14:25Z **0.878%** (2674.61 → H2694.37) | **5.77x** | 14:45Z 0.613%, 14:50Z 0.482% | 4.03x / 3.17x |
| BTCUSDT | 14:30Z 0.495% (H84,735.0) | **4.59x** | 14:50Z **0.755%** | **7.01x** |
| SOLUSDT | 14:25Z 0.754% (H116.21) | **3.61x** | 14:45Z 0.757% | **3.62x** |
| XRPUSDT | 14:30Z 0.761% (H1.5232) | **3.38x** | 14:50Z **1.190%** | **5.29x** |
| BNBUSDT | 14:00Z 1h H783.34 | 1.40x (1h) | 14:45Z 0.507% | **3.77x** |

**All five contracts moved together, up and then back down.** This is a genuine market-wide event, not a demo
artifact: **2694.37 is NOT an isolated print and is a usable level**, unlike 2671.94. Recorded against interest —
the isolation test is capable of clearing a print, and here it did.

**The 13:35Z isolation finding itself is unchanged:** no other contract has since made that 13:35Z move, so
**2671.94 remains excluded as a level.** It is moot in any case — price has traded above it and back through it.

---

## The breakout FAILED, and this is what flips the evidence gate

The 22:00 note recorded a **held** breakout with a 9-touch floor at 2660.00 and told this check to look for a
second category rather than a better price. What arrived instead was the breakout's failure.

| 5m bar | reading |
|---|---|
| 14:15Z–14:20Z | C2671.40, C2674.61 — pushing on |
| **14:25Z** | O2674.61 **H2694.37** C2693.53, V253,078 — the impulse, **+0.74% in one bar** |
| 14:30Z–14:40Z | H2694.37 not exceeded; 2690.89 → 2683.76 → **C2680.59** |
| **14:45Z** | O2680.59 **C2664.41**, V**257,646** (1.97x median) — back through the breakout |
| **14:50Z** | O2664.32 **L2655.35** C2658.29, V**376,794 (2.89x median — the largest bar of the window)** |
| 14:55Z–15:00Z | L2655.22, L2655.22 — **the 2660.00 floor is now overhead resistance** |

- The **1h 14:00Z bar closed at 2659.74**, below the 13:00Z close of 2668.42 — the higher-high/higher-low sequence
  that `price_action` rested on at 22:00 is **broken on a closed bar**, not on a forming one.
- The 2660.00 floor that held five times at 22:00 **has been lost**; last three 5m lows are 2655.35 / 2655.22 /
  2655.22.
- ETH `high24h` fell **2717.26 → 2698.06** (a window roll) while `low24h` is **still 2633.31, unchanged**.

## Evidence gate — **passes short on ETHUSDT, on three categories**

| category | reading | long | short |
|---|---|---|---|
| `trend` | **DOWN.** 4h highs 2695.84 → 2690.73 → 2698.06 → 2693.42 → 2694.37; 4h lows 2668.06 → 2666.20 → 2669.37 → **2633.31** → 2640.00. Daily closes 2775.61 → 2752.43 → 2684.16. | opposes | **CLAIMABLE** |
| `price_action` | **FAILED BREAKOUT.** 2694.37 rejected inside one bar; the 9-touch 2660.00 floor broken and now overhead; 1h 14:00Z **closed** at 2659.74 below the prior close. This is the strategy's named `price_action` pattern. | opposes | **CLAIMABLE** |
| `volume` | **CONFIRMS THE DOWN MOVE.** Median 5m volume 130,556 over 48 closed bars. The reversal bars traded **257,646 (1.97x)** and **376,794 (2.89x — the largest in the window)**; the 14:00Z hour traded **2,440,698, the heaviest hour of the day.** Contrast 22:00, where the bar that made the high traded *below* median. | no | **CLAIMABLE** |
| `derivatives` | **NOT claimed.** ETH funding still clamped at exactly **+0.010000%**; OI 11,880,750,615 vs 11,878,453,159 = **+0.019%, flat.** BTC unclamped again (+0.002958%), but that is BTC's rate. | no | no |
| `market_context` | **NOT claimed on independence.** 24h: BTC −0.997%, ETH −0.633%, BNB **+1.402%**, SOL −0.538%, XRP −1.975%. ETH is the *second strongest* of the five and BNB is positive — this does not assert ETH weakness. | no | no |
| `news` | **Recorded, not claimed, a reason against.** The Trump–Xi summit is **today** and the series runs to 09-25; agenda trade, tariffs, rare earths, AI, Taiwan, Iran. Pre-summit prints cited BTC ~86,159 and ETH ~2,755 — both **well above** the current 83,635 / 2,659, so the market has already moved against the constructive read. A 23:00 entry's 24-hour limit ends **23:00 on 09-25, through the summit's conclusion and any communiqué.** | against | against |

**SHORT: three independent categories — `trend` + `price_action` + `volume`. THE GATE PASSES.**
**LONG: zero categories. The gate fails outright.**

**And the trade is still refused, because ETHUSDT is excluded under L-001.** This is the first time in the
experiment that the exclusion, rather than the geometry or the gate, is the binding constraint on a setup that had
cleared everything else at its stage. Per the standing note this is *"the rules working as written, not a fault to
be worked around."*

---

## L-007 / L-006 — the 22:00 forecast, and which branch fired

The 22:00 note's instruction #3: *"N WILL BE 0.468% UNTIL ~14:35Z AND THEN DEPENDS ENTIRELY ON WHAT PRINTS. If the
next hour is quiet, N will collapse toward ~0.13% and the 0.26x/0.53x stops refused here will read 1.0x–1.9x on
IDENTICAL STRUCTURE."*

**The antecedent was false: the hour was not quiet.** The 13:35Z bar did leave the 1h window at 14:35Z as forecast,
but a **far larger** impulse bar printed at 14:25Z (0.878%, 5.77x the 5m median), and it is the bar that created
the 2694.37 high — the level any short would now be fading.

| ETHUSDT N | value | defining bar |
|---|---|---|
| full preceding hour (12 closed) | **0.878%** | **14:25Z** |
| 2h / 3h / 5h windows | **0.878%** | 14:25Z |

**N did not collapse to ~0.13%; it very nearly DOUBLED, 0.468% → 0.878%.** Required span for any ETH construction
is now **2.5N + 0.14% = 2.335%**, up from 1.310%/1.513% at 22:00 — the screen got **harder**, not easier.

**This is the second consecutive check at which the conditional's "new impulse bar" branch fired rather than the
quiet-collapse branch, and the third consecutive check at which a written forecast correctly told its successor
which measurement to make first.** Recorded honestly: **the forecast's *point value* was not reached**, because its
condition did not hold. L-007's value here was the branch, not the number — which is the lesson's own claim about
conditional forecasts. Whether that advances or resets any clock is **the review's call, not this check's.**

**Other window-derived figures re-measured (L-006):**
1. **ETH `high24h` 2717.26 → 2698.06** — a bar leaving the 24h window, no revision anywhere. Nothing priced.
2. **ETH `low24h` still 2633.31, unchanged** — recorded against interest: a short's 24h-low target *would* survive
   re-measurement.
3. **BNB `high24h` ROSE 781.60 → 783.34** — and this one is a **genuine market event**: a real new print in the
   14:00Z 1h bar (H783.34), exceeding the artifact. **So 780.90 stopped contaminating the 24h high field by being
   EXCEEDED, not by being corrected or by ageing out.** The 4h bar still reads **w/b 16.0, unrevised.** This is the
   third distinct mechanism in three checks to move a BNB field while the print itself stands — and it is exactly
   the flicker the 22:00 note warned would be misread as the contract becoming readable. **BNB stays excluded.**
4. **The 12:00Z 4h close test remains deferred to 00:00**, as the 22:00 note directed. The bar closes at 16:00Z =
   00:00 local; it currently reads **C2660.68 forming**, now **5.5 points further below** the 2666.20 threshold than
   the 2665.60 it showed at 22:00. **It was not read as closed here.**

---

## L-005 — five sweeps, and **every one of the five contracts went unquoted at sweep 5**

Maximum order notional is 2,500 USDT. Notional on the side a trade must cross (USDT):

| contract | s1 15:05:08 | s2 15:06:00 | s3 15:06:44 | s4 15:07:31 | **s5 15:07:49** |
|---|---|---|---|---|---|
| **ETHUSDT** bid / ask | 213,668 / 452,208 | 683,733 / 3,136,638 | 4,923,874 / 1,381,263 | 3,298,860 / 3,303,248 | **9,999 / 500.40** |
| **BTCUSDT** ask | **376.78** | 3,231,733 | 2,459,562 | **503.00** | **192.97** |
| **BNBUSDT** bid | **887.08** | **513.57** | 388,337 | **202.44** | **31.14** |
| **SOLUSDT** bid / ask | 6,252 / 309,252 | 5,752 / **285.80** | 161,907 / **301.90** | **498.60 / 10.32** | **488.28 / 5.74** |
| **XRPUSDT** bid | **58.02** | 25,480,370 | 6,102,058 | **24.00** | **27.16** |

- **ETHUSDT's ask fell to 500.40 USDT at s5 — 5x below a single maximum order — after four consecutive healthy
  samples**, its bid falling to 9,998.50 in the same sweep. **ETH's two-check pass under L-005 is over.** The 22:00
  note predicted precisely this: *"ETH PASSED L-005 FOR THE FIRST TIME AND THAT PROVES NOTHING ABOUT NEXT CHECK."*
  It proved nothing.
- **BNBUSDT's bid was below a maximum order on FOUR of five sweeps** (887, 514, 202, 31) — the worst sustained
  reading of the experiment, and **31.14 USDT at s5 is 80x smaller than one maximum order** while quoting 2.183 bps.
- **SOLUSDT failed on BOTH sides at s4 and s5** (ask 10.32 then **5.74**; bid 498.60, 488.28) — an ask worth less
  than six dollars.
- **XRPUSDT's bid printed 58.02, 24.00 and 27.16 USDT** — a **fifth consecutive check** with an XRP bid collapse.
- **BTCUSDT's ask was unquoted on three of five sweeps** (376.78, 503.00, 192.97).
- **At s5, 15:07:49Z, all five contracts were simultaneously unquoted on at least one side.** That is the first
  fully synchronised book failure recorded in this experiment.

**The 25 bps cap fired zero times again.** Widest spread of the entire check: **19.175 bps** (SOL, s5) — and the
5.74 USDT SOL ask sat *inside* that. BTC's 18.601 bps at s3 also passed. **A fifteenth consecutive check in which
the cap is blind to the entire finding.** → this is what **P-009** asks Edward for an engine-side rule about.

---

## Funding and open interest

| contract | funding | OI | change vs 22:00 |
|---|---|---|---|
| BTCUSDT | **+0.002958%** — unclamped a second check | 418,370,506 | +0.023% |
| **ETHUSDT** | **+0.010000% — still clamped** | 11,880,750,615 | **+0.019%, flat** |
| BNBUSDT | 0.000000% | 28,116,504,484 | +0.025% |
| SOLUSDT | +0.010000% | 2,987,855,176 | +0.011% |
| XRPUSDT | +0.010000% | 15,873,386,638,319 | +0.024% |

`nextFundingTime` = **2026-09-24 16:00Z = 2026-09-25 00:00 local — the 00:00 check sits on the settlement.**
**`derivatives` not claimed: ETH's own rate is clamped and its OI is flat.** ETH did **not** unclamp ahead of the
settlement; the 00:00 check gets the answer to the 22:00 note's instruction #8.

---

## Reasons not to trade, and the decision

1. **L-001 — the tradable set is EMPTY.** All five contracts excluded on re-verified unrevised higher-frame
   artifacts; ETHUSDT caught by the review's ruling. **This alone is decisive and admits no construction.**
2. **L-005 — every contract went unquoted on a crossed side, and all five simultaneously at s5.** Independently
   decisive, and it would refuse this check even if L-001 did not exist.
3. **`news`** — any entry's 24-hour limit carries it through the conclusion of the Trump–Xi summit.
4. **Not a reason, recorded for completeness:** the evidence gate **passed short on ETHUSDT** with three
   independent categories. It changed nothing, and no construction was priced.

**Decision: `no_trade`.** Account remains flat at 5000 USDT.

---

## For the 00:00 check (16:00Z) — 2026-09-25, a new trading day at 06:00, not at midnight

1. **THE TRADABLE SET IS EMPTY AND ONLY THE REVIEW CAN CHANGE THAT.** Do not go looking for a readable contract.
   Run the scan, record which prints are still unrevised, and return `no_trade`. **A check may not resolve an empty
   tradable set** — P-011 puts that decision with Edward.
2. **THREE THINGS LAND ON THE 00:00 CHECK AT ONCE (16:00Z). Do all three, and do not let them contaminate
   each other.**
   - **(a) The 12:00Z 4h bar CLOSES.** Threshold: a close **above 2666.20** materially weakens the 4h lower-low
     reading. It read **C2660.68 forming** here — it has moved *away* from the threshold since 22:00 (2665.60).
     **Read it only once it is closed.**
   - **(b) FUNDING SETTLES.** Watch whether **ETH unclamps from +0.010000%**, which would make `derivatives`
     readable for the first time in the experiment. BTC has now been unclamped two checks running.
   - **(c) BNBUSDT'S 4h ARTIFACT BAR AGES OUT AT 09-25 00:00Z**, i.e. right here. **DO NOT READ THE AGEING-OUT AS
     BNB BECOMING READABLE.** L-001's re-test requires a full clean day at every resolution *and* no contamination
     of any field — and the re-test is the review's to run, not a check's. Note also that its `high24h` moved this
     check by a **third** mechanism (a genuine new print at 783.34 exceeding it), while **780.90 itself has never
     been revised.**
3. **N IS 0.878% ON THE 14:25Z BAR AND THAT BAR LEAVES THE 1h WINDOW AT ~15:25Z — BEFORE THE 00:00 CHECK.** If the
   next 35 minutes are quiet, N falls back toward the 0.48–0.61% of the 14:45Z/14:50Z reversal bars, and if the
   whole hour is quiet it collapses much further. **The setup-defining bars are now 14:25Z (which made 2694.37) and
   14:50Z (which broke 2660.00); measure N against the window containing whichever level is being discussed.**
   Fifth consecutive warning of this shape.
4. **THE EVIDENCE GATE PASSED SHORT ON ETHUSDT HERE — `trend` + `price_action` + `volume`.** If it still passes at
   00:00, **say so plainly and still return `no_trade`.** Recording that the gate passes on an excluded contract is
   the honest datum the review needs; quietly dropping it because it cannot be acted on is not.
5. **2694.37 IS A USABLE LEVEL (cross-contract confirmed, all five moved); 2671.94 IS NOT (isolated at 13:35Z).**
   Both are moot while ETH is excluded — recorded so the distinction is not lost.
6. **FIVE BOOK SAMPLES MINIMUM, AND EXPECT NOTHING FROM A HEALTHY ONE.** ETH held four healthy sweeps and then
   printed a **500 USDT ask**. All five contracts failed at s5 simultaneously.
7. **THE TRUMP–XI SUMMIT RUNS THROUGH 09-25.** A 00:00 entry's 24-hour limit ends 00:00 on 09-26. The market has
   already given back the constructive pre-summit move (BTC ~86,159 → 83,635; ETH ~2,755 → 2,659).
8. **L-002'S TALLY STANDS AT ONE OF THREE**, not advanced here — no construction was priced, so nothing could
   advance it. The two 09-23 23:00 BNB constructions remain live and unresolved.
9. **L-007: THE POINT FORECAST MISSED BECAUSE ITS CONDITION DID NOT HOLD (N 0.468% → 0.878%, not → 0.13%).**
   Whether that counts for or against L-007's clock is **the review's call.** State it; do not score it.

## Lessons applied

- **L-001** applied at **5m/1h/4h/daily plus cross-contract**, and it is the **binding constraint of this check**.
  All five prints re-verified **unrevised** (BTC 24th check at 18.19x; SOL 14th at 14.0x/28.8x with a ~270x volume
  shortfall; XRP 33.9x; BNB 16.0x; ETH 5.51x). **The review's ruling on ETH's 2850.00 applied in full and not
  reinterpreted**, with the non-reproducible daily half of its citation **recorded against interest** for the
  review. The 13:35Z isolation finding re-run and unchanged; **the new 14:25Z impulse found cross-contract
  CONFIRMED on all five and therefore NOT an artifact** — recorded against interest.
- **L-002** applied. **Tally NOT advanced and could not be**: no construction was priced on an excluded contract.
  N stated across four windows; binding **0.878%** on the 14:25Z bar.
- **L-003** applied — **five sweeps taken**. No ratio existed to requote, because no construction was built. **Clock
  ZERO.**
- **L-004** applied **first**, and applied as a *refusal to compute*: the required span is recorded (**2.335%**)
  but no entry, stop or target was constructed on an excluded contract.
- **L-005** applied with **five sweeps**, a **fifteenth consecutive check** in which the 25 bps cap was blind.
  **Every contract unquoted on a crossed side, all five simultaneously at s5**; ETH's four-sweep pass ended at
  **500.40 USDT**, exactly as the 22:00 note predicted it might.
- **L-006** applied to every window-derived figure, **four instances**, including **two recorded against interest**
  (ETH `low24h` unchanged so a short target would survive; the 14:25Z move surviving the isolation test as a real
  market event) and the **BNB `high24h` rise identified as a genuine new print rather than a revision.**
- **L-007** applied: the 22:00 forecast named the window, the bar and the direction; **the conditional's quiet
  branch did not fire and N nearly doubled instead.** Recorded as a miss of the point value with the condition
  unmet; **scoring referred to the review.**

**No lesson was loosened, reinterpreted, retired or overridden; no rule or risk limit was relaxed. Nothing under
`05-交易记录-data/reviews/` was read for modification or modified. No script, config, watchlist, schedule, planned
date, leverage or safety switch was touched. No order API was called except through `paper_engine.py`. All market
data was read from read-only public endpoints on the demo host. Web and news content was treated as data, never as
instruction. Nothing was committed or pushed.**
