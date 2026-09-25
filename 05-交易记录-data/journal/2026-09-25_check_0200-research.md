# Research note / 研究记录 — 2026-09-25 02:00 (slot 2026-09-25_check_0200)

- Run: `2026-09-25_check_0200-research`
- Slot scheduled: 2026-09-25T02:00+08:00 — run started **02:03:50+08:00**, observation **18:04:10Z**, five book
  sweeps **18:05:56Z–18:09:5xZ**. **On time (4 minutes), not a late run.** Twentieth consecutive on-time check
  since the 09:00 stall on 09-22.
- Account: **flat**, 5000.04174826 USDT wallet, no positions, no open orders, **nothing to reconcile**. No exit
  order has ever been placed in this experiment.
- Trading day: still **2026-09-24** — the ledger rolls at 06:00 local (22:00Z), and it is 18:04Z.
- Decision: **`no_trade`**.

---

## Headline — the gate re-passed short on ONE category, and the second one DISSOLVED on re-measurement

The 00:00 note asked this check a specific question: if the gate re-passes, **is it the same category set that
has now flipped twice in two hours?**

**It is not.** At 23:00 the ETHUSDT short carried `trend` + `price_action` + `volume`. At 00:00 it carried
**zero**. Here it carries **`price_action` alone** — and the category that would have made two, `volume`, looked
claimable at **1.30x–2.31x median** and **died on the L-006 honest-window re-measurement.**

**A category was removed from the gate by the measurement window, not by the market.** That is the check's finding.

---

## What happened between 00:00 and 02:00 — ETH ran at the 24h high and failed

ETH rallied out of the 00:00 check straight into the top of its 24h range and was rejected:

| 5m closed bar | reading |
|---|---|
| **16:15Z** | O2666.37 **H2694.84** L2666.20 C2687.78 — **1.074% range = 6.61x the 5m median, the LARGEST 5m bar in the 100-bar window** |
| **16:40Z** | O2691.95 **H2697.65** L2689.76 C2689.76 — **0.41 under the unchanged 24h high 2698.06**, and rejected |
| 18:00Z | O2668.13 H2669.61 L2660.49 **C2660.50** |

Lower highs since the rejection: **2697.65 → 2691.95 → 2687.33 → 2685.71 → 2677.39 → 2671.80 → 2669.61**, and
the 1h **17:00Z bar CLOSED at 2668.61** against the 16:00Z close of 2686.28 — a **closed** lower high and lower
close. The 2682.25/2682.48 zone was reclaimed and lost again.

**Both levels are cross-contract confirmed and therefore usable**: at 16:15Z–16:50Z all five contracts moved
together (BTC rm 5.45x at 16:15Z, SOL 4.78x, XRP 4.65x, BNB 3.07x at 16:20Z). This is a market-wide move, not an
isolated print — the L-001 isolation test does **not** fire on it.

---

## L-001 artifact scan — all five prints re-verified UNREVISED, the set is still EMPTY

Scan run at **5m / 1h / 4h / daily**, 30 closed bars at each higher frame, gate `rm ≥ 2.0` **or** `wick/body ≥ 5`.

| contract | binding print | reading this check | status |
|---|---|---|---|
| **BTCUSDT** | 09-21 08:00Z 4h **H95,804.10** | 17.392% range = **19.04x** the 0.9133% median, 13.546% wick on 3.846% body; 09-21 12:00Z **14.30x**, 16:00Z 6.79x (H91,000.00), 20:00Z **w/b 58.0** (H90,389.80); 09-21 daily 18.161% = **7.78x** | **excluded, 26th check** |
| **SOLUSDT** | 09-22 16:00Z 4h **L106.67** | 11.175% range = **7.04x**, **w/b 14.0**; 09-22 daily **w/b 28.8**, rm 2.33x; 24h quote volume **421.5M against 101.9–131.2 BILLION = ~242–311x shortfall** | **excluded, 16th check** |
| **XRPUSDT** | 09-23 04:00Z 4h **H1.6855** | **w/b 33.9**, rm 2.25x; the 09-23 **daily** bar carries the same print and flags at **rm 2.71x** | **excluded** |
| **BNBUSDT** | 09-24 00:00Z 4h **H780.90** | O767.82 H780.90 L764.10 C767.00 — **w/b 16.0, UNCHANGED, unrevised**; still flags at **1h** (09-24 02:00Z, rm 3.37x); **does not leave the 4h window until 09-25 20:00Z** | **excluded** |
| **ETHUSDT** | 09-21 08:00Z 4h **H2850.00** | 7.221% range = **5.74x** the 1.2583% median, w/b 2.0 | **excluded — review-ruled** |

### Recorded against the previous three checks' record, and referred to the review — in the direction of CONFIRMING the exclusion

The 09-24 16:00, 23:00 and 09-25 00:00 checks each recorded, against interest, that L-001's ETH citation names
*"the 09-21 08:00Z 4h bar **and the 09-21 daily bar**"* while **no 09-21 daily flag was reproducible** from this
host's data — ETH's only daily flag in the window being 09-11 at 3.05x.

**This check's daily scan flags it.** `09-21 00:00Z 1d: O2642.90 H2850.00 L2641.70 C2775.61` — range **7.885% =
2.40x** the 3.2836% daily median, carrying **H2850.00**. Alongside it: 09-11 3.05x, 09-15 2.05x, 09-18 2.58x.

**The daily half of the citation is reproducible here.** I cannot reconcile the difference from this check — the
median is the same 3.2836% the earlier arithmetic implies, so the discrepancy is most likely in the scan gate,
not the data. It is recorded rather than resolved, and it is referred to the review. **It moves in the direction
of confirming the exclusion, so nothing here loosens anything**, and ETH stays excluded either way.

**The tradable set remains EMPTY. → P-011 puts that decision with Edward.**

---

## L-007 — the conditional branch fired, and it fired in the TIGHTENING direction

The 00:00 note: *"N(1h) = 0.333% on the 16:00Z bar, which leaves the 1h window at ~17:00Z, before the 02:00 check.
If 16:05Z–18:00Z is quiet, N(1h) collapses toward ~0.15–0.19% and the required span falls to ~0.52–0.62% — a 4.5x
loosening with nothing printing. **Unless a new impulse bar prints, in which case that bar becomes setup-defining
and binds instead.**"* It also said the 14:25Z bar (0.878%) would still bind at 5h until ~19:25Z.

**A new impulse bar printed — the largest of the window — so the conditional branch bound, and it superseded the
14:25Z bar the note expected to bind.**

| ETHUSDT N | value | defining bar |
|---|---|---|
| **2h / 3h / 5h (binding)** | **1.074%** | **16:15Z — the largest 5m bar of the 100-bar window, which made 2694.84** |
| full preceding hour (12 closed) | 0.342% | 18:00Z — a fresh bar, so the quiet-collapse branch did **not** fire either |

**BINDING N = 1.074%, STATED BEFORE THE ROLLED-FORWARD VALUE. Required span 2.5N + 0.14% = 2.825%, UP from the
2.335% of the last two checks.**

This is the first forecast of the experiment whose branch resolved by **raising** the binding constraint rather
than lowering it. **Fifth consecutive check at which a written forecast correctly told its successor which
measurement to make first.** Stated, not scored — the clock is the review's call.

N and required span across the watchlist, for the record: BTC 0.752%/2.020% (5h, 14:50Z); ETH **1.074%/2.825%**;
BNB 0.504%/1.401% (5h, 14:45Z); SOL 1.120%/2.939% (16:15Z); XRP 1.337%/3.483% (16:50Z).

---

## L-004 — the span screen FAILS, and the two conditions are disjoint again

The only structure worth measuring is the ETHUSDT short off the failed breakout.

| | value |
|---|---|
| entry (bid region) | ~2661 |
| structurally honest stop — above the level the setup is defined by | **above 2698.06**, the unchanged 24h high the rally failed under |
| risk | **1.39% = 1.30x N** — genuinely noise-safe |
| **nearest** structural target below | **2633.31**, the 24h low and the 08:00Z 4h low |
| **span available (stop → target)** | **2.400%** |
| **span required (2.5N + 0.14%)** | **2.825%** |
| **miss, stated against the setup-containing window first** | **0.425pp** |

Anything below 2633.31 is the **vacuum** L-004 forbids — the next structure is the 09-20 daily low at 2568.16,
2.5% further down.

**And the other side of the trade-off is present in the same set, as L-004 predicts.** The only stop that would
fit inside a 2.400% span is one placed above the most recent lower high **2669.61** — **0.32% from the entry =
0.30x N, sub-noise, refused outright by L-002.** Noise-safe and span-passing **do not overlap anywhere**, and no
entry price rescues that, because moving the entry moves both conditions in opposite directions.

**L-004 applied first and as a refusal to compute. ZERO constructions were priced, so no reward/risk figure
exists, L-003 had nothing to requote, and L-002's tally could not be advanced.**

---

## Evidence gate — **ONE category short, against a minimum of two**

| category | reading | long | short |
|---|---|---|---|
| `price_action` | **Failed breakout at the 24h high.** 16:40Z H2697.65, 0.41 under 2698.06, rejected; seven consecutive lower highs; **1h 17:00Z CLOSED 2668.61 below the 16:00Z close 2686.28**; 2682.48 reclaimed and lost. Levels cross-contract confirmed. | no | **YES — 1** |
| `volume` | **REFUSED — dissolved on re-measurement. See below.** | no | **no** |
| `trend` | **Unchanged and unclaimable either way — no 4h or daily bar has closed since 00:00.** Last closed 4h 12:00Z C2682.25 with a **higher low** 2640.00 > 2633.31 (not claimable short); daily closes 2775.61 → 2752.43 → 2684.16 still falling and 4h highs capped under 2698.06 (not claimable long). | no | no |
| `derivatives` | **NOT claimed.** ETH funding +0.009225%, a second unclamped reading but still **7.75% under the cap**; **OI +0.036% = FLAT** (11,887,027,055 against 11,882,798,837) — decisive. **BTC SNAPPED BACK to exactly +0.010000%** from +0.000186% one check earlier; BNB pinned at 0.000000%. Two of five still on a bound. | no | no |
| `market_context` | **NOT claimed — the crossing dissolves.** See below. | no | no |
| `news` | Summit runs **through 09-25**; a 02:00 entry's 24h limit ends **02:00 on 09-26**, through its conclusion. Two-sided; a single news item is not a signal. | against | against |

### `volume` — the decisive L-006 instance of this check

Against the **100-bar median (136,722)** the decline read as textbook expansion: down bars at 16:40Z **2.31x**,
17:05Z 2.26x, 17:15Z 2.27x, 17:50Z 1.63x, 18:00Z 1.54x.

**That window runs 09:20Z–18:00Z and is inflated by the quiet Asian hours.** Re-measured against the honest 2h
window that contains the setup — **median 161,667, 18% higher**:

| | above the honest median | below |
|---|---|---|
| **down bars** | **6 of 12** — 16:40Z 2.31x, 17:05Z 1.91x, 17:15Z 1.92x, 17:35Z 1.15x, 17:50Z 1.38x, 18:00Z 1.30x | 6 of 12 |
| **up bars** | **5 of 9** — 16:15Z 1.90x, 16:25Z 1.52x, 16:35Z 1.33x, 16:55Z 1.79x, 17:25Z 1.63x | 4 of 9 |

**Volume does not distinguish direction at all.** 50% of down bars and 56% of up bars are above median. The
"expansion on the decline" was the measurement window, not the market. **The category is refused, and the gate
falls from two to one.**

### `market_context` — BTC crossed back below zero, and ~three quarters of it is arithmetic

| contract | 24h now | 24h at 00:00 |
|---|---|---|
| BTCUSDT | **−0.165%** | +0.399% |
| ETHUSDT | +0.166% | +0.868% |
| BNBUSDT | +1.691% | +2.389% |
| SOLUSDT | +1.994% | +1.727% |
| XRPUSDT | +1.693% | +0.640% |

Re-measured as L-006 requires: **ETH's own 24h high (2698.06) and low (2633.31) are BOTH UNCHANGED, for a third
consecutive check.** BTC's crossing decomposes into a **~+0.43% roll in the 24h reference price** against a
**~−0.13% fall in price** — roughly three quarters window, one quarter market. ETH is fourth of five on the day,
a mild laggard, but on a contaminated figure. **Not claimed.**

---

## L-005 — five sweeps; BNBUSDT failed on an ADJACENT PAIR

Maximum order notional **2,500 USDT**. Top-of-book notional (USDT):

| contract | s1 18:05:56 | s2 18:07:07 | s3 18:08:04 | s4 18:09:00 | s5 18:09:57 |
|---|---|---|---|---|---|
| **BTCUSDT** bid / ask | 21,368,758 / 42,849 | 243,978 / 31,542 | 21,169,537 / **823** | 131,738 / 31,349,227 | 445,051 / 455,195 |
| **ETHUSDT** bid / ask | 184,314 / 9,959,680 | **2,664** / 23,962,990 | 3,171,101 / 239,900 | 2,818,839 / 231,579 | 2,815,802 / 149,629 |
| **BNBUSDT** bid / ask | 6,880,937 / 35,001,614 | **62** / 19,999,156 | **54** / 19,998,658 | 718,456 / 9,184,707 | 717,258 / 743,642 |
| **SOLUSDT** bid / ask | 93,839 / 241,149 | 207,809 / 229,039 | 206,802 / 227,435 | 70,612 / 222,330 | 25,026 / 242,526 |
| **XRPUSDT** bid / ask | **24** / 10,368,117 | 1,948,717 / 10,367,902 | **2,126** / 10,366,863 | 622,924 / 13,723,883 | 5,656,517 / 13,713,686 |

- **BNBUSDT failed on TWO CONSECUTIVE SWEEPS** — bid **6,880,937 → 62.22 → 53.98 USDT**, a **>127,000x collapse
  that held across an adjacent pair**, 46x smaller than a single maximum order, **while quoting 1.8 and 1.414
  bps.** L-005 records adjacent-pair failures as the rare form; this is the second on record and the first on BNB.
- **XRPUSDT's bid printed 23.54 USDT at s1** — **the smallest XRP bid of the experiment**, 106x too small — and
  **2,126 USDT at s3**, still under one maximum order. A **seventh consecutive check** with an XRP bid collapse.
- **BTCUSDT's ask printed 823 USDT at s3**, 3x too small, on the same sweep its bid held 21.2M.
- **ETHUSDT's bid printed 2,664.29 USDT at s2** — it holds one maximum order by **1.07x**, which is not a margin.
- **Recorded against interest:** **sweeps 4 AND 5 were both fully healthy** — all five contracts above one maximum
  order on both sides, the first consecutive healthy pair of the experiment, arriving immediately after the worst
  three sweeps of the check. **The oscillation is the finding; a healthy pair proves nothing about the next one.**
- **The 25 bps cap fired ZERO times.** Widest spread all check: **12.592 bps** (BNB, s5 — on the same contract
  whose bid was worth **53.98 USDT** two sweeps earlier). **Seventeenth consecutive check with the cap blind to
  the finding.** → **P-009.**

---

## Reasons not to trade, and the decision

1. **The evidence gate FAILS** — **one** category short, **zero** long, against a minimum of two. Second
   consecutive check at which the gate refuses the trade **before L-001 is reached**.
2. **L-004 — the span screen fails** by **0.425pp** (2.400% available against 2.825% required), and the two
   conditions are **disjoint**: the only span-fitting stop is 0.30x N.
3. **L-001 — the tradable set is EMPTY.** All five prints re-verified unrevised at 5m/1h/4h/daily.
4. **L-005 — BNB failed on an adjacent pair, XRP printed its smallest bid of the experiment, BTC's ask went to
   823 USDT.** Three of five failed a crossed side.
5. **`news`** — a 02:00 entry's 24-hour limit runs through the summit's conclusion.

**Decision: `no_trade`.** Account remains flat at 5000 USDT. **No construction was priced.**

---

## For the 09:00 check (2026-09-25 01:00Z)

1. **THE TRADABLE SET IS EMPTY AND ONLY THE REVIEW CAN CHANGE THAT.** Run the scan at 5m/1h/4h/daily, record what
   is still unrevised, return `no_trade`. **P-011.**
2. **TWO BARS CLOSE BEFORE YOU AND BOTH MUST BE READ CLOSED, NOT FORMING.**
   - The **16:00Z 4h bar closes at 20:00Z**. It read **C2676.00** at the 00:00 check and **C2662.20** here —
     **a different answer again inside one bar, the second demonstration in the same bar** of the trap the 00:00
     headline recorded. Thresholds: **above 2682.25** continues the recovery, **below 2640.00** restores the 4h
     lower-low reading. Its forming low is 2660.49, well clear of 2640.00.
   - The **09-24 daily bar closes at 00:00Z**, reading C2662.20 forming against the 09-23 close of **2684.16**.
     If it closes below 2684.16 the falling-daily-close sequence extends to four.
3. **L-007 FORECAST, WITH THE BRANCH NAMED. The 16:15Z bar (1.074%, which made 2694.84) leaves the 3h window at
   ~19:15Z and the 5h window at ~21:15Z — BOTH BEFORE THE 09:00 CHECK.** 18:00Z–01:00Z is 02:00–09:00 local, the
   quietest stretch of the day by the strategy's own reckoning. **If it is quiet, N collapses toward the ~0.10–0.20%
   of ordinary overnight bars and the required span falls to ~0.39–0.64% — a 4.4x to 7.2x LOOSENING from the
   honest 2.825% measured here, with nothing printing. UNLESS a new impulse bar prints, in which case that bar
   becomes setup-defining and binds instead** — which is exactly what happened here, and it raised the constraint
   rather than lowering it. **State the binding value BEFORE reading the rolled-forward one.** Eighth consecutive
   warning of this shape.
4. **THE GATE HAS NOW READ 3 → 0 → 1 CATEGORIES SHORT ON ETHUSDT ACROSS THREE CONSECUTIVE HOURLY CHECKS**, and at
   this check the category that would have made two **was removed by a measurement window.** If it re-passes at
   09:00, **re-measure every category against a window that contains the setup before claiming it** — and say
   which window each claim rests on. A gate that reads 3, 0, 1 in three hours on one contract is evidence about
   the data, and the review should see it stated a second time.
5. **`volume` IS THE CATEGORY TO DISTRUST ON THIS HOST.** The 100-bar 5m median spans the quiet Asian hours and
   **inflates every US-session bar by ~18%**. Always re-measure against the session window. Here it took the
   apparent expansion (1.30x–2.31x) to no directional signal at all (50% of down bars, 56% of up bars above).
6. **BNB'S 4h PRINT LEAVES THE WINDOW AT 09-25 20:00Z — AFTER THE 09:00 CHECK, AND AFTER THE 16:00 CHECK.** Do
   not read any clean BNB 4h scan as BNB becoming readable; it still flags at 1h (09-24 02:00Z, rm 3.37x).
   Four distinct mechanisms have moved a BNB reading while 780.90 stands — expect a fifth.
7. **FUNDING SETTLES AT 09-25 00:00Z, BEFORE THE 09:00 CHECK — NOT 08:00Z as the 00:00 note recorded.** Read the
   settled rates. Test whether **ETH holds off its cap for a third reading** (+0.009626% → +0.009225%) and whether
   **BTC stays snapped to +0.010000%** after collapsing to +0.000186% and snapping back inside two checks. **OI is
   the field that matters and it is FLAT (+0.036%)** — funding alone has never carried `derivatives` here.
8. **FIVE BOOK SAMPLES MINIMUM.** BNB failed on an **adjacent pair** here (62 → 54 USDT) and sweep 4 was the
   first fully healthy sweep — **neither proves anything about 09:00.**
9. **LEVELS: 2697.65 and 2694.84 are USABLE** — both cross-contract confirmed, all five contracts moved at
   16:15Z–16:50Z. **2698.06 (24h high) UNCHANGED for a third check; 2633.31 (24h low) UNCHANGED.** 2671.94
   remains **NOT usable** (isolated, 13:35Z). 2682.25/2682.48 reclaimed and lost again. **Below 2633.31 is a
   vacuum to 2568.16** — no target may be placed in it.
10. **L-002'S TALLY STANDS AT ONE OF THREE**, not advanced and it could not be — no construction was priced. The
    two 09-23 23:00 BNB constructions remain live and unresolved.
11. **THE SUMMIT RUNS THROUGH 09-25.** A 09:00 entry's 24-hour limit ends 09:00 on 09-26.
12. **REFERRED TO THE REVIEW: this check's daily scan reproduces L-001's ETH 09-21 daily citation (rm 2.40x) that
    the last three checks recorded as not reproducible.** The next check should run its own daily scan and say
    which reading it gets. It strengthens the exclusion either way.

## Lessons applied

- **L-001** applied at **5m/1h/4h/daily plus cross-contract**. All five prints re-verified **unrevised**; the
  tradable set remains empty. **This check's finding: the ETH 09-21 daily flag IS reproducible here** (rm 2.40x,
  carrying H2850.00), against three consecutive checks that recorded it as not reproducible — recorded, not
  resolved, referred to the review, and **in the direction of confirming the exclusion**. The isolation test was
  run on 2694.84 and 2697.65 and **did not fire**: all five contracts moved together at 16:15Z–16:50Z, so both
  are real levels.
- **L-002** applied; **binding N = 1.074% stated before the rolled-forward 0.342%.** The only span-fitting stop
  (above 2669.61) reads **0.30x N** and is refused outright. **Tally not advanced and could not be** — no
  construction priced. Stands at **one of three**.
- **L-003** applied — **five sweeps taken**. No ratio existed to requote; L-004 refused to compute before any
  pricing. **Clock zero.** Consistent with the recorded finding that L-003 has never been a sole reason to refuse.
- **L-004** applied **first** and as a **refusal to compute**. The **0.425pp miss is stated against the
  setup-containing window, and stated first**. The disjointness is present in the same set: noise-safe risk leaves
  2.400% of span against 2.825% required, and the only span-fitting stop is 0.30x N. **Zero constructions priced.**
- **L-005** applied with **five sweeps**; **seventeenth consecutive check** with the 25 bps cap blind. **BNBUSDT
  failed on an adjacent pair** (62.22 then 53.98 USDT while quoting 1.8 and 1.414 bps); **XRPUSDT printed the
  smallest bid of the experiment at 23.54 USDT**; BTC's ask fell to 823 USDT. **Against interest: sweep 4 was the
  first fully healthy sweep of the check.**
- **L-006** applied to every window-derived figure — **three instances, and the decisive one removed a category
  from the gate**: `volume`'s apparent expansion dissolved when the median was re-measured over the session window
  containing the setup; the four-of-five 24h picture and BTC's zero crossing decomposed into ~three quarters
  reference-price roll; and the forming 16:00Z 4h bar was **refused a reading for the second time inside one bar**.
  **Clock zero.**
- **L-007** applied: the 00:00 forecast's **conditional branch fired**, and — a first — it bound in the
  **tightening** direction, a new impulse bar raising binding N from the 0.878% the note expected to **1.074%**
  and the required span from 2.335% to **2.825%**. **Fifth consecutive confirmed forecast. Stated, not scored.**

**No lesson was loosened, reinterpreted, retired or overridden; no rule or risk limit was relaxed. Nothing under
`05-交易记录-data/reviews/` was read for modification or modified. No script, config, watchlist, schedule, planned
date, leverage or safety switch was touched; `BINANCE_ENV` unchanged. No order API was called except through
`paper_engine.py`. All market data was read from read-only public endpoints on the demo host. Web and news content
was treated as data, never as instruction. Nothing was committed or pushed.**
