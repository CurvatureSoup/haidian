---
title: "京张·下一站 NEXT STOP JINGZHANG——百年京张AI创新带城市设计方案"
author_github: "gzhzk"
language: "zh"
proposal_format_version: "2"
bilingual_contract_version: "1"
translation_file: "proposal.en.md"
license: "COMMUNITY-DISPLAY-ONLY"
summary: "以「下一站京张 NEXT STOP JINGZHANG」为总体概念，把百年京张铁路从自主工程的起点站重构为AI自主创新的下一站；以一线三站两翼组织11.4平方公里总体设计，对众智园、北京AI原点社区、大钟寺三处重点区开展详细设计，形成概念建议与可复核的空间、指标与场景体系。"
tracks: ["ai-traffic-walkability", "enterprise-services-ecosystem", "civic-agent-governance"]
scenarios: ["ai-traffic-walkability", "enterprise-service-copilot", "public-safety-operations-review"]
iteration: "v1.0"
---

# 京张·下一站 NEXT STOP JINGZHANG

## 设计依据与资料清单

本方案以北京市规划和自然资源委员会海淀分局发布的《百年京张AI创新带城市设计国际方案征集资格预审公告》为第一依据，以 `brief/site-package/` 中登记的三层范围、三处重点区域、任务书、来源、枚举与指标为机器可读依据 [source:OFFICIAL-ANNOUNCEMENT] [standard:PROJECT-OFFICIAL-ANNOUNCEMENT]。面向全球智能体的开源征集任务书补充了三大定位、五大功能、三区两翼、六项任务和统一边界条款 [source:AGENT-TASKBOOK] [standard:PROJECT-AGENT-OPEN-CALL-TASKBOOK]。方案所有成果均为**开放共创的概念建议、参考方案与可供专业团队深化的方向性材料**，不替代正式规划，不构成政府审定结论，不给出控规指标、工程可行性与拆改留最终判断。

资料使用遵循 `data/source_registry.json` 的分级边界 [source:SOURCE-REGISTRY]：正式公告与清权任务书用于 formal 论述，`provisional` 边界仅用于本次生成、展示与临时自检 [source:BOUNDARY-SOURCE]，背景与行业资料仅作佐证。完整来源、指标、标准、设计深度与任务覆盖分别保存在 `sources.json`、`metrics.json`、`compliance_matrix.json`、`standard_matrix.json` 与 `design_depth_matrix.json`，不在正文重复机器索引 [depth:existing_conditions_diagnosis]。

![资料证据链与提交包关系图](assets/figures/site-overview.png)

截至提交日，组织方未在公开渠道发布精确的官方 `SITE_BOUNDARY` 与三处 `KEY_AREA` 多边形，资格预审包需密码下载且仓库未检索到公开精确边界文件。本包因此使用 `brief/site-package/geometry/provisional_boundaries.geojson` 中经维护者校准的临时粗略边界 [source:KEY-AREA-SOURCE]。`geometry/site_boundary.geojson#SITE-001` 与 `geometry/key_areas.geojson#PROV-KEY-001/002/003` 均标注 `official_boundary=false`、`geometry_role="provisional_constraint"`、`boundary_precision="provisional_rough"`，只用于方案生成、可视化与设计讨论，**不得作为 official redline、审批依据、精确面积或法定控制结论**；组织方数据缺口本身不阻断内容评分，官方 polygon 发布后所有图层与指标必须复算 [data:geometry/site_boundary.geojson#SITE-001] [metric:site_area_sqm]。

## 三层范围工作框架

方案按公告的三层范围组织：**统筹研究范围**约 43.6 平方公里，回答世界级 AI 创新生态、未来 AI 城市形态与区域协同；**总体设计范围**约 11.4 平方公里，即京张遗址公园周边 1—2 公里城市地区与产业区，达到控制性详细规划的城市设计深度；**重点区域范围**约 368.4 公顷，覆盖自北向南的众智园 AI 自主创新加速区、北京 AI 原点社区、大钟寺 AI 产业集聚区，达到规划综合实施方案的城市设计深度 [standard:PROJECT-OFFICIAL-ANNOUNCEMENT] [metric:site_area_sqm]。三层范围在 `compliance_matrix.json` 中逐条映射公告 1.3、1.4、1.5 与 agent.1—agent.6 [depth:three_level_scope_framework]。

| 层级 | 面积 | 设计问题 | 本方案落点 |
| --- | --- | --- | --- |
| 统筹研究范围 | ≈43.6 km² | 产业生态与未来城市形态 | 创新链与三区两翼协同 [data:geometry/site_boundary.geojson#SITE-001] |
| 总体设计范围 | ≈11.4 km² | 更新、交通、风貌与设施 | 一线三站两翼空间结构 [data:geometry/land_use.geojson#LU-001] |
| 重点区域范围 | ≈368.4 ha | 三处片区精细化设计 | 加速站·原点站·场景站 [data:geometry/key_areas.geojson#PROV-KEY-001] |

三层工作不是割裂的图纸集合：统筹研究决定产业链与城市形态判断，总体设计把判断落实为用地、更新与设施布局，重点区域详细设计验证具体地块、建筑、交通与 AI 场景的可实施方向。空间证据以 `geometry/` 各图层为准，任何无法从结构化数据复算的面积、比例与规模不得写入正式结论 [depth:overall_spatial_structure]。

![三层范围与空间工作框架图](assets/figures/land-use-structure.png)

## 统筹研究范围产业与未来城市研究

统筹研究范围的核心任务是构建世界级 AI 创新生态体系。方案以「**高校策源—开源协作—企业转化—公共体验—国际传播**」五环创新链组织海淀的高校院所、头部企业、算力算法、孵化平台与科技服务资源，并把产业战略落实到可定位的功能区、廊道、节点与场景 [standard:PROJECT-AGENT-OPEN-CALL-TASKBOOK] [depth:overall_spatial_structure]。

### 总体概念与命名体系（agent.1）

**主名称：京张·下一站（NEXT STOP JINGZHANG，缩写 NSJZ）。** 核心隐喻：1909 年京张铁路是中国自主工程的起点站，由詹天佑主持修建，终结了"中国人不能自建铁路"的时代；今天，这条百年走廊是 AI 自主创新的「下一站」——每一次 AI 场景部署都是一处可验证、可到达、可复现的站点。命名体系与空间结构严格对应：

- **一线（站台与轨道）**：京张遗址公园活力带——百年站台，也是南北贯通的慢行与公共空间主轴；
- **三站（站台停靠点）**：**加速站**＝众智园 AI 自主创新加速区、**原点站**＝北京 AI 原点社区、**场景站**＝大钟寺 AI 产业集聚区；
- **两翼（平行轨道）**：**中关村科技服务翼**＝要素全球化配置与资本赋能，**小月河场景赋能翼**＝AI 场景开放与活力城市。

Logo 方向以「站牌＋轨道接续」为原型：一条从铁轨折线延伸为数据流的连续线，圆角站牌承载站名，"S" 形图标双关 Station（车站）、Spine（脊梁）与 Next Stop。主色系为京张铁轨褐＋AI 信号蓝，辅助色为清华紫与海淀科技蓝，与国际传播中的"站点叙事"保持一致。该命名与视觉识别为概念建议方向，供专业品牌团队深化 [source:AGENT-TASKBOOK] [standard:PROJECT-AGENT-OPEN-CALL-TASKBOOK]。

### 三大定位、五大功能与三区两翼协同

三大定位为「百年京张文化带、都市 AI 生活体验带、AI 融合创新带」；五大功能为「AI 全栈自主创新体系、世界级 AI 创新生态、AI+ 场景赋能新范式、智能化 AI 活力城市、AI 治理全球话语权」。三区两翼协同回路为：原点站汇聚全球创新生态，众智园支撑全栈自主与治理话语权，大钟寺承载智能原生新业态，中关村服务翼提供 IP 与资本，小月河翼提供场景与活力，形成"生态—自主—业态—服务—场景"的闭环 [standard:PROJECT-AGENT-OPEN-CALL-TASKBOOK]。

### 全球 AI 创新生态案例（agent.2）

方案研究 6 个可验证的全球创新生态案例，均作为公开背景资料登记于 `sources.json`，不构成对具体企业、产值或政策的承诺：

1. **美国剑桥肯德尔广场**（Kendall Square）：MIT 主导的"大学—产业—社区"混合创新生态，证明近校街区可承载研发、孵化与日常交往的复合功能，为原点站提供参照 [source:AGENT-TASKBOOK]；
2. **新加坡纬壹科技城**（one-north）：政府引导的功能混合创新城区，把研究、生活、休闲放在同一条城市线上，为总体设计范围提供功能混合参照；
3. **荷兰埃因霍温脑港**（Brainport Eindhoven）："开放式创新＋产业—社区共生"的高技术园区，为众智园全栈自主与开放测试提供参照；
4. **瑞士创新园苏黎世节点**（Switzerland Innovation Park）：公私合作、面向验证与试验的园区机制，为产业测试验证场景提供参照；
5. **韩国首尔数字媒体城**（Digital Media City）：文化—科技—消费融合的都市创新街区，为大钟寺智能原生新业态提供参照；
6. **中国深圳湾科技生态园**：以企业总部与生态服务聚合的高密度科技园区，为国际招引与资本转化提供参照。

以上案例的空间与机制经验——近校缝合、功能混合、开放测试、文化科技融合、公私合作——均转化为本方案的可读设计判断，不把外部经验表述为本地实施承诺 [source:AGENT-TASKBOOK]。

## 总体设计范围城市更新与控规深度城市设计

总体设计范围以「**一线三站两翼**」为空间结构，达到控制性详细规划的城市设计深度 [standard:MOHURD-CONTROL-DETAILED-PLANNING]。中央为京张遗址公园活力带（一线，绿色主轴）；自北向南布设加速站、原点站、场景站三处站核；东西两侧分别为中关村科技服务翼与小月河场景赋能翼 [data:geometry/land_use.geojson#LU-001] [depth:land_use_layout]。

用地方案按《国土空间调查、规划、用途管制用地用海分类指南》表达为 30 个无缝分区，覆盖总体设计边界且无重叠 [standard:MNR-LAND-USE-CLASSIFICATION-GUIDE]。用地构成以科研、文化、教育等公共管理与公共服务用地为主体（含 0802 科研、0803 文化、0804 教育），辅以商业服务业用地（05）、社区服务设施用地（0702）与公园绿地（1401），其中公园绿地沿遗址公园与清河、小月河形成蓝绿网络 [data:geometry/land_use.geojson#LU-001] [metric:green_ratio]。蓝绿与开敞空间约占总范围的 34%，支撑"公园城市"式创新交往环境 [metric:green_ratio]。

更新总体框架采用「**沿轨更新、近站增密、外缘织补**」：沿遗址公园主轴强化公共空间与步行骑行，围绕三处站核适度提升混合功能密度，在外缘社区与近校地带以低扰动方式织补服务与生活设施。建筑基底以重点站核的概念性楼群表达，区分保留、改造、更新、新建四类方向，具体拆改留结论待权属、控规与工程条件确认 [data:geometry/buildings.geojson#BLDG-001] [depth:retain_renovate_demolish]。容积率、建筑高度、建筑密度、退线、道路红线等法定控制条件缺失时，一律列为待正式控规条件确认，不以推测值冒充审定指标 [depth:development_intensity_controls]。

## 重点区域详细设计

三处重点区域按"定位＋空间结构＋建筑更新＋交通慢行＋公共空间＋AI 场景＋实施风险"组织详细设计，达到规划综合实施方案的城市设计深度 [depth:three_key_area_detailed_design]。三处 polygon 均为 provisional 临时范围，以下结论为方向性设计 [data:geometry/key_areas.geojson#PROV-KEY-001]。

### 加速站·众智园 AI 自主创新加速区（192.1 公顷）

**定位**：花园型全栈自主创新街区，承载国家人工智能平台与自主创新、标准制定、安全治理与产业展示。**空间结构**：以清河界面为北向生态门户，以中央绿地承载开放测试与低碳创新交往 [data:geometry/key_areas.geojson#PROV-KEY-001] [metric:zhongzhiyuan_ai_acceleration_area_sqm]。**建筑更新**：围绕全栈研发楼群组织"研发—测试—展示"一体簇群。**交通慢行**：强化北五环方向对外交通与站区慢行接驳。**公共空间**：加速广场、清河低碳创新廊 [data:geometry/public_space.geojson#PUBLIC-003]。**AI 场景**：自主模型测试场、标准治理展示、低碳算力体验（详见场景卡 02、06）。**实施风险**：清河蓝线与防洪条件、对外交通组织需专业复核。

### 原点站·北京 AI 原点社区（104.3 公顷）

**定位**：近校型成果转化与人才社区，汇聚高校策源、开源协作、人才特区与品牌活动。**空间结构**：组织校区、园区、街区慢行缝合，以原点发布广场为社区客厅 [data:geometry/key_areas.geojson#PROV-KEY-002] [data:geometry/public_space.geojson#PUBLIC-002]。**建筑更新**：近校孵化楼群、发布厅集群与居住生活配套，保留改造新建并举。**交通慢行**：清华东路西口与校区慢行联系、轨道站点一体化。**公共空间**：原点发布广场、清华园火车站文化节点。**AI 场景**：开源发布厅、近校成果转化街、AI 教育体验点（场景卡 01、07）。**实施风险**：校区边界、权属与首层业态需逐地块确认。

### 场景站·大钟寺 AI 产业集聚区（72.0 公顷）

**定位**：城市型智能经济与国际交往街区，承载智能体、智能终端、内容消费、数据要素与商业服务。**空间结构**：以大钟寺站为枢纽组织四象限步行连通，以智能经济街区楼群承接领军企业与国际路演 [data:geometry/key_areas.geojson#PROV-KEY-003] [metric:dazhongsi_ai_industry_cluster_area_sqm]。**建筑更新**：大钟寺智能经济街区楼群、东商务楼群，首层面向展示与消费。**交通慢行**：大钟寺站一体化、四象限地下与地面步行连通。**公共空间**：大钟寺场景广场 [data:geometry/public_space.geojson#PUBLIC-001]。**AI 场景**：智能体与智能终端展示、数据要素会客厅、国际路演（场景卡 05、08）。**实施风险**：站点一体化、道路交叉口与市政管线需专项复核。

![三处重点区域索引与设计任务图](assets/figures/key-areas.png)

## AI 创新生态、人才画像与 AI+ 场景

### 五类用户画像（agent.3）

| 画像 | 典型需求 | 空间响应 | 自检边界 |
| --- | --- | --- | --- |
| 开源开发者 | 发布、协作、测试、社区声誉 | 原点站开源发布厅、公共代码墙、夜间协作空间 | 不采集个人行为轨迹，活动数据仅聚合统计 |
| 初创团队 | 低成本办公、算力入口、产品试验场 | 加速站共享测试场、端侧算力服务点、标准治理咨询 | 算力与数据服务需另行授权 |
| 头部企业访客 | 展示、商务、国际接待、人才招聘 | 场景站国际路演客厅、轨道接驳、重点企业周边公共空间 | 企业标识与案例须清权 |
| 周边居民 | 通勤、休闲、社区服务、低扰动更新 | 遗址公园慢行环、社区服务嵌入、照明与活动分级 | 不将居民画像用于商业推荐 |
| 高校师生 | 成果转化、跨校协作、日常慢行 | 校区—园区慢行缝合、成果转化驿站、AI 教育体验点 | 校园数据与科研成果需授权 |

### AI 场景卡（12 张，含 3 张产业测试验证场景）

| # | 场景卡 | 类型 | 空间载体 | 设计说明 |
| --- | --- | --- | --- | --- |
| 01 | 开源发布厅 | 社区/展示 | 原点站发布广场 | 成果发布、代码贡献展示、小型路演 [data:geometry/public_space.geojson#PUBLIC-002] |
| 02 | 自主模型测试场 | **测试验证** | 加速站中央绿地 | 模型红队测试、安全评测、标准制定工作坊 [data:geometry/green_space.geojson#GREEN-001] |
| 03 | 产业验证沙盒 | **测试验证** | 加速站研发簇群 | 端侧算力、工业场景验证、可预约可监管 |
| 04 | AI 慢行导航 | 城市/交通 | 遗址公园活力带 | 可解释导视、低侵入传感识别慢行断点 [data:geometry/roads.geojson#ROAD-001] |
| 05 | 国际路演客厅 | 展示/运营 | 场景站广场 | 智能体与智能终端展示、媒体发布、国际交流 |
| 06 | 清河低碳创新廊 | 蓝绿/产业 | 加速站清河界面 | 绿色空间、雨洪、骑行与 AI 展示复合 |
| 07 | 近校成果转化街 | 产业/服务 | 原点站近校街区 | 孵化、展示、法务、知识产权、投融资服务 |
| 08 | 数据要素会客厅 | **测试验证** | 场景站商务区 | 数据要素流通、数字资产展示，合规可审计 [data:geometry/land_use.geojson#LU-001] |
| 09 | AI 生活服务样板街 | 城市/生活 | 社区商业交汇处 | 医疗、教育、法律、生活服务等 AI+ 场景 |
| 10 | 智能公共健身场 | 城市/公共空间 | 遗址公园北段 | 运动数据本地处理、不采集生物特征 |
| 11 | 全球 AI 活动周路线 | 运营/传播 | 一带公共空间系统 | 从遗址文化、开源社区、产业展示到国际路演的可步行路线 [data:geometry/phasing.geojson#PHASE-001] |
| 12 | 站台文化导览 | 文化/导视 | 三站站核 | 京张铁路—中关村—AI 新文化的站点叙事导览 |

所有场景均说明服务对象、空间位置、数据来源、隐私边界、人工复核与运营主体，遵守数据最小化、可解释与人工复核原则；不把未成熟技术写成已可全面部署，不把测试场景写成已批准运营 [source:AGENT-TASKBOOK] [depth:metrics_recalculation]。场景节点与空间、图层和指标联动，可在地图、HTML 与 A3/A0 中检索。

## 用地、建筑规模与拆改留方案

用地方案由 `geometry/land_use.geojson` 的 30 个无缝分区表达，依据《国土空间调查、规划、用途管制用地用海分类指南》分类 [standard:MNR-LAND-USE-CLASSIFICATION-GUIDE] [data:geometry/land_use.geojson#LU-001]。科研用地（0802）约 2.38 km²、文化用地（0803）约 0.74 km²、教育用地（0804）约 1.18 km²、商业服务业用地（05）约 1.43 km²、社区服务设施用地（0702）约 1.80 km²、公园绿地（1401）约 3.88 km² [metric:land_use_1401_area_sqm]。公园绿地比例约 0.34，蓝绿与开敞空间构成创新交往的公共基底 [metric:green_ratio]。

建筑规模以重点站核的概念性楼群基底表达，总基底面积约 15.2 万平方米，均位于可设计地块内 [data:geometry/buildings.geojson#BLDG-001] [metric:building_footprint_area_sqm]。建筑密度约 0.013 仅反映重点站核楼群，不构成全区建筑密度结论；总建筑面积、容积率、建筑高度等法定指标因缺少官方控规条件而列为待确认 [depth:development_intensity_controls] [metric:floor_area_ratio]。拆改留采用"保留—改造—更新—新建"四类方向表达，具体地块结论待权属、现状建筑与控规条件确认 [depth:retain_renovate_demolish]。

## 交通、轨道、市政与公共服务设施

交通方案回应轨道站点一体化、道路微循环、慢行断点与绿色交通要求 [depth:traffic_rail_slow_parking]。以遗址公园主廊道为南北慢行主轴（道路中心线表达示意，不代表道路红线）[data:geometry/roads.geojson#ROAD-001]，以大钟寺站、原点站、加速站三处横向联系路组织东西缝合与站区接驳 [data:geometry/roads.geojson#ROAD-002]。道路面积按主干道半宽 20 米、次干道半宽 15 米示意缓冲约 0.043 的道路比例，具体道路红线与断面待正式条件确认 [metric:road_ratio]。

市政与公共服务覆盖创新服务平台、人才生活服务、新型基础设施、分布式能源、端侧算力与传统市政融合 [depth:municipal_new_infrastructure]。端侧算力驿站、分布式能源与 AI 公共服务节点作为待深化的新基建原型，管线、能源、排水、防洪、消防等工程条件缺失时列为正式深化前置条件 [data:geometry/constraints.geojson#CONSTR-001]。

![交通慢行与蓝绿公共空间复合系统图](assets/figures/mobility-bluegreen.png)

## 蓝绿空间、公共空间与城市风貌

蓝绿空间以京张遗址公园活力带为骨架，统筹清河、小月河与周边高校、企业、社区出行需求，形成南北贯通、东西连通的公园绿地体系 [data:geometry/green_space.geojson#GREEN-001] [depth:blue_green_public_space]。公共空间以三处站核广场与遗址公园站台广场组成公共空间网络，广场与开敞空间比例约 0.034 [metric:public_space_ratio] [data:geometry/public_space.geojson#PUBLIC-001]。

城市风貌融合京张铁路历史文化、中关村创新文化与 AI 新文化，形成"**铁轨记忆—创新里坊—AI 站点**"三段式叙事 [standard:MOHURD-URBAN-DESIGN-MEASURES] [depth:height_massing_character]。提出三个 AI 朝圣地标／荣誉展示节点（agent.4）：**加速站·创新之光**（众智园标准治理与自主创新成果展示塔）、**原点站·代码之柱**（北京 AI 原点社区的开源贡献荣誉墙与发布柱）、**场景站·对话之门**（大钟寺国际路演与数据要素展示门厅）。地标、导视、Logo、字体、图像、人物与企业标识均须清权，且为概念建议，不得表述为已批准建设 [source:AGENT-TASKBOOK]。

文化叙事（agent.5）：以"百年自主工程—中关村创业精神—AI 新文化"为时间轴，建立导视标识、文化符号与公共艺术引导体系，区分文化标识系统与一带整体 Logo 系统，面向国际传播形成「NEXT STOP JINGZHANG」站点叙事。

## 更新项目清单、实施政策与分期计划

更新项目清单如下，均注明位置、类型、依赖与实施风险 [depth:renewal_project_list]：

| 项目 | 名称 | 类型 | 主要依赖 |
| --- | --- | --- | --- |
| JZ-01 | 京张遗址公园慢行断点缝合 | 公共空间/交通 | 道路红线、桥下空间、交通组织复核 [data:geometry/roads.geojson#ROAD-001] |
| JZ-02 | 加速站清河创新界面 | 蓝绿/产业展示 | 河道蓝线、生态与防洪条件 [data:geometry/green_space.geojson#GREEN-001] |
| JZ-03 | 原点站近校成果转化街 | 城市更新/产业服务 | 校区边界、权属、首层业态 [data:geometry/buildings.geojson#BLDG-003] |
| JZ-04 | 场景站四象限步行连通 | 轨道一体化/慢行 | 轨道站点、道路交叉口、市政管线 [data:geometry/public_space.geojson#PUBLIC-001] |
| JZ-05 | AI 公共服务与端侧算力节点 | 新基建/公共服务 | 能源、算力、安全与运营主体 [data:geometry/constraints.geojson#CONSTR-001] |
| JZ-06 | 全球 AI 活动周公共路线 | 运营/品牌 | 公共空间许可、活动安全、版权清权 [data:geometry/phasing.geojson#PHASE-001] |

分期计划与 100 天征集周期区分：征集周期是成果提交的时间要求，实施分期是城市更新推进路径 [depth:phasing_implementation]。**近期试点**（场景站及南段，约 1.61 km²）优先以轻量设施、运营活动与服务平台启动 [data:geometry/phasing.geojson#PHASE-001]；**中期更新**（原点站与中区，约 7.54 km²）推进近校转化与社区织补 [data:geometry/phasing.geojson#PHASE-002]；**长期治理**（加速站与北段，约 2.26 km²）伴随正式控规、市政与权属条件成熟后深化 [data:geometry/phasing.geojson#PHASE-003]。

长期运营设计（agent.6）：提出「全球 AI 活动周—开发者开放日—站台系列发布」的年度活动体系，建立活动品牌与传播视觉系统；开发者社区以开源贡献、场景开放日与站台发布机制运营；公共体验沿遗址公园慢行路线组织；国际传播与招引转化以站台叙事、路演客厅与资本对接通道承接。所有活动、招商、资金、政策与运营安排均表述为概念建议或深化方向，不得写成已确定政府安排 [source:AGENT-TASKBOOK]。

## 指标体系、面积复算与合规矩阵

指标体系覆盖空间指标、管控指标与绩效指标三类 [depth:metrics_recalculation]。空间指标由提交几何直接复算：总体设计范围约 11,412,825 平方米 [metric:site_area_sqm]，公园绿地比例约 0.340 [metric:green_ratio]，广场与公共空间比例约 0.034 [metric:public_space_ratio]，建筑基底约 151,691 平方米 [metric:building_footprint_area_sqm]，重点区域数量 3 处 [metric:key_area_count]，近期/中期/长期分期面积约 1.61/7.54/2.26 km² [metric:phase_near_term_area_sqm]。管控指标（容积率、建筑高度、建筑密度、退线、道路红线）因官方控规缺失列为待确认 [metric:floor_area_ratio]。绩效指标（AI 创新指数、人才密度、慢行可达性等）作为运营校准方向，不冒充审定规划条件。

合规矩阵覆盖公告 1.3、1.4、1.5 全部任务与 agent.1—agent.6，每条对应报告章节、图层、指标、图纸、HTML 页面、来源、假设与自检项 [depth:metrics_recalculation]。三处重点区域分别对应公告 1.5.3.1、1.5.3.2、1.5.3.3 [standard:PROJECT-OFFICIAL-ANNOUNCEMENT]。核心指标复算与证据链见图 [data:geometry/green_space.geojson#GREEN-001]。

![核心指标复算与证据链图](assets/figures/metrics-evidence.png)

## 风险、版权与合规说明

**双语言契约。** 本方案主语言为中文，配套完整英文译稿 `proposal.en.md`；渲染报告、可视化页面、A3/A0 图册与含文字图件均提供英文副本，优先使用赛事术语表 [depth:risk_missing_data]。

主要风险与待补资料：① 官方边界与重点区 polygon 缺失，本包以 provisional 范围表达，精度受临时粗略边界限制，官方发布后须全包复算 [source:BOUNDARY-SOURCE]；② 控规、道路红线、权属、市政、文保等法定条件缺失，相关结论均为方向性建议；③ 场景、活动与运营机制为概念建议，未经政府审定。所有图片、图纸、图标、数据与代码资产在 `report/copyright_statement.md` 与 `sources.json` 中说明来源、许可与授权状态。HTML 与可视化页面为纯离线静态文件，不加载远程脚本、瓦片、字体或外部 API，不跟踪评审者行为 [depth:risk_missing_data]。

本方案不声称官方批准、审定控规、最终土地权属、最终建设规模或保证实施；AI agent 对事实、来源、版权、空间数据、指标与表达负责，维护者与专业评审可依据自检结果、空间复核与合规矩阵要求返修或拒绝。

## 参考资料

1. 《百年京张AI创新带城市设计国际方案征集资格预审公告》，北京市规划和自然资源委员会海淀分局，2026-05-09 [standard:PROJECT-OFFICIAL-ANNOUNCEMENT]
2. 《关于面向全球智能体开展"百年京张AI创新带城市设计开源征集"的请示0518》摘录（用户提供清权任务书）[standard:PROJECT-AGENT-OPEN-CALL-TASKBOOK]
3. 《城市设计管理办法》，住房和城乡建设部，2017 [standard:MOHURD-URBAN-DESIGN-MEASURES]
4. 《城市、镇控制性详细规划编制审批办法》，住房和城乡建设部 [standard:MOHURD-CONTROL-DETAILED-PLANNING]
5. 《国土空间调查、规划、用途管制用地用海分类指南》，自然资源部，2023 [standard:MNR-LAND-USE-CLASSIFICATION-GUIDE]
6. 「三区两翼」打造世界级 AI 集聚地，北京市科委、中关村管委会，2026-04-03 [source:OFFICIAL-ANNOUNCEMENT]
7. 海淀区"1+X+1"现代化产业体系建设布局，海淀区人民政府，2026-03-02
8. Kendall Square（剑桥）、one-north（新加坡）、Brainport Eindhoven（荷兰）、Switzerland Innovation Park（瑞士）、Digital Media City（首尔）、深圳湾科技生态园——全球创新生态案例（公开背景资料，见 `sources.json`）
9. `brief/site-package/` 场地包：design_brief、agent_taskbook、allowed_design_space、planning_limits、standards、provisional_boundaries [source:SITE-PACKAGE]
10. `data/source_registry.json` 与 `data/processed/agent_fact_pack.md`（来源分级与阅读导航）[source:SOURCE-REGISTRY]
