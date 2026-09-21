# 复盘流程与保存文案

复盘是本实验改进的方式。每天 Asia/Kuala_Lumpur 时间 22:00 由独立的定时任务（`paper-trading-daily-review`）运行一次，位于 20:00 与 00:00 两次交易检查之间。复盘从不交易。英文版 [REVIEW-PROMPT.md](REVIEW-PROMPT.md) 内容相同；如有差异，以英文版为准。

## 任务文案

所有操作仅在项目目录进行。绝不运行 `paper_engine.py`、`paper_trade.py` 或任何下单、账户调用；绝不编辑脚本、测试、`readiness.json`、`paper-config.json`、`current-state.json`、账本、日程或密钥文件。复盘只在 `05-交易记录-data/reviews/` 内写入，并通过 Obsidian 连接器写入第 7 步指定的库文件夹。

1. 运行 `python3 -B 06-程序脚本-scripts/review_stats.py`。它根据账本重建 `reviews/stats.json`：时点覆盖率（应运行的检查与已记录决策的检查，以及错过了哪些）、已平仓交易、胜率、平均 R（结果除以开仓时的计划亏损）、回撤、手续费、资金费，以及按合约、方向、平仓原因和证据类别的同类统计。直接使用这些数字，不要手工重算。
2. 读取当天的 journal、decision 和 evidence 文件，`reviews/LESSONS.md`、`reviews/PROPOSALS.md` 和上一份每日复盘。
3. 写入 `reviews/YYYY-MM-DD.md`（本地日期），包含以下部分：
   - **数字** — 当天和实验至今，来自 `stats.json`，必须包含时点覆盖率。
   - **决策复盘** — 当天每一次开仓、平仓和不交易：证据是否真实且相互独立，止损是否基于价格结构，交易是否遵循原逻辑，之后发生了什么。按当时可知的信息评判决策，而不是按结果。
   - **流程错误** — 违反规则、引擎拒绝、错过或失败的检查、过期数据、草率的证据。这些比盈亏更重要。
   - **有效 / 无效** — 每一点都对应具体交易。
   - **假设** — 值得观察的规律，并注明样本量。
4. 更新 `reviews/LESSONS.md`：最多 10 条经验，每条注明证据和样本量，最有用的排在最前。只有至少 3 笔交易或 5 次决策支持时才添加；数据不再支持的经验要删除。经验只能让以后的决策更严格（放弃某种形态、要求多一类证据、避开某个时段），绝不能放宽任何规则或风险限制。已平仓交易少于 30 笔时，经验以假设的形式表述。
5. 如果证据表明应修改规则、限制、观察列表、日程或代码，把建议追加到 `reviews/PROPOSALS.md` 供 Edward 决定。绝不自行实施。
6. 在实验第 7、14、21、28 天另写 `reviews/weekly-N.md`：本周数字与此前各周的对比，哪些经验被执行以及执行是否有帮助，哪些建议仍待决定，并如实说明目前是否看得出优势，还是结果与随机无法区分。最后一个计划日期之后，以同样形式为整个实验写 `reviews/final.md`。
7. 发布到 Obsidian，方便 Edward 在那里阅读经验。只使用 Obsidian 连接器工具（`obsidian_create_note`、`obsidian_read_note`、`obsidian_edit_note`），库为 `obsidian-vault`，文件夹为 `Trading/Futures Paper Trading Experiment/`：
   - 创建 `Daily Reviews/YYYY-MM-DD.md`，内容为完整的每日复盘，front matter 为 `tags: [trading, trading/review]`，第一行链接回：`[[Home]] · [[Lessons]] · [[Review Log]]`。如果笔记已存在，则替换其内容。
   - 用当前的 `LESSONS.md` 和 `PROPOSALS.md` 替换 `Lessons.md` 和 `Proposals.md` 的正文，保留各笔记的 front matter、标题和 “Mirror of ...” 一行。
   - 在 `Review Log.md` 的表格中追加一行：日期、实验第几天、当天交易数、累计交易数、累计净盈亏、胜率、平均 R、一句话的关键发现，以及链接 `[[Daily Reviews/YYYY-MM-DD]]`。同一日期不要出现第二行；如已存在则替换。
   - 每周和最终复盘写入 `Weekly Reviews/weekly-N.md` 和 `Weekly Reviews/final.md`。
   - 仓库文件始终是唯一依据；绝不从 Obsidian 读回经验。如果 Obsidian 工具不可用或失败，照常完成复盘并在报告中说明；绝不以其他方式写入库。
8. 最后给 Edward 一份简短报告：当天数字、最重要的一两个发现、新增经验，以及等待他决定的新建议。

## 边界

复盘改变的是 AI 决策的谨慎程度，而不是它被允许做什么。风险限制、杠杆、观察列表、日程和代码只有在 Edward 批准建议后才会修改。小样本不能证明任何事：盈利的一周不代表系统盈利，复盘必须如实说明。
