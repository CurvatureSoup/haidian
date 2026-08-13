# PROJECT_BRIEF

## 当前目标

启动 G1 资料、空间与现状数据基线，先完成仓库内资料盘点、缺口登记和关键数据策略决策。当前已安全暂停在 `G1-DIR-001`，等待人类选择空间数据提取范围；不开展正式城市设计、不生成投稿方案、不进行大规模数据下载。

## 项目与仓库

- 官方仓库：`open-city-ai/haidian`
- 工作 fork：`CurvatureSoup/haidian`
- Agent 架构分支：`codex/agent-architecture`
- 历史 G0 基线：官方 `main@d28c14002a77d19221888ffe8ac447876aca3165`
- 当前规则基线：官方 `main@9051ca77fe1a15657bc3abf0513c402561afae0f`
- 规则复核校验点：官方 `main@c4765c8baff68794dca212f2f57167769f809efe`；相对当前规则基线，顶层 Git tree 唯一变化为 `submissions/`
- 远端同步：`codex/agent-architecture` 已通过 `a59a6fd37a766ef675cb182cc0ea5326e638f157` 合并当前规则基线，并在 `de301b91a8e9a33701d64d7a7679f66648d23c5a` 完成规则后置复核记录
- 本机 Skill：七个文件已与当前规则基线逐一校验一致
- 本地 Git：已于 2026-08-10 使用 blobless sparse fetch 安全快进至远端 `de301b91`；工作树与远端一致，旧规则树阻断已解除
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
- 总叙事冻结为 **AI-native, not AI-dependent**；`AI-Ready, AI-Optional` 保留为工程约束。两者均为项目自定义方法，不是官方事实或评分标准。
- 本轮只实施 `project_control/ai_native/AI_NATIVE_METHOD_V0_1.md`、设施记录 Schema/validator、合成测试和六个 Agent 契约，不进入真实设计或新增研究。
- 方法覆盖 8 类设施，首轮校准道路、路缘、入口、公园、市政物流、能源/边缘节点 6 类；采用 ATS×R 双轴、三态运行、Second Life 与 Boom/Fragmentation/Retreat 压力测试。
- 未来正式投稿必须遵守官方 package、证据、几何、版权与 PR 范围要求。
- 新投稿采用 `proposal_format_version="2"` 与 `bilingual_contract_version="1"`，中英文及所有文字型交付物必须成对一致。
- 中央 `data/source_registry.json` 只管理共享和统一复核资料；投稿自采源、字体及工具链依赖写入包内 `sources.json` 或版权说明，不得擅自修改中央表。
- 未来投稿可使用成对的 `model_family` / `model_detail` 进行机器可读模型披露；它们不等于当前 Codex 子代理的运行时模型证据。
- 临时边界不阻断内容评分，但不得作为官方红线、精确面积、法定判断或正式专业评分依据。

## G0 冻结条件

1. 远端架构分支、安装 Skill 与本地工作树指向同一规则快照；后续 return pass 仍须先执行轻量更新检查。
2. 必读规则、9 个 JSON Schema、数据准入规则和关键验证脚本均有固定 Git blob 基线。
3. 已知资料缺口、用途边界和计分口径写入 SSOT。
4. 总控确认 G0 是否可冻结以及后续仍被阻断的阶段。
5. 没有启动正式城市规划工作。

## G1 启动边界

1. 只建立资料、空间、标准和现状底数基线，不生产设计方案。
2. 不复跑 smoke；不合并仅含 `submissions/` 的上游更新；不物化其他投稿媒体。
3. 中央 `data/source_registry.json` 只读，新的参赛者自采来源先进入本项目 G1 记录，申请中央登记必须另行授权并走 Issue。
4. provisional geometry 只可在用户选择工作策略后用于明确标注的临时提取、检查或讨论，不得升级为官方边界。
5. 关键方向、范围或法定口径决策必须暂停并由人类决定；当前门为 `G1-DIR-001`。

## 当前验证结论

- 2026-08-12 已将最新官方规则 `upstream/main@905b8be6ed6b9eb9e84307ef2dbf565fe96dc6f0` 合入本地架构分支，合并提交为 `b84f1ca11cb27408e36d964f449fb273a2faaa9a`；旧规则 SHA 只保留为历史记录。
- 最新 manifest 契约为 0.2：未来投稿须严格校验哈希；ready 包改动后先 refresh manifest，再重新 self-check。AI-native 矩阵未来使用既有 `evidence_data` role，不修改中央 Schema。
- AI-native v0.1 Schema、合法模板、合成 High–High 正例与负例突变均已通过独立契约测试，结果为 `SYNTHETIC_METHOD_CONTRACT_PASS`；这不代表真实方案或运行时模型验证。
- `d28c1400..9051ca77` 的 10 个非投稿路径已完成影响复核：来源登记职责、模型披露、仿真一致性、符号链接拒绝和 provisional 背景核对均已回写；gallery 自动维护与生成快照不影响 Agent 架构。
- OSM 背景核对暴露了 provisional 总体范围的不确定性，但不能证明临时范围错误，也不能把 OSM 升级为官方边界；仍等待官方 polygon 裁决。
- 六个 Agent 配置可解析，三项 smoke 原始产物结论仍有效；项目配置验收为 `CONFIG_VALIDATED`，运行时模型审计为 `NOT OBSERVABLE`，不得声称三级实际模型路由通过。
- 当前规则影响复核与本地 Git 同步均为 `PASS`；G1 仓库内盘点已启动并完成首轮清单，状态为 `PAUSED_AT_HUMAN_GATE`。
- 官方精确范围 polygon、项目控规指标、现状专业底数和一份需官方文件补齐的设计深度标准仍缺失。
- `G1-DIR-001` 等待人类选择工作空间范围策略；`DESIGN-START` 继续保持 `BLOCKED`，需要未来另行授权。
