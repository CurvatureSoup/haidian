# G1_DATA_BASELINE

## 结构化交接

- task_id: `G1-DATA-BASELINE`
- status: `PAUSED_AT_HUMAN_GATE`
- producer_agent: `orchestrator`
- summary: 已完成 G1 仓库内资料、空间、标准与缺口盘点；在空间数据工作范围决策前停止。
- source_ids: `DATA-SRC-OFFICIAL-ANNOUNCEMENT-20260509`、`DATA-SRC-AGENT-TASKBOOK-20260518`、`DATA-SRC-MOHURD-URBAN-DESIGN-MEASURES`、`DATA-SRC-MOHURD-CONTROL-DETAILED-PLANNING`、`DATA-SRC-MNR-LAND-USE-CLASSIFICATION-202311`、`DATA-SRC-PROVISIONAL-BOUNDARIES-20260605`
- assumption_ids: `none`
- related_fact_ids: `F-010`、`F-016`、`F-022`、`F-023`、`M-002`、`M-003`、`M-004`
- blockers: `G1-DIR-001`、官方精确 polygon、项目控规条件、现状专业底数、`MOHURD-ARCH-DESIGN-DEPTH-2016` 官方文件
- output_paths: `project_control/G1_DATA_BASELINE.md`、`project_control/PROJECT_BRIEF.md`、`project_control/FACTS_ASSUMPTIONS.md`、`project_control/TASK_BOARD.md`、`project_control/DECISION_LOG.md`
- escalation_target: `human`

## 已授权范围

- 建立资料目录、来源等级、缺口清单、坐标与数据处理规则。
- 轻量检查官方规则路径；不合并只含 `submissions/` 的上游更新。
- 不复跑三级 smoke。
- 不启动城市设计、空间方案、投稿制包或法定指标计算。
- 关键范围、口径或方向决策必须暂停并由人类选择。

## G1 启动校验

- 检查时间：2026-08-10（Asia/Shanghai）。
- 官方校验点：`open-city-ai/haidian main@c4765c8baff68794dca212f2f57167769f809efe`。
- 相对规则基线 `9051ca77fe1a15657bc3abf0513c402561afae0f`，顶层 Git tree 唯一变化为 `submissions/`。
- 处理：不合并纯投稿更新；规则基线、Agent 配置和 smoke 结论不变。

## 当前基线盘点

| 领域 | 已确认 | 仍缺失或受限 | 当前可做 |
|---|---|---|---|
| 来源治理 | 中央 registry 6 条；其中 5 条 `approved + usable_for_formal=yes`，1 条 `provisional_only` | OSM 背景读数未形成中央可重放来源 | 使用已批准来源建立任务和标准索引；中央 registry 保持只读 |
| 范围与面积 | 公告提供三层范围及三处重点区共 6 个约面积值 | 三层范围、三处重点区的官方精确 polygon 和正式测绘基准 | 引用公告面积与文字四至；不得称为精确红线 |
| 临时几何 | 6 个 provisional 要素均具备 `source_type`、`confidence`、`geometry_role`、`official_boundary` 和 `boundary_precision` | `PROV-SITE-001` 与公开背景核对存在 412.5 m 空间不确定性 | 仅在 `G1-DIR-001` 决定后按批准策略使用 |
| 控规条件 | 已定义缺失字段和可接受官方来源类型 | FAR、高度、密度、绿地率、退线/控制线全部 missing | 只能建立字段字典和取证要求，不得填入推定值 |
| 现状专业底数 | 已形成 9 类缺口清单 | 道路、宗地、建筑、文保、市政安全、公服等底数未补齐 | 建立来源采集矩阵；不得形成拆改留或工程判断 |
| 专业标准 | 6 项登记；5 项 mandatory 已有本地参考 | `MOHURD-ARCH-DESIGN-DEPTH-2016` 仍缺官方文件且非 mandatory | 使用已有 5 项原则性标准；缺失项保持待补 |

## 已登记的九类缺口

1. `GAP-BOUNDARY-001`：三层范围 official polygon。
2. `GAP-BOUNDARY-002`：三处重点区 official KEY_AREA polygon。
3. `GAP-CONTROL-001`：项目控规条件。
4. `GAP-ROAD-001`：道路红线和断面。
5. `GAP-PARCEL-001`：现状宗地与权属状态。
6. `GAP-BUILDING-001`：现状建筑轮廓、用途、高度、年代与状态。
7. `GAP-HERITAGE-001`：遗址公园与文保控制范围。
8. `GAP-MUNICIPAL-001`：市政、消防、防洪排涝与海绵条件。
9. `GAP-SERVICE-001`：公共服务设施底数。

## 关键方向门：G1-DIR-001

### 需要人类决定的问题

在官方 polygon 仍缺失且 Issue #846 未关闭的情况下，G1 应采用哪种空间数据工作范围策略？该选择会改变公开数据的查询范围、下载量、返工成本和空间结论风险，因此总控不代替人类决定。

### A. 官方边界优先

- 在取得官方 polygon 前，只做非空间资料、字段字典、来源目录和官方附件追踪。
- 优点：返工和误落位风险最低。
- 代价：道路、建筑、设施和环境数据的空间基线基本停滞。

### B. Provisional 并行推进

- 使用 `PROV-RESEARCH-001` / `PROV-SITE-001` 作为明确标注的临时查询和裁剪范围，开始公开数据提取。
- 优点：推进最快，可较早发现数据质量问题。
- 代价：Issue #846 已提示总体范围可能偏移；官方 polygon 到位后可能需要整体重取、重算。

### C. 双轨策略（总控建议）

- 以统筹研究范围或宽松上下文范围做“来源发现和目录”，但不把空间裁剪结果升级为正式基线。
- 对必须试跑的数据，只保存原始查询、抓取时间、许可、快照/hash 和 provisional 标签；不计算法定指标，不形成设计判断。
- 官方 polygon 到位后再冻结正式裁剪范围并整体复算。
- 优点：兼顾进度和证据边界。
- 代价：需要同时维护 provisional 与 official-pending 两套状态，治理成本高于 A。

## 暂停时未执行的工作

- 未开展新的外部数据源发现或批量下载；只回读了已登记的 Issue #846 当前结论。
- 未调用 OSM / Overpass、商业地图或公共数据 API。
- 未生成或修改任何空间图层、指标、图纸、方案或投稿文件。
- 未修改中央 `data/source_registry.json`，未创建 Issue、PR 或外部评论。

## 人类决定后的恢复点

1. 记录 `G1-DIR-001` 选择及适用范围。
2. 按九类缺口建立来源采集矩阵、字段字典、许可与复算要求。
3. 优先追踪资格预审文件、正式任务书、补遗答疑和清权官方附件。
4. 只对获准范围执行分批、可追溯的数据获取；每批完成后回写来源和限制。
5. G1 完成不自动解除 `DESIGN-START`。
