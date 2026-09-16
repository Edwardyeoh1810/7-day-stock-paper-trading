# 定时任务说明与保存文案

本文件是当前 GPT heartbeat 的仓库内说明副本。实际部署状态见 [automation-status.json](automation-status.json)。

## 当前安排

项目目录为 `/Users/a123/Desktop/7天股票交易实验`，任务返回当前实验会话。America/Chicago 时间每日 07:45、08:35、11:00、13:00、14:15、14:45；七天日期见 [schedule.json](schedule.json) 及 [中文版](schedule.zh-CN.json)，共 42 个时点，迟到容差 30 分钟。GPT heartbeat 自动任务 7 已启用；GitHub 托管 Runner 仍受 Binance HTTP 451 限制。

## 任务文案

所有项目操作仅在本桌面目录进行。每次读取中英文 AGENTS、策略、schedule、CONTINUITY、readiness、current-state 和最新 journal。

先运行 `python3 -B 06-程序脚本-scripts/run_observation.py --dry-run`；不在预定七个美股交易日和研究时点十分钟容差内则静默结束。有效时点运行 `python3 -B 06-程序脚本-scripts/run_observation.py`。若返回 duplicate_skipped 或 another_run_active 则结束，不重复操作；中断运行须先用恢复流程核对。

随后按该时点主题查询官方日历、新闻和可验证行情，将研究另存为以同一 run_id 命名并加 `-research` 后缀的日志和证据，更新下一任务重点，不修改自动导出的 API 检查日志。

研究完成后，独立决定本地 paper ledger 应开仓、管理、平仓还是不交易。用户仅授权自动 paper trading；绝不提交真实 Binance 订单、转账、代币化请求或账户设置修改。

每次决策在 `05-交易记录-data/decisions/` 新建不含密钥的 JSON，必须有 `paper_trading_only: true`，`action` 只能为 `open_long`、`manage`、`close` 或 `no_trade`；开仓时必须写入证据、逻辑、止损和目标。随后运行 `python3 -B 06-程序脚本-scripts/paper_engine.py --decision <file> --run-id <date_slot>_paper`；`_paper` 后缀可防止覆盖只读运行器生成的证据文件。引擎会刷新只读 Stocks 行情，拒绝过期或不安全状态，并且只写入本地 paper ledger。只有 08:35 与 11:00 Central 可考虑新开仓；13:00 只管理风险；14:15 必须清掉没有明确隔夜许可的纸面仓位。

保持 10000 USDT 模拟资金及既有风险上限；费用、流动性、数据质量或证据不满足时必须记不交易。此任务不承担连续止损职责。密钥只由脚本在本机读取，禁止输出。

未变化或不可行动时保持安静；计划报告、重大变化、完成、失败或需要用户处理时发送通知。若实际开始日期延后，重新核验七个交易日并同步中英文日程。七天结束后暂停本任务。

## 验证边界

已离线核对 42 个时点和中英文时间一致性。GPT heartbeat 自动任务 7 已在桌面项目中执行。2026-09-15 曾出现一次严重延迟，因此每轮必须比较主机实际时间与目标 Central 时点，绝不补造历史交易。
