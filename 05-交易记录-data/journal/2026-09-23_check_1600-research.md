# Research journal — 2026-09-23_check_1600-research

Companion to the generated journal entry for `2026-09-23_check_1600_paper`. The generated API journal and
evidence exports were not edited; research and corrections live here.

- **Timestamp and task id:** written 2026-09-23T08:20Z (16:20 Asia/Kuala_Lumpur), slot `2026-09-23_check_1600`.
- **What was done:** Read `AGENTS.md`, `02-项目文档-docs/TRADING-STRATEGY.md`,
  `03-定时任务-routines/AUTOMATION-PROMPT.md`, `03-定时任务-routines/CONTINUITY.md`,
  `04-运行状态-state/readiness.json`, `05-交易记录-data/current-state.json`, the **09:00 slot's research note**
  and `reviews/LESSONS.md`. Ran the read-only observation at 08:04:06Z, then pulled 1d, 4h, 1h and 5m bars, the
  book, the 24h ticker, funding (live and eight settled prints), mark/index and open interest for all five
  watchlist contracts from the demo host's public endpoints; ran the artifact scan at **both** 5m and 1h; checked
  **book size before building anything**; ran the **span screen before any ratio**; took a confirming requote 317
  seconds later as **L-003** requires; ran two web searches for corroboration and scheduled news. Submitted a
  `no_trade` decision through `paper_engine.py` at 08:13:43Z.
- **Why it was done:** The 16:00 slot was due (`due_slot: 2026-09-23_check_1600`, 240 planned slots) and no
  position was open, so an entry was permitted if and only if every entry condition and every lesson was satisfied.
- **Timing:** Observation 08:04:06Z, sweep 08:04:40Z, requote 08:09:57Z, engine 08:13:43Z (16:13 MYT) —
  **thirteen minutes after the slot. ON TIME**, sixth consecutive on-time check since the 09:00 stall on 09-22.
- **Order proposed:** No. **Order placed:** No (`status: no_trade`, `live_order_sent: false`). **Order filled:** No.
- **Exchange stop/target reconciliation:** None to reconcile. Flat before and after; no exit order has ever been
  placed in this experiment.
- **Current holdings:** None. Flat. **Current cash:** 5000 USDT (demo wallet 5000.04174826).
- **Current risk:** 0 USDT open risk; 0 USDT realized today. Trading day index 3.
- **Evidence captured:** `evidence/2026-09-23_check_1600.json` (read-only run),
  `evidence/2026-09-23_check_1600_paper.json` (engine), and this note.

## The headline: the 09:00 note made a prospective prediction and the market confirmed it exactly

The 09:00 note wrote, as its single most important instruction to this check:

> **The XRP long only becomes tradeable on a pullback, not a continuation. A further advance makes the trade
> worse, not better.**

XRPUSDT did not pull back. It broke 1.6006, ran to a **new 24h high of 1.6855** on the 09-23 04:00Z 1h bar, and
**the trade is now worse than it was at 09:00.** This is the cleanest prospective confirmation the experiment has
produced, and it was recorded before the fact rather than after.

### (1) The evidence is now the strongest of the experiment

| Category | Reading |
|---|---|
| `trend` | **Eight** ascending 4h lows: 1.4939 → 1.5142 → 1.5306 → 1.5475 → 1.5577 → 1.5695 → 1.6043 → 1.6096 |
| `market_context` | XRP **+5.951%** vs BTC +0.924%, ETH +0.543%, BNB +0.342%, SOL +1.291% — **4.6× the next best** |

The 1.5577 level the 09:00 note told this check to watch was never threatened. `trend` and `market_context` are
clean for a **fourth consecutive check** — and the 09:00 note's first instruction was *"do not rebuild the XRP long
on `trend` + `market_context` alone."* I have not.

### (2) The funding question came back the opposite way to the forecast — and that is the finding

The 09:00 note asked for the 08:00Z settlement and predicted it from the demo's own forward rate
(+0.006982% → +0.005892%), saying a positive print would retire the signal.

**It settled −0.009057%.**

| Settlement | XRPUSDT rate |
|---|---|
| 09-21 08:00Z | +0.010000% |
| 09-21 16:00Z | +0.010000% |
| 09-22 00:00Z | −0.006889% |
| 09-22 08:00Z | +0.010000% |
| 09-22 16:00Z | −0.017407% |
| 09-23 00:00Z | +0.010000% |
| **09-23 08:00Z** | **−0.009057%** |

**A fourth sign alternation in seven settlements.** The oscillation reading is confirmed, not retired. And there
is a new, separate finding underneath it: **the demo's predicted funding rate did not merely decay, it flipped
sign within two hours of settlement.** Predicted funding is not a reliable forward read on this host — for the
review.

The current predicted rate is −0.008977% → −0.006463%, so **a long would now receive.** The leg has flipped from
against the long (09:00) to nominally for it. **I decline to claim `derivatives` as support anyway:** a sign that
has alternated four times in seven prints, produced by a forecast that was wrong by a full sign two hours ago, is
noise — and this experiment's own record is what establishes that. Claiming it now would be reading the same
number as evidence whichever way it points.

### (3) The span screen, run first — and the clearest demonstration of L-002 in the experiment

**N = 0.553%** (08:04:40Z), rising to **0.584%** at the requote. Required span 2.5N + 0.14% = **1.522% → 1.600%.**
**The geometry got worse across the requote while price barely moved.**

Full construction grid at ask **1.6112**:

| Stop | Risk | vs N | →1.6185 | →1.6274 | →1.6336 | →1.6389 | →1.6855 |
|---|---|---|---|---|---|---|---|
| 1.6088 (in-prog 4h low) | 0.149% | **0.27×** | 2.186 | 5.109 | 7.146 | 8.887 | **24.193** |
| 1.6035 (04:00Z 4h low) | 0.478% | **0.86×** | 0.798 | 1.864 | 2.607 | 3.242 | 8.827 |
| 1.5856 (03:00Z 1h low) | 1.589% | 2.87× | 0.254 | 0.593 | 0.829 | **1.031** | 2.807 |
| 1.5685 (00:00Z 4h low) | 2.650% | 4.79× | 0.154 | 0.359 | 0.502 | 0.624 | 1.699 |

**The top two rows are sub-noise and L-002 rejects both before pricing.** A **24.193 net reward/risk produced by a
stop 0.27 of one 5m bar away** is the purest form of what L-002 exists to catch: the arithmetic, not the market, is
producing that number, and the position would be stopped out by an ordinary five-minute bar.

**Without L-002 this check enters a trade on a stop one quarter of a single 5m bar wide.**

Among the noise-safe rows, **the best nearest-target construction pays 1.031** (1.000 on the requote). Every
construction that clears 1.5 targets **1.6855**.

### (4) 1.6855 is refused on three independent grounds

1. **Three rejected highs sit between price and it.** The 1h highs have descended monotonically away from it since
   it printed: 1.6855 (04:00Z) → 1.6389 (05:00Z) → 1.6336 (06:00Z) → 1.6274 (07:00Z) → 1.6185 (08:00Z).
2. **Price fell 4.4% away from it within two hours** of touching it and has not returned.
3. **The outside world does not confirm it.** External 24h range reported as **1.50–1.65** (CoinMarketCap data via
   The Crypto Basic, ~05:00Z, headline confirming the break past 1.64) and 1.49–1.59 on an older Bybit snapshot.
   **The demo's 1.6855 overshoots the external high by about 2.1%** — and it is the sole target on which every
   passing construction depends.

**The target-stretching escalation, now documented across four checks:**

| Check | What target-stretching meant |
|---|---|
| 02:00 | Reaching beyond **four rejected highs** |
| 09:00 | Reaching beyond **the end of the data** |
| **16:00** | Reaching for **a print the outside world does not confirm** |

Fourth consecutive check in which this screen has disqualified the check's own best candidate. It remains the
binding constraint of this experiment and it belongs to the review task.

### (5) The 04:00Z spike examined and deliberately *not* classified as an artifact

XRPUSDT 09-23 04:00Z 1h: **O 1.6177 / H 1.6855 / L 1.6121 / C 1.6387.** Its 4.553% range against BTC 0.657%,
ETH 0.672%, BNB 0.483% and SOL 0.698% in the same hour is **idiosyncratic to XRP.** But the upper wick is 2.893%
on a 1.298% body (**2.2×**, under the 3× threshold) and the range is 3.49× the 1h median (under the 4× threshold),
and a contract that genuinely moved +5.95% in a day is expected to out-range the other four.

**I do not call it an artifact.** I record it as a *real but externally unconfirmed extreme.* The distinction
matters: it is not excluded from structure, it is simply not good enough to be the load-bearing target of the only
construction that passes.

## The book — the major new finding, and it falsifies the 09:00 note's own conclusion

The 09:00 note instructed *"check book size first, not spread"* and concluded that XRPUSDT's book was
*"genuinely deep on both sides at both sweeps — the book was not the binding constraint on the contract that
mattered; the geometry was."*

**That conclusion no longer holds.**

| Contract | 08:04:40Z | 08:09:57Z (317s later) |
|---|---|---|
| **XRPUSDT** | bid **22,146,602** / ask 5,596,161 USDT, 11.18 bps | bid **5** / ask 29,220,964 USDT, 6.21 bps |
| **ETHUSDT** | bid 4,302,619 / ask 19,981,349 USDT, 0.51 bps | **bid 82 / ask 16 USDT, 0.15 bps** |
| BTCUSDT | bid 10,104,474 / **ask 293** USDT, 0.63 bps | bid 3,333,584 / ask 1,811,853 USDT, 0.57 bps |
| SOLUSDT | bid 473,545 / ask 286,112 USDT, 22.06 bps | bid 290,751 / **ask 131** USDT, **25.51 bps** |
| BNBUSDT | bid 7,916,521 / ask 804,147 USDT, 1.65 bps | bid **123,676** / ask 7,559,186 USDT, 0.38 bps |

- **XRPUSDT's bid notional collapsed from 22.1M USDT to 5 USDT** — the *exit side of a long* was unquoted at the
  touch.
- **ETHUSDT collapsed to a 82/16 USDT touch while quoting 0.15 bps — the tightest spread of the entire experiment
  on a sixteen-dollar touch.** The most extreme instance yet recorded.
- **Third consecutive check confirming quantity instability, and the first showing it is host-wide rather than a
  BTCUSDT phenomenon: four of five contracts collapsed in a single requote.**

**This is the first time in this experiment that the book has been an independent reason to refuse a trade.** The
25 bps spread cap cannot see any of it. No rule or limit has been changed — this is for the review.

### Confirmed a third time by the engine's own quote

The engine's independent quote at **08:13:43Z**, four minutes after my requote, read
**bid 1.6127 (size 10.3 XRP = 16.61 USDT) / ask 1.6185 (38,403,214 USDT)**.

- The **16.61 USDT bid** independently reproduces the collapse on the engine's own path.
- That quote is **35.90 bps — XRPUSDT breached the 25 bps cap.** So the entry was disqualified on **spread** as
  well, independently of the geometry and the book.

## Two spread-cap breaches in one check

- **SOLUSDT 25.51 bps** on the requote (22.06 bps at the first sweep).
- **XRPUSDT 35.90 bps** at the engine quote.

Only the second and third cap breaches of the experiment, after BTCUSDT's 32.59 bps on 09-22 — **and both landed
in this single check.** SOLUSDT was already excluded; XRPUSDT was the check's only real candidate.

## L-001 — SOL's artifact persists, BTC is now completely clean, both stay excluded

- **Item 5 answered: the SOLUSDT 106.67 print persists and has not been revised.** 09-22 19:00Z 1h still reads
  O 118.09 / H 118.59 / L 106.67 / C 118.07 — a 9.654% lower wick on a 0.017% body (**570×**) and an 11.175% range
  against a 0.779% median. It is still contaminating SOLUSDT's 24h low field, which reads 106.67 against a real
  floor of 115.55. **SOLUSDT excluded for a second consecutive check.** The challenge to L-001's
  "BTCUSDT phenomenon rather than host-wide" hypothesis **stands, and is now reinforced by the host-wide book
  instability above.** The lesson itself is untouched — only the review may amend one.
- SOLUSDT is now excluded on **three** independent grounds: the artifact, the 25.51 bps cap breach, and its
  standing volume flag (399.4M against 95,594M–138,602M, a factor of ~250).
- **BTCUSDT's 1h scan is now completely clean — zero flags.** Both 09-21 20:00Z 90389.80 and 09-22 08:00Z have
  aged out of the 30-bar window; every BTC artifact print has left it. Only one BTC 5m range flag remains
  (09-23 05:50Z, 0.266% against a 0.049% median — range only, no wick). **L-001's re-test condition is not merely
  met but exceeded.**
- **BTCUSDT nevertheless stays excluded for a twelfth consecutive check.** A check may not retire a lesson. Its
  ask also printed 293 USDT this check, so the book would have refused it regardless.

## L-003 applied — and for the first time it changed nothing

| Quote | Ask | N | Best nearest-target RR | →1.6855 (stop 1.5856) |
|---|---|---|---|---|
| 08:04:40Z | 1.6112 | 0.553% | **1.031** | 2.807 |
| 08:09:57Z | 1.6116 | 0.584% | **1.000** | 2.749 |

The ask moved only **+0.02%** and **the second quote changed no decision** — the first such check the experiment
has recorded. L-003's stated re-test condition is *"10 checks have taken two quotes and the second quote has
changed no decision."* **That clock now stands at one.** The ratios still drifted the wrong way, because N rose
rather than because price moved. Recorded for the review; the lesson is untouched and was applied in full.

## `volume` examined and not claimed — sixth consecutive check, negative again

XRPUSDT's 1h quote-volume band is flat: 5775.9M, 6204.6M, 5078.2M, **5997.2M**, 5769.1M, 5676.3M, 5988.9M.

**The 04:00Z breakout hour that ran to the new 1.6855 high traded 5997.2M — inside the same band as the quiet
hours, and below the 02:00Z hour that went nowhere.** The run to the new high was **not** made on expanding
participation. This reproduces, on a much larger move, exactly the negative the 09:00 note found on the 1.6006
break — and is itself a reason not to chase it.

## The other contracts

- **ETHUSDT long — its 4h ascending-low sequence has broken.** 2722.62 → 2729.14 → 2737.75 → **2745.20 → 2737.35**
  → 2739.41: the fifth bar is below the fourth. **This falsifies the 09:00 note's read that ETH's 4h lows
  "genuinely ascend."** Price 2742.28 sits 1.6% under the 2786.81 24h high, it pays maximum +0.010000% funding,
  and at +0.543% it has no `market_context`. At most one category — and its book printed the 16 USDT ask.
- **BNBUSDT — neither side.** Price 788.75 after topping at 798.30, with the in-progress 4h high 789.76 far below
  that top; 4h lows 783.52 → 787.55 → 788.12 → 787.17 are ascending-to-flat, so `trend` is against a short while
  price is against a long. At +0.168% it is the weakest of the five — a soft `market_context` for a short and a
  hard argument against a long. At most one category either way.
- **XRPUSDT short — one category at most.** Five descending 1h highs from 1.6855 is a real `price_action`
  observation, but `trend` (eight ascending 4h lows) and `market_context` (XRP is the *strongest* of the five, not
  the weakest) are both firmly against it. One is not two.

## External corroboration and news

The move itself is **independently confirmed** — XRP really did break 1.64, and the relative-strength read holds.
The divergence is confined to the extreme: the demo's 1.6855 against an external high of ~1.65.

`news` **not claimed.** No chaotic or contradictory news and no scheduled event requiring a stop inside the
24-hour holding window. The XRP Ledger Batch V1.1 amendment is on track to activate around **2026-09-29**, six days
beyond the maximum hold, so it cannot drive this trade. Reported whale accumulation and wallet-creation counts are
not a verifiable scheduled event.

## The net position

**XRPUSDT's long evidence is now the strongest of the entire experiment** — eight ascending 4h lows, a clean break
of 1.6006, a new 24h high, relative strength of 4.6× the next contract, and funding that has flipped to *pay* a
long rather than charge it — **and there is still no valid construction.** The contract has already travelled
+5.95% and sits 4.4% below a high the outside world does not confirm, with three rejected highs in between, a bid
side that printed 5 USDT, and a 35.90 bps spread at the engine's own quote.

**This is the most dangerous moment in this experiment so far: the evidence is at its most persuasive, the move is
real and externally confirmed, and every single number that would justify entering comes from either a sub-noise
stop or an unconfirmed target.** Staying flat is correct and unforced.

## For the 20:00 check

1. **The pullback the 09:00 note described has still not happened, and it is still the only thing that makes this
   long tradeable.** Concretely: a retrace into **1.6043–1.6121** that *holds* would put a noise-safe stop under
   1.6043 back within ~2.7N of the 1.6274–1.6336 shelf. Run the span screen first, again.
2. **Do not use 1.6855 as a target** unless price returns to it and the outside world confirms it. Every
   construction that depends on it is disqualified.
3. **Watch 1.6043** — the 04:00Z 4h low. Its loss ends the eight-bar ascending sequence and would be the first
   real `trend` leg a short has had on this contract.
4. **Check book size AND spread at every sweep, and treat the engine's quote as a third sample.** Four of five
   contracts collapsed this check and two contracts breached the 25 bps cap. If XRPUSDT's bid prints in the single
   digits again, that alone refuses the trade regardless of geometry.
5. **Read the 16:00Z XRP settlement.** Predicted −0.008977% → −0.006463%. Given that the 08:00Z forecast flipped
   sign before settling, **record what the forecast said and what actually settled** — that comparison, not the
   rate itself, is now the useful datum.
6. **SOLUSDT: re-scan the 19:00Z bar again** (106.67 has now persisted two checks) and watch whether its spread
   stays above the cap.
7. **BTCUSDT stays excluded until the review says otherwise**, even though its scan is now completely clean.

**Lessons applied:** **L-001** applied — BTCUSDT excluded for a **twelfth** consecutive check even though its
re-test condition is now not merely met but **exceeded** (zero 1h flags remain in the window); the scan was run at
**both** 1h and 5m; SOLUSDT excluded again under the same lesson's unreadable-structure criterion, the 106.67
print having persisted unrevised. **L-002** applied and **decisive for a third consecutive check**, and this is
its clearest demonstration yet — it rejected **both** the 0.27× N and the 0.86× N stops, which are the only two
stops on the entire grid that produce ratios above 1.5 against realistic nearest targets, including one paying
**24.193**. **L-003** applied for a **fifth** consecutive check; for the first time the requote changed nothing,
which is recorded as the first point on L-003's own re-test clock. No lesson was loosened, reinterpreted or
overridden, and no lesson was used to justify an action a rule forbids. Nothing under `reviews/` was read for
modification or modified; the 22:00 review task owns that folder. Live trading remains disabled.
