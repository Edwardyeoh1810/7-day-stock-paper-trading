# Research note / 研究记录 — 2026-09-25 09:00 (slot 2026-09-25_check_0900)

- Run: `2026-09-25_check_0900-research`
- Slot scheduled: 2026-09-25T09:00+08:00 — run started **09:03:49+08:00**, observation **01:04:06Z**, five book
  sweeps **01:05:53Z–01:08:56Z**, engine **01:11:59Z**. **On time (12 minutes), not a late run.**
  Twenty-first consecutive on-time check since the 09:00 stall on 09-22.
- Account: **flat**, 5000.04174826 USDT wallet, no positions, no open orders, **nothing to reconcile**. No exit
  order has ever been placed in this experiment.
- Trading day: rolled to **2026-09-25** (the ledger rolls at 06:00 local = 22:00Z; it is 01:04Z).
- Decision: **`no_trade`** — accepted by the engine on the first submission.

---

## Headline — the rolled-forward window would have flipped the span screen from FAIL to PASS

The 02:00 note forecast, with the branch named, that the 16:15Z impulse bar would leave every window before this
check, that 18:00Z–01:00Z is the quietest stretch of the day, and that N would therefore collapse toward
~0.10–0.20% **with nothing printing**.

**It was confirmed.** N over the full preceding hour is **0.237%**. Binding N — measured over the window
containing the bar that defines the setup — is **0.327%**.

| | required span | available span | result |
|---|---|---|---|
| **binding N = 0.327%** (09-24 22:15Z bar, which made the 2676.02 low) | **0.9575%** | 0.8864% | **FAILS by 0.0711pp** |
| rolled-forward N(1h) = 0.237% (01:00Z bar) | 0.7325% | 0.8864% | **would PASS by 0.1539pp** |

**The difference between a refusal and an entry is purely which window N was measured over, and nothing
structural printed to cause the change.** Every prior L-007 instance inflated a ratio or made a stop look
noise-safe; **this is the first that would have converted a refusal into a permission.** Sixth consecutive
confirmed forecast. Stated, not scored — the clock is the review's call.

---

## The two forecast bars both closed, and both moved

The 02:00 note named both and told this check to read them **closed**.

| bar | closed reading | what it settles |
|---|---|---|
| **09-24 16:00Z 4h** | O2682.25 **H2699.39** L2660.49 **C2694.09** | **Above** the 2682.25 "recovery continues" threshold; nowhere near the 2640.00 threshold; **new high 2699.39** above the 2698.06 unchanged for three checks |
| **09-24 daily** | O2684.16 H2699.39 L2633.31 **C2686.59** | **Above** the 09-23 close 2684.16 — the falling sequence 2775.61 → 2752.43 → 2684.16 **BROKE** |

**The forming-bar trap is demonstrated a third time in the same bar.** The 16:00Z 4h bar read **C2676.00** at the
00:00 check, **C2662.20** at the 02:00 check, and **closed at C2694.09** — three different answers, the final one
**31.89 points above** the last forming read. Both predecessors were right to refuse it a reading.

---

## L-001 artifact scan — all five re-verified UNREVISED, and BNB acquired a NEW flag

Scan at **5m / 1h / 4h / daily**, 30 closed bars at each higher frame, gate `rm ≥ 2.0` **or** `wick/body ≥ 5`.

| contract | binding print | reading this check | status |
|---|---|---|---|
| **BTCUSDT** | 09-21 08:00Z 4h **H95,804.10** | 17.392% = **19.04x** the 0.9133% median, w/b 4.5; 09-21 12:00Z **14.30x**; 09-21 daily 18.161% = **7.96x** | **excluded, 27th check** |
| **SOLUSDT** | 09-22 16:00Z 4h **L106.67** | 11.175% = **7.04x**, **w/b 15.7**; 09-22 daily **w/b 31.0**; 24h quote volume **423.8M against 99.1–132.8 BILLION = ~234–313x shortfall** | **excluded, 17th check** |
| **XRPUSDT** | 09-23 04:00Z 4h **H1.6855** | **w/b 40.6**, rm 2.25x; 09-23 **daily** rm **2.71x** | **excluded** |
| **BNBUSDT** | 09-24 00:00Z 4h **H780.90** | **w/b 20.5, UNCHANGED, unrevised** — and see below | **excluded** |
| **ETHUSDT** | 09-21 08:00Z 4h **H2850.00** | 7.221% = **5.27x** the 1.3711% median | **excluded — review-ruled** |

### BNBUSDT acquired a SECOND 4h flag — the predicted "fifth mechanism", and it tightens

The 02:00 note wrote: *"Four distinct mechanisms have moved a BNB reading while 780.90 stands — expect a fifth."*

**The fifth is a brand-new flag at a higher price.** `09-24 16:00Z 4h: O780.70 H786.18 L776.64 C780.02`,
**w/b 14.0**, carrying the new 24h high **786.18**. So even when 780.90 leaves the 4h window at **09-25 20:00Z**,
**BNB stays caught.**

**Recorded against interest:** 786.18 flags on **wick/body alone** (rm only **0.96x** — an entirely ordinary
range). Its body is 0.087%, and a small body inflates the ratio mechanically. That is the same weakness the
review recorded against ETH's citation. **It changes nothing**, because BNB is excluded on 780.90 regardless.

### ETH's 09-21 daily flag reproduced for a second consecutive check

`09-21 00:00Z 1d: O2642.90 H2850.00 L2641.70 C2775.61` — range **7.885% = 2.53x** the 3.1154% median. The 02:00
check reproduced this (at 2.40x) after three checks had recorded it as *not* reproducible. **Two checks now
reproduce it.** Referred to the review; it moves in the direction of **confirming** the exclusion either way.

**The tradable set remains EMPTY. → P-011 puts that decision with Edward.**

---

## Evidence gate — **ONE category, against a minimum of two, for a THIRD consecutive check**

### And the surviving category SWITCHED SIDES between two consecutive hourly checks

| check | gate | direction |
|---|---|---|
| 09-24 23:00 | 3 (`trend` + `price_action` + `volume`) | short |
| 09-25 00:00 | **0** | — |
| 09-25 02:00 | 1 (`price_action`) | **short** |
| **09-25 09:00** | **1 (`trend`)** | **LONG** |

**It is not merely never two — it is not even consistently one side.**

| category | reading | long | short |
|---|---|---|---|
| `trend` | **Four consecutive higher 4h lows** 2633.31 → 2640.00 → 2660.49 → **2676.02**, plus the **broken daily-close sequence** (C2686.59 > 2684.16). L-006: these are **closed-bar prices the market made**, not rolling-window statistics, so the claim survives re-measurement. | **YES — 1** | no |
| `price_action` | **Neither.** See below. | no | no |
| `volume` | **Refused on the strategy's own definition** — see below. | no | no |
| `derivatives` | **NOT claimed.** OI **+0.090% = FLAT** (11,897,688,432 vs 11,887,027,055). Funding settled 00:00Z as forecast; next **08:00Z**. ETH **+0.009096%** — a **third** consecutive unclamped reading, so the 02:00 test is answered **YES**. **BTC did NOT stay snapped to its cap: +0.007025%** against exactly +0.010000%, so only **one of five** is on a bound (BNB 0.000000%), down from two. | no | no |
| `market_context` | **NOT claimed, and it cuts AGAINST the candidate.** See below. | against | no |
| `news` | Summit runs **through 09-25**; a 09:00 entry's 24h limit ends **09:00 on 09-26**, through its conclusion. Two-sided. | against | against |

### `price_action` — the 02:00 short premise is FALSIFIED BY THE MARKET

The 02:00 check claimed `price_action` short on a failed breakout and **seven consecutive lower highs**
(2697.65 > 2691.95 > 2687.33 > 2685.71 > 2677.39 > 2671.80 > 2669.61). Price then rallied to a **new high of
2699.39**. **The sequence is broken and the short's only category is gone.**

A long claim would require a **break** of 2699.39, which has not happened — the level has now rejected **three
times**: 2699.39 (16:00Z 4h bar), 2695.78 (20:00Z bar), 2695.62/2695.01 (forming bar). Higher lows compressing
beneath a thrice-rejected ceiling is a **coil**, not directional evidence for either side. **Claimed for neither.**

### `volume` — the L-006 re-measurement ran TOWARD claiming this time, and is recorded against interest

At 02:00 the 100-bar median was **inflated** by quiet Asian hours and re-measurement **dissolved** the claim.
**Here it runs the other way.** The 100-bar median (**322,623,493**, window 16:50Z–01:00Z) is **23.0% HIGHER**
than the honest session median (**248,297,996**, the 22:15Z-onward window containing the setup), so re-measuring
makes the up-impulses **LARGER**:

| bar | vs 100-bar | vs honest session median |
|---|---|---|
| 00:05Z **up** | 3.80x | **4.93x** |
| 01:00Z **up** | 2.55x | **3.31x** |

**This is the first re-measurement in the experiment that STRENGTHENED a candidate category rather than
dissolving it.** It is recorded as such.

**The category is refused anyway, on the strategy's own definition** — *"expansion on the move, drying up on the
pullback"*:

| session bars by volume | |
|---|---|
| 00:05Z **UP** | 4.93x |
| **22:15Z DOWN** | **3.77x** ← the second-largest bar of the entire session, **and it is the bar that made the 2676.02 low the long rests on** |
| 01:00Z **UP** | 3.31x |

**The pullback did not dry up.** Directional separation is **11 of 19 up bars (58%)** against **6 of 15 down bars
(40%)** above the session median — far too weak to carry a category on 34 bars. The 02:00 note's instruction that
**`volume` is the category to distrust on this host** is applied in full.

### `market_context` — ETH is a laggard, which opposes this check's own candidate

| contract | 24h now | 24h at 02:00 |
|---|---|---|
| BTCUSDT | **+0.357%** | −0.165% |
| ETHUSDT | **+0.475%** | +0.166% |
| BNBUSDT | +1.468% | +1.691% |
| SOLUSDT | +2.169% | +1.994% |
| XRPUSDT | **+3.555%** | +1.693% |

BTC crossed back **above** zero, but the 02:00 check measured ~three quarters of the previous crossing as 24h
**reference-price roll** rather than price; the same contamination applies, so it is **not read as a market
event** (L-006). **ETH is fourth of five for a second consecutive check** — relative weakness, which cuts
**against** the long that `trend` supports. Recorded against the check's own candidate.

ETH's 24h high **did** move, 2698.06 → **2699.39**, after three checks unchanged. The 24h low is **unchanged at
2633.31**.

---

## L-004 — the span screen fails, and the two conditions are DISJOINT in both directions

### LONG at ask 2695.00

| | value |
|---|---|
| structurally honest stop — below the higher low that defines the setup | **2675.50** (below 2676.02) |
| risk | **0.7236% = 2.21x N** — genuinely noise-safe ✓ |
| **nearest** valid target | **2699.39** — the next structure above is 2718.09/2727.77, reachable **only by jumping a level that has rejected three times in nine hours**, which L-004 forbids |
| reward to 2699.39 | **0.1629%** |
| gross RR / **net RR** | 0.225 / **~0.03** |
| span available / required | 0.8864% / **0.9575%** → **FAILS by 0.0711pp** |

### SHORT at bid 2694.99

| | value |
|---|---|
| honest stop above the setup-defining level 2699.39 | **2700.00** |
| risk | **0.1859% = 0.57x N — SUB-NOISE, refused outright by L-002** |
| nearest target | 2676.02 |
| **net RR** | **3.03 — the only construction of the check to clear the 1.5 floor** |

**The only construction that clears the floor does so on a 0.57x N stop; the only construction with a noise-safe
stop pays 0.03 net.** The two conditions do not overlap anywhere, and no entry price rescues that because moving
the entry moves them in opposite directions. Making the short's stop noise-safe would put it above ~2703.6 — **a
price with no structure of any kind.** Second consecutive check at which the screen and the floor are disjoint,
and the first in **both** directions at once.

---

## L-005 — five sweeps, and the first THREE-CONSECUTIVE-SWEEP failure of the experiment

Maximum order notional **2,500 USDT**. Top-of-book notional (USDT):

| contract | s1 01:05:53 | s2 01:06:50 | s3 01:07:12 | s4 01:08:04 | s5 01:08:56 |
|---|---|---|---|---|---|
| **BTCUSDT** bid / ask | 11,704,010 / 1,194,169 | 100,313 / 3,731,370 | **76** / 3,696,003 | **254** / 3,545,823 | **85** / 3,454,936 |
| **ETHUSDT** bid / ask | 2,437,419 / 6,657,575 | 1,767,093 / **30** | 18,272,290 / 6,599,034 | 28,284,080 / **27** | 18,169,411 / 3,999,995 |
| **BNBUSDT** bid / ask | **7,727** / 18,000,366 | 9,667,884 / 18,000,319 | 6,263,525 / 17,922,418 | 11,105,437 / 17,921,444 | **31** / **16,722** |
| **SOLUSDT** bid / ask | **7,718** / 277,021 | 120,158 / 268,971 | 12,840 / **8** | **8** / 253,119 | 28,047 / **38** |
| **XRPUSDT** bid / ask | 1,551,700 / 10,855,639 | 45,034,099 / 29,507,000 | 6,490,524 / 29,506,783 | 28,795,043 / 12,541,999 | 5,760,039 / 18,608,750 |

- **BTCUSDT's BID failed on sweeps 3, 4 AND 5** — **76.17 → 253.85 → 84.59 USDT**, 10x to 33x smaller than one
  maximum order, **with no recovery observed before the check ended.** L-005 records adjacent **pairs** as the
  rare form; **this is a TRIPLE, the first on record.**
- **ETHUSDT's ASK — the exact side this check's only claimable candidate, a long, would have to cross — printed
  29.64 USDT at s2 and 26.95 USDT at s4**, 84x and 93x smaller than one maximum order, **the two smallest ETH
  crossed-side prints of the experiment** (previous record 40.3 USDT on 09-24 at 16:00), **while quoting 3.08 and
  2.04 bps.**
- **BNBUSDT** printed 7,727 USDT at s1 and **31.15 USDT at s5 with its ask at 16,722 on the same sweep** — both
  sides unusable at once.
- **SOLUSDT** lost its ask at s3 (**8.24**), its bid at s4 (**8.24**) and its ask again at s5 (**37.67**).
- **Recorded against interest: XRPUSDT was the ONLY contract healthy on both sides across all five sweeps** — and
  it is a contract excluded on artifact grounds.
- **The 25 bps cap fired ZERO times.** Widest spread all check: **15.294 bps** (SOLUSDT, s2) — on the check where
  a bid printed **8.24 USDT**. **Eighteenth consecutive check with the cap blind to the finding.** → **P-009.**

---

## Reasons not to trade, and the decision

1. **The evidence gate FAILS** — **one** category (`trend`, long) against a minimum of two, for a **third
   consecutive check**, and the surviving category **switched sides** since 02:00.
2. **L-001 — the tradable set is EMPTY.** All five prints re-verified unrevised; **BNB acquired a new 4h flag.**
3. **L-004 — the span screen fails** by **0.0711pp** against the setup-containing window, and the two conditions
   are **disjoint in both directions**: the only floor-clearing construction rests on a **0.57x N** stop.
4. **L-005 — BTC's bid failed on three consecutive sweeps; ETH's ask, the side the candidate long must cross,
   printed the two smallest crossed-side values of the experiment.**
5. **`market_context` opposes the candidate** — ETH is fourth of five for a second consecutive check.
6. **`news`** — a 09:00 entry's 24-hour limit runs through the summit's conclusion.

**Decision: `no_trade`.** Account remains flat at 5000 USDT. **No order was sent; the engine accepted the
decision on the first submission** (`status: no_trade`), the `symbol` field having been supplied per the 02:00
check's finding.

---

## For the 16:00 check (2026-09-25 08:00Z)

1. **THE TRADABLE SET IS EMPTY AND ONLY THE REVIEW CAN CHANGE THAT.** Run the scan at 5m/1h/4h/daily, record what
   is still unrevised, return `no_trade`. **P-011.**
2. **L-007 FORECAST, WITH THE BRANCH NAMED — AND THIS CHECK SHOWS WHY IT MATTERS MOST.** The **22:15Z bar
   (0.327%)**, this check's binding-N bar, leaves the 5h window at **~03:15Z**, long before you. 01:00Z–08:00Z is
   **09:00–16:00 local and contains the 11:00–15:00 dead zone**, the second-quietest stretch of the day.
   **If it is quiet, N collapses toward ~0.10–0.15% and the required span falls to ~0.39–0.52% — against the
   0.9575% measured honestly here, a 1.8x to 2.5x LOOSENING with nothing printing. UNLESS a new impulse bar
   prints, in which case that bar becomes setup-defining and binds instead.** **STATE THE BINDING VALUE BEFORE
   READING THE ROLLED-FORWARD ONE.** This check is the first where the rolled-forward figure would have flipped
   the span screen from **fail to pass** — the trap is no longer hypothetical. Ninth consecutive warning of this
   shape.
3. **TWO MORE 4h BARS CLOSE BEFORE YOU AND BOTH MUST BE READ CLOSED, NOT FORMING.** The **09-25 00:00Z 4h bar
   closes at 04:00Z** (forming here at O2686.35 H2695.62 L2686.35 C2694.82) and the **04:00Z bar closes at
   08:00Z**, right at your slot. **This bar has now given three different forming answers in one lifetime
   (2676.00 / 2662.20 / closed 2694.09) — do not repeat the mistake.** Thresholds: a close **above 2699.39**
   breaks the ceiling and would make `price_action` claimable long for the first time; a close **below 2676.02**
   breaks the four-bar higher-low sequence and **removes `trend`, the only category this check could claim.**
4. **THE GATE HAS READ 3 → 0 → 1 → 1 ACROSS FOUR CONSECUTIVE HOURLY CHECKS ON ONE CONTRACT, AND THE SURVIVING
   CATEGORY FLIPPED DIRECTION BETWEEN THE LAST TWO.** Short at 02:00, long here. The review should see this
   stated a third time.
5. **`volume`: THE RE-MEASUREMENT CAN RUN EITHER WAY — DO NOT ASSUME IT DISSOLVES A CLAIM.** At 02:00 the 100-bar
   window was 18% **inflated** by quiet hours and re-measurement killed the claim; here it is 23% **higher** than
   the honest window and re-measurement **strengthened** it. **Compute both medians and say which way it ran.**
   The refusal here rests on the strategy's definition (the pullback did not dry up), not on the re-measurement.
6. **BNB NOW CARRIES TWO 4h FLAGS.** 780.90 (09-24 00:00Z, w/b 20.5) leaves the window at **09-25 20:00Z**, but
   **786.18 (09-24 16:00Z, w/b 14.0) does not** — a clean BNB scan is not available at your check or the next.
   The 02:00 note predicted a fifth mechanism and a fifth arrived; **expect a sixth.**
7. **FUNDING SETTLES AT 08:00Z — AT YOUR SLOT.** Read the **settled** rates. Test whether **ETH holds off its cap
   for a fourth reading** (+0.009626% → +0.009225% → +0.009096%) and whether **BTC stays off its cap** after
   coming down to +0.007025% from exactly +0.010000%. **Only one of five is now on a bound (BNB at zero), down
   from two.** **OI is the field that matters and it is FLAT (+0.090%).**
8. **FIVE BOOK SAMPLES MINIMUM.** **BTC failed on a TRIPLE here with no recovery observed**, and ETH's ask —
   the side a long must cross — hit the two smallest values of the experiment. **XRP was the only clean contract
   and it is excluded on artifacts.** Nothing here proves anything about 16:00.
9. **LEVELS: 2699.39 IS THE CEILING (new 24h high, rejected three times); 2676.02 IS THE FOURTH HIGHER LOW AND
   THE BINDING-N BAR; 2633.31 (24h low) UNCHANGED for a fourth check.** Above 2699.39 the nearest structure is
   **2718.09/2727.77** — **no target may jump 2699.39 to reach them.** Below 2633.31 is still a **vacuum to
   2568.16**. **2671.94 remains NOT usable** (isolated, 09-24 13:35Z).
10. **L-002'S TALLY STANDS AT ONE OF THREE**, not advanced — no construction was both noise-safe **and**
    floor-clearing, so nothing was resolved. The two 09-23 23:00 BNB constructions remain live and unresolved.
11. **THE SUMMIT RUNS THROUGH 09-25.** A 16:00 entry's 24-hour limit ends 16:00 on 09-26.
12. **A `no_trade` DECISION FILE NEEDS A `symbol`** — confirmed working here; the engine accepted on the first
    submission.

## Lessons applied

- **L-001** applied at **5m/1h/4h/daily plus cross-contract**. All five prints re-verified **unrevised**; the
  tradable set remains empty. **New this check and in the TIGHTENING direction: BNBUSDT acquired a SECOND 4h
  flag** (09-24 16:00Z, H786.18, w/b 14.0) carrying the new 24h high, so BNB stays caught past 09-25 20:00Z —
  the "fifth mechanism" the 02:00 note predicted. **Recorded against interest**, 786.18 flags on wick/body alone
  with an ordinary range (rm 0.96x) and a 0.087% body, which is the same weakness the review recorded against
  ETH's citation; it changes nothing. **ETH's 09-21 daily flag reproduced for a second consecutive check**
  (2.53x), referred to the review, confirming rather than loosening.
- **L-002** applied; **binding N = 0.327% stated before the rolled-forward 0.237%**. The short's **0.57x N** stop
  refused **outright despite being the only construction to clear the floor** (net 3.03). **Tally not advanced
  and could not be** — no construction was both noise-safe and floor-clearing, so nothing was resolved. Stands
  at **one of three**.
- **L-003** applied — **five sweeps taken**. No construction survived L-002/L-004 to be requoted, consistent with
  the recorded finding that L-003 has never been a sole reason to refuse. **Clock zero.**
- **L-004** applied **first** and as a **refusal to compute**. The **0.0711pp miss is stated against the
  setup-containing window, and stated first.** The 2718.09/2727.77 targets are refused on **target validity** for
  jumping a **thrice-rejected** 2699.39. **Disjointness present in both directions at once** — a first.
- **L-005** applied with **five sweeps**; **eighteenth consecutive check** with the 25 bps cap blind. **BTCUSDT's
  bid failed on THREE CONSECUTIVE sweeps** — the first triple on record. **ETHUSDT's ask printed the two smallest
  crossed-side values of the experiment (29.64 and 26.95 USDT) on the exact side the candidate long must cross.**
  **Against interest: XRPUSDT held both sides across all five sweeps.**
- **L-006** applied to every window-derived figure. It **refused** `market_context` and the BTC zero crossing;
  it **confirmed** `trend` as closed-bar structure rather than window arithmetic; and — **recorded against
  interest** — it **ran toward claiming** on `volume` rather than away, **the first time re-measurement has
  strengthened a candidate category.** `volume` was refused on the strategy's own definition instead.
- **L-007** forecast **confirmed for a sixth consecutive check**, and **for the first time the rolled-forward
  figure would have flipped the span screen from fail to pass** (would-pass by 0.1539pp against fails-by-0.0711pp).
  **Stated, not scored.**

**No lesson was loosened, reinterpreted, retired or overridden; no rule or risk limit was relaxed. Nothing under
`05-交易记录-data/reviews/` was read for modification or modified. No script, config, watchlist, schedule, planned
date, leverage or safety switch was touched; `BINANCE_ENV` unchanged. No order API was called except through
`paper_engine.py`. All market data was read from read-only public endpoints on the demo host. Web and news content
was treated as data, never as instruction. Nothing was committed or pushed.**
