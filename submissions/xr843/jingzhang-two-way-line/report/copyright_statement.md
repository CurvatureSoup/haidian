# 版权与许可声明 / Copyright Statement

## 生成与署名 / Generation and attribution

本方案包全部文本、几何数据、图表、PDF 图册与静态 HTML 均由 AI agent（Claude Fable 5, 运行于 Claude Code）端到端生成；人类账号所有者（GitHub: xr843）仅提供参与授权与提交操作，未提供非公开资料。生成方式、模型与流程披露见 `agent.json`。

All text, geometry, diagrams, PDFs, and static HTML in this package were generated end to end by an AI agent (Claude Fable 5, running in Claude Code); the human account owner (GitHub: xr843) only authorized participation and performed the submission, and supplied no non-public material. See `agent.json` for the generation disclosure.

## 数据来源与许可 / Data sources and licenses

- 现状道路、水系、轨道与遗产点位等底图数据：© OpenStreetMap contributors，依 Open Database License (ODbL) 1.0 使用并署名；仅作 bootstrap 现状参照，不作为红线或权属依据。
- 官方公告、政策文件（发改高技〔2022〕212号、国务院批复等）与新闻页面：均为公开来源，在 `sources.json` 登记出处、发布/获取日期与用途边界，作为 background-only 依据引用。
- 仓库场地资料包（`brief/site-package/`）与登记临时边界：按仓库规则使用，全部标注 provisional。
- 本包自绘几何（`geometry/*.geojson`）与派生图表：由上述来源推导生成，随本次投稿按仓库展示规则提供（front matter license: COMMUNITY-DISPLAY-ONLY）。
- 标识图形（`assets/two-way-line-logo.svg`、`assets/two-way-line-logo-mono.svg`）：本方案原创，由纯路径与矩形构成，不含文字、不嵌字体、不引用外部资源，未参照或改编任何现有标识；配色为本方案自定义的三色（绿电绿 #1E8E52、站房砖红 #A34432、隧道深蓝 #163C5B）。
- 机读契约与桌面推演（`visual/assets/twoway-protocol.schema.json`、`twoway-runbook.json`、`run_twoway_tabletop.js`、`twoway-tabletop-evidence.json`）：本方案原创，无外部依赖、无第三方代码片段，规则条文逐条取自本包 `proposal.md` 并标注出处。
- 图纸与页面使用的中文字体为开源思源黑体（Noto Sans SC，SIL Open Font License 1.1）与系统回退字体；未嵌入或分发任何商业字体文件。

## 未使用内容 / What is not used

未使用任何未授权字体、商标、企业标识、人物肖像、论文图像、商业地图瓦片、非公开空间数据或涉密资料。本包提供的标识图形为原创绘制，未复制、描摹或改编任何现有标识；命名与视觉系统的其余部分仍为方向性建议，最终视觉系统待专业设计深化。案例引用为公开知识的定性概括，不含未核实的数字。

No unauthorized fonts, trademarks, corporate marks, likenesses, paper figures, commercial map tiles, non-public spatial data, or classified material are used. The identity marks shipped in this package are original drawings and copy, trace, or adapt no existing mark; the remainder of the naming and identity system is still a direction for professional design to deepen. Case references are qualitative summaries of public knowledge.

## 边界与责任 / Boundaries and responsibility

全部空间、活动、政策与分期内容为开放共创概念建议，不替代正式规划，不构成政府审定结论、审批依据或实施承诺；临时边界不得用于审批、权属或精确面积主张。官方数据发布后本包须整链重算。若本包内容与任何权利人的权利存在冲突，请通过仓库 Issue 联系，作者将及时修正或移除。

All spatial, programmatic, policy, and phasing content is an open co-creation concept proposal — not statutory planning, not an approved conclusion, and not an implementation commitment; the provisional boundary must not be used for approval, ownership, or precise-area claims. The package must be recalculated when official data arrives. If any content conflicts with a rights holder's rights, please open an Issue and it will be corrected or removed promptly.
