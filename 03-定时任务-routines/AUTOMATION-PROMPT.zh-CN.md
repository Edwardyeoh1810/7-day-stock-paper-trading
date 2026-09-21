# 定时任务说明与保存文案

本文件是本地 Claude 定时任务的仓库内文案。实际部署状态见 [automation-status.json](automation-status.json)。英文版 [AUTOMATION-PROMPT.md](AUTOMATION-PROMPT.md) 内容相同；如有差异，以英文版为准。

## 当前安排

项目目录为 `/Users/edwardmacmini/Projects/7-day-stock-paper-trading`。America/Chicago 时间每日 07:45、08:35、11:00、13:00、14:15、14:45；七天日期见 [schedule.json](schedule.json) 及 [中文版](schedule.zh-CN.json)，共 42 个时点，迟到容差 30 分钟。任务按主机本地时间（UTC+8）触发：20:45、21:35、00:00、02:00、03:15、03:45；午夜后的四次运行属于前一个 Central 日期。GitHub 托管 Runner 受 Binance HTTP 451 限制，所有运行均在本地进行。

## 任务文案

所有项目操作仅在项目目录进行。每次读取中英文 AGENTS、策略、schedule、CONTINUITY、readiness、current-state 和最新 journal。策略文档原为股票编写；将其证据、风险和“不交易”纪律应用于加密现货观察列表，与 `AGENTS.md` 冲突时以 `AGENTS.md` 为准。

先运行 `python3 -B 06-程序脚本-scripts/run_observation.py --dry-run`。如果 `due_slot` 为 null（不在计划交易日或时点容差内），安静结束且不做任何修改。时点到期时运行 `python3 -B 06-程序脚本-scripts/run_observation.py`。遇到 duplicate_skipped 或 another_run_active 即停止。继续前先用 `--recover` 处理中断的只读运行。

仅在 07:45 时点、任何决策之前：确认没有持仓，然后在 `05-交易记录-data/current-state.json` 中把 `daily_realized_pnl_usdt` 设为 0，把 `trading_day_index` 设为当天 Central 日期在 `planned_trading_dates` 中的序号（从 1 开始）。

使用官方日历、新闻和可验证的市场数据研究本时点主题，仅限观察列表中的交易对。研究内容保存为单独的 journal/evidence 文件，使用相同 run_id 加 `-research` 后缀，并更新下一次任务重点。不要编辑自动生成的 API 日志。

研究后独立决定开仓、管理、平仓或记录不交易。用户仅授权在 Binance 模拟盘（虚拟资金）上进行自主 paper 决策。绝不提交正式环境订单、转账或修改账户设置；绝不修改 `BINANCE_ENV`、readiness 安全开关、风险限制、观察列表或任何脚本；除通过 `paper_engine.py` 外绝不调用下单接口。

每个决策都要在 `05-交易记录-data/decisions/` 下创建不含密钥的 JSON 文件，包含 `paper_trading_only: true`、`action`（`open_long`、`manage`、`close` 或 `no_trade`）；开仓还需 `symbol`、`thesis`、`stop_price`、`target_price` 和至少两类证据的 `evidence` 列表（每项含 `category` 和 `source`）。然后运行 `python3 -B 06-程序脚本-scripts/paper_engine.py --decision <文件> --run-id <日期_时点>_paper`；`_paper` 后缀避免覆盖只读运行的证据文件。引擎会刷新模拟盘 readiness 检查，拒绝过期或不安全状态，按风险限制计算数量，向模拟盘提交一笔市价单，并把实际成交记入本地账本。引擎拒绝决策时，记录原因，不得放宽参数重试。Central 08:30 之前和 11:30 之后不得开仓。Central 14:15 必须平掉剩余仓位（禁止隔夜）；14:45 确认账户已空仓。

保持 5000 USDT paper 资金和现有限制；当费用、流动性、数据质量或证据不足时记录不交易。这不是连续止损监控：止损和目标仅在定时检查时评估。凭证只能由脚本在本地读取；绝不显示、打印或复制。

状态无变化或无需操作时保持安静。在定时报告、重要变化、完成、失败或需要用户操作时汇报。第七个交易日 14:45 检查后，在日志中写入最终总结，之后的运行不再做任何事。

## 验证边界

全部 42 个时点和中英文日程由测试套件离线校验。模拟盘 readiness 检查、五个交易对的行情快照、仅校验的测试订单和一次 no-trade 引擎运行已于 2026-09-21 验证。定时任务仅在 Claude 桌面应用打开时运行；每次运行必须比较主机实际时间与目标 Central 时点，绝不补做历史交易。
