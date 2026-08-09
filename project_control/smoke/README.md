# Multi-Agent Smoke Test

只执行以下三个微型任务。每个任务必须写入自己的文件，不得修改其他结果，不得扩展为正式研究或设计。

## SMOKE-L1 — librarian

将以下三条记录按 `source_id` 去重，保留更新时间较新的记录；统一状态为小写，输出 JSON：

```text
SRC-A | Public Brief | AVAILABLE | 2026-08-08
SRC-A | Public Brief v2 | available | 2026-08-09
SRC-B | Taskbook | AVAILABLE | 2026-08-09
```

输出：`project_control/smoke/librarian_result.json`

固定字段：`task_id`、`producer_agent`、`configured_model`、`runtime_model_evidence`、`records`、`duplicates_removed`、`escalation_required`。不得联网，不得解释资料含义。

## SMOKE-L2 — researcher

只读取 `brief/public-brief.md` 和 `brief/site-package/agent_taskbook.json`，用不超过 180 个中文字比较两者对“公开共创边界”的共同点与差异。不得检索外部资料，不得提出空间方案。

输出：`project_control/smoke/researcher_result.md`，包含 task、configured model、runtime model evidence、共同点、差异、来源路径、是否升级。

## SMOKE-L3 — evidence_planner

只读取最新 `skills/urban-design-ai-submission/SKILL.md` 和 `docs/formal-submission-guide.md`，判断以下说法是否允许，并用不超过 180 个中文字说明理由：

> “在缺少官方 polygon 时，可把 provisional boundary 当作官方红线并据此给出最终法定指标。”

输出：`project_control/smoke/evidence_planner_result.md`，包含 task、configured model、runtime model evidence、结论、证据路径、规划影响、是否升级。不得生成方案。

## 总控汇总

总控读取三个结果后写入 `project_control/smoke/orchestrator_summary.md`，逐项记录 configured model、可核实的实际模型、PASS/FAIL/BLOCKED 和限制。只有存在运行时证据时才能声称模型路由通过。
