# 生成与迭代说明 / Generation and iteration note

本包围绕一个窄问题生成：一项公共服务究竟在哪个具体动作才可能需要知道使用者是谁。它不再把“免App”当作创新主轴，也不再建立另一套服务等价综合指数，而是交付M0-M3身份门槛、敏感信息S覆盖闸、12项字段级ledger和空间柜台剖面。

The package asks one narrow question: at which exact transaction step may a public service need to know who the user is? It delivers an M0-M3 threshold model, an orthogonal sensitive-data overlay, twelve field-level ledgers, and spatial counter sections. Every M2/M3 gate remains unverified until a responsible service entity and legal review confirm it.

Generation used public repository material and primary public sources only. No site visit, stakeholder interview, non-public map, personal data, remote map tile, third-party photograph, logo, or rendered architectural image is included.

## 本包的机器可读指标约定 / Package-local machine-readable metric convention

仓库的 `brief/site-package/schemas/metrics.schema.json`（`0.1.x`）规定了 `status`、`value` 与未知值所需的 `reason`，同时允许单项指标携带扩展字段；但它目前没有正式定义 `metric_kind` 或 `design_target`。因此，下列写法只是本投稿包为避免“现状值／概念推导值／设计目标”互相混淆而采用的局部约定，不代表主办方或仓库级标准：

- 可复算的包内结果使用 `status: "known"` 和数值型 `value`。若它来自 provisional 概念几何或设计参数，同时标记 `metric_kind: "conceptual_derived"`；这里的 known 仅表示“可在本包假设内复算”，不表示官方现状数据或建设承诺。
- 尚未取得现场基线的设计目标使用 `status: "unknown"`、`value: null`、`confidence: "unknown"` 和非空 `reason`，目标值单独写入数值型 `design_target`，并标记 `metric_kind: "design_target"`。
- `value` 只承载由 `status` 描述的当前值或包内派生值；`design_target` 只承载待验证目标。即使读取程序忽略扩展字段，也应把这类目标的当前值显示为 unknown，而不能显示成已经达成的成绩。

The repository schema `brief/site-package/schemas/metrics.schema.json` (`0.1.x`) defines `status`, `value`, and the `reason` required for unknown values, while allowing additional properties on each metric. It does not currently standardize `metric_kind` or `design_target`. The following is therefore a package-local convention, not an organizer- or repository-wide standard:

- A result reproducible within the package uses `status: "known"` and a numeric `value`. If it comes from provisional concept geometry or design parameters, it also uses `metric_kind: "conceptual_derived"`; known then means reproducible under package assumptions, not official existing-condition data or a development commitment.
- An unmeasured design target uses `status: "unknown"`, `value: null`, `confidence: "unknown"`, a non-empty `reason`, a numeric `design_target`, and `metric_kind: "design_target"`.
- `value` carries only the current or package-derived value described by `status`; `design_target` carries the criterion to be tested. A consumer that ignores extension fields should still report the current value as unknown rather than as an achieved result.

This convention is applied to `identity_before_confirmed_step_target`, `offline_completion_target`, and `total_floor_area_sqm` in `metrics.json`.
