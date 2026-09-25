# Research journal — 2026-09-23_check_2100-research

Companion to the generated journal entry for `2026-09-23_check_2100_paper`. The generated API journal and
evidence exports were not edited; research and corrections live here.

- **Timestamp and task id:** written 2026-09-23T13:14Z (21:14 Asia/Kuala_Lumpur), slot `2026-09-23_check_2100`.

> **Timestamp correction.** The decision file was first written carrying `checked_at_local: 21:32+08:00`, and this
> note carrying 13:36Z — both **estimates made without reading the clock**, not measured times. The true values are
> **21:11** and **21:14**. The decision file has been corrected and carries a `timestamp_correction` field; the
> engine's generated export `evidence/2026-09-23_check_2100_paper.json` embeds the original incorrect 21:32 and was
> **not** edited, being a deterministic export. **Every measured timestamp below was read from the tooling and is
> correct**, the run was on time by any reading, and the decision was `no_trade`, so the 45-minute entry window
> never bound. Recorded because a wrong clock time in the record would mislead the review.
- **What was done:** Read `AGENTS.md`, `02-项目文档-docs/TRADING-STRATEGY.md`,
  `03-定时任务-routines/AUTOMATION-PROMPT.md`, `03-定时任务-routines/CONTINUITY.md`,
  `04-运行状态-state/readiness.json`, `04-运行状态-state/paper-config.json`,
  `05-交易记录-data/current-state.json`, the **20:00 slot's research note** and `reviews/LESSONS.md`. Ran the
  read-only observation at 13:04:13Z, then pulled 1d, 4h, 1h and 5m bars, the book, the 24h ticker, funding (live
  and nine settled prints), mark/index and open interest for all five watchlist contracts from the demo host's
  public endpoints. Ran the artifact scan at **both** 5m and 1h; checked **book size before building anything**;
  ran the **span screen before any ratio**; took **three** book samples rather than two, as the 20:00 note
  required; ran two web searches for scheduled news and corroboration. Submitted a `no_trade` decision through
  `paper_engine.py` at 13:13:18Z.
- **Why it was done:** The 21:00 slot was due (`due_slot: 2026-09-23_check_2100`, 240 planned slots) and no
  position was open, so an entry was permitted if and only if every entry condition and every lesson was satisfied.
- **Timing:** Observation 13:04:13Z, sweep 13:04:56Z, requote 13:08:33Z, engine 13:13:18Z (21:13 MYT) —
  **thirteen minutes after the slot. ON TIME**, eighth consecutive on-time check since the 09:00 stall on 09-22.
- **Order proposed:** No. **Order placed:** No (`status: no_trade`, `live_order_sent: false`). **Order filled:** No.
- **Exchange stop/target reconciliation:** None to reconcile. Flat before and after; no exit order has ever been
  placed in this experiment.
- **Current holdings:** None. Flat. **Current cash:** 5000 USDT (demo wallet 5000.04174826).
- **Current risk:** 0 USDT open risk; 0 USDT realized today. Trading day index 3.
- **Evidence captured:** `evidence/2026-09-23_check_2100.json` (read-only run),
  `evidence/2026-09-23_check_2100_paper.json` (engine), and this note.

---

## The headline: the binding constraint moved from evidence to geometry and execution

Every one of the eight prior decisions died on the **evidence count** — one clean category where two were needed.
This check is different. **Two contracts cleared the two-category bar honestly, and both were refused anyway.**

| | `trend` | `market_context` | two categories? | outcome |
|---|---|---|---|---|
| **BNBUSDT short** | daily highs 807.74 → 800.90 → 798.30, three lower daily closes | weaker than BTC on **all four** windows | **YES** | refused — L-002 stop, L-003 decay, bid collapse |
| **ETHUSDT short** | 4h highs 2786.81 → 2748.23 → 2727.77; 2716.01 broken | weaker than BTC on **all four** windows | **YES** | refused — 2.65% structural vacuum, bid unquoted |
| XRPUSDT short | same candles as `price_action` | **flips sign** — see below | no (one) | refused on evidence |

That is a materially better failure than the eight before it, and it is the first evidence in this experiment that
**the entry criteria and the demo host's execution quality — not an unwillingness to trade — are what keep the
account flat.**

### (1) The 20:00 note made three prospective calls; all three resolved, one against the trade

**(a) The XRP condition resolved AGAINST the trade — a first.** The 20:00 note's item (1) set the test:

> *If the 24h figure turns negative while the 4h/8h weakness persists, the contradiction resolves and
> `market_context` becomes claimable.*

The 4h/8h weakness **persisted** — XRP is still the weakest of the five at −2.059% (4h) and −2.972% (8h). But the
24h figure **did not turn negative**: **+1.305%** at the sweep, **+0.886%** at the requote, and still the *only*
positive 24h figure of the five. **The condition is unmet, `market_context` stays unclaimable, and the XRP short
still has one category.**

This is the third consecutive check in which the prior note wrote a falsifiable condition and the market resolved
it — and **the first in which it resolved against trading.** A condition that only ever fires in favour of a trade
is not a test. This one declined to fire.

**(b) ETH did not reject — it went through.** Item (7) said *"if price reaches 2716–2717 and rejects, the geometry
may open."* ETH broke the 09-22 daily low 2716.01 to **2714.88**, then **2713.46**. The geometry did not open; it
opened the vacuum instead.

**(c) "A single healthy sample means nothing on this host."** Item (4). Three samples were taken. That is exactly
what they showed — see (5).

### (2) L-002 was decisive on BNB, and it turned entirely on which bar you measure

This is the most instructive finding of the check.

| N measured over | N | stop 783.46 is | verdict |
|---|---|---|---|
| last **12** closed 5m bars | 0.222% | **2.89× N** | looks comfortable |
| **full preceding hour** (what L-002 requires) | **0.800%** | **0.80× N** (0.93× on requote) | **sub-noise** |

N over the full hour is 0.800% because the **12:00Z 5m bar — O 783.27 / H 783.46 / L 777.24 / C 777.24, volume
1460.2M, the largest of the last 26 bars — is the breakdown bar that created the entire setup.** The stop at
783.46 is not merely inside that bar's range; **it is that bar's exact high.**

L-002 verbatim: *"a stop narrower than recent bar noise is a position size, not a stop."* **Rejected before the
ratio is allowed to count.** And 783.46 is the *only* stop that ever cleared 1.5:

| stop | × N | 766.72 (09-21 daily **low**) | 762.42 (09-19 daily *close*) |
|---|---|---|---|
| **783.46** (sub-noise) | 0.80 → 0.93 | **1.753 → 1.430** | 2.461 → 2.054 |
| **786.19** (structural, above the 11:00Z lower high) | 1.24 → 1.37 | 1.210 → 1.024 | 1.698 → **1.471** |

**The choice was between a sub-noise stop that passes and a structural stop that fails.** That is the definition of
choosing a stop to fit the arithmetic, which the strategy forbids in as many words.

*The narrower measurement window would have permitted this trade.* Worth recording plainly.

### (3) L-003 killed BNB independently — and for the first time in its honest direction

Across 217 seconds BNB's bid drifted **778.47 → 777.66**, i.e. **away** from the fixed stop. The risk therefore
**grew** and the ratio **decayed: 1.753 → 1.430, through the 1.5 floor.**

Every previous L-003 catch in this experiment was the *pathological* version — a ratio **improving** because price
drifted **onto** its stop (ETH 1.493 → 1.765 and BNB 1.529 → 2.112 at 20:00; XRP 1.736 → 2.809 at 02:00). **This is
the legitimate version: the trade got worse because it went my way before I could take it**, and chasing it would
have meant widening the risk to keep the same target. **Both failure directions are now documented**; that
completes L-003's case and belongs to the review. Its re-test clock **stays at zero** — a seventh consecutive check
in which the second quote changed the answer.

### (4) ETH fails on the vacuum, exactly as the 20:00 note predicted — now with price inside it

N = 0.372% (5m 12:20Z). Honest structural stop **2736.85** (above the 11:00Z lower high, **2.02× N**):

| target | 2713.46 (24h low) | 2700 | 2687.56 (20:00's derived number) | 2670 (**no structure**) | 2641.70 (09-21 daily **low**) |
|---|---|---|---|---|---|
| net RR, sweep | −0.035 | 0.52 | 1.033 | **1.757** | 2.925 |
| net RR, requote | −0.132 | 0.37 | 0.829 | **1.481** | 2.531 |

The first passing target is **2670 — a price with no structure of any kind** — and it **fell below the floor on the
requote.** The nearest genuinely structural target is the 09-21 daily low **2641.70, 2.65% away, with nothing
whatsoever between 2714.88 and it.**

The tighter stop **2727.77** is rejected under L-002 on a second, distinct ground: at **1.12× N** it is barely above
the noise floor **and it sits just 0.21% above 2722.14 — a level the market touched three times in twenty minutes**
(12:45Z, 12:50Z, 13:00Z 5m highs, all exactly 2722.14). L-002's defect, mirrored.

### (5) The entry side of both shorts went unquoted — and BNB was the *sound* contract at 20:00

**A short sells into the bid.** Four samples, the last being the engine's own quote at 13:13:18Z:

| bid notional (USDT) | 13:04:56Z | 13:07:55Z | 13:08:33Z | engine 13:13:18Z |
|---|---|---|---|---|
| **BNBUSDT** | 36,721,037 | **9,669** | 20,187,299 | 24,063,443 |
| **ETHUSDT** | 245,634 | **111** | **217** | — |
| **XRPUSDT** | 19,566,411 | 6,451,197 | **100** | — |
| BTCUSDT | 2,390,913 | 2,976,135 | 2,145,336 | — |

- **BNB collapsed 3,798× and recovered, inside 217 seconds.** At the 9,669 USDT print, a maximum-size **2,500 USDT**
  market sell would have consumed **roughly a quarter of the entire visible bid.**
- **ETH's bid went and did not come back** — unquoted on two consecutive samples. Worse than BNB.
- **XRP was healthy on two samples then 100 USDT on the third** — the precise reason a single sample cannot be
  trusted. Second consecutive check with an XRP bid collapse.
- **BTCUSDT had the only stable book of the five** — and it belongs to the contract L-001 excludes. Recorded
  against interest.

**Fifth consecutive check confirming host-wide quantity instability — and the first to prove it is not
contract-specific: BNB was the sole contract to *improve* at 20:00 and is the worst collapse here.** The
oscillation is the finding, not any single print. It is exactly why a reduce-only stop resting on this book between
checks cannot be trusted to fill near its trigger.

### (6) SOLUSDT breached the spread cap outright

**7.71 → 18.83 → 30.06 bps** against a **25 bps** cap — the **fifth cap breach** of the experiment and **the first
to worsen monotonically across three consecutive samples** rather than spiking and requoting back. Combined with the
**106.67 print persisting a fourth check** (09-22 19:00Z 1h, 9.654% wick on a 0.017% body, still contaminating the
24h low field against a real floor of 116.45), SOL is excluded on two independent grounds — one of them now a hard
rule breach rather than a judgement call.

### (7) News: confirmed, larger than the 20:00 note knew, and inside the hold window

The Trump–Xi summit on **2026-09-24** is confirmed by multiple independent outlets, and the fuller picture is that
**Xi is on a state visit to Washington from 09-23 to 09-25 — it began today** — with the summit meeting and a state
dinner on 09-24 and **trade, AI, critical minerals and Taiwan** on the agenda **against an expiring trade truce.**

A position opened at this check would be held through the arrival, the summit and the dinner. This is a **binary,
two-way macro event and gives no direction.** Recorded as **event risk, not claimed as evidence.**

### (8) Volume was arguably positive for the first time in eight checks — and declined anyway

BNB's 12:00Z breakdown 5m bar traded **1460.2M, the largest of the last 26 bars by more than 2×** — genuine
expansion on the break of 781.56. **Not claimed**, on two grounds: a single 5m bar is not *"participation compared
with recent average"* in any robust sense, and **the 1h frame contradicts it** (12:00Z hour 4912.9M against a day
band of 3592.1–4997.2M — mid-range). **Claiming it would have manufactured a third category out of one candle.**

XRP's break of **1.5621** — the 20:00 note's item (2) watch level, which **did** break, to 1.5603 — came on a 13:00Z
bar too young to measure. That note's hoped-for "first volume confirmation in seven checks" is **deferred, neither
confirmed nor denied.**

### (9) Derivatives: both legs favour the trades being declined, which is why neither is claimed

- **BNBUSDT live funding 0.00000000** (settled 0.0, 0.000518, 0.00609, 0.005188, 0.0, 0.0) — a short would pay and
  receive **nothing**, the most benign funding leg of the experiment.
- **ETHUSDT +0.010000%** — a short would **receive**.
- **The 20:00 note's forecast test (item 5) cannot be run at this check.** The next settlement for all five is
  **2026-09-23 16:00Z**, about three hours away and not yet settled. **It carries to the 00:00 check.**
- XRP funding still sign-alternating: +0.010000, −0.006889, +0.010000, −0.017407, +0.010000, −0.009057.
- Open interest flat across the requote on all five (BNB +0.0002%, ETH +0.0009%, XRP +0.0021%).

---

## Lessons applied

- **L-001** — applied. BTCUSDT excluded a **fourteenth** consecutive check; artifact scan run at **both** 5m and 1h
  resolutions. Its re-test condition remains **not met** (the 09-21 95,804.10 print still contaminates the daily
  frame). Recorded against interest: **BTC had the healthiest book of the five here.** A check may not retire a
  lesson; the review owns that. SOLUSDT excluded again on the persisting 106.67 print.
- **L-002** — applied and **decisive for a fifth consecutive check**, and this time the *measurement discipline* was
  the whole story: taking N over the **full preceding hour** rather than the last twelve bars turned BNB's only
  passing stop from 2.89× N into **0.80× N** and killed the trade. It also rejected ETH's 1.12× N stop resting
  0.21% above a thrice-touched level.
- **L-003** — applied for a **seventh** consecutive check and it **changed the answer again**, this time in the
  honest direction: BNB decayed **1.753 → 1.430** through the floor because price moved *away* from its stop. Its
  re-test clock **stays at zero**.

No lesson was loosened, reinterpreted or overridden. Nothing under `reviews/` was read for modification or
modified; the 22:00 review task owns that folder.

---

## For the 22:00 check

1. **BNBUSDT is the contract to watch, and the specific falsifiable condition is a *stop*, not a level.** Its
   evidence bar is already met (`trend` + `market_context`, neither flipping sign). It failed because the only
   passing stop sat on the breakdown bar's own high. **If BNB prints a genuine lower high above 783.46 and below
   786.19, a stop above that high would be both structural and above the noise floor** — that is the one
   development that opens this trade. A further drift *down* without such a high makes it worse, not better (L-003).
2. **Re-measure N over the full preceding hour, not the last twelve bars.** BNB's N was 0.800% only because the
   12:00Z breakdown bar was in the window; by 22:00 that bar rolls out and N will collapse toward 0.222%,
   **mechanically making the same 783.46 stop look acceptable.** It is the same stop on the same structure. **Do not
   let the passage of time manufacture a pass** — this is the single most likely way the next check gets this wrong.
3. **ETHUSDT stays refused until something exists below 2713.46.** Nothing between there and the 09-21 daily low
   2641.70 (2.65%). Only a *new* intraday low that then holds and builds a shelf creates an honest target.
4. **XRP: the condition is unchanged and still unmet** — the 24h figure must turn **negative** while the 4h/8h
   weakness persists. It has decayed +1.822% → +1.305% → +0.886% across three checks; it may cross before 00:00.
   **If it does, the XRP short reaches two categories and must then be priced honestly, not waved through.**
5. **Take three book samples, not two, and treat the engine quote as a fourth.** BNB went 36.7M → 9,669 → 20.2M →
   24.1M USDT in nine minutes. Any candidate whose *entry* side is unquoted on any sample is disqualified.
6. **SOLUSDT is out on a hard limit** (30.06 bps vs a 25 bps cap), not a judgement. **BTCUSDT stays excluded**
   under L-001 until the review says otherwise.
7. **The 16:00Z funding settlement will have occurred by the 00:00 check** — record the forecast against the
   outcome there. It cannot be done at 22:00 either way for the 21:00 forecasts, but the 16:00Z prints will be
   readable.
8. **Trump–Xi runs 09-23 to 09-25.** Anything opened from here is held through the summit and the state dinner.
   Any entry must be justified *through* that event, not around it.
9. **22:00 is also the daily review slot.** The review task owns `reviews/`; this check wrote nothing there.

## For the review (22:00)

Findings this check that belong to the review rather than to a trading decision:

- **The binding constraint has moved from evidence to geometry and execution** — the first check where candidates
  cleared the two-category bar and were refused on other grounds. Worth measuring: how often does the evidence bar
  now bind versus the stop, the target and the book?
- **L-002 is sensitive to the measurement window in a way the lesson does not currently state.** "The largest 5m bar
  range of the preceding hour" gave 0.800% here and 0.222% over a twelve-bar window — a 3.6× difference that flipped
  the decision. The lesson may deserve an explicit note that the window includes the setup-defining bar.
- **L-003's second failure direction is now documented** (ratio decaying because price moved away from the stop),
  completing its evidence base.
- **Host book instability is confirmed non-contract-specific** — BNB improved at 20:00 and collapsed worst at 21:00.
- **Target-stretching is separating into two distinct failure modes**: BNB's honest target (766.72, 1.51% away) was
  a real level and the trade failed on the *stop*; ETH's was a pure stretch into an empty 2.65%.

## Outstanding for Edward

Carried from the 09:00, 22:00, 23:00, 00:00, 02:00, 09:00, 16:00 and 20:00 checks: the 09:00 run on 2026-09-22
stalled ~12h40m and **three slots were lost** — 16:00, 20:00 and 21:00 on 2026-09-22 did not run. **Eight
consecutive checks have now run on time**, strong evidence the condition has cleared, but **the cause was never
identified**; scheduled tasks only run while the Claude desktop app is open, so it is worth confirming whether the
machine slept or the app was closed. The account was flat throughout, so the cost was observations, not money.
Live trading remains disabled. **No action is required tonight.**
