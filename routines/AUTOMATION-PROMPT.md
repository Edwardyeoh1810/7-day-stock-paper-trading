# Automation Description and Saved Prompt

This preserves the earlier app card's work description for later review or recreation. Writing this file does not create or activate a task. See [automation-status.json](automation-status.json).

## Provisional Schedule

Use `/Users/a123/Desktop/7天股票交易实验` and return to the existing experiment conversation. Six America/Chicago checks: 07:45, 09:30, 11:00, 13:00, 14:15 and 14:45. Dates are in [schedule.json](schedule.json) and its [Chinese companion](schedule.zh-CN.json): 42 occurrences and a ten-minute late-start tolerance. Start paused; authenticate, review the draft and validate execution before activation. Rebase dates if setup is delayed.

## Saved Prompt

Perform all project operations only in the Desktop experiment directory. Read both languages of AGENTS, strategy, schedule and CONTINUITY, plus readiness, current-state and the latest journal.

Run `python3 -B scripts/run_observation.py --dry-run` first. Outside the planned sessions or slot tolerance, finish quietly. For a due slot, run `python3 -B scripts/run_observation.py`. Stop on duplicate_skipped or another_run_active. Reconcile interrupted read-only runs using recovery before continuing.

Research the slot's topic with official calendars, news and verifiable data. Save research in separate journal/evidence files using the same run_id with a `-research` suffix, and update next-task focus. Do not edit generated API journals.

Observe only when authentication or data is invalid or the stop/fill draft is unapproved. Keep 20 USDT paper capital and existing limits; record no trade when actual fees or minimum amounts make trading infeasible. Do not implement or execute live orders, transfers, tokenization or automatic agreement acceptance. This is not a continuous stop monitor. Read credentials locally through the script; never display them.

Stay quiet for unchanged or non-actionable state. Notify only on meaningful changes, completion, failure or required user action. Activate only after authentication passes and draft review completes. Revalidate seven sessions and synchronize schedules if the start is delayed. Pause after the seventh session.

## Verification Boundary

All 42 provisional times and language schedules were checked offline. The app rendered a timezone-specific card; saving, wake-up execution and unattended file access remain unverified. The Desktop project differs from the conversation's original Documents workspace. Verify Desktop access before activation. A rendered card is not a successful scheduler run.
