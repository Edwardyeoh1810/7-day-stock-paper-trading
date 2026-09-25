# Research journal — 2026-09-22_check_2200-research

Companion to the generated journal entry for `2026-09-22_check_2200_paper`. The generated API journal and
evidence exports were not edited; research and corrections live here.

- **Timestamp and task id:** written 2026-09-22T14:12Z (22:12 Asia/Kuala_Lumpur), slot `2026-09-22_check_2200`.
- **What was done:** Read AGENTS.md, TRADING-STRATEGY.md, CONTINUITY.md, AUTOMATION-PROMPT.md, readiness.json,
  current-state.json, the 09:00 slot's research note and reviews/LESSONS.md. Ran the read-only observation for the
  due slot at 14:04:29Z, then pulled 5m, 1h, 4h and 30 daily bars, the book, the 24h ticker, funding and open
  interest for all five watchlist contracts from the demo host's public endpoints, ran the artifact scan at both 5m
  and 1h as the standing instruction requires, re-implemented the engine's reward/risk formula independently from
  `paper_ledger.py`, and took a confirming quote sweep four minutes after the first. Submitted a `no_trade`
  decision through `paper_engine.py`.
- **Why it was done:** The 22:00 slot was due (`due_slot: 2026-09-22_check_2200`, 240 planned slots) and no
  position was open, so an entry was permitted if and only if every entry condition was met.
- **Timing:** Observation 14:04:29Z, research 14:05:02Z, confirming sweep 14:09:20Z, decision submitted 14:11:08Z
  (22:11 MYT) — **11 minutes after the slot**. This run is **ON TIME**. It is the first check since the stall where
  the late-run rule was not the governing constraint, and the entry was refused on evidence rather than on the clock.
- **Order proposed:** No.
- **Order placed:** No. The engine returned `status: no_trade`, `live_order_sent: false`.
- **Order filled:** No.
- **Exchange stop/target reconciliation:** None to reconcile. The account was flat before this check and is flat
  after it; no exit order has ever been placed in this experiment.
- **Current holdings:** None. Flat.
- **Current cash:** 5000 USDT. Demo wallet balance 5000.04174826 USDT.
- **Current risk:** 0 USDT open risk; 0 USDT realized today. Ledger date `2026-09-22`.
- **Evidence captured:** `05-交易记录-data/evidence/2026-09-22_check_2200.json` (read-only run),
  `05-交易记录-data/evidence/2026-09-22_check_2200_paper.json` (engine), and this note.

## The check answered its own question, in four minutes

This is the first check of the experiment where the market resolved the decision *while the decision was being
written*, and it is worth recording precisely because the refusal did not have to rest on judgement.

| Time | XRPUSDT | Event |
|---|---|---|
| 13:45Z | 1.5523 → 1.5637 | Thrust begins, +0.734% on 498,476,861 |
| 13:55Z | 1.5638 → **1.5875** | Breakout bar, **+1.516%**, closes at its high, 625,770,303 |
| 14:05Z (first quote) | 1.5794 / 1.5799 | 0.49% off the high |
| 14:05Z bar | O1.5799 H1.5799 **L1.5699** C1.5715 | **552,264,819 — back below the broken level** |
| 14:09Z (confirming sweep) | 1.5715 / 1.5716 | −0.50% in four minutes |
| 14:11Z (engine quote) | 1.5703 / 1.5704 | Sitting exactly on 1.5701 |

**XRPUSDT broke a genuine 30-day high and gave it all back inside fifteen minutes.** The maximum daily high over
the 30 preceding sessions, excluding today, is 1.5701 — set yesterday. The 13:55Z bar printed 1.5876. By 14:05Z
price had traded 1.5699, below it.

## Why this was nevertheless the best setup the experiment has seen

It deserves saying plainly, because the next check should not dismiss XRPUSDT on the strength of this failure.

- **Trend genuinely agreed.** Daily: 09-18 +7.781%, 09-19 +1.010%, 09-20 −0.035%, 09-21 +8.994%, 09-22 +2.825%.
  4h ascending lows 1.3871 → 1.3938 → 1.4042 → 1.4143 → 1.4383 → 1.4765 → 1.4814 → 1.5041 → 1.4939 → 1.5142 →
  1.5306, with the 09-22 00:00 pullback bar (−1.367%) completed and 08:00 (+1.265%) and 12:00 (+2.778%) resuming.
- **Clean air above.** A 30-day high means that for the first time a passing target would **not** have had to jump
  two or three intervening levels — the objection that killed the 00:00, 02:00 and 09:00 constructions.
- **Clean data.** XRPUSDT returned **no artifacts at either 5m or 1h**, and its spread was 3.17 bps against the
  25 bps cap.
- **Funding favoured the long.** −0.019946%, the only negative rate in the complex against the 0.0100% baseline
  (BNB 0.0000%), with mark 1.58037172 above the 1.57965 mid — a perp discount during a rally. A long would have
  *received* at the 16:00Z settlement.

## And why it still failed, on the same problem as every check before it

Re-implementing the engine's formula from `paper_ledger.py` (fee 5 bps, slippage 2 bps per side,
entry = ask × 1.0002 = 1.580216):

| Stop | Risk | 1.6039 (+1.50%) | 1.6200 (+2.52%) | 1.6463 (+4.18%) | Verdict |
|---|---|---|---|---|---|
| 1.5690 — below the broken 1.5701 | **0.710%** | **1.661** | 2.889 | 4.895 | Passes, but **noise-width** |
| 1.5625 — below the 1.5635 shelf | 1.121% | 1.111 | 1.932 | 3.273 | Fails at the anchored target |
| **1.5470 — below the 1.5476 double low** | **2.102%** | 0.509 | 1.079 | **1.828** | Noise-safe, needs a **4.18% reach** |
| 1.5300 — below the 4h bar low | 3.178% | 0.343 | 0.727 | 1.232 | Fails outright |

**The inversion held for a fourth consecutive check.** The only construction clearing 1.5 on a modest target did so
on a 0.710% stop — less than half the 1.534% range of the single 5m bar that made the breakout, and about half a
typical recent hourly range (12:00 0.928%, 11:00 1.456%, 10:00 1.313%, 08:00 2.291%). That is trap (a). The honest
noise-safe stop at 1.5470 (1.37× the largest 5m bar) needed roughly 1.636 to reach the floor and cleared properly
only at the 1.6463 measured move.

**Then the tape adjudicated trap (a) directly.** Price traded 1.5699 — within **0.0009** of the 1.5690 stop that
made the tight construction "pass" — inside the same check that proposed it. Previous notes argued that a
noise-width stop is a size rather than a stop; this check did not have to argue it.

## The finding that matters most: volume never confirmed, at any timeframe

This is the reason the setup was thin *before* it failed, and it is a new and specific finding about XRPUSDT.

- **Hourly volume is uninformative.** The +2.971% breakout hour (13:00Z) traded **3,908,273,922** — *less* than the
  flat 11:00Z hour (4,029,644,508) and the 08:00Z hour (4,025,945,039). XRPUSDT's hourly volume sits in a
  3.5–4.0B band **every single hour regardless of what price does**. It carries no directional information and
  should not be cited as a `volume` category on this contract at 1h.
- **5m volume argued the other way.** The breakout bar's 625,770,303 was only the **second** heaviest of the last
  thirty bars. The heaviest — 707,658,833 at 13:25Z — was a **down** bar. And the 14:05Z failure bar traded
  552,264,819, nearly matching the breakout itself.

A 30-day-high break on no volume expansion, faded on heavy volume, is the textbook false-breakout profile. The
`volume` category was therefore recorded as evidence **against** the long rather than merely unavailable.

## What remained was not independent enough

Stripping `price_action` (unconfirmed, then failed) and `volume` (absent, then adverse) leaves `trend`,
`market_context` and `derivatives` — nominally three, but honestly fewer:

- `trend` and `market_context` are largely **the same observation over the same candles** — XRP has risen a lot
  recently, more than the others. The strategy is explicit that a moving average and a trend line over the same
  candles are one observation, not two, and the same logic applies here.
- `derivatives` remains **degraded to funding alone** — `/futures/data/openInterestHist` still returns the bare
  string `ok` with no history — and −0.019946% is small in absolute terms.
- The +6.8-point divergence from the weakest contract also cuts both ways: the strategy treats these five as five
  ways to express one view, and an idiosyncratic single-name move of that size is as consistent with mean reversion
  against the complex as with leadership.

The strategy's session-timing rule settled the rest: *a breakout at 21:00 that has not held is not evidence yet.*
At 22:00–22:11 MYT this check sat thirty to forty minutes past the 21:30 US open, inside exactly the erratic window
that rule names, looking at a breakout fifteen minutes old.

## Artifact scan

| Contract | 1h | 5m |
|---|---|---|
| BTCUSDT | **5 contaminated bars** — 95804.10 (09-21 09:00Z, 13.347% wick on a 1.042% body), 95804.10 (14:00Z, 11.747% on 0.429%), 87888.00 (12:00Z, 2.991%), 91000.00 (19:00Z, 5.148%), 90389.80 (20:00Z, 3.985%) | clean |
| ETHUSDT | **1 contaminated bar — NEW** — 2850.00 at 09-21 09:00Z, 4.797% upper wick on a 0.896% body | clean |
| BNBUSDT / SOLUSDT / XRPUSDT | clean | clean |

**The ETHUSDT artifact is a new find and shares the 09:00Z hour with BTCUSDT's 95804.10** — the two are the same
demo event, not two independent ones. It now sits outside the 24h window (which reads 2804.59), but it should be
excluded from ETHUSDT resistance. The 5m scan over 48 bars on all five returned **nothing**, a third consecutive
fully clean 5m scan.

**BTCUSDT is excluded for a seventh consecutive check**, but the basis has narrowed and the record should say so:
**the spread breach did not recur.** BTCUSDT quoted 12.82 bps at 14:04Z and 0.13 bps at 14:09Z, against 32.59 bps
at the 09:00 check. That earlier reading was demo book instability, not a persistent condition, and the exclusion
now rests on the artifacts alone. Its 24h high field still reads 95804.10 against a real session top near 86251.

## Next task focus

Account is flat; cash and equity 5000 USDT; nothing to reconcile. The 23:00 check is one hour away and there is a
specific, concrete thing to look for.

1. **Watch 1.5701 on XRPUSDT — it is now the pivot, not the breakout.** Price is sitting on it (1.5703/1.5704 at
   14:11Z). Three outcomes, and they are not symmetric:
   - **Holds and retests from above**, forming a pullback low *above* 1.5701 → this is the setup worth taking. A
     structural stop just beneath the retest low would be **both noise-safe and close**, which is the first
     construction in this experiment that would actually **solve** the distance problem rather than work around it.
     Re-derive the RR from the fresh ask; do not reuse this note's numbers.
   - **Loses 1.5701 and builds structure below it** → the failed-breakout short becomes discussable, but *only*
     with a second independent category and a structural stop above the 1.5876 high or a lower swing high. Note
     that funding is negative, so a short **pays**.
   - **Chops across it** → no trade; that is the most likely outcome and it is fine.
2. **Do not claim `volume` on XRPUSDT at 1h.** This check established that its hourly volume is a flat 3.5–4.0B
   band independent of price. If volume is to be used on this contract, it must be from the 5m series and it must
   be compared against the full 30-bar window, not against the neighbouring bar.
3. **The distance problem now has a fourth data point and should go to the review as one problem.** The 00:00
   note's ~2.5% stop-to-target requirement, the 02:00 note's unaffordable confirmation wait, the 09:00 note's
   nearest-target-pays-0.19-to-0.52 finding, and this check's split between a passing 0.710% noise stop and a
   noise-safe 2.102% stop needing a 4.18% reach are **four forms of one finding**: the 1.5 net floor and the
   structural-stop requirement are jointly selecting against this watchlist at these volatilities. This check adds
   the sharpest version yet, because the tape then confirmed the noise-stop objection within minutes.
4. **BTCUSDT stays excluded on artifacts alone** — the spread breach was transient and should not be carried
   forward as a standing reason. **Keep running the artifact scan at 1h as well as 5m**; it is what found the new
   ETHUSDT contamination this check.
5. **The 16:00Z funding settlement** falls between this check and the 00:00 one. XRPUSDT was the only negative rate
   in the complex; worth re-reading at 23:00 to see whether the discount persisted through the failed breakout.

## Human confirmations needed

None for demo paper trading; live trading remains disabled.

**One item from the previous check is still outstanding and is Edward's to close.** The 09:00 run stalled for
roughly twelve hours and forty minutes and **three slots were lost** — 16:00, 20:00 and 21:00 on 2026-09-22 did not
run at all. This check ran normally and on time, which is a good sign that the condition has cleared, but the cause
was never identified. Scheduled tasks only run while the Claude desktop app is open, so it is worth Edward
confirming whether the machine slept or the app was closed. The account was flat throughout the stall, so the cost
was observations rather than money; had a position been open, the 24-hour hold limit and the between-check
reconciliation would both have been missed, and only the exchange-side stop and target would have protected it.

`LESSONS.md` was read and is still empty — no closed trades, so no lesson exists to apply. **Nothing under
`reviews/` was modified**; the 22:00 review task owns that folder and may be running concurrently with this check.
