# 定时任务说明与保存文案

本文件是本地 Claude 定时任务的仓库内文案。实际部署状态见 [automation-status.json](automation-status.json)。英文版 [AUTOMATION-PROMPT.md](AUTOMATION-PROMPT.md) 内容相同；如有差异，以英文版为准。

## 当前安排

项目目录为 `/Users/edwardmacmini/Projects/7-day-stock-paper-trading`。加密货币全天交易，因此按 Asia/Kuala_Lumpur 时间每四小时检查一次，每天六次：00:00、04:00、08:00、12:00、16:00、20:00，连续七个自然日；日期见 [schedule.json](schedule.json) 及 [中文版](schedule.zh-CN.json)，共 42 个时点，迟到容差 30 分钟。一个本地 Claude 定时任务（`paper-trading-4h-check`）按主机本地时间（即日程时区）在这些时点触发。GitHub 托管 Runner 受 Binance HTTP 451 限制，所有运行均在本地进行。

## 任务文案

所有项目操作仅在项目目录进行。每次读取中英文 AGENTS、策略、schedule、CONTINUITY、readiness、current-state 和最新 journal。策略文档原为股票编写；将其证据、风险和“不交易”纪律应用于加密现货观察列表，与 `AGENTS.md` 冲突时以 `AGENTS.md` 为准。

先运行 `python3 -B 06-程序脚本-scripts/run_observation.py --dry-run`。如果 `due_slot` 为 null（不在计划交易日或时点容差内），安静结束且不做任何修改。时点到期时运行 `python3 -B 06-程序脚本-scripts/run_observation.py`。遇到 duplicate_skipped 或 another_run_active 即停止。继续前先用 `--recover` 处理中断的只读运行。

使用官方日历、新闻和可验证的市场数据研究本时点主题，仅限观察列表中的交易对。研究内容保存为单独的 journal/evidence 文件，使用相同 run_id 加 `-research` 后缀，并更新下一次任务重点。不要编辑自动生成的 API 日志。

研究后独立决定开仓、管理、平仓或记录不交易。用户仅授权在 Binance 模拟盘（虚拟资金）上进行自主 paper 决策。绝不提交正式环境订单、转账或修改账户设置；绝不修改 `BINANCE_ENV`、readiness 安全开关、风险限制、观察列表或任何脚本；除通过 `paper_engine.py` 外绝不调用下单接口。

每个决策都要在 `05-交易记录-data/decisions/` 下创建不含密钥的 JSON 文件，包含 `paper_trading_only: true`、`action`（`open_long`、`manage`、`close` 或 `no_trade`）；开仓还需 `symbol`、`thesis`、`stop_price`、`target_price` 和至少两类证据的 `evidence` 列表（每项含 `category` 和 `source`）。然后运行 `python3 -B 06-程序脚本-scripts/paper_engine.py --decision <文件> --run-id <日期_时点>_paper`；`_paper` 后缀避免覆盖只读运行的证据文件。引擎会刷新模拟盘 readiness 检查，拒绝过期或不安全状态，在新的本地日重置当日亏损计数，按风险限制计算数量，向模拟盘提交一笔市价单，把实际成交记入本地账本，并立即在模拟盘挂出止损和止盈（OCO）委托。引擎拒绝决策时，记录原因，不得放宽参数重试。

只要有持仓，每次检查都要提交 `manage` 决策（或 `close`，`reason` 为 `thesis_invalid` 或 `manual_exit`）：引擎会先对账上次检查以来模拟盘已触发的止损或止盈（状态 `exchange_exit_reconciled`），并平掉持有满 24 小时的仓位。没有持仓时，任何一次检查都可以开新仓。最后一个计划日期的 20:00 检查必须对剩余仓位提交 `close`（reason 为 `end_of_day`）并确认账户已空仓。绝不自行下达、撤销或修改交易所委托。

保持 5000 USDT paper 资金和现有限制；当费用、流动性、数据质量或证据不足时记录不交易。两次检查之间，止损和止盈委托挂在模拟盘上；止损触发后按市价卖出，实际亏损可能与计划亏损略有差异。凭证只能由脚本在本地读取；绝不显示、打印或复制。

状态无变化或无需操作时保持安静。在定时报告、重要变化、完成、失败或需要用户操作时汇报。第七个交易日 14:45 检查后，在日志中写入最终总结，之后的运行不再做任何事。

## 验证边界

全部 42 个时点和中英文日程由测试套件离线校验。模拟盘 readiness 检查、五个交易对的行情快照、仅校验的测试订单、一次 no-trade 引擎运行，以及一次模拟盘实单往返（市价买入、挂 OCO、查询状态、撤单、市价卖出）已于 2026-09-21 验证。定时任务仅在 Claude 桌面应用打开时运行；每次运行必须比较主机实际时间与目标时点，绝不补做历史交易。
