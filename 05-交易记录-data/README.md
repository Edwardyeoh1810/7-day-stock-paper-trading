# 05 交易记录

- `current-state.json`：当前现金、权益、持仓、盈亏和下一次任务重点。
- `paper-ledger.json`：本地模拟成交事件账本。
- `decisions/`：每次 AI 的非秘密结构化决策。
- `journal/`：按日期和任务保存的人类可读运行日志。
- `evidence/`：行情快照、新闻链接、只读检查结果和决策证据。
- `runs.sqlite3`：只读调度器数据库，已被 Git 忽略。

复盘时先看 `current-state.json`，再按时间查看 `journal/` 与对应的 `evidence/`。
