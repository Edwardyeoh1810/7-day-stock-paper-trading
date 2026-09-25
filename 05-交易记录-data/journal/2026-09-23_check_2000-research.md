# Research journal — 2026-09-23_check_2000-research

Companion to the generated journal entry for `2026-09-23_check_2000_paper`. The generated API journal and
evidence exports were not edited; research and corrections live here.

- **Timestamp and task id:** written 2026-09-23T12:20Z (20:20 Asia/Kuala_Lumpur), slot `2026-09-23_check_2000`.
- **What was done:** Read `AGENTS.md`, `02-项目文档-docs/TRADING-STRATEGY.md`,
  `03-定时任务-routines/AUTOMATION-PROMPT.md`, `04-运行状态-state/readiness.json`,
  `05-交易记录-data/current-state.json`, the **16:00 slot's research note** and `reviews/LESSONS.md`. Ran the
  read-only observation at 12:04:50Z, then pulled 1d, 4h, 1h and 5m bars, the book, depth, the 24h ticker,
  funding (live and nine settled prints), mark/index and open interest for all five watchlist contracts from the
  demo host's public endpoints; ran the artifact scan at **both** 5m and 1h; checked **book size before building
  anything**; ran the **span screen before any ratio**; took a confirming requote 511 seconds later as **L-003**
  requires; ran two web searches for corroboration and scheduled news. Submitted a `no_trade` decision through
  `paper_engine.py` at 12:17:48Z.
- **Why it was done:** The 20:00 slot was due (`due_slot: 2026-09-23_check_2000`, 240 planned slots) and no
  position was open, so an entry was permitted if and only if every entry condition and every lesson was satisfied.
- **Timing:** Observation 12:04:50Z, sweep 12:05:29Z, requote 12:14:00Z, engine 12:17:48Z (20:17 MYT) —
  **seventeen minutes after the slot. ON TIME**, seventh consecutive on-time check since the 09:00 stall on 09-22.
- **Order proposed:** No. **Order placed:** No (`status: no_trade`, `live_order_sent: false`). **Order filled:** No.
- **Exchange stop/target reconciliation:** None to reconcile. Flat before and after; no exit order has ever been
  placed in this experiment.
- **Current holdings:** None. Flat. **Current cash:** 5000 USDT (demo wallet 5000.04174826).
- **Current risk:** 0 USDT open risk; 0 USDT realized today. Trading day index 3.
- **Evidence captured:** `evidence/2026-09-23_check_2000.json` (read-only run),
  `evidence/2026-09-23_check_2000_paper.json` (engine), and this note.

---

## The headline: the 16:00 note's watch level broke exactly as written — and the short it predicted still fails

The 16:00 note's watch item (3) said:

> **Watch 1.6043 — the 04:00Z 4h low; its loss ends the eight-bar ascending sequence and hands the short its
> first real trend leg on this contract.**

XRPUSDT lost 1.6043 at 05:00Z, fell to **1.5621** by 12:00Z and now trades **1.5644**, **−7.137% from the 1.6855
high**. The eight-bar ascending 4h low sequence is **broken**: 1.6043 → 1.5695 → 1.5621.

This is the **second consecutive check** in which the previous note made a prospective, falsifiable call and the
market resolved it. At 16:00 it was *"a further advance makes the trade worse, not better"* — confirmed. At 20:00
it is *"1.6043 hands the short its first trend leg"* — also confirmed. **But the short the note anticipated still
does not clear the bar**, and the reasons are worth more than the prediction.

### (1) The long is dead; the short has one clean category

| Category | Reading | Claimed? |
|---|---|---|
| `price_action` | **Nine** descending 1h highs 1.6855 → 1.6389 → 1.6336 → 1.6274 → 1.6185 → 1.6028 → 1.5976 → 1.5951 → 1.5734, plus breaks of 1.6043 and 1.5695 | **YES — the only one** |
| `trend` | 4h ascending-low sequence broken, but drawn over the **same candles** as the descending highs; daily still **up** seven days 1.2824 → 1.5652 | No |
| `market_context` | **Weakest** over 4h (−3.132%) and 8h (−3.245%) — *and* **strongest** over 24h (+1.822%) | No |
| `volume` | Breakdown hour **below** median | No |
| `derivatives` | Funding sign alternating; forecast proven wrong by a full sign | No |
| `news` | Real, but event **risk**, not direction | No |

**One category is below the two-category bar, and that alone ends the entry before any geometry is priced.**

The `market_context` refusal is the one that matters. XRP is simultaneously the weakest contract on the 4h and 8h
windows (2.4× the next weakest) and the strongest on 24h (+1.822% against BTC −0.537%, ETH −0.762%, BNB −0.821%,
SOL −0.375%). The 16:00 check claimed `market_context` **for the long** on the 24h number. Claiming it **for the
short** four hours later on a different window would be reading one field as evidence whichever way it points —
precisely the error the 16:00 note refused on funding. **Refused again, on the opposite side of the book.**

### (2) The span screen killed the check's own best candidate for a fifth straight check — first time on a short

N = **0.728%** (5m bar 11:30Z), unchanged across the requote. Grid at bid 1.5652, structural stop **1.5960** (above
the 11:00Z lower high 1.5951, 2.70× N):

| Target | 1.5621 today | 1.5577 4h | 1.5475 4h | 1.5306 **24h low** | 1.5142 4h |
|---|---|---|---|---|---|
| net RR, sweep | 0.047 | 0.183 | 0.499 | 1.021 | **1.527** |
| net RR, requote | 0.022 | 0.155 | 0.462 | 0.972 | **1.467** |

The only target that ever cleared 1.5 was **1.5142 — 3.26% away, beyond four untested supports and below the 24h
low** — and it fell under 1.5 on the requote. The two tighter stops that paid more were rejected first: **1.5834**
is 1.60× N but sits *under* the 1.5842 high the market touched at 11:25Z and 11:30Z (L-002's *"a stop resting just
under a level the market keeps touching is a size, not a stop"*), and **1.5762** is 0.97× N — **sub-noise**,
rejected before pricing, where it would have shown 2.629 and 3.934.

**Target-stretching escalation, now across five checks and both directions:** 02:00 beyond four rejected highs →
09:00 beyond the end of the data → 16:00 for a print the outside world does not confirm → **20:00 below the 24h low
into a structural vacuum, on the short side.** *The binding constraint of this experiment is not direction-specific.*
That is new, and it belongs to the review.

### (3) The requote changed the answer on all three candidates — L-003's clock resets to zero

| | entry drift | RR before → after | what happened |
|---|---|---|---|
| **XRP short** | 1.5652 → 1.5644 | 1.527 → **1.467** | bounced off 1.5621 to 1.5710; premise weakened in 10 minutes |
| **ETH short** | 2719.86 → **2721.81** | 1.493 → **1.765** | price drifted **onto** its fixed stop; risk shrank 0.628% → 0.556% |
| **BNB short** | 778.65 → **780.23** | 1.529 → **2.112** | stop fell **1.24× N → 0.98× N**, *below the noise floor* |

ETH is L-003's trap verbatim: the ratio improved 18% purely because the risk shrank, while ETH bounced off the
2717.02 low that was the short's entire premise. **BNB is the cleanest joint L-002/L-003 demonstration the
experiment has produced — the ratio improved 38% at the exact instant the stop became sub-noise.** Two lessons
catching one construction simultaneously is new.

At 16:00, L-003's re-test clock ("10 checks where the second quote changed no decision") reached **one**. It
**resets to zero** — one check later.

### (4) The entry side of the short was unquoted, at the widest spread of the experiment

Over 511 seconds XRPUSDT's **bid notional collapsed 3,118,829 → 4,309 USDT** (724×) while the ask held 7.8M, and
the spread blew **0.64 → 42.10 bps**. A short sells into the bid: **this is the first time the collapse has landed
on the side the trade actually needs.** Previous checks watched the *exit* side of a long go; this check the
*entry* side of the short went. 42.10 bps is the **fourth cap breach** of the experiment and **the widest yet**,
and XRP has now breached in **two consecutive checks**.

Host-wide instability **confirmed a fourth consecutive check**, four of five contracts: BTC ask 49,615 → **162**
USDT, SOL ask 97,891 → **70** USDT (15.43 → 18.85 bps), ETH ask 496,993 → 52,908 (3.86 → 6.50 bps). **Only BNBUSDT
improved** — ask 1,542 → 6,421,731 USDT, spread 1.28 → **0.26 bps**: the first contract in four checks to
*strengthen* across a requote.

**The engine's quote at 12:17:48Z is a third sample and it recovered:** bid 1.5636 × 2,356,090.7 = **3,683,983
USDT**, ask 13,453,249 USDT, spread **3.84 bps**. So the 42.10 bps / 4,309 USDT reading was **transient, requoting
back to health within four minutes** — the same pattern L-001 recorded for BTC's 32.59 bps → 1.06 bps. That makes
the finding *worse*, not better: **the book oscillates between deep and effectively unquoted within minutes**,
which is exactly why a stop resting on this exchange between checks cannot be trusted to fill near its trigger.

### (5) External corroboration: the direction is real, the level is not, and the drift has flipped sign

External reporting independently describes **an XRP-led market pullback of nearly 7% driven by a leverage unwind
with roughly $1.35bn of liquidations** — matching the demo's −7.137% almost exactly. This **retrospectively
vindicates the 16:00 decision** to classify the 04:00Z 1.6855 spike as *real but externally unconfirmed* rather
than as an artifact: a genuine spike and reversal did occur.

But external XRP prints **~1.61 against the demo's 1.5644** — the demo is now **~2.9% below** the outside world,
having been **~2.1% above** it at 16:00. **The demo tracks external direction while its level drifts several
percent either way within a single session.** New finding; a further reason never to anchor a stop or target within
a few percent of a demo level.

Third-party technical opinion (RSI 69.67; *"a daily close below 1.57 opens the door to the EMA20 at 1.42"*) was
**read as data and not acted on** — it is opinion, not a verifiable event, and no level in this check rests on it.

### (6) News is a reason to stand aside, not a reason to short

A **Trump–Xi meeting is scheduled for 2026-09-24 — inside the 24-hour hold window**. A position opened now would
have to be held through it. Combined with a reported liquidation cascade, the strategy's condition that *"the move
is not so fast that a controlled stop cannot be defined"* fails on both clauses. Recorded as event risk, **not**
claimed as directional evidence.

### (7) Volume: seventh consecutive negative, and now negative in both directions

The 11:00Z hour that broke 1.5695 traded **3366.0M** against a day band of 3160.0 / 3407.3 / 3626.3 / 3697.5 /
3501.8 / 3565.6 / 3657.9 / 3168.0 / 3907.6 / 3637.2 / 3669.2M — **below the median**. The same contract has now
made a new 24h high **and** a 7% reversal, **both on below-median volume**. That is a finding about the host's
volume series rather than about XRP, and it belongs to the review.

### (8) Other contracts

- **ETHUSDT short** — the only construction that came close to **two categories**: `trend` (4h ascending lows
  2716.01 → 2722.76 → 2722.62 → 2729.14 → 2737.75 → 2745.20 broke to 2737.35 → 2717.02) and `market_context`
  (ETH −0.762% vs BTC −0.537% on 24h **and** −1.911% vs −1.311% on 8h — weaker than BTC on **both** windows, and
  unlike XRP it does not flip sign). **Refused on geometry, not evidence:** the structural stop 2736.95 pays 0.006
  to the 24h low and clears 1.5 only at 2687.56, a number derived to make the arithmetic work. **There is no
  structure at all between 2716.01 and the 09-20 daily low 2568.16 — a 5.4% vacuum.** L-003 then killed it outright.
- **BNBUSDT short** — structural stop 786.29 pays 0.075 to the 24h low; its only passing target, 765.00, is below
  the 09-21 daily low 766.72. Same vacuum, plus the L-002/L-003 collision above.
- **SOLUSDT** — excluded a **third** consecutive check on three independent grounds: the **106.67 print persists
  unrevised** (09-22 19:00Z 1h, 9.654% lower wick on a 0.017% body = 570×, 10.094% range vs 0.795% median, still
  contaminating the 24h low field against a real floor of 116.60); spread deteriorating 15.43 → 18.85 bps for a
  third check running; 24h quote volume 390.9M against 100,116M–137,716M for the other four, a factor of ~250.
- **BTCUSDT** — excluded for a **thirteenth** consecutive check under L-001.

### (9) L-001: its re-test condition, exceeded at 16:00, is no longer met

The 16:00 note recorded BTC's 1h scan as **completely clean** and its re-test condition as *exceeded*. **It is not
clean now.** Nine 1h wick/body flags have reappeared — 09-22 21:00Z at **57.4×**, 23:00Z at **35.0×**, 20:00Z 7.0×,
09-22 14:00Z 7.5×, 09:00Z 5.6×, 16:00Z 5.4×, 18:00Z 4.1×, 09-23 06:00Z 3.4×, 09-22 17:00Z 3.0× — all of **small
magnitude** (wicks 0.09%–0.79%), recorded honestly rather than argued away. And the **09-21 95,804.10 print still
contaminates the daily frame** (1d H 95,804.10 against an 86,523.40 close, a 10.7% wick).

L-001's re-test condition — *"a full day with no artifact print while the scan is still running at both
resolutions"* — is therefore **no longer met, one check after it was exceeded.** A check may not retire a lesson in
any case; this is recorded for the review, which owns that decision. BTC's 162 USDT ask would have refused it
independently.

---

## Lessons applied

- **L-001** — applied. BTCUSDT excluded a thirteenth consecutive check; scan run at **both** 5m and 1h; its
  re-test condition **no longer met** after nine fresh 1h flags and a daily frame still carrying 95,804.10.
  SOLUSDT excluded again on the persisting 106.67 print.
- **L-002** — applied and **decisive for a fourth consecutive check, and for the first time on a short.** It
  rejected the 0.97× N stop before pricing, rejected the 1.60× N stop resting under a level touched forty minutes
  earlier, and caught BNB's stop falling to 0.98× N mid-requote.
- **L-003** — applied for a **sixth** consecutive check, and it **changed the answer on all three candidates**.
  Its re-test clock resets from one to **zero**.

No lesson was loosened, reinterpreted or overridden. Nothing under `reviews/` was read for modification or
modified; the 22:00 review task owns that folder.

---

## For the 21:00 check

1. **Do not rebuild the XRP short on `price_action` alone.** It has one clean category. The honest second
   category would be `market_context` on a *consistent* window — check whether XRP is still weakest on 4h/8h
   **and** has lost its 24h relative-strength lead. **If the 24h figure turns negative while the 4h weakness
   persists, the contradiction resolves and `market_context` becomes claimable.** That is the specific,
   falsifiable condition to test.
2. **Watch 1.5621 and 1.5306.** 1.5621 is today's low and was already bought once (12:05Z reversal bar). Its loss
   on *expanding* volume would be the first volume confirmation in seven checks. 1.5306 is the 24h low and the
   nearest target that any honest stop could reach.
3. **Watch 1.5951 and 1.6043 on the upside.** A reclaim of 1.6043 restores the broken 4h sequence and puts the
   long back on the table — but only on a *pullback that holds*, never on a continuation.
4. **Check the book at every sample and treat the engine quote as a third.** XRP went 3.1M → 4,309 → 3.7M USDT and
   0.64 → 42.10 → 3.84 bps inside thirteen minutes. **A single healthy sample means nothing on this host.**
5. **Read the 16:00Z XRP settlement** (predicted −0.008977% → −0.006463% at the 16:00 check; live rate now
   +0.010000%). Record what the forecast said against what actually settled — that comparison, not the rate, is
   the useful datum, and this is now the second forecast to test.
6. **Trump–Xi, 2026-09-24, is inside the hold window** for anything opened from here. Any entry must be justified
   *through* that event, not around it.
7. **ETHUSDT is the contract to watch for a genuine two-category short** — it is the only one whose
   `market_context` does not flip sign between windows. It failed on a 5.4% structural vacuum below 2716.01, not
   on evidence. If price reaches 2716–2717 and *rejects*, the geometry may open.
8. **SOLUSDT** — re-scan the 19:00Z bar (106.67 has now persisted three checks) and watch whether the spread
   crosses the 25 bps cap.
9. **BTCUSDT stays excluded** until the review says otherwise.

## Outstanding for Edward

Carried from the 09:00, 22:00, 23:00, 00:00, 02:00, 09:00 and 16:00 checks: the 09:00 run on 2026-09-22 stalled
~12h40m and **three slots were lost** — 16:00, 20:00 and 21:00 on 2026-09-22 did not run. **Seven consecutive
checks have now run on time**, strong evidence the condition has cleared, but **the cause was never identified**;
scheduled tasks only run while the Claude desktop app is open, so it is worth confirming whether the machine slept
or the app was closed. The account was flat throughout, so the cost was observations, not money. Live trading
remains disabled.
