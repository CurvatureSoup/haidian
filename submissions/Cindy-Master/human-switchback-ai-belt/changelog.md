# 方案迭代记录

## v1.1 - 2026-08-10

### 改动摘要

- 将 `manifest.validation_claim.known_blockers` 清空。原因见下。内容、几何、指标、图纸与正文均未改动，
  仅重算 manifest 哈希。

### 采纳反馈

- 采纳 PR #1205 上维护者的 known-blocker hold 反馈。该 hold 指出：本包 CI 确定性校验通过，但 manifest
  自声明了 known blocker，因而被判定无法进入 formal professional scoring，付费 AI 评分与合并被挂起。
- 复核后确认这是本方案的登记错误，而非组织方数据缺口的正确表达方式：
  1. `known_blockers` 应登记**参赛者可解决**的阻断项；官方 SITE_BOUNDARY 与三处 KEY_AREA 精确 polygon
     未公开属于组织方数据缺口，参赛者无法解决，按项目规则也不阻断内容评分；
  2. `scripts/finalize_submission.py` 的默认行为就是把 scaffold 阶段的 known blocker 移除、留空；
  3. 抽样 14 份已合入方案，`known_blockers` 全部为空，而它们同样使用 provisional 边界。
- 因此清空该字段是恢复正确登记，不是隐瞒。该数据缺口的披露完整保留在：`assumptions.json`
  （A-BOUNDARY-001 / A-PEER-846 / A-PEER-1029）、`self_check.json`（BOUNDARY_TRUST / KEY_AREAS_TRUST）、
  每个几何要素的 `official_boundary=false` 与 `boundary_precision=provisional_rough`、`proposal.md` 与
  `proposal.en.md` 的设计依据与风险两章、五张图件页脚、展示页顶部横幅，以及本文件的复算清单；
  确定性校验也会独立报出 provisional boundary 警告。

### 暂未采纳或待复核事项

- 官方 polygon 仍未公开，本包仍不满足 formal scoring readiness 的前两项（official boundary / official
  key areas），这一点如实保留，不通过清空字段来规避。

## v1.0 - 2026-08-10

### 改动摘要

- 提出「人字轨 SWITCHBACK」总体概念：把京张人字形展线的折返上行逻辑转译为
  上行段（众智园）—折返点（AI原点社区）—发车段（大钟寺）+ 中关村与小月河两翼回流的闭环空间结构。
- 生成 9 个设计图层：用地分区由统一切分线对提交边界整体拓扑剖分，无缝隙、无重叠；
  含道路中心线 22 条、建筑基底 142 个、AI 场景节点 18 处、约束与断点标注 8 处。
- 从提交几何在 EPSG:4548 下复算 56 项指标（51 known / 5 unknown），unknown 项逐条给出原因与前置条件。
- 绘制 5 张演示级核心图并提供英文对照版；生成离线展示页与 A3 文册、A0 展板，中英各一套。
- 撰写中文主稿与等义英文对照稿，覆盖公告 1.3/1.4/1.5 与智能体任务书 agent.1–agent.6，
  含 14 张 AI 场景卡（其中 3 个产业测试验证场景）、6 类用户画像、6 个全球生态案例、
  4 处 AI 朝圣地标、12 项更新项目与年度活动体系。

### 采纳反馈

- 暂无，首版提交。

### 暂未采纳或待复核事项

- 官方 SITE_BOUNDARY 与三处 KEY_AREA 精确 polygon 未公开，全部范围线标注为 `provisional_rough`。
- 容积率、建筑高度、建筑密度、退线与地块拆改留结论一律不给出，相关指标记为 unknown。
- 轨道站位、慢行断点跨越方式、市政与文保条件均须由专业团队另行论证。
- 官方数据发布后必须依次重跑：替换边界与重点区 polygon → 重新生成设计图层 → 重算指标 →
  重绘 5 张图与展示页、A3/A0 图册 → render_proposal_html → finalize_submission →
  self_check_submission → participant_preflight。

### 公开资料与合规说明

- 本版本仅使用公开与已清权资料，未使用个人隐私数据、未授权企业数据或未审定的规划控制指标。
- 六个国际城市创新区案例仅作定性机制借鉴，登记为 background_only，未引用未经核实的数量数据。
- 全部图形由本包脚本从提交的 GeoJSON 与指标生成，不含第三方图片、嵌入字体、商标或肖像素材。
