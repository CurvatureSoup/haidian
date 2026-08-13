# G1 双轨数据协议 v0.1

## 状态与适用范围

- 决策：`G1-DIR-001 = C`。
- 适用阶段：G1 资料、空间与现状数据基线。
- 不包含：城市设计、工程判断、法定指标、正式边界认定、投稿制包。
- `DESIGN-START` 继续为 `BLOCKED`。

## 两条轨道

### Track A：官方待定轨

只接收组织方附件、政府主管部门发布的正式文件、清权 CAD/GIS/PDF 或经来源审查后可承担相应主张的公开数据。进入正式基线前必须记录发布者、URL/附件名、发布时间与抓取时间、许可或访问条件、空间和时间覆盖、原始 CRS、文件哈希、转换过程及限制。

### Track B：发现与试跑轨

可用统筹研究范围、宽松上下文范围或现有 provisional geometry 做来源发现、接口可用性检查和处理链试跑。任何产物必须标记 `provisional_working` 或 `discovery_only`，不得升级为 `official_constraint`，不得计算法定面积、控规指标或形成拆改留、工程可行性和设计判断。

## 试跑最小回执

每次网络获取或空间查询至少记录：

1. `query_id`、`source_id`、发布者与原始 URL；
2. `retrieved_at`、HTTP 状态、内容类型、字节数和 SHA-256；
3. 查询参数、bbox 或 provisional feature ID；
4. 原始 CRS、许可/访问条件和使用限制；
5. 原始数据保存位置；如未保存，明确 `metadata_only`；
6. 转换脚本、版本、输出位置和派生数据哈希；
7. 适用缺口、允许用途与禁止用途；
8. 官方数据到位后的替换触发器。

本轮回执保存在 `project_control/G1_SOURCE_DISCOVERY_LOG.csv`。本轮仅做网页元数据与内容哈希试跑，不把网页正文或图片复制进仓库。

## 双轨状态机

`candidate → retrieved → reviewed → background_only / provisional_working / formal_candidate → approved_for_project_use`

- `candidate`：仅为线索。
- `retrieved`：已可重放获取，尚未完成内容、许可和范围审查。
- `reviewed`：已核对发布者、内容和局限。
- `background_only`：只能支撑背景叙述或来源发现。
- `provisional_working`：可做临时裁剪或处理链试跑，不可形成正式结论。
- `formal_candidate`：可能支撑特定正式主张，但仍需证据规划复核。
- `approved_for_project_use`：由 evidence_planner 明确批准用途；不等于进入上游中央 registry。

## 替换与整体复算

下列任一事件触发替换审计：官方三层范围或重点区 polygon 到位、官方控规/道路/文保/市政附件到位、来源版本或许可变化、provisional 范围变化、坐标系或拓扑规则变化。

触发后必须：冻结旧输入哈希 → 归档查询参数 → 用官方范围重新裁剪 → 重算几何与指标 → 比较差异 → 更新来源/假设/图件/正文 → 重新校验。旧 provisional 结果保留为历史，不得静默覆盖。

## 停止条件

遇到以下情况保存并交人类决定：

- 需要注册、登录、付费、签署许可或提供个人/机构信息；
- 需要对组织方、主管部门或社区发出 Issue、邮件或公开评论；
- 候选来源之间对范围、权属、控制指标或法律效力有冲突；
- 需要把 provisional 结果升级为正式基线；
- 需要开始真实设施、空间方案、图件、造价或指标生产。

## 最新官方接口兼容

- 未来正式 `design_depth_matrix.json` 的核心项仍必须是 `complete`；可选 `completeness_limited_by` 只披露组织方未公开数据造成的限制，不会把未知事实变成已确认事实。
- 未来 manifest 继续使用 0.2 严格哈希契约；已登记工件变更后执行 refresh，再重新 self-check。
- 本协议只属于 `project_control/`，不修改上游 schema、模板、中央来源表或投稿目录。
