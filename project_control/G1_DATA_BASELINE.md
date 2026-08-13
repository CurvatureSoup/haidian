# G1_DATA_BASELINE

## 结构化交接

- task_id: `G1-DATA-BASELINE`
- status: `PAUSED_AT_BASELINE_DEPTH_GATE`
- producer_agent: `orchestrator`
- summary: 人类已选择双轨策略 C，并完成九类缺口的公开网络尽调；确认没有全域正式底包但有局部官方碎片和开放现状数据，现停在公开基线深度选择门。
- source_ids: `DATA-SRC-OFFICIAL-ANNOUNCEMENT-20260509`、`DATA-SRC-AGENT-TASKBOOK-20260518`、`DATA-SRC-MOHURD-URBAN-DESIGN-MEASURES`、`DATA-SRC-MOHURD-CONTROL-DETAILED-PLANNING`、`DATA-SRC-MNR-LAND-USE-CLASSIFICATION-202311`、`DATA-SRC-PROVISIONAL-BOUNDARIES-20260605`
- assumption_ids: `none`
- related_fact_ids: `F-010`、`F-016`、`F-022`、`F-023`、`M-002`、`M-003`、`M-004`
- blockers: `G1-BASELINE-DEPTH-001`、官方精确 polygon、项目控规条件、现状专业底数、`MOHURD-ARCH-DESIGN-DEPTH-2016` 官方文件
- output_paths: `project_control/G1_DATA_BASELINE.md`、`project_control/PROJECT_BRIEF.md`、`project_control/FACTS_ASSUMPTIONS.md`、`project_control/TASK_BOARD.md`、`project_control/DECISION_LOG.md`
- escalation_target: `human`（决定是否授权外部联系、登记/登录或获取受限附件）

## 已授权范围

- 建立资料目录、来源等级、缺口清单、坐标与数据处理规则。
- 轻量检查官方规则路径；不合并只含 `submissions/` 的上游更新。
- 不复跑三级 smoke。
- 不启动城市设计、空间方案、投稿制包或法定指标计算。
- 关键范围、口径或方向决策必须暂停并由人类选择。

## G1 启动与恢复校验

- 检查时间：2026-08-10（Asia/Shanghai）。
- 官方校验点：`open-city-ai/haidian main@c4765c8baff68794dca212f2f57167769f809efe`。
- 相对规则基线 `9051ca77fe1a15657bc3abf0513c402561afae0f`，顶层 Git tree 唯一变化为 `submissions/`。
- 处理：不合并纯投稿更新；规则基线、Agent 配置和 smoke 结论不变。
- 2026-08-13 恢复时，官方 `main` 为 `464aead8cac0cc0664b060343efb156ef4a83e52`；相对 `61306151` 的 7 个提交、60 个文件全部位于 `submissions/`。
- 已将最新官方提交以第二父提交合入远端架构分支，合并提交为 `65a060717b652a36182a217753dfeaddc0bf2057`。项目自有路径无冲突。
- `905b8be6..61306151` 的规则变化已复核：正式深度项仍须 `complete`；可选 `completeness_limited_by` 仅披露官方数据缺口，不改变 formal 资格，也不把未知事实升级为已确认。

## 当前基线盘点

| 领域 | 已确认 | 仍缺失或受限 | 当前可做 |
|---|---|---|---|
| 来源治理 | 中央 registry 6 条；其中 5 条 `approved + usable_for_formal=yes`，1 条 `provisional_only` | OSM 背景读数未形成中央可重放来源 | 使用已批准来源建立任务和标准索引；中央 registry 保持只读 |
| 范围与面积 | 公告提供三层范围及三处重点区共 6 个约面积值 | 三层范围、三处重点区的官方精确 polygon 和正式测绘基准 | 引用公告面积与文字四至；不得称为精确红线 |
| 临时几何 | 6 个 provisional 要素均具备 `source_type`、`confidence`、`geometry_role`、`official_boundary` 和 `boundary_precision` | `PROV-SITE-001` 与公开背景核对存在 412.5 m 空间不确定性 | 按双轨协议仅作来源发现或处理链试跑，不进入正式基线 |
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

## 已决方向门：G1-DIR-001

### 人类决定

2026-08-13 人类选择 **C. 双轨策略**。完整执行约束见 `project_control/G1_DUAL_TRACK_PROTOCOL.md`。

### A. 官方边界优先

- 在取得官方 polygon 前，只做非空间资料、字段字典、来源目录和官方附件追踪。
- 优点：返工和误落位风险最低。
- 代价：道路、建筑、设施和环境数据的空间基线基本停滞。

### B. Provisional 并行推进

- 使用 `PROV-RESEARCH-001` / `PROV-SITE-001` 作为明确标注的临时查询和裁剪范围，开始公开数据提取。
- 优点：推进最快，可较早发现数据质量问题。
- 代价：Issue #846 已提示总体范围可能偏移；官方 polygon 到位后可能需要整体重取、重算。

### C. 双轨策略（已采用）

- 以统筹研究范围或宽松上下文范围做“来源发现和目录”，但不把空间裁剪结果升级为正式基线。
- 对必须试跑的数据，只保存原始查询、抓取时间、许可、快照/hash 和 provisional 标签；不计算法定指标，不形成设计判断。
- 官方 polygon 到位后再冻结正式裁剪范围并整体复算。
- 优点：兼顾进度和证据边界。
- 代价：需要同时维护 provisional 与 official-pending 两套状态，治理成本高于 A。

## 本轮已完成

- 建立 `G1_SOURCE_ACQUISITION_MATRIX.csv`，为 9 类缺口固定权威来源、允许用途、抓取和整体复算要求。
- 建立 `G1_FIELD_DICTIONARY.csv`，固定边界、控规、道路、宗地、建筑、文保、市政与公服核心字段及缺失处理。
- 建立 `G1_DUAL_TRACK_PROTOCOL.md`，规定官方待定轨、发现试跑轨、查询回执、状态机、替换复算与停止条件。
- 对 6 个官方网页完成 metadata-only 试跑并记录 HTTP 200、内容类型、字节数与 SHA-256；未复制网页正文或图片，未进行批量下载。
- 新识别的控规公示采信通告仅作为控规/道路背景；清华园车站旧址页面可支撑官方文字约束，但没有可核实空间基准的图件，均不能替代正式 GIS/CAD polygon。
- 未调用 OSM / Overpass、商业地图或需凭证 API；未生成或修改任何空间图层、指标、图纸、方案或投稿文件。
- 未修改中央 `data/source_registry.json`，未创建 Issue、PR、邮件或外部评论。

## 公开网络全面尽调后的判断

完整记录见 `project_control/G1_PUBLIC_SOURCE_AUDIT_20260813.md`。未找到全域正式 GIS/CAD 或可无条件下载的组织方密码包；找到蓝景丽家局部成套官方附件、文保文字约束、控规进度、开放公服名录及 OSM/Microsoft 现状底图路径。这些资料的空间范围、证据等级和许可不同，不能静默合并为官方基线。

## 下一关键门：G1-BASELINE-DEPTH-001

需要人类选择：

- A（推荐）：L0 官方文本 + L1 官方项目碎片 + L2 开放现状数据 + L3 machine-readable data gaps；
- B：只获取官方碎片和无条件开放名录，不使用 OSM/Microsoft；
- C：暂停下载，先授权一次不冒充机构的公开询问。

选择会改变下载量、ODbL/CDLA 义务、空间覆盖、返工成本和后续 GIS 验证能力，因此总控在此停止。

## 仍保留的外部访问门：G1-EXT-ACCESS-001

若未来选择外部询问、注册登录或请求受限附件，仍需单独授权。资格预审密码包领取期已结束且要求法人/联合体资格，个人参赛者不得绕过该流程。

在决定前：

1. `G1-DATA-BASELINE` 保持暂停，不把候选网页升级为正式基线。
2. `DESIGN-START` 保持 `BLOCKED`。
3. 不创建 Issue、邮件、公开评论，不注册或提交机构/个人信息。
