# 百年京张 AI 创新带：项目级 Agent 协作规则

## 当前阶段

- 当前只搭建、验证多 Agent 系统，不开展正式城市设计，不生成正式方案，不批量下载数据。
- 进入任何规划生产前，必须由总控在 `project_control/DECISION_LOG.md` 记录阶段冻结决定。
- 两篇用户提供的深度调研是工作方法输入，不自动等同于官方事实或正式证据。

## 唯一事实源（SSOT）

所有 Agent 开始工作前只读取与任务有关的仓库文件，并优先读取：

1. `project_control/PROJECT_BRIEF.md`
2. `project_control/FACTS_ASSUMPTIONS.md`
3. `project_control/DATA_REGISTRY.csv`
4. `project_control/TASK_BOARD.md`
5. `project_control/DECISION_LOG.md`

禁止在个人笔记或聊天中建立另一套互相冲突的项目事实。新信息必须标记为 `CONFIRMED`、`ASSUMPTION`、`MISSING` 或 `CONFLICT`；没有来源的信息不得升级为 `CONFIRMED`。不要把完整背景反复复制给子 Agent，只传任务 ID、必要输入路径、输出路径和验收标准。

## 最低成本路由

- `librarian` / `qa_worker`（L1 Luna）：明确、机械、重复、可按固定规则验证的任务。
- `researcher`（L2 Terra）：资料检索、批量阅读、案例比较、摘要和普通分析。
- `evidence_planner` / `gis_analyst`（L3 Sol）：规划证据判断、多约束推理、GIS 与空间决策。
- `orchestrator`（Sol Max）：总体战略、任务拆解、跨专业冲突、重大阶段冻结和最终综合。

默认选择足够完成任务的最低层级。低层 Agent 一旦发现任务需要专业判断、空间推理、规则裁决或外部授权，必须停止猜测，输出 `ESCALATE`，说明已完成部分、问题、证据和建议接收 Agent，不得自行扩大范围。

## 统一工作流

1. 总控在 `TASK_BOARD.md` 建立边界清晰的任务，写明 Agent、输入、输出和验收标准。
2. 执行 Agent 只处理分配范围；输出优先写入指定文件，消息只返回结论摘要和文件路径。
3. 事实、来源、假设或冲突分别回写 SSOT；不得悄悄改写其他 Agent 的专业结论。
4. 总控读取结构化成果，裁决冲突并记录 `DECISION_LOG.md`；重大结论未经记录不得视为冻结。
5. 确定性检查由 `qa_worker` 执行；专业判断不能用格式检查代替。

统一交接至少包含：`task_id`、`status`、`producer_agent`、`summary`、`source_ids`、`assumption_ids`、`blockers`、`output_paths`、`escalation_target`。

## 证据与规划边界

- 优先使用官方、第一手、已清权资料；记录发布者、URL/路径、日期、许可、尺度、处理方法和限制。
- `provisional` 几何不得称为官方红线，不得据此给出法定指标、工程线位、权属或投资承诺。
- 不得使用秘密资料、非公开规划图件、个人隐私数据或未清权素材。
- 当前不得把概念建议写成政府决定、已批准工程或已确认实施安排。
- 正式投稿相关约束以最新 `skills/urban-design-ai-submission/SKILL.md`、`brief/` 和 `docs/formal-submission-guide.md` 为准。

## 权限与 Git 边界

- 专业和研究 Agent 默认不执行 push、merge、PR、Issue、外部发布或账号设置变更。
- 涉及 GitHub 写入、对外沟通、采购、付费服务、受限数据或账号授权时，升级给总控和人类项目负责人。
- Agent 架构在 `codex/agent-architecture` 分支维护；未来正式投稿分支必须从最新官方 `main` 创建，并确保 PR 只修改 `submissions/<login>/<slug>/`。
- 保留现有有效配置和用户修改；禁止破坏性 Git 操作。

## 当前 smoke test

系统初始化完成后，只执行 `project_control/smoke/README.md` 中三个微型任务。不得借 smoke test 开展正式研究、城市诊断或方案设计。总控必须汇总实际调度结果；如果模型没有按配置运行，记录真实限制，不得声称通过。
