#!/usr/bin/env python3
"""Purely synthetic contract smoke; it is not a design or model-routing test."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VALIDATOR = ROOT / "validate_facility_records.py"


def run(data: dict, expected: str | None = None) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".json", encoding="utf-8", delete=False) as handle:
        json.dump(data, handle, ensure_ascii=False)
        path = Path(handle.name)
    try:
        proc = subprocess.run([sys.executable, str(VALIDATOR), str(path), "--json"], text=True, capture_output=True)
        payload = json.loads(proc.stdout)
        checks = {item["check_id"] for item in payload["issues"]}
        if expected is None:
            assert proc.returncode == 0 and payload["valid"], payload
        else:
            assert proc.returncode == 1 and expected in checks, (expected, proc.returncode, payload, proc.stderr)
    finally:
        path.unlink(missing_ok=True)


def main() -> int:
    template = json.loads((ROOT / "facility-record.template.json").read_text(encoding="utf-8"))
    valid = json.loads((ROOT / "synthetic-valid.json").read_text(encoding="utf-8"))
    run(template)
    run(valid)

    cases = []
    item = copy.deepcopy(valid); item["facilities"][0]["ats"]["total"]["value"] = 75; cases.append((item, "ATS_TOTAL_MISMATCH"))
    item = copy.deepcopy(valid); del item["facilities"][0]["compatibility"]; cases.append((item, "SCHEMA_INVALID"))
    item = copy.deepcopy(valid); item["facilities"][0]["r_score"]["components"]["rt"]["score"] = 0; cases.append((item, "R_COMPONENT_BUCKET_MISMATCH"))
    item = copy.deepcopy(valid); item["facilities"][0]["r_score"]["total"]["value"] = 80; cases.append((item, "R_TOTAL_MISMATCH"))
    item = copy.deepcopy(valid); item["facilities"][0]["r_score"]["raw"]["stranded_ai_asset_ratio"] = 0.5; cases.append((item, "R_COMPONENT_BUCKET_MISMATCH"))
    item = copy.deepcopy(valid); item["facilities"][0]["r_score"]["raw"]["ai_dedicated_asset_ratio"] = None; cases.append((item, "ASSESSMENT_STATUS_INCOMPLETE"))
    item = copy.deepcopy(valid); item["facilities"][0]["r_score"]["components"]["rl"]["score"] = 5; cases.append((item, "RL_MATURITY_MISMATCH"))
    item = copy.deepcopy(valid); item["facilities"][0]["physical_change"]["interventions"] = [{"kind":"sensor","description":"synthetic"}]; cases.append((item, "ANTI_STICKER_ATS"))
    item = copy.deepcopy(valid); item["facilities"][0]["physical_change"]["interventions"] = [{"kind":"sensor","description":"synthetic"}]; item["facilities"][0]["classification"] = {"declared_quadrant":"high_ats_only","high_high_eligible":False}; cases.append((item, "ANTI_STICKER_ATS"))
    item = copy.deepcopy(valid); item["facilities"][0]["users"]["ai_users"] = []; cases.append((item, "AI_PHYSICAL_USER_REQUIRED"))
    item = copy.deepcopy(valid); item["facilities"][0]["reverse_design"]["decision"] = "retain"; cases.append((item, "ELIGIBILITY_MISMATCH"))
    item = copy.deepcopy(valid); item["facilities"][0]["gates"]["safety"]["status"] = "fail"; cases.append((item, "ELIGIBILITY_MISMATCH"))
    item = copy.deepcopy(valid); item["facilities"][0]["gates"]["safety"]["status"] = "unknown"; cases.append((item, "ASSESSMENT_STATUS_INCOMPLETE"))
    item = copy.deepcopy(valid); item["facilities"][0]["futures"]["retreat"]["status"] = "fail"; cases.append((item, "ELIGIBILITY_MISMATCH"))
    item = copy.deepcopy(valid); item["facilities"][0]["futures"]["retreat"]["status"] = "unknown"; cases.append((item, "ASSESSMENT_STATUS_INCOMPLETE"))
    item = copy.deepcopy(valid); item["facilities"][0]["futures"]["retreat"]["required_capacity"] = None; cases.append((item, "ASSESSMENT_STATUS_INCOMPLETE"))
    item = copy.deepcopy(valid); item["facilities"][0]["operation_states"]["ai_degraded"]["network"]["status"] = "unknown"; cases.append((item, "ASSESSMENT_STATUS_INCOMPLETE"))
    item = copy.deepcopy(valid); item["facilities"][0]["second_life"]["paths"][0]["path_type"] = "reuse"; cases.append((item, "SECOND_LIFE_ASSET_RULE"))
    item = copy.deepcopy(valid); item["facilities"][0]["second_life"]["paths"][0]["status"] = "unknown"; cases.append((item, "ASSESSMENT_STATUS_INCOMPLETE"))
    item = copy.deepcopy(valid); item["facilities"][0]["basic_service"]["ai_off_immediate_capacity"] = 90; cases.append((item, "SERVICE_RETENTION_MISMATCH"))
    item = copy.deepcopy(valid); item["facilities"][0]["evidence_ids"] = ["E-MISSING"]; cases.append((item, "REFERENCE_UNRESOLVED"))
    item = copy.deepcopy(valid); item["facilities"].append(copy.deepcopy(item["facilities"][0])); cases.append((item, "FACILITY_ID_DUPLICATE"))
    item = copy.deepcopy(valid); item["facilities"][0]["classification"]["declared_quadrant"] = "low_low"; cases.append((item, "QUADRANT_MISMATCH"))
    item = copy.deepcopy(valid); item["portfolio_summary"]["evaluation_coverage_pct"]["value"] = 50; cases.append((item, "PORTFOLIO_COVERAGE_MISMATCH"))
    item = copy.deepcopy(valid); item["portfolio_summary"]["facility_class_ats_medians"][0]["value"] = 70; cases.append((item, "PORTFOLIO_MEDIAN_MISMATCH"))
    item = copy.deepcopy(valid); item["portfolio_summary"]["high_high_capacity_shares"][0]["value_pct"] = 50; cases.append((item, "PORTFOLIO_CAPACITY_SHARE_MISMATCH"))
    for data, check in cases:
        run(data, check)

    duplicate = '{"schema_version":"0.1.0","schema_version":"0.1.0"}'
    with tempfile.NamedTemporaryFile("w", suffix=".json", encoding="utf-8", delete=False) as handle:
        handle.write(duplicate); path = Path(handle.name)
    try:
        proc = subprocess.run([sys.executable, str(VALIDATOR), str(path), "--json"], text=True, capture_output=True)
        payload = json.loads(proc.stdout)
        assert proc.returncode == 2 and payload["issues"][0]["check_id"] == "JSON_DUPLICATE_KEY"
    finally:
        path.unlink(missing_ok=True)
    print("SYNTHETIC_METHOD_CONTRACT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
