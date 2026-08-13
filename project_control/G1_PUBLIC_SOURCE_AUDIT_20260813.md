# G1 公开网络资料尽调（2026-08-13）

## 结论

公开网络上**没有**覆盖约 11.4 平方公里总体设计范围和三个重点区的完整、正式、可下载 GIS/CAD 底包，也没有公开的组织方正式任务书密码包。公开资料并非空白，而是呈现四层结构：

1. 官方公告和规划进度可确认任务范围、约面积、规划状态与部分定性结论；
2. 大钟寺局部的蓝景丽家项目公开了较完整的宗地、测量、市政交通、噪声和规划指标附件；
3. 北京公共数据平台可补公园、医疗、养老、步道等名录，但时效、坐标和容量字段不完整；
4. OSM、Microsoft 建筑数据等可补现状道路/建筑的工作底图，但只能是 `existing_condition` 或 `agent_inferred_from_public_data`，不能充当规划红线、权属或正式建筑调查。

因此，不能通过“把公开碎片拼起来”制造完整官方基线；但可以在人类批准后建立一套分层、可替换、非正式的公开数据基线。

## 正式竞赛附件可得性

- 官方资格预审公告明确：资格预审文件须先下载领取登记表并发送至征集邮箱，组织机构再发送下载密码；领取期为 2026-04-30 至 2026-05-12。
- 资格预审对象要求合法注册法人或联合体，并具有相应资质和业绩。当前用户作为公开 GitHub 参赛人员，不应冒充机构、倒填登记或绕过密码流程。
- GitHub 开放投稿规则明确容许官方 polygon 缺失时使用诚实标注的 provisional geometry；缺失不等于可以把 provisional 或公开拼接数据升级为官方资料。

结论：密码包不是当前可无条件取得的公开资料；本轮不发送邮件、不提交身份或机构信息、不尝试绕过访问控制。

## 九类缺口尽调结果

| 缺口 | 公开资料状态 | 当前能做 | 不能做 |
|---|---|---|---|
| `GAP-BOUNDARY-001` 三层范围 | 只有官方文字四至和约面积；未找到 polygon | 建立宽松发现范围、保存公告口径 | 正式裁剪、精确面积和官方红线声明 |
| `GAP-BOUNDARY-002` 三重点区 | 未找到 official KEY_AREA polygon；仓库 provisional 存在明显位置争议 | 按地名和官方文字做目录检索 | 用现有 provisional 做车站级详细判断或称其官方范围 |
| `GAP-CONTROL-001` 控规 | 草案采信通告公开；2026-04-30 官方进展为“已通过市级部门联审、推进获批实施” | 证明控规存在、状态及部分道路节点结论；用上位规划做结构背景 | 把草案/联审当已批控规，填造全域 FAR、高度、密度或控制线 |
| `GAP-ROAD-001` 道路 | 控规通告有道路等级与节点形式；蓝景丽家有局部道路和市政交通附件；OSM 有现状路网 | 局部项目事实、现状中心线和拓扑试跑 | 用 OSM buffer 冒充道路红线；把局部线位推广全域 |
| `GAP-PARCEL-001` 宗地权属 | 完整权属依法不向社会主动公开；公共资源交易只覆盖逐宗事件 | 登记蓝景丽家等公开交易宗地及其时点 | 拼成完整权属图层或推断未公开权属 |
| `GAP-BUILDING-001` 建筑 | 未找到全域官方现状调查；OSM/Microsoft 可提供推定轮廓，Microsoft 另有密度/高度栅格 | 覆盖率、处理链和几何质量试跑 | 将机器识别高度/轮廓写成官方测绘或直接判拆改留 |
| `GAP-HERITAGE-001` 文保 | 清华园车站旧址保护范围及建控地带文字四至主动公开；正式图纸“另行印发”但未公开取得 | 将法定文字作为硬约束文本；必要时生成明确 provisional 的推定面 | 无官方本体坐标时声称精确保护 polygon |
| `GAP-MUNICIPAL-001` 市政安全 | 蓝景丽家公开局部市政交通、水影响、地震、地灾和噪声附件；全域专项未公开 | 建立局部案例事实和字段模板 | 推广为整个创新带的管线、消防、防洪或承载结论 |
| `GAP-SERVICE-001` 公服 | 北京/海淀开放数据有医疗、养老、公园、步道等名录，部分数据较旧或需登录 userKey 调 API | 无条件下载文件和公开页面可做名录试跑，逐项记录时效 | 假设名录完整、把地址当测绘坐标或编造容量 |

## 重点公开来源

### 1. 官方规划与范围

- 征集公告：<https://ghzrzyw.beijing.gov.cn/zhengwuxinxi/tzgg/hd/202605/t20260509_4643047.html>
- 京张沿线街区控规草案采信通告：<https://ghzrzyw.beijing.gov.cn/chengxiangguihua/ghlgg/hd_ghlgg/202502/t20250207_4005553.html>
- 2026 年一季度规划重点任务进展：<https://zyk.bjhd.gov.cn/jbdt/auto4523/zdrw/202604/t20260430_4813611_hd.shtml>
- 海淀分区规划 PDF：<https://ghzrzyw.beijing.gov.cn/zhengwuxinxi/ghcg/fqgh/202002/P020200213595742434523.pdf>

关键判断：截至公开进展页，京张沿线街区控规是“通过市级部门联审、推进获批实施”，不是已公开获批成果。

### 2. 大钟寺局部正式碎片

- 蓝景丽家公共资源交易公告及 17 项附件：<https://ggzyfw.beijing.gov.cn/zpgcrgg/20251231/5391270.html>
- 市政交通规划综合方案 PDF：<https://ggzyfw.beijing.gov.cn/cmsbj/u/cms/cn.gov.bjggzyfw.www/202601/8651375391270.pdf>
- 多规合一初审意见：<https://ggzyfw.beijing.gov.cn/cmsbj/u/cms/cn.gov.bjggzyfw.www/202601/9874635391270.pdf>
- 建设工程规划用地测量条件：<https://ggzyfw.beijing.gov.cn/cmsbj/u/cms/cn.gov.bjggzyfw.www/202601/8132045391270.pdf>
- 大钟寺更新片区公示：<https://www.beijing.gov.cn/fuwu/lqfw/ztzl/bjchshgx/xmgsh/202607/t20260714_4762615.html>

这些材料覆盖蓝景丽家约 5.03/7.97 公顷级局部项目，不能代表约 72 公顷大钟寺重点区，更不能代表全域。

### 3. 文保与公园

- 清华园车站旧址：<https://wwj.beijing.gov.cn/bjww/362771/362782/743928533/743928745/index.html>
- 第十一批文保范围通知：<https://wwj.beijing.gov.cn/bjww/362690/2024zcwj/743748025/index.html>
- 京张公园规划解读：<https://ghzrzyw.beijing.gov.cn/zhengwuxinxi/zxzt/wsghs/2021dej/d5j/202112/t20211216_2562970.html>
- 京张公园二期进展：<https://www.beijing.gov.cn/ywdt/gqrd/202409/t20240920_3902264.html>

### 4. 公共服务与开放底图

- 北京市公共数据开放平台：<https://data.beijing.gov.cn/>
- 海淀数据开放：<https://zyk.bjhd.gov.cn/sjkf/>
- 天地图·北京：<https://beijing.tianditu.gov.cn/?type=4>
- Microsoft Global ML Building Footprints：<https://github.com/microsoft/GlobalMLBuildingFootprints>
- Microsoft 建筑密度与高度数据：<https://github.com/microsoft/buildings>
- OpenStreetMap 许可：<https://www.openstreetmap.org/copyright>

许可边界：OSM 和部分 Microsoft footprint 为 ODbL；Microsoft 密度/高度数据为 CDLA Permissive 2.0。正式使用前要确认具体产品、版本、归属和衍生数据库义务，不能把两个 Microsoft 产品的许可混写。

### 5. 社区交叉核查

- Issue #1774 对六类公开约束来源做了 50 个 URL 的可达性审计，结论与本轮一致：文保文字最强，控规中等，宗地最低；该 Issue 是参与者索引，不是官方来源：<https://github.com/open-city-ai/haidian/issues/1774>
- Issue #846 仍显示总体 provisional 与 OSM 公园不相交、最近约 412.5 m：<https://github.com/open-city-ai/haidian/issues/846>
- Issue #1029 显示 `PROV-KEY-003` 质心落在北京北站附近、距大钟寺站约 2.26 km：<https://github.com/open-city-ai/haidian/issues/1029>

## 若没有完整官方资料，下一步如何做

### A. 分层公开基线（推荐）

建立四层而不是伪造一张“完整底图”：

- L0：官方文本、法律状态、发布日期和限制；
- L1：蓝景丽家等官方项目碎片，只在其真实空间和时点内使用；
- L2：OSM/Microsoft/开放名录作为 `existing_condition` 或 `agent_inferred`，保存原始查询、版本、许可和哈希；
- L3：官方边界、权属、全域控规红线和全域市政继续为空，并写机器可读 `data_gap`。

下一执行批次只做数据工程：下载和哈希选定官方附件，宽松范围获取现状道路/建筑，做覆盖率与字段质量报告，建立替换复算脚本；不做城市设计、法定指标或拆改留。

### B. 官方碎片优先

只下载官方网页/PDF和无条件开放名录，不使用 OSM/Microsoft 建筑数据。证据风险最低，但建筑、道路和服务空间覆盖长期保持严重缺失，难以提前验证 GIS 管线。

### C. 先尝试外部询问

暂停数据获取，由人类授权后以公开参赛者身份向 GitHub 维护者或组织方提出一个聚焦问题：是否会提供正式范围、重点区锚点或去敏后的任务附件。不得声称具有法人资质，也不索要或传播受限密码包。回复仍只是一条线索，需按来源等级复核。

## 建议决策门

`G1-BASELINE-DEPTH-001`：选择 A、B 或 C。

推荐 A，因为当前官方规则已经允许诚实披露官方缺数，且 A 能尽早验证数据处理链；同时通过 L0–L3 分层避免把开放底图冒充官方资料。A 的代价是要承担 ODbL/CDLA 归属、较大数据量、双轨版本和未来整体复算。

无论选择哪项，`DESIGN-START` 均不自动解除。
