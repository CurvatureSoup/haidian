# TASK_BOARD

| Task ID | 状态 | 层级/Agent | 任务 | 输入 | 输出 | 验收/阻断 |
|---|---|---|---|---|---|---|
| SYS-001 | DONE | orchestrator | 读取官方规则、仓库状态和两篇调研，确定最小架构 | 官方四文件、用户调研 | PROJECT_BRIEF / Agent 配置 | 未开展正式设计 |
| SYS-002 | DONE | orchestrator | 建立 AGENTS.md、.codex 配置和 SSOT | 当前 Codex 正式 schema | 项目配置文件 | TOML/CSV/Markdown 已解析 |
| UPSTREAM-SYNC | DONE | orchestrator | 合并并发布当前规则基线 | 官方 `main@9051ca77` | 远端合并提交 `a59a6fd` | GitHub 远端架构分支已包含规则基线 |
| G0-RULE-FREEZE-HISTORICAL | DONE | orchestrator | 历史 G0 冻结 | upstream/main `d28c1400` | 历史五个 SSOT | 仅保留审计；已被当前规则基线取代 |
| G0-RULE-REFRESH | DONE | orchestrator | 复核 `d28c1400..9051ca77` 的 10 个非投稿路径并回写受影响工作 | 最新上游规则变化 | Agent 职责、五个 SSOT、smoke summary、安装 Skill | 来源治理、模型披露、仿真/符号链接及边界不确定性均已处理；未启动设计 |
| LOCAL-REMOTE-SYNC | BLOCKED | librarian | 将本地对象库快进到远端架构分支 | `origin/codex/agent-architecture` | 本地 Git 历史 | `github.com:443` 当前不可达；恢复后执行 fetch/fast-forward |
| SMOKE-L1 | DONE | librarian | 微型机械去重与字段规范化 | smoke README 固定样例 | `project_control/smoke/librarian_result.json` | 产物与行为 PASS；模型遥测 NOT OBSERVABLE |
| SMOKE-L2 | DONE | researcher | 微型本地资料比较 | public brief 与 taskbook 的指定片段 | `project_control/smoke/researcher_result.md` | 产物与行为 PASS；模型遥测 NOT OBSERVABLE |
| SMOKE-L3 | DONE | evidence_planner | 微型证据边界判断 | Skill 与 formal guide 的 provisional 规则 | `project_control/smoke/evidence_planner_result.md` | 原始产物保留；9051ca77 后置复核确认结论仍有效；模型遥测 NOT OBSERVABLE |
| SMOKE-ORCH | DONE | orchestrator | 读取三项结果并汇总路由状态 | 三个 smoke 输出与规则后置复核 | `project_control/smoke/orchestrator_summary.md` | 行为交接 PASS；配置 CONFIG_VALIDATED；实际模型 NOT OBSERVABLE |
| ROUTE-MODEL-VERIFY | DONE | orchestrator | 核对项目级 Agent 配置与运行边界 | 当前配置与 smoke 结果 | CONFIG_VALIDATED | 配置优先级和行为通过；平台未提供独立运行时模型遥测 |
| G1-DATA-BASELINE | BLOCKED | orchestrator | 建立资料、空间与现状诊断基线 | 当前 G0 结论与后续人类授权 | 未启动 | 本地 Git 未同步；且缺官方精确 polygon、控规条件和专业底数 |
| DESIGN-START | BLOCKED | orchestrator | 正式城市规划与 Baseline Freeze | 后续单独授权 | 未启动 | 当前明确禁止 |
