# 06 程序脚本

- `binance_readiness_check.py`：只读检查账户、权限、股票规则、报价和未结订单。
- `run_observation.py`：识别六个日程时点，写入 SQLite、日志和证据。
- `paper_engine.py`：执行本地 paper 决策，不包含真实下单路径。
- `paper_ledger.py`：仓位、费用、滑点、止损、目标和盈亏记账。
- `paper_trade.py`：手动调用本地模拟账本的维护入口。
- `run_store.py`：运行去重、中断恢复和确定性导出。

这些脚本均不得输出密钥或向 Binance 提交真实订单。
