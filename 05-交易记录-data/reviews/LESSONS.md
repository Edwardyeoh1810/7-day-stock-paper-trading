# Current lessons

Read before every decision. Maintained only by the daily review: at most 10 lessons of at most 100 words each, most useful first, each stating its evidence and sample size. A lesson may make the AI more selective within the rules; it cannot loosen or override any rule in `AGENTS.md`, the strategy, `readiness.json` or `paper-config.json`. The review retires a lesson the data no longer supports, or that would shut the experiment.

**Reset on 2026-09-26 (day 6, 0 closed trades, 35 decisions).** The previous file had grown to 7 lessons and ~5,800 words, and its L-001 excluded all five contracts until after the experiment's end. Edward approved a rewrite of the artifact and target rules in the strategy and a reset of this file; the old file is kept at `archive/LESSONS-2026-09-21-to-25.md`. Retired: L-001 (superseded by the strategy's bounded artifact rule), L-004 (its span screen assumed structural-only targets; the strategy now allows measured targets), L-006 and L-007 (window-roll bookkeeping; useful discipline, but they had become the decision's centre of gravity). Kept in short form below.

## L-002 — A stop inside recent bar noise is a position size, not a stop
Hypothesis (35 decisions, 0 trades). Before pricing any reward/risk, measure N = the largest 5m bar range of the full preceding hour. A stop closer to the entry than N is inside noise: decline the setup regardless of how well the ratio scores. Evidence: on 2026-09-23 a BNBUSDT stop that looked like 2.9x N over the last twelve bars was 0.8x N over the full hour, because the bar that created the setup was the largest in the window.

## L-003 — Requote before acting on a ratio
Hypothesis (35 decisions, 0 trades). Take a second quote several minutes after the first and recompute the reward/risk before any entry. A ratio that improved because price drifted toward a fixed stop is the risk shrinking, not the trade improving, and it usually comes with the premise breaking. Evidence: XRPUSDT short ratio moved 1.74 to 2.81 on 2026-09-22 purely by drift.

## L-005 — Check book depth, not just the spread
Hypothesis (35 decisions, 0 trades). The spread cap is blind to quantity. Sample top-of-book notional on both sides at least three times across the check; decline if the side the entry must cross, or the side the exit must cross, is effectively unquoted at any sample. Evidence: SOLUSDT's book went unquoted on the crossing side twice on 2026-09-23 while its spread was inside the cap.
