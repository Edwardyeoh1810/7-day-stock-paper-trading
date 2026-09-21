# 06 程序脚本

- `binance_readiness_check.py`：只读检查账户、权限、交易规则、报价和未结订单；`BINANCE_ENV=demo` 时检查 Binance 模拟盘 USDT 永续合约。
- `run_observation.py`：识别六个日程时点，写入 SQLite、日志和证据。
- `paper_engine.py`：执行 paper 决策；通过 `demo_orders.py` 只向 Binance 模拟盘下单，不包含正式环境下单路径。
- `demo_orders.py`：唯一的 POST 路径；固定指向 `demo-fapi.binance.com`（合约模拟盘，虚拟资金），`BINANCE_ENV` 不是 `demo` 时拒绝运行。
- `paper_ledger.py`：仓位、费用、滑点、止损、目标和盈亏记账。
- `paper_trade.py`：手动调用本地模拟账本的维护入口（不向模拟盘下单，可能与模拟盘账户不一致）。
- `run_store.py`：运行去重、中断恢复和确定性导出。

这些脚本均不得输出密钥或向 Binance 提交真实订单。
