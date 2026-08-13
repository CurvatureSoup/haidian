# FACTS_ASSUMPTIONS

状态只允许：`CONFIRMED`、`ASSUMPTION`、`MISSING`、`CONFLICT`。

| ID | 状态 | 内容 | 来源 | 影响/处理 | Owner | 更新日期 |
|---|---|---|---|---|---|---|
| F-001 | CONFIRMED | 官方仓库为 `open-city-ai/haidian`，默认分支为 `main`。 | GitHub repository metadata | 所有规则同步以官方 main 为准。 | orchestrator | 2026-08-09 |
| F-002 | CONFIRMED | 项目级自定义 Codex Agent 使用 `.codex/agents/*.toml`，每个文件至少包含 name、description、developer_instructions。 | OpenAI Docs: Subagents | 本项目按正式 schema 建立 Agent。 | qa_worker | 2026-08-09 |
| F-003 | CONFIRMED | 正式投稿 PR 只允许修改本人 `submissions/<login>/<slug>/`。 | 最新项目 Skill / formal guide | Agent 架构使用独立分支，不能混入未来投稿 PR。 | orchestrator | 2026-08-09 |
| F-004 | CONFIRMED | 当前阶段已启动 G1 资料、空间与现状数据基线，但不开始城市设计。 | 用户任务 / D-020 | 只允许盘点、来源治理、缺口登记和经人类确认的数据基线工作；`DESIGN-START` 保持冻结。 | orchestrator | 2026-08-10 |
| A-001 | CONFIRMED | `AI-Ready, AI-Optional` 已冻结为 `AI-native, not AI-dependent` 下的工程约束。 | 用户决定 / D-022 | 这是项目方法，不是外部事实或官方规则；人类权利、停止权和最终决定权优先。 | evidence_planner | 2026-08-12 |
| A-002 | ASSUMPTION | 调研中的大规模专业 Agent 清单适合分阶段扩展，而不适合初始化时一次建立。 | 用户调研 + 当前第一批范围 | 第一阶段只保留六个 Agent。 | orchestrator | 2026-08-09 |
| F-005 | CONFIRMED | librarian、researcher、evidence_planner 和 orchestrator 均完成了指定微型任务与共享文件交接。 | `project_control/smoke/` | 角色行为与总控读取能力已验证。 | orchestrator | 2026-08-09 |
| F-006 | CONFIRMED | `d28c14002a77d19221888ffe8ac447876aca3165` 是历史 G0 审计基线，已被当前规则基线 `9051ca77fe1a15657bc3abf0513c402561afae0f` 取代。 | GitHub compare / D-014 | 仅保留历史审计，不再作为当前规则输入。 | librarian | 2026-08-09 |
| F-007 | CONFIRMED | `56ce8b49..d28c1400` 的 487 个变化全部位于 `submissions/`。 | `git diff 56ce8b49 d28c1400` | 仅描述历史区间，不能证明 `d28c1400` 之后规则未变化。 | qa_worker | 2026-08-09 |
| F-008 | CONFIRMED | 本机安装的 `urban-design-ai-submission` 七个文件与当前规则基线 `9051ca77` 的 Git blob 哈希逐一一致。 | 本机 Skill 校验 / GitHub Git trees API | 新会话使用与当前规则快照一致的 Skill。 | qa_worker | 2026-08-09 |
| F-009 | CONFIRMED | 新投稿必须采用 proposal v2 与 bilingual contract v1；中英文正文、HTML、视觉页、A3/A0 和文字型图件必须成对一致。 | 最新项目 Skill / formal guide | 未来制包必须从一开始按双语合同组织。 | orchestrator | 2026-08-09 |
| F-010 | CONFIRMED | 当前只有 provisional 三层范围与三处重点区 polygon，没有可信官方精确 polygon。 | design brief / source registry / missing-data | 可用于临时生成、展示和 intake 自检；不得用于官方红线、精确复算、法定结论或正式专业评分。 | gis_analyst | 2026-08-09 |
| F-011 | CONFIRMED | “临时边界不阻断内容评分”与“临时边界不能作为正式专业评分依据”适用于不同评价层面，不构成规则冲突。 | Skill / formal guide / allowed design space | 内容工作可在充分披露下继续；精度敏感专业结论仍保持阻断。 | evidence_planner | 2026-08-09 |
| F-012 | CONFIRMED | `data/source_registry.json@9051ca77` 是维护者中央共享登记表，登记 6 项：5 项 `usable_for_formal=yes`，1 项 provisional geometry 为 `provisional_only`；它不是投稿自采来源全量清单。 | source registry / data workflow @ 9051ca77 | 中央记录仍只能用于登记的 allowed uses；投稿实际来源另写包内 `sources.json`。 | librarian | 2026-08-09 |
| F-013 | CONFIRMED | GitHub 远端 `codex/agent-architecture` 已通过 `a59a6fd37a766ef675cb182cc0ea5326e638f157` 包含官方 `main@9051ca77`。 | GitHub commits API | Agent 架构远端已包含当前规则基线。 | orchestrator | 2026-08-09 |
| F-014 | CONFIRMED | `d28c1400..9051ca77` 有 10 个非 `submissions/` 路径变化；其中 gallery workflow 和 `submissions-data.js` 不影响 Agent 架构。 | GitHub compare / path impact review | 其余规则影响已回写 SSOT 与相关 Agent 职责。 | qa_worker | 2026-08-09 |
| F-015 | CONFIRMED | 投稿自采公开资料、案例、图像、字体和工具链依赖应记录在包内 `sources.json` 或版权说明；未进入中央表不等于自动批准或自动禁用。 | README / data workflow / formal guide @ 9051ca77 | 只有中央 approved+formal yes 或明确官方/清权附件可支撑 formal 权威结论；申请中央登记走 `[source-registry]` Issue。 | evidence_planner | 2026-08-09 |
| F-016 | CONFLICT | OSM 背景核对显示已测公园与 `PROV-SITE-001` 相交 0%、最近 412.5 m，但双方都不足以裁决官方总体范围。 | provisional boundaries basis / Issue #846 | 只登记为空间不确定性；不得把 OSM 或 provisional 任一方升级为官方边界，等待官方 polygon。 | gis_analyst | 2026-08-09 |
| F-017 | CONFIRMED | 投稿包 `manifest.json`/`agent.json` 可选使用成对的 `model_family` 和 `model_detail`；占位符或只填一项会校验失败，旧包两项均缺省仍兼容。 | manifest schema / scaffold / validator @ 9051ca77 | 这是参赛者声明字段，不是 `.codex/agents/*.toml` 字段，也不是运行时模型遥测。 | qa_worker | 2026-08-09 |
| F-018 | CONFIRMED | 最新 validator 拒绝投稿包符号链接；若存在 `simulation.json`，任务数量、聚合指标、可视化声明和基线必须可复算且一致。 | validator / formal guide @ 9051ca77 | 未来确定性 QA 必须执行这些检查；当前 smoke 不含投稿包，不受影响。 | qa_worker | 2026-08-09 |
| F-019 | CONFIRMED | 在规则复核校验点 `main@f05026c028b2b68700c986f2ff3a29aef75a4bf4`，`9051ca77..f05026c0` 没有非 `submissions/` 路径变化。 | GitHub compare API | 当前规则影响复核以 `9051ca77` 为稳定基线；后续会话仍须重新 fetch 检查。 | librarian | 2026-08-09 |
| F-020 | CONFIRMED | 在规则复核校验点 `main@1a40a99daba7228aabf81b97e51ab3ddbbe7c911`，相对 `9051ca77` 的顶层 Git tree 唯一变化为 `submissions/`。 | GitHub commits / Git trees API | `9051ca77` 继续作为当前规则基线；无需因其他投稿更新而重跑 smoke 或改写 Agent 规则。 | librarian | 2026-08-10 |
| F-021 | CONFIRMED | 在 G1 启动校验点 `main@c4765c8baff68794dca212f2f57167769f809efe`，相对 `9051ca77` 的顶层 Git tree 唯一变化仍为 `submissions/`。 | GitHub commits / Git trees API | 不合并纯投稿更新；当前规则基线和 smoke 结论保持不变。 | librarian | 2026-08-10 |
| F-022 | CONFIRMED | 首轮 G1 仓库内盘点得到：中央 registry 共 6 条记录（5 条 approved+formal yes、1 条 provisional only）；6 个公告面积值可用；6 个 provisional 几何要素元数据齐全；9 类关键资料缺口仍未关闭。 | source registry / planning limits / provisional GeoJSON / missing data checklist | 可以建立缺口和来源计划，但不能据此生成官方边界、项目控规或现状专业结论。 | orchestrator | 2026-08-10 |
| F-023 | CONFIRMED | Issue #846 仍为 OPEN；维护者最后结论是不修改 `PROV-SITE-001`，不把 OSM 加入中央 registry，继续等待官方 polygon 裁决。 | GitHub Issue #846 / merged background note `5b5e9901` | 使用 provisional 范围开展空间提取前必须由人类选择 G1 工作策略，并保留整体重算义务。 | orchestrator | 2026-08-10 |
| M-001 | MISSING | 当前子线程接口未暴露可独立核实的运行时模型元数据。 | `project_control/smoke/orchestrator_summary.md` / Codex Subagents 文档 | 配置和行为验证通过；遥测记为 NOT OBSERVABLE，不阻断 G0，也不得声称已取得实际模型审计证据。 | qa_worker | 2026-08-09 |
| M-002 | MISSING | 项目特定容积率、高度、建筑密度、绿地率、退线、道路红线等正式控规条件未提供。 | planning_limits / missing-data | 不得自行推定；进入专业设计前继续作为缺口。 | evidence_planner | 2026-08-09 |
| M-003 | MISSING | `建筑工程设计文件编制深度规定（2016年版）` 在标准登记中仍为 `needs_official_file`。 | standards.json | 不能仅凭 URL 当作本地正式专业标准证据。 | evidence_planner | 2026-08-09 |
| M-004 | MISSING | 现状地块、建筑、交通、市政、公服、文保和权属等专业底数尚未补齐。 | `brief/site-package/missing-data.md` | G1 数据基线不得自动判定完成。 | orchestrator | 2026-08-09 |
| M-005 | CONFIRMED | 2026-08-09 记录的 Git HTTPS 阻断已解除；本地 `codex/agent-architecture` 已安全快进至远端 `de301b91a8e9a33701d64d7a7679f66648d23c5a`，同步前 10 个本地修改文件与该远端提交逐一同哈希。 | `git fetch --filter` / `git merge --ff-only` / GitHub contents API | 本地旧历史不再阻断后续工作；用户仍明确暂不进入 G1。 | orchestrator | 2026-08-10 |
| F-024 | CONFIRMED | 本轮授权只限 AI-native v0.1 方法基础设施、六个 Agent 契约与合成测试，不解除设计门。 | 用户实施计划 / D-027 | 不得生成真实设施、坐标、尺寸、造价、图件或新增研究。 | orchestrator | 2026-08-12 |
| F-025 | CONFIRMED | ATS 与 R-Score 是项目自定义 v0.1 双轴指标，不是官方评分；权重和 High 阈值是待未来真实记录校准的工作参数。 | AI_NATIVE_METHOD_V0_1 / D-024 / D-025 | 不得冒充既有标准或实证阈值，不得将二者相加。 | evidence_planner | 2026-08-12 |
| F-026 | CONFIRMED | 方法全集为 8 类设施，首轮为 6 类；High–High 要求 AI 物理使用行为、可测物理改变并通过 anti-sticker 门。 | AI_NATIVE_METHOD_V0_1 / D-023 | 单纯摄像头、传感器或后台算法不能进入 High–High。 | qa_worker | 2026-08-12 |
| F-027 | CONFIRMED | 当前官方规则基线为 `905b8be6`，未来正式投稿 manifest 使用 0.2 严格哈希与 refresh→self-check 流程。 | upstream main / manifest migration | 项目方法不写入中央 Schema；正式投稿仍只改 submissions 目录。 | qa_worker | 2026-08-12 |
