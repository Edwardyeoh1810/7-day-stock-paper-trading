# 7 天股票交易实验

项目唯一工作目录：`/Users/a123/Desktop/7天股票交易实验`。

这是使用币安股票 API 的研究与模拟实验。币安股票接口只读连接已经验证，实验使用 10000 USDT 本地 paper trading 账本。真实交易始终关闭；当前自动运行器只能检查和记录，还没有完整的自主模拟成交与盈亏更新能力。

## 从这里阅读

| 你要了解什么 | 打开文件 |
| --- | --- |
| 全部决定、当前进度、下一步 | [项目交接说明](docs/PROJECT-HANDOFF.zh-CN.md) |
| 2026-09-15 GitHub Actions 与安全修改 | [本次修改记录](docs/2026-09-15修改记录.md) |
| GitHub Actions 部署与密钥填写 | [云端运行说明](docs/GITHUB-ACTIONS-RUNBOOK.zh-CN.md) |
| 配置 API 和运行检查 | [开始使用](开始使用.md) |
| 币安股票接口与认证排查 | [币安接口说明](docs/BINANCE-API.zh-CN.md) |
| 审阅止损与模拟成交规则 | [止损成交草案 v0.1](docs/STOP-AND-FILL-DRAFT.zh-CN.md) |
| 原有交易策略与额度 | [策略](docs/TRADING-STRATEGY.zh-CN.md) |
| AI 每次运行应遵守的规则 | [运行规则](AGENTS.zh-CN.md) |
| 日程、恢复与定时任务说明 | [连续性协议](routines/CONTINUITY.zh-CN.md)、[定时任务说明](routines/AUTOMATION-PROMPT.zh-CN.md) |
| 测试结果和验收边界 | [验证记录](data/evidence/2026-09-14-validation.md) |
| 最初发现的问题及后续处理 | [项目审阅](docs/项目审阅.md) |
| English overview | [README English](README.en.md) |

## 状态快照

更新于 2026-09-15。本表来自 `state/readiness.json`、`data/current-state.json` 和自动测试结果。

| 项目 | 状态 |
| --- | --- |
| 独立本地凭证文件 | 已配置；实际内容只保存在 binance-api.env |
| 币安公共接口 | 最近一次检查通过 |
| 真实账户与股票 API | 只读验证成功；账户、股票规则、AAPL 报价、股票未完成订单与权限均可读取 |
| 只读检查与 SQLite 运行记录 | 已实现并做过端到端演练 |
| 自动测试 | 16 项通过；42 个日程槽位验证通过 |
| 研究日程 | 2026-09-15 至 2026-09-23 的七个交易日，每天六次 Central 检查 |
| GitHub Actions | 已上传至私有仓库并完成首次手动触发；GitHub 托管 Runner 访问 Binance 返回 HTTP 451 |
| GitHub 仓库 | `yomislight/7-day-stock-paper-trading`，私有仓库 |
| 止损成交规则 | v0.1 草案，尚未批准 |
| 模拟成交引擎、持续风险监控 | 尚未实现 |
| 实盘下单 | 未实现、未启用、未下单 |
| 本地模拟资金 | 初始及当前现金 10000 USDT，空仓 |

后续实际状态以 [readiness](state/readiness.json)、[current-state](data/current-state.json)、[自动任务状态](routines/automation-status.json) 和最新证据为准。

## 文件如何组织

```text
7天股票交易实验/
  README.md / README.en.md       项目首页
  开始使用.md                    本地操作步骤
  AGENTS.md / AGENTS.zh-CN.md    中英文运行规则
  binance-api.env               真实本地凭证，不分享
  binance-api.env.example       空白分享模板
  docs/                        接口、策略、草案、审阅和交接说明
  .github/workflows/           GitHub Actions 定时只读检查工作流
  routines/                    日程、连续性协议、自动任务说明与状态
  scripts/                     币安只读检查、运行器、SQLite 记录
  tests/                       接口与运行机制测试
  state/                       readiness 和运行锁
  data/                        组合状态、SQLite、日志、证据
  AI Trading with Codex and GPT 6 Astra.pdf  原始参考材料
```

已有文件路径保持不变，方便脚本和日程继续使用。原 PDF 是 Alpaca 示例，不是当前币安实现的运行指令；当前币安版内容以接口说明为准。

只维护本桌面目录。早先误放到 Documents 项目的启动日期和记录没有合并，避免把另一个目录的记录误当成此实验的真实进度。

分享时使用空白凭证模板，不复制真实 env、编辑器交换文件或备份。GitHub 密钥只能填写在仓库 Actions Secrets 中；不要写入工作流、文档或聊天。当前三个 Binance Secrets 已通过 GitHub CLI 安全设置，仓库文件中仍没有密钥值。Git 忽略规则不会自动过滤 Finder 复制或压缩包。
