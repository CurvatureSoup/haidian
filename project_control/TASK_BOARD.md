# TASK_BOARD

| Task ID | 状态 | 层级/Agent | 任务 | 输入 | 输出 | 验收/阻断 |
|---|---|---|---|---|---|---|
| SYS-001 | DONE | orchestrator | 读取官方规则、仓库状态和两篇调研，确定最小架构 | 官方四文件、用户调研 | PROJECT_BRIEF / Agent 配置 | 未开展正式设计 |
| SYS-002 | DONE | orchestrator | 建立 AGENTS.md、.codex 配置和 SSOT | 当前 Codex 正式 schema | 项目配置文件 | TOML/CSV/Markdown 已解析 |
| UPSTREAM-SYNC | DONE | orchestrator | 合并并发布当前规则基线 | 官方 `main@9051ca77` | 远端合并提交 `a59a6fd` | GitHub 远端架构分支已包含规则基线 |
| G0-RULE-FREEZE-HISTORICAL | DONE | orchestrator | 历史 G0 冻结 | upstream/main `d28c1400` | 历史五个 SSOT | 仅保留审计；已被当前规则基线取代 |
| G0-RULE-REFRESH | DONE | orchestrator | 复核 `d28c1400..9051ca77` 的 10 个非投稿路径并回写受影响工作 | 最新上游规则变化 | Agent 职责、五个 SSOT、smoke summary、安装 Skill | 来源治理、模型披露、仿真/符号链接及边界不确定性均已处理；未启动设计 |
| LOCAL-REMOTE-SYNC | DONE | orchestrator | 将本地对象库快进到远端架构分支 | `origin/codex/agent-architecture@de301b91` | 本地 HEAD `de301b91` | blobless sparse fetch 与 ff-only 完成；工作树干净且本地/远端 SHA 一致 |
| RULE-MONITOR | DONE | orchestrator | 轻量核对最新官方 main 是否改变当前规则树 | `upstream/main@c4765c8b` 与 `9051ca77` 顶层 Git tree | PROJECT_BRIEF / FACTS_ASSUMPTIONS | 唯一变化为 `submissions/`；不合并纯投稿更新，规则基线保持 `9051ca77` |
| SMOKE-L1 | DONE | librarian | 微型机械去重与字段规范化 | smoke README 固定样例 | `project_control/smoke/librarian_result.json` | 产物与行为 PASS；模型遥测 NOT OBSERVABLE |
| SMOKE-L2 | DONE | researcher | 微型本地资料比较 | public brief 与 taskbook 的指定片段 | `project_control/smoke/researcher_result.md` | 产物与行为 PASS；模型遥测 NOT OBSERVABLE |
| SMOKE-L3 | DONE | evidence_planner | 微型证据边界判断 | Skill 与 formal guide 的 provisional 规则 | `project_control/smoke/evidence_planner_result.md` | 原始产物保留；9051ca77 后置复核确认结论仍有效；模型遥测 NOT OBSERVABLE |
| SMOKE-ORCH | DONE | orchestrator | 读取三项结果并汇总路由状态 | 三个 smoke 输出与规则后置复核 | `project_control/smoke/orchestrator_summary.md` | 行为交接 PASS；配置 CONFIG_VALIDATED；实际模型 NOT OBSERVABLE |
| ROUTE-MODEL-VERIFY | DONE | orchestrator | 核对项目级 Agent 配置与运行边界 | 当前配置与 smoke 结果 | CONFIG_VALIDATED | 配置优先级和行为通过；平台未提供独立运行时模型遥测 |
| G1-INTERNAL-INVENTORY | DONE | orchestrator | 盘点仓库内来源、面积、临时几何、标准和资料缺口 | source registry / site package / processed fact pack / Issue #846 | `project_control/G1_DATA_BASELINE.md` | 6 条中央来源、6 个公告面积、6 个 provisional 要素、9 类缺口已登记；未开展外部采集或设计 |
| G1-DIR-001 | WAITING_HUMAN | human + orchestrator | 决定 G1 空间数据工作范围策略 | provisional 边界限制 / Issue #846 / 官方 polygon 缺失 | 待人类选择 A、B 或 C | 该选择会改变采集范围、返工量和空间口径；未决前停止空间提取 |
| G1-DATA-BASELINE | PAUSED | orchestrator | 建立资料、空间与现状数据基线 | 用户授权 / G1 内部盘点 | `project_control/G1_DATA_BASELINE.md` | 已安全保存；等待 `G1-DIR-001`，不自动进入外部采集或设计 |
| DESIGN-START | BLOCKED | orchestrator | 正式城市规划与 Baseline Freeze | 后续单独授权 | 未启动 | 当前明确禁止 |
| UPSTREAM-SYNC-20260812 | DONE | orchestrator | 合并并发布官方规则 | `upstream/main@905b8be6` | remote merge `f1cecdd5`；method commit `4f1e397e` | 无语义冲突；远端 SHA 与树已核验；未启动设计 |
| AI-NATIVE-METHOD-V01 | DONE | orchestrator | 建立方法规范、Schema、模板、合成夹具和 validator | 用户冻结的 v0.1 方法 | `project_control/ai_native/` | 正例与公式重算通过；无真实设计数据 |
| AI-NATIVE-AGENT-CONTRACTS | DONE | orchestrator | 更新六个 Agent 的方法职责 | v0.1 规范 | `.codex/agents/*.toml` | 模型、effort、sandbox 保持不变 |
| AI-NATIVE-CONTRACT-SMOKE | DONE | qa_worker | 运行独立纯合成方法契约 smoke | 合成 fixture 与负例突变 | `SYNTHETIC_METHOD_CONTRACT_PASS` | 不覆盖历史 smoke、不验证运行时模型、不生成设计 |
