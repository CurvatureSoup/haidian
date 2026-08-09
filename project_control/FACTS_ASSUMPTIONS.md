# FACTS_ASSUMPTIONS

状态只允许：`CONFIRMED`、`ASSUMPTION`、`MISSING`、`CONFLICT`。

| ID | 状态 | 内容 | 来源 | 影响/处理 | Owner | 更新日期 |
|---|---|---|---|---|---|---|
| F-001 | CONFIRMED | 官方仓库为 `open-city-ai/haidian`，默认分支为 `main`。 | GitHub repository metadata | 所有规则同步以官方 main 为准。 | orchestrator | 2026-08-09 |
| F-002 | CONFIRMED | 项目级自定义 Codex Agent 使用 `.codex/agents/*.toml`，每个文件至少包含 name、description、developer_instructions。 | OpenAI Docs: Subagents | 本项目按正式 schema 建立 Agent。 | qa_worker | 2026-08-09 |
| F-003 | CONFIRMED | 正式投稿 PR 只允许修改本人 `submissions/<login>/<slug>/`。 | 最新项目 Skill / formal guide | Agent 架构使用独立分支，不能混入未来投稿 PR。 | orchestrator | 2026-08-09 |
| F-004 | CONFIRMED | 当前阶段仅搭系统，不开始城市设计。 | 用户任务 | 任何规划生产任务保持冻结。 | orchestrator | 2026-08-09 |
| A-001 | ASSUMPTION | `AI-Ready, AI-Optional` 是后续方案的候选总原则。 | 用户提供的两篇深度调研 | 进入规划阶段前由总控结合正式证据决定是否冻结。 | evidence_planner | 2026-08-09 |
| A-002 | ASSUMPTION | 调研中的大规模专业 Agent 清单适合分阶段扩展，而不适合初始化时一次建立。 | 用户调研 + 当前第一批范围 | 第一阶段只保留六个 Agent。 | orchestrator | 2026-08-09 |
| F-005 | CONFIRMED | librarian、researcher、evidence_planner 和 orchestrator 均完成了指定微型任务与共享文件交接。 | `project_control/smoke/` | 角色行为与总控读取能力已验证。 | orchestrator | 2026-08-09 |
| F-006 | CONFIRMED | G0 官方规则基线为 `upstream/main@d28c14002a77d19221888ffe8ac447876aca3165`，本地架构分支已纯快进到该提交。 | Git HEAD / upstream/main | 后续变更检查以该提交为比较基准。 | librarian | 2026-08-09 |
| F-007 | CONFIRMED | 旧基线 `56ce8b49` 到 G0 基线的 487 个文件变化全部位于 `submissions/`；Skill、brief、data registry、docs、Schema、关键脚本与模板没有树差异。 | `git diff 56ce8b49 d28c1400` | G0 规则内容连续，未被投稿更新改变。 | qa_worker | 2026-08-09 |
| F-008 | CONFIRMED | 本机安装的 `urban-design-ai-submission` 七个文件与 G0 基线的 Git blob 哈希逐一一致。 | 本机 Skill 校验 / Git tree | 新会话使用最新版 Skill。 | qa_worker | 2026-08-09 |
| F-009 | CONFIRMED | 新投稿必须采用 proposal v2 与 bilingual contract v1；中英文正文、HTML、视觉页、A3/A0 和文字型图件必须成对一致。 | 最新项目 Skill / formal guide | 未来制包必须从一开始按双语合同组织。 | orchestrator | 2026-08-09 |
| F-010 | CONFIRMED | 当前只有 provisional 三层范围与三处重点区 polygon，没有可信官方精确 polygon。 | design brief / source registry / missing-data | 可用于临时生成、展示和 intake 自检；不得用于官方红线、精确复算、法定结论或正式专业评分。 | gis_analyst | 2026-08-09 |
| F-011 | CONFIRMED | “临时边界不阻断内容评分”与“临时边界不能作为正式专业评分依据”适用于不同评价层面，不构成规则冲突。 | Skill / formal guide / allowed design space | 内容工作可在充分披露下继续；精度敏感专业结论仍保持阻断。 | evidence_planner | 2026-08-09 |
| F-012 | CONFIRMED | `data/source_registry.json` 当前登记 6 项：5 项 `usable_for_formal=yes`，1 项 provisional geometry 为 `provisional_only`。 | source registry @ d28c1400 | 每条资料仍只能用于登记的 allowed uses。 | librarian | 2026-08-09 |
| F-013 | CONFIRMED | GitHub 远端 `codex/agent-architecture` 已通过合并提交 `a59a6fd37a766ef675cb182cc0ea5326e638f157` 包含官方 `main@9051ca77fe1a15657bc3abf0513c402561afae0f`。 | GitHub commits API | Agent 架构已发布并包含操作时核实的最新上游快照。 | orchestrator | 2026-08-09 |
| F-014 | CONFIRMED | 从历史 G0 `d28c1400` 到 `9051ca77` 有 10 个非 `submissions/` 路径变化，涉及 formal guide、Skill 参考、Schema、数据工作流和校验脚本。 | GitHub compare API | 历史 G0 不能继续冒充最新规则冻结；必须重新复核。 | qa_worker | 2026-08-09 |
| M-001 | MISSING | 当前子线程接口未暴露可独立核实的运行时模型元数据。 | `project_control/smoke/orchestrator_summary.md` / Codex Subagents 文档 | 配置和行为验证通过；遥测记为 NOT OBSERVABLE，不阻断 G0，也不得声称已取得实际模型审计证据。 | qa_worker | 2026-08-09 |
| M-002 | MISSING | 项目特定容积率、高度、建筑密度、绿地率、退线、道路红线等正式控规条件未提供。 | planning_limits / missing-data | 不得自行推定；进入专业设计前继续作为缺口。 | evidence_planner | 2026-08-09 |
| M-003 | MISSING | `建筑工程设计文件编制深度规定（2016年版）` 在标准登记中仍为 `needs_official_file`。 | standards.json | 不能仅凭 URL 当作本地正式专业标准证据。 | evidence_planner | 2026-08-09 |
| M-004 | MISSING | 现状地块、建筑、交通、市政、公服、文保和权属等专业底数尚未补齐。 | `brief/site-package/missing-data.md` | G1 数据基线不得自动判定完成。 | orchestrator | 2026-08-09 |
| M-005 | MISSING | 本机 Git HTTPS 当前无法连接 `github.com:443`，所以本地对象库尚未补拉远端合并后的 270 个上游提交；GitHub 远端状态已通过 API 独立核实。 | `git fetch` / GitHub commits API | 网络恢复后先 fetch，并核对本地与远端 SHA；在此之前不从本地旧规则树开展后续阶段。 | librarian | 2026-08-09 |
