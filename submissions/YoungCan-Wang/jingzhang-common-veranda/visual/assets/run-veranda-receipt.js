#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const defaultSource = path.join(__dirname, "..", "..", "simulation.json");
const defaultReport = path.join(__dirname, "veranda-receipt-report.json");
let source = defaultSource;
let reportPath = defaultReport;
let checkMode = false;
for (let i = 2; i < process.argv.length; i += 1) {
  const arg = process.argv[i];
  if (arg === "--check") checkMode = true;
  else if (arg === "--report") reportPath = process.argv[++i];
  else source = arg;
}
const simulation = JSON.parse(fs.readFileSync(source, "utf8"));
function evaluate(x) {
  const gates = [
    ["G0", x.authorized_for_tabletop && !x.real_world_run],
    ["G1", x.site_interface_recorded && x.access_egress_check_recorded],
    ["G2", x.synthetic_data && !x.personal_data],
    ["G3", x.rights_recorded],
    ["G4", x.steward_role_assigned && x.manual_takeover_rehearsed],
    ["G5", x.public_notice_complete && x.non_ai_route_available],
    ["G6", x.receipt_complete && x.exit_available && x.rollback_steps >= 5]
  ];
  for (const [gate, ok] of gates) if (!ok) return {decision:"stop", failed_gate:gate};
  return {decision:"pass", failed_gate:null};
}
const cases = simulation.tasks.map(task => {
  const actual = evaluate(task.inputs);
  return {task_id:task.task_id, expected:task.expected, actual,
    match:JSON.stringify(actual) === JSON.stringify(task.expected)};
});
const output = {
  runner:"visual/assets/run-veranda-receipt.js", generated_from:"simulation.json",
  tabletop_only:true, case_count:cases.length,
  expected_outcome_matches:cases.filter(x=>x.match).length,
  expected_outcome_match_rate:cases.filter(x=>x.match).length / cases.length,
  negative_stop_branches:cases.filter(x=>x.actual.decision === "stop").length,
  rollback_step_count:simulation.pilot_contract.rollback.length, cases,
  claim_limit:"Structure and stop/exit logic only; no real-world authorization, performance or safety claim.",
  boundary_disclosure:{
    status:"provisional_geometry",
    assumption_id:"A-BOUNDARY-001",
    statement:"Site and key-area geometry is provisional and is not an official redline, parcel, ownership boundary or approval basis.",
    metric_limit:"Areas and ratios support internal concept comparison only and are not statutory planning indicators.",
    replacement_trigger:"Replace geometry, recalculate metrics and regenerate every bilingual artifact when rights-cleared official vectors are supplied."
  }
};
function canonical(value) {
  if (Array.isArray(value)) return value.map(canonical);
  if (value && typeof value === "object") return Object.fromEntries(
    Object.keys(value).sort().map(key => [key, canonical(value[key])])
  );
  return value;
}
if (checkMode) {
  if (!fs.existsSync(reportPath)) {
    console.error(`report missing: ${reportPath}`);
    process.exitCode = 2;
  } else {
    const checked = JSON.parse(fs.readFileSync(reportPath, "utf8"));
    if (JSON.stringify(canonical(checked)) !== JSON.stringify(canonical(output))) {
      console.error(`report differs semantically: ${reportPath}`);
      process.exitCode = 2;
    }
  }
} else {
  fs.writeFileSync(reportPath, JSON.stringify(output, null, 2) + "\n");
}
console.log(JSON.stringify(output, null, 2));
if (output.expected_outcome_matches !== output.case_count) process.exitCode = 1;
