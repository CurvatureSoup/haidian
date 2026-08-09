# PROJECT_BRIEF

## 当前目标

维护多 Agent 架构并跟随官方规则。G0 曾冻结到 `d28c1400`；架构分支现已合并更新的官方 `main`，因此必须先复核变化后的规则路径，才能建立新的冻结基线。当前仍不开展正式城市设计、不生成投稿方案、不进行大规模数据下载。

## 项目与仓库

- 官方仓库：`open-city-ai/haidian`
- 工作 fork：`CurvatureSoup/haidian`
- Agent 架构分支：`codex/agent-architecture`
- 历史 G0 冻结基线：官方 `main` commit `d28c14002a77d19221888ffe8ac447876aca3165`
- 最新上游快照：官方 `main` commit `9051ca77fe1a15657bc3abf0513c402561afae0f`
- 同步状态：GitHub 远端 `codex/agent-architecture` 已通过合并提交 `a59a6fd37a766ef675cb182cc0ea5326e638f157` 包含该上游快照
- 规则状态：相对历史 G0 有 10 个非 `submissions/` 路径发生变化，新的 G0 尚未复核冻结
- 本机 Skill：仅确认与历史 G0 提交一致；与最新上游快照的一致性待复核
- 正式规则入口：`skills/urban-design-ai-submission/SKILL.md`

## 第一批 Agent

| Agent | 层级 | 模型 | Reasoning | 当前用途 |
|---|---|---|---|---|
| orchestrator | 总控 | gpt-5.6-sol | max | 拆解、路由、裁决、冻结、综合 |
| evidence_planner | L3 | gpt-5.6-sol | high | 规划证据与约束判断 |
| gis_analyst | L3 | gpt-5.6-sol | high | GIS 与空间推理 |
| researcher | L2 | gpt-5.6-terra | medium | 检索、阅读、比较、普通分析 |
| librarian | L1 | gpt-5.6-luna | low | 归档、字段、去重、索引 |
| qa_worker | L1 | gpt-5.6-luna | low | 格式和确定性检查 |

## 工作原则

- 使用足够完成任务的最低成本 Agent。
- 所有事实与项目状态只在 `project_control/` 维护。
- 用户提供的工作原则 `AI-Ready, AI-Optional` 作为后续待总控冻结的项目方法，不是官方事实。
- 未来正式投稿必须遵守官方 package、证据、几何、版权与 PR 范围要求。
- 新投稿采用 `proposal_format_version="2"` 与 `bilingual_contract_version="1"`，中英文及所有文字型交付物必须成对一致。
- 临时边界不阻断内容评分，但不得作为官方红线、精确面积、法定判断或正式专业评分依据。

## G0 冻结条件

1. 当前分支与安装 Skill 指向同一官方提交。
2. 必读规则、9 个 JSON Schema、数据准入规则和关键验证脚本均有固定 Git blob 基线。
3. 已知资料缺口、用途边界和计分口径写入 SSOT。
4. 总控确认 G0 是否可冻结以及后续仍被阻断的阶段。
5. 没有启动正式城市规划工作。

## 当前验证结论

- 历史 G0 规则树在 `d28c1400` 的复核结论仍作为审计记录保留，但不代表最新上游状态。
- 最新上游已修改 formal guide、Skill 参考、Schema、数据工作流和校验脚本等非投稿路径；新 G0 状态为 `BLOCKED`，等待独立规则复核。
- 六个 Agent 配置可解析，微型任务的行为边界与文件交接通过；运行时模型遥测为 `NOT OBSERVABLE`，不得冒充实际模型证据，但不再阻断 G0。
- 官方精确范围 polygon、项目控规指标、现状专业底数和一份需官方文件补齐的设计深度标准仍缺失。
- `DESIGN-START` 与 G1 资料/空间基线阶段仍保持 `BLOCKED`，需要人类另行授权。
