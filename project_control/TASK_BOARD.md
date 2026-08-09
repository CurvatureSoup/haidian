# TASK_BOARD

| Task ID | 状态 | 层级/Agent | 任务 | 输入 | 输出 | 验收/阻断 |
|---|---|---|---|---|---|---|
| SYS-001 | DONE | orchestrator | 读取官方规则、仓库状态和两篇调研，确定最小架构 | 官方四文件、用户调研 | PROJECT_BRIEF / Agent 配置 | 未开展正式设计 |
| SYS-002 | DONE | orchestrator | 建立 AGENTS.md、.codex 配置和 SSOT | 当前 Codex 正式 schema | 项目配置文件 | TOML/CSV/Markdown 已解析 |
| UPSTREAM-SYNC | DONE | orchestrator | 合并并发布操作时核实的最新上游历史 | 官方 `main@9051ca77` | 远端合并提交 `a59a6fd` | GitHub 远端架构分支已包含上游；本地 fetch 因 443 网络故障待补 |
| G0-RULE-FREEZE | DONE | orchestrator | 冻结 Skill、任务书、数据规则、Schema、关键脚本与用途边界 | upstream/main `d28c1400` | 五个 SSOT | 总控复核 PASS；规则树一致；缺口和限制已登记；未启动设计 |
| G0-RULE-REFRESH | BLOCKED | orchestrator | 复核 `d28c1400..9051ca77` 的 10 个非投稿路径并建立新冻结基线 | 最新上游规则变化 | 待更新五个 SSOT | 当前仅完成合并；未授权扩展研究，且本地 Git 对象待补拉 |
| SMOKE-L1 | DONE | librarian | 微型机械去重与字段规范化 | smoke README 固定样例 | `project_control/smoke/librarian_result.json` | 产物与行为 PASS；模型遥测 NOT OBSERVABLE |
| SMOKE-L2 | DONE | researcher | 微型本地资料比较 | public brief 与 taskbook 的指定片段 | `project_control/smoke/researcher_result.md` | 产物与行为 PASS；模型遥测 NOT OBSERVABLE |
| SMOKE-L3 | DONE | evidence_planner | 微型证据边界判断 | Skill 与 formal guide 的 provisional 规则 | `project_control/smoke/evidence_planner_result.md` | 产物与行为 PASS；模型遥测 NOT OBSERVABLE |
| SMOKE-ORCH | DONE | orchestrator | 读取三项结果并汇总路由状态 | 三个 smoke 输出 | `project_control/smoke/orchestrator_summary.md` | 文件交接 PASS；模型遥测 NOT OBSERVABLE |
| ROUTE-MODEL-VERIFY | DONE | orchestrator | 核对项目级 Agent 配置与运行边界 | 当前配置与 smoke 结果 | CONFIG_VALIDATED | 配置优先级和行为通过；平台未提供独立运行时模型遥测 |
| G1-DATA-BASELINE | BLOCKED | orchestrator | 建立资料、空间与现状诊断基线 | 最新 G0 结论与后续人类授权 | 未启动 | 新 G0 尚未复核；且缺官方精确 polygon、控规条件和专业底数 |
| DESIGN-START | BLOCKED | orchestrator | 正式城市规划与 Baseline Freeze | 后续单独授权 | 未启动 | 当前明确禁止 |
