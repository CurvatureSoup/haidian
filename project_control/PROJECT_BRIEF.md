# PROJECT_BRIEF

## 当前目标

完成 G0 规则基线冻结：把项目分支、安装 Skill、任务书、数据规则、Schema、验证脚本和 SSOT 锁定到同一官方提交。当前仍不开展正式城市设计、不生成投稿方案、不进行大规模数据下载。

## 项目与仓库

- 官方仓库：`open-city-ai/haidian`
- 工作 fork：`CurvatureSoup/haidian`
- Agent 架构分支：`codex/agent-architecture`
- G0 冻结基线：官方 `main` commit `d28c14002a77d19221888ffe8ac447876aca3165`
- 同步状态：`codex/agent-architecture` 已纯快进到该提交；相对旧基线的 487 个文件变化全部位于 `submissions/`，规则路径内容未变化
- 本机 Skill：已与上述提交的 `skills/urban-design-ai-submission/` 七个文件逐一校验一致
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

- G0 规则树已冻结到 `d28c1400`；规则与安装 Skill 一致，总控只读复核为 `PASS`，当前没有未解决的规则文本冲突。
- 六个 Agent 配置可解析，微型任务的行为边界与文件交接通过；运行时模型遥测为 `NOT OBSERVABLE`，不得冒充实际模型证据，但不再阻断 G0。
- 官方精确范围 polygon、项目控规指标、现状专业底数和一份需官方文件补齐的设计深度标准仍缺失。
- `DESIGN-START` 与 G1 资料/空间基线阶段仍保持 `BLOCKED`，需要人类另行授权。
