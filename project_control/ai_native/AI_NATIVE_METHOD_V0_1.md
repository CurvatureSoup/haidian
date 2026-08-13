# AI-native 城市设施方法 v0.1

## 1. 定位与边界

总叙事为 **AI-native, not AI-dependent**。工程约束为 **AI-Ready, AI-Optional**：城市可以因 AI、机器人和自动驾驶成为物理使用者而改变，但人的安全、无障碍、基础服务权、停止权和最终决定权优先，且 AI 退出后城市仍可运行。

“AI 反向设计”正式定义为“AI 需求反推、由人治理的设施重构”。它不是让城市服从技术，也不赋予 AI 法律人格。该方法、ATS、R-Score 和阈值均为投稿者自定义的项目方法 v0.1，不是官方评分、国家标准或既有学术标准。

当前 `G1-DIR-001` 仍待人类决定，`DESIGN-START` 仍为 `BLOCKED`。本目录只定义方法、机器接口和纯合成测试，不包含真实设施方案、坐标、尺寸、造价或图件，不启动新增研究。

## 2. 设施范围与记录链

全集包括八类：道路/交叉口、路缘装卸区、建筑入口、停车设施、公园公共空间、灯杆/街道家具、市政物流节点、能源/边缘节点。首轮校准六类：道路、路缘、入口、公园、市政物流、能源/边缘节点；停车和灯杆为第二批。

每条记录必须回答：Who、非 AI 基准 B0、Why change、Physical change、Compatibility、AI-Native、AI-Degraded、AI-Off、基础服务 S_min、Second Life、ATS、R-Score、Boom/Fragmentation/Retreat、证据、假设、置信度和成熟度。反向设计先选择 `retain / adapt / reconstruct`；`retain` 是合法结果，不能为了高 ATS 制造无必要土建。

AI-native 的物理门要求 AI 使用者直接进入、穿越、停靠、排队、装卸、充电或占用容量，并至少有空间、尺度、结构或物理接口的一项可测改变。仅增加传感器、摄像头、软件或运营规则可以记录，但不得进入 High–High。

## 3. ATS

四个分项均为 0–5：`P` 空间/结构、`F` 功能组织、`I` 人机接口、`U` AI 作为实际物理使用者。

`ATS = 5 × (P + F + I + U)`。

High ATS 暂定为 `ATS >= 70`，并要求 `P >= 2`、`U >= 3`，必要性、公共价值、安全和无障碍四门均为 PASS。高 ATS 只表示改变强，不表示改变合理。

## 4. R-Score

R-Score 评价物理—运营可逆性：

`R = 20 × (0.30rq + 0.15rt + 0.15rc + 0.15rd + 0.15ro + 0.10rl)`。

- `rq`：AI-Off 即时服务保持率；
- `rt`：转换时间 / RTO；
- `rc`：转换成本 / 当前重置价值 CRV；
- `rd`：AI 专用且不可转用的搁浅资产比例；
- `ro`：开放接口、互操作和离线/人工替代；
- `rl`：Second Life 成熟度。

High R 暂定为 `R >= 80`，六项均不得低于 3。关键设施即时服务保持率必须达到 100%；非关键设施也必须达到其 S_min。时间、成本和搁浅资产均为反向项，由校验器按固定分档重算。

ATS 与 R 不相加。High–High 必须同时满足 ATS、R、四门、anti-sticker、AI 物理使用者、三未来全部 PASS、无 unknown；关键设施还须满足 100% 服务保持率。

## 5. 三态、Second Life 与三未来

AI-Degraded 固定检查网络、定位、模型、传感、供电和厂商接口六类故障，并记录触发、服务底线、控制权、安全状态、最长持续时间和恢复方式。AI-Off 保持基础服务，不要求保留全部 AI 专用服务；安全相关 AI 功能可以受控停运。

固定或长寿命资产必须有 `alternate_use`；可拆电子设备可以采用迁移、再利用或材料回收；混合资产至少包含一条不同用途路径。

三未来是不可相互补偿的 PASS/FAIL 门：Boom 检查容量与冲突；Fragmentation 检查多厂商、多标准和单云退出；Retreat 检查 AI 需求接近零且厂商支持退出。FAIL/unknown 可以诚实记录，但不得宣称 High–High。

## 6. 数据、图件和正式投稿映射

本目录的设施记录 schema 与校验器是项目控制工具。未来设计解锁后，同一记录派生到：

- `visual/assets/ai-native-facility-matrix.json`：完整矩阵；Manifest 0.2 登记为 `role=evidence_data`；
- `metrics.json`：设施及组合 ATS/R 指标，使用官方允许的 `index`/`ratio`；
- 既有 GeoJSON feature properties：设施 ID 和核心字段；不得新增几何文件或 layer；
- `proposal.md`、双语图件、A3/A0、离线 HTML：从同一矩阵派生；
- 十张卡固定映射为六类设施、三未来压力测试和一张 AI-Off/Second Life 转换卡，同时继续满足官方 persona 等硬要求。

正式新投稿使用 Manifest `schema_version=0.2.0`。除 manifest 自身外，文件条目具有 `path/role/required/sha256`；本地运行 `validate_local_submission.py ... --strict-manifest`。ready 包修改已登记文件后先运行 `refresh_submission_manifest.py`，再完整运行带 `--mark-self-checked --json` 的自检。空 constraints 可以登记数据缺口，不得编造控制几何。

## 7. 组合指标与校准

组合层报告八类设施的 ATS 中位数、关键设施最低 R、评价覆盖率，以及按 `capacity_group_id + unit` 分组的 High–High 服务容量占比。不同单位不得合并成一个总体容量占比。unknown 不按 0 插补，不得进入 High–High。

阈值和权重是 v0.1 工作参数。未来以首轮六类记录进行双评审、敏感性分析和校准；任一分项差异超过 1 分交 orchestrator 复核。原则参考 NIST AI RMF、NIST SP 800-160 Vol.2、ISO 20887 与 OECD/JRC 复合指标方法，但这些来源不定义本项目公式或阈值。

