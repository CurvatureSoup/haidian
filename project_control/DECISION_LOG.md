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
| D-013 | 2026-08-09 | 将官方 `main@9051ca77` 合并到远端 Agent 架构分支并复核 10 个非投稿变化路径。 | 用户授权合并、推送和修正受影响成果。 | 继续把 `d28c1400` 冒充当前规则状态，或借同步启动城市设计。 | FROZEN | human + orchestrator |
| D-014 | 2026-08-09 | 当前规则基线更新为 `9051ca77`；`d28c1400` 降格为历史审计基线。 | 来源治理、Schema、校验脚本和边界依据发生实质变化；安装 Skill 已同步校验。 | 删除历史记录，或在未复核时声称新规则已冻结。 | FROZEN | orchestrator + qa_worker |
| D-015 | 2026-08-09 | 中央 registry 与投稿包来源分开治理；OSM 背景核对不改变 provisional 的法律或精度等级。 | data workflow、formal guide、provisional basis 与 Issue #846。 | 强制把全部自采源写中央表，或把 OSM/provisional 任一方升级成官方边界。 | FROZEN | evidence_planner + gis_analyst |
| D-016 | 2026-08-09 | 投稿包 `model_family` / `model_detail` 只作为参赛者机器可读声明，不改写 Codex Agent TOML，也不充当实际运行模型证据。 | manifest schema、scaffold、validator 与 smoke 遥测限制。 | 用投稿声明字段冒充运行时模型审计。 | FROZEN | orchestrator + qa_worker |
| D-017 | 2026-08-09 | D-011 仅解除模型遥测对项目 G0 Gate 的阻断，不推翻 D-007“三级实际模型路由未验证”的结论。 | 配置与行为可验收，平台遥测仍不可观察。 | 把 `CONFIG_VALIDATED` 写成实际 Luna/Terra/Sol 已获证明。 | FROZEN | orchestrator |
| D-018 | 2026-08-10 | 本地 Agent 架构分支完成安全快进；最新官方校验点为 `main@1a40a99d`，当前规则基线继续保持 `9051ca77`。 | 本地与远端 HEAD 已核对；`9051ca77..1a40a99d` 顶层 Git tree 唯一变化为 `submissions/`。 | 为追逐其他投稿提交而改写规则基线、重跑 smoke 或批量物化投稿媒体。 | FROZEN | human + orchestrator |
| D-019 | 2026-08-10 | 完成同步与校验点登记后暂不进入 G1，`DESIGN-START` 继续保持阻断。 | 用户明确授权只执行本地同步与规则校验点更新，并明确暂不进入 G1。 | 把 Git 同步完成解释为资料研究或规划生产授权。 | FROZEN | human + orchestrator |
| D-020 | 2026-08-10 | 启动 G1 资料、空间与现状数据基线，同时继续执行轻量规则监控、不复跑 smoke、不合并纯投稿更新，并保持 `DESIGN-START` 阻断。 | 用户明确授权执行原清单 1、2、3、5 并启动 G1。 | 把 G1 授权解释为城市设计、正式指标计算或投稿生产授权。 | FROZEN | human + orchestrator |
| D-021 | 2026-08-10 | G1 遇到会改变范围、数据口径或后续方向的关键决策时，先安全保存并停止，未经人类选择不得继续。 | 用户要求关键性方向决策立即停止等待；未决时安全保存。 | 总控自行选择 provisional 空间工作范围或扩大采集。 | FROZEN | human + orchestrator |
| D-022 | 2026-08-12 | 总叙事冻结为 `AI-native, not AI-dependent`；`AI-Ready, AI-Optional` 为工程约束，人类权利与最终决定权优先。 | 用户实施计划。 | 让城市依赖某一代 AI，或赋予 AI 法律人格和优先城市权利。 | FROZEN | human + orchestrator |
| D-023 | 2026-08-12 | 采用“AI需求反推、由人治理的设施重构”，先判 retain/adapt/reconstruct；全集 8 类、首批 6 类，并设物理使用者与 anti-sticker 门。 | 用户实施计划与同行差异审计。 | 为追求高 ATS 制造无必要土建，或把外挂传感器称为 AI-native。 | FROZEN | human + orchestrator |
| D-024 | 2026-08-12 | ATS 采用 P/F/I/U 四项 0–5、总分 `5×sum`，High 暂定 ≥70 且 P≥2、U≥3。 | 用户实施计划。 | 把 ATS 冒充官方分数或用单一设备数量代替转型程度。 | FROZEN | human + orchestrator |
| D-025 | 2026-08-12 | R-Score 采用六分项权重、High 暂定 ≥80；关键设施 AI-Off 基础服务保持率 ≥100%，ATS 与 R 不相加。 | 用户实施计划。 | 用专用资产比例单项决定可逆性，或将双轴压成总分。 | FROZEN | human + orchestrator |
| D-026 | 2026-08-12 | 每设施必须有三态故障合同、Second Life，并在 Boom/Fragmentation/Retreat 三未来下全 PASS 才可 High–High。 | 用户实施计划。 | 只写人工接管口号或单一未来叙述。 | FROZEN | human + orchestrator |
| D-027 | 2026-08-12 | 当前只改方法、六 Agent 与合成测试；不新增设计 Agent、研究或真实方案，不解除 `G1-DIR-001` 和 `DESIGN-START`。 | 用户实施计划与现有 Gate。 | 借方法实施提前生产设施、坐标、造价或图件。 | FROZEN | human + orchestrator |
| D-028 | 2026-08-13 | `G1-DIR-001` 选择 C 双轨策略：官方待定轨与发现试跑轨并行，provisional 结果不进入正式基线，官方数据到位后整体复算。 | 人类明确选择 C；Issue #846 与官方 polygon 缺失仍在。 | A 完全等待官方边界；B 直接以 provisional 推进空间基线。 | FROZEN | human + orchestrator |
| D-029 | 2026-08-13 | 最新官方 main 合入架构分支；`completeness_limited_by` 仅用于披露正式深度受官方缺数限制，不改变 complete 门或证据等级。 | `905b8be6..61306151` 规则差异及 `main@464aead8` 同步审计。 | 用该字段掩盖 incomplete/data_gap，或因纯投稿更新改写项目方法。 | FROZEN | orchestrator + qa_worker |
| D-030 | 2026-08-13 | 无凭证公开来源发现可执行；外部联系、注册登录、机构/个人信息提交和受限附件请求设为 `G1-EXT-ACCESS-001` 人类门。 | 双轨协议与来源采集矩阵显示 P0 缺口需组织方或主管部门附件。 | 总控擅自发邮件、Issue、注册账号或接受未知许可。 | FROZEN | human + orchestrator |
