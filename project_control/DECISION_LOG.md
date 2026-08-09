# DECISION_LOG

| Decision ID | 日期 | 决定 | 理由/证据 | 被否决方案 | 状态 | Owner |
|---|---|---|---|---|---|---|
| D-001 | 2026-08-09 | Agent 架构在 `codex/agent-architecture` 独立分支维护。 | 官方投稿 PR 只能修改本人 submissions 目录。 | 直接把根配置混入正式投稿分支。 | FROZEN | human + orchestrator |
| D-002 | 2026-08-09 | 第一批只建立六个 Agent，不一次创建调研中的全部专业角色。 | 用户明确的第一批范围；降低上下文、成本和返工。 | 初始化时创建 18—20 个 Agent。 | FROZEN | human + orchestrator |
| D-003 | 2026-08-09 | 使用 Luna low / Terra medium / Sol high / Sol max 四档，并默认最低成本路由。 | 用户路由要求和当前 Codex 模型分层。 | 所有任务默认 Sol。 | FROZEN | human + orchestrator |
| D-004 | 2026-08-09 | `project_control/` 是唯一事实与状态源。 | 两篇调研均要求结构化共享状态，避免聊天记忆漂移。 | 各 Agent 各存一套事实。 | FROZEN | orchestrator |
| D-005 | 2026-08-09 | 当前只做系统初始化和 smoke test。 | 用户明确禁止开始城市设计和重复研究。 | 借测试提前开展城市诊断。 | FROZEN | human |
| D-006 | 2026-08-09 | 两篇调研只作为方法输入登记，调研中的外部事实仍需按正式证据流程核验。 | 调研不是官方任务书，且包含需复核的时效性主张。 | 直接把调研全文当作已确认事实。 | FROZEN | evidence_planner |
| D-007 | 2026-08-09 | 本轮只判定角色行为和文件交接通过，不判定三级模型路由通过。 | 当前子线程没有暴露可独立核实的模型元数据；四个结果均记录 UNVERIFIED。 | 用配置文件中的模型名冒充实际运行模型。 | FROZEN | orchestrator |
| D-008 | 2026-08-09 | G0 规则基线冻结为 `upstream/main@d28c14002a77d19221888ffe8ac447876aca3165`。 | 本地 HEAD、安装 Skill 与官方规则树已核对；旧基线后的 487 个变化全部属于 submissions。 | 在旧提交上继续推进或为同步投稿内容完整下载全部媒体。 | FROZEN | human + orchestrator |
| D-009 | 2026-08-09 | 新投稿从一开始采用 proposal v2 与 bilingual contract v1。 | 最新 Skill、formal guide、模板和验证脚本共同定义双语阻断门。 | 先做单语正文后在末期补翻译。 | FROZEN | orchestrator |
| D-010 | 2026-08-09 | 临时边界可支撑内容生成、展示和 intake，但不能支撑正式专业评分、精确面积或法定结论。 | Skill、formal guide、source registry 与 allowed design space 的适用范围一致。 | 把“内容评分不阻断”解释为临时边界可替代官方红线。 | FROZEN | evidence_planner + gis_analyst |
| D-011 | 2026-08-09 | Agent 配置与行为验收记为 `CONFIG_VALIDATED`，运行时模型审计记为 `NOT OBSERVABLE`，不再阻断 G0。 | 项目配置已加载并完成角色任务；Codex 当前未提供独立模型遥测。 | 声称已取得实际模型证明，或无限重复同一 smoke test。 | FROZEN | orchestrator + qa_worker |
| D-012 | 2026-08-09 | G0 完成不自动解除 G1 和 `DESIGN-START`。 | 官方精确 polygon、控规条件、现状专业底数和部分标准文件仍缺失；用户只授权 G0。 | 借规则冻结直接开始城市诊断或方案生产。 | FROZEN | human + orchestrator |
