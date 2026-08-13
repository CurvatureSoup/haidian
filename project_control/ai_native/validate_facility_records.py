#!/usr/bin/env python3
"""Validate AI-native facility records without modifying the input."""

from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from pathlib import Path
from typing import Any

import jsonschema

VALIDATOR_VERSION = "0.1.0"
METHOD_VERSION = "ai-native-facility-v0.1"
CLASSES = (
    "road_intersection", "curb_loading", "building_entrance", "parking",
    "park_public_space", "lamp_street_furniture", "municipal_logistics", "energy_edge_node",
)
WAVE_ONE = {"road_intersection", "curb_loading", "building_entrance", "park_public_space", "municipal_logistics", "energy_edge_node"}
PHYSICAL_ACTIONS = {"enter", "traverse", "dock", "queue", "load", "unload", "occupy_capacity", "charge"}
SUBSTANTIVE_KINDS = {"space", "scale", "structure", "physical_interface"}
TOL = 1e-6


class DuplicateKeyError(ValueError):
    pass


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def close(a: float, b: float) -> bool:
    return math.isclose(a, b, rel_tol=TOL, abs_tol=TOL)


def bucket_retention(value: float) -> int:
    return 5 if value >= 100 else 4 if value >= 90 else 3 if value >= 75 else 2 if value >= 50 else 1 if value >= 25 else 0


def bucket_time(value: float) -> int:
    return 5 if value <= .10 else 4 if value <= .25 else 3 if value <= .50 else 2 if value <= 1 else 1 if value <= 2 else 0


def bucket_ratio(value: float) -> int:
    return 5 if value <= .05 else 4 if value <= .10 else 3 if value <= .20 else 2 if value <= .35 else 1 if value <= .50 else 0


def issue(items: list[dict[str, Any]], check_id: str, target: str, message: str, pointer: str = "", severity: str = "error") -> None:
    items.append({"severity": severity, "check_id": check_id, "target_record_id": target, "json_pointer": pointer, "message": message})


def refs_from(value: Any) -> tuple[set[str], set[str]]:
    evidence: set[str] = set()
    assumptions: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "evidence_ids" and isinstance(child, list): evidence.update(child)
            elif key == "assumption_ids" and isinstance(child, list): assumptions.update(child)
            else:
                e, a = refs_from(child); evidence.update(e); assumptions.update(a)
    elif isinstance(value, list):
        for child in value:
            e, a = refs_from(child); evidence.update(e); assumptions.update(a)
    return evidence, assumptions


def component_known(group: dict[str, Any], names: tuple[str, ...]) -> bool:
    return all(group[name]["status"] == "known" and group[name]["score"] is not None for name in names)


def validate_facility(f: dict[str, Any], evid_ids: set[str], ass_ids: set[str], issues: list[dict[str, Any]]) -> dict[str, Any]:
    fid = f["facility_id"]
    expected_wave = 1 if f["facility_class"] in WAVE_ONE else 2
    if f["calibration_wave"] != expected_wave:
        issue(issues, "CALIBRATION_WAVE_MISMATCH", fid, f"{f['facility_class']} must use wave {expected_wave}", "/calibration_wave")

    used_e, used_a = refs_from(f)
    for missing in sorted(used_e - evid_ids): issue(issues, "REFERENCE_UNRESOLVED", fid, f"unknown evidence_id: {missing}")
    for missing in sorted(used_a - ass_ids): issue(issues, "REFERENCE_UNRESOLVED", fid, f"unknown assumption_id: {missing}")

    assessed = f["assessment_status"] == "assessed"
    ats_components = f["ats"]["components"]
    r_components = f["r_score"]["components"]
    ats_known = component_known(ats_components, ("p", "f", "i", "u"))
    r_known = component_known(r_components, ("rq", "rt", "rc", "rd", "ro", "rl"))
    gates_known = all(g["status"] != "unknown" for g in f["gates"].values())
    futures_known = all(x["status"] != "unknown" and x["safety"] != "unknown" and x["accessibility"] != "unknown" for x in f["futures"].values())
    faults_known = all(x["status"] != "unknown" for x in f["operation_states"]["ai_degraded"].values())
    complete = ats_known and r_known and gates_known and futures_known and faults_known and f["second_life"]["status"] == "known"
    if assessed and not complete:
        issue(issues, "ASSESSMENT_STATUS_INCOMPLETE", fid, "assessed records must have known scores, gates, futures, degraded faults and Second Life")
    if not assessed and f["classification"]["declared_quadrant"] != "not_evaluable":
        issue(issues, "QUADRANT_MISMATCH", fid, "draft records must declare not_evaluable")

    ats_value = None
    if ats_known:
        ats_value = 5 * sum(ats_components[k]["score"] for k in ("p", "f", "i", "u"))
        total = f["ats"]["total"]
        if total["status"] != "known" or total["value"] is None or not close(total["value"], ats_value):
            issue(issues, "ATS_TOTAL_MISMATCH", fid, f"ATS must equal {ats_value}", "/ats/total")
    elif f["ats"]["total"] != {"status": "unknown", "value": None}:
        issue(issues, "ATS_TOTAL_MISMATCH", fid, "unknown ATS components require unknown/null total", "/ats/total")

    service = f["basic_service"]
    ai_off = f["operation_states"]["ai_off"]
    retention = 100 * service["ai_off_immediate_capacity"] / service["baseline_capacity"]
    time_ratio = ai_off["conversion_time_hours"] / ai_off["recovery_time_objective_hours"]
    cost_ratio = ai_off["conversion_cost_amount"] / ai_off["capital_replacement_value_amount"]
    raw = f["r_score"]["raw"]
    derived_raw = {"retention_pct": retention, "time_to_rto_ratio": time_ratio, "cost_to_crv_ratio": cost_ratio}
    for key, expected in derived_raw.items():
        if raw[key] is None or not close(raw[key], expected): issue(issues, "SERVICE_RETENTION_MISMATCH" if key == "retention_pct" else "R_COMPONENT_BUCKET_MISMATCH", fid, f"{key} must equal {expected}", f"/r_score/raw/{key}")

    expected_buckets = {"rq": bucket_retention(retention), "rt": bucket_time(time_ratio), "rc": bucket_ratio(cost_ratio), "rd": bucket_ratio(raw["stranded_ai_asset_ratio"] or 0)}
    for key, expected in expected_buckets.items():
        comp = r_components[key]
        if comp["status"] == "known" and comp["score"] != expected:
            issue(issues, "R_COMPONENT_BUCKET_MISMATCH", fid, f"{key} must use bucket {expected}", f"/r_score/components/{key}/score")
    for key in ("ro", "rl"):
        if r_components[key]["status"] == "known" and r_components[key]["score"] is None:
            issue(issues, "R_COMPONENT_BUCKET_MISMATCH", fid, f"{key} known score is required")

    r_value = None
    if r_known:
        scores = {k: r_components[k]["score"] for k in ("rq", "rt", "rc", "rd", "ro", "rl")}
        r_value = 20 * (.30*scores["rq"] + .15*scores["rt"] + .15*scores["rc"] + .15*scores["rd"] + .15*scores["ro"] + .10*scores["rl"])
        total = f["r_score"]["total"]
        if total["status"] != "known" or total["value"] is None or not close(total["value"], r_value):
            issue(issues, "R_TOTAL_MISMATCH", fid, f"R-Score must equal {r_value}", "/r_score/total")
    elif f["r_score"]["total"] != {"status": "unknown", "value": None}:
        issue(issues, "R_TOTAL_MISMATCH", fid, "unknown R components require unknown/null total", "/r_score/total")

    for name, future in f["futures"].items():
        if future["unit"] != service["unit"]: issue(issues, "CAPACITY_GROUP_UNIT_CONFLICT", fid, f"{name} unit differs from basic service")
        if future["required_capacity"] is not None and future["delivered_capacity"] is not None:
            expected = future["delivered_capacity"] >= future["required_capacity"]
            if future["service_floor_met"] is not expected: issue(issues, "FUTURE_FLOOR_FLAG_MISMATCH", fid, f"{name} service_floor_met must be {expected}")
    boom, frag, retreat = f["futures"]["boom"], f["futures"]["fragmentation"], f["futures"]["retreat"]
    bp, fp, rp = boom["parameters"], frag["parameters"], retreat["parameters"]
    if assessed and not (bp.get("demand_multiplier", 0) >= 1 and bp.get("concurrency_multiplier", 0) >= 1 and bp.get("curb_load_multiplier", 0) >= 1): issue(issues, "ASSESSMENT_STATUS_INCOMPLETE", fid, "Boom requires three multipliers >= 1")
    if assessed and not (fp.get("vendor_count", 0) >= 3 and fp.get("standard_count", 0) >= 2 and fp.get("single_cloud_unavailable") is True): issue(issues, "ASSESSMENT_STATUS_INCOMPLETE", fid, "Fragmentation parameters are incomplete")
    if assessed and not (rp.get("ai_demand_share_pct", 100) <= 5 and rp.get("vendor_support_available") is False): issue(issues, "ASSESSMENT_STATUS_INCOMPLETE", fid, "Retreat parameters are incomplete")

    paths = f["second_life"]["paths"]
    scope = f["second_life"]["asset_scope"]
    if assessed and not paths: issue(issues, "SECOND_LIFE_ASSET_RULE", fid, "assessed records require a Second Life path")
    if scope in {"fixed_or_long_lived", "mixed"} and f["second_life"]["status"] == "known" and not any(p["path_type"] == "alternate_use" for p in paths):
        issue(issues, "SECOND_LIFE_ASSET_RULE", fid, f"{scope} assets require alternate_use")

    actions = {a for user in f["users"]["ai_users"] for a in user["physical_actions"]}
    interventions = {x["kind"] for x in f["physical_change"]["interventions"]}
    anti_sticker = bool(interventions & SUBSTANTIVE_KINDS) and bool(f["physical_change"]["measurable_changes"])
    all_gates = all(x["status"] == "pass" for x in f["gates"].values())
    all_futures = all(x["status"] == "pass" and x["service_floor_met"] is True and x["safety"] == "pass" and x["accessibility"] == "pass" for x in f["futures"].values())
    compat = f["compatibility"]
    compat_ok = compat["human_priority_preserved"] and compat["non_ai_access_preserved"] and compat["accessibility_preserved"]
    service_ok = service["ai_off_immediate_capacity"] >= service["required_floor"] and (f["criticality"] != "critical" or retention >= 100 - TOL)
    high_ats = ats_value is not None and ats_value >= 70 and ats_components["p"]["score"] >= 2 and ats_components["u"]["score"] >= 3 and all_gates
    high_r = r_value is not None and r_value >= 80 and all(r_components[k]["score"] >= 3 for k in r_components) and service_ok
    eligible = bool(assessed and complete and f["overall_confidence"] != "unknown" and high_ats and high_r and all_futures and compat_ok and anti_sticker and actions & PHYSICAL_ACTIONS and f["reverse_design"]["decision"] != "retain")
    quadrant = "not_evaluable" if not assessed or not (ats_known and r_known) else "high_high" if eligible else "high_ats_only" if high_ats else "high_r_only" if high_r else "low_low"
    declared = f["classification"]
    if declared["high_high_eligible"] != eligible: issue(issues, "ELIGIBILITY_MISMATCH", fid, f"high_high_eligible must be {eligible}")
    if declared["declared_quadrant"] != quadrant: issue(issues, "QUADRANT_MISMATCH", fid, f"declared_quadrant must be {quadrant}")
    if declared["high_high_eligible"] and not anti_sticker: issue(issues, "ANTI_STICKER_HIGH_HIGH", fid, "High–High requires substantive physical intervention and measurable change")
    if declared["high_high_eligible"] and not actions: issue(issues, "AI_PHYSICAL_USER_REQUIRED", fid, "High–High requires an AI physical user")
    if declared["high_high_eligible"] and not eligible: issue(issues, "HIGH_HIGH_GATE_FAILED", fid, "one or more High–High gates failed")
    return {"assessed_complete": assessed and complete, "ats": ats_value, "r": r_value, "eligible": eligible, "service": service}


def validate_semantics(data: dict[str, Any]) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []
    expected_synthetic = data["dataset_kind"] in {"template", "synthetic_fixture"}
    if data["synthetic"] != expected_synthetic: issue(issues, "SYNTHETIC_FLAG_MISMATCH", "$", f"synthetic must be {expected_synthetic}")
    evid = [x["evidence_id"] for x in data["evidence_register"]]; ass = [x["assumption_id"] for x in data["assumption_register"]]
    for values, check in ((evid, "EVIDENCE_ID_DUPLICATE"), (ass, "ASSUMPTION_ID_DUPLICATE")):
        if len(values) != len(set(values)): issue(issues, check, "$", "register IDs must be unique")
    fids = [x["facility_id"] for x in data["facilities"]]
    if len(fids) != len(set(fids)): issue(issues, "FACILITY_ID_DUPLICATE", "$", "facility IDs must be unique")
    results = [validate_facility(f, set(evid), set(ass), issues) for f in data["facilities"]]

    summary = data["portfolio_summary"]
    rows = summary["facility_class_ats_medians"]
    if {x["facility_class"] for x in rows} != set(CLASSES): issue(issues, "PORTFOLIO_MEDIAN_MISMATCH", "$", "summary must contain each facility class exactly once")
    for cls in CLASSES:
        vals = [r["ats"] for f, r in zip(data["facilities"], results) if f["facility_class"] == cls and r["assessed_complete"] and r["ats"] is not None]
        row = next((x for x in rows if x["facility_class"] == cls), None)
        if row:
            expected = statistics.median(vals) if vals else None; status = "known" if vals else "not_applicable"
            if row["status"] != status or ((expected is None) != (row["value"] is None)) or (expected is not None and not close(row["value"], expected)):
                issue(issues, "PORTFOLIO_MEDIAN_MISMATCH", "$", f"{cls} median must be {expected}")
    critical = [r["r"] for f, r in zip(data["facilities"], results) if f["criticality"] == "critical" and r["assessed_complete"] and r["r"] is not None]
    expected_min = min(critical) if critical else None; row = summary["critical_min_r_score"]
    expected_status = "known" if critical else "not_applicable"
    if row["status"] != expected_status or ((expected_min is None) != (row["value"] is None)) or (expected_min is not None and not close(row["value"], expected_min)):
        issue(issues, "PORTFOLIO_CRITICAL_MIN_R_MISMATCH", "$", f"critical minimum R must be {expected_min}")
    coverage = 100 * sum(r["assessed_complete"] for r in results) / len(results); row = summary["evaluation_coverage_pct"]
    if row["status"] != "known" or row["value"] is None or not close(row["value"], coverage): issue(issues, "PORTFOLIO_COVERAGE_MISMATCH", "$", f"coverage must be {coverage}")
    grouped: dict[tuple[str, str], list[int]] = {}
    group_units: dict[str, set[str]] = {}
    for idx, r in enumerate(results):
        s = r["service"]; key=(s["capacity_group_id"], s["unit"]); grouped.setdefault(key, []).append(idx); group_units.setdefault(s["capacity_group_id"], set()).add(s["unit"])
    for group, units in group_units.items():
        if len(units) > 1: issue(issues, "CAPACITY_GROUP_UNIT_CONFLICT", "$", f"{group} has multiple units")
    shares = {(x["capacity_group_id"], x["unit"]): x for x in summary["high_high_capacity_shares"]}
    if set(shares) != set(grouped): issue(issues, "PORTFOLIO_CAPACITY_SHARE_MISMATCH", "$", "capacity-share groups do not match facilities")
    for key, idxs in grouped.items():
        denom=sum(results[i]["service"]["baseline_capacity"] for i in idxs); num=sum(results[i]["service"]["baseline_capacity"] for i in idxs if results[i]["eligible"]); value=100*num/denom
        row=shares.get(key)
        if not row or row["status"] != "known" or not close(row["numerator"], num) or not close(row["denominator"], denom) or not close(row["value_pct"], value): issue(issues, "PORTFOLIO_CAPACITY_SHARE_MISMATCH", "$", f"{key} must be {num}/{denom}={value}%")
    return sorted(issues, key=lambda x: (x["severity"], x["check_id"], x["target_record_id"], x["json_pointer"]))


def report(path: Path, valid: bool, issues: list[dict[str, Any]], as_json: bool, exit_code: int) -> int:
    payload = {"validator_version": VALIDATOR_VERSION, "method_version": METHOD_VERSION, "input": str(path), "valid": valid, "summary": {"errors": sum(x["severity"] == "error" for x in issues), "issues": len(issues)}, "issues": issues}
    if as_json: print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    else:
        print(f"{'PASS' if valid else 'FAIL'} {path}")
        for x in issues: print(f"[{x['severity']}] {x['check_id']} {x['target_record_id']} {x['message']}")
    return exit_code


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        text = args.input.read_text(encoding="utf-8")
        data = json.loads(text, object_pairs_hook=unique_object, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(f"non-finite number {x}")))
    except DuplicateKeyError as exc:
        return report(args.input, False, [{"severity":"error","check_id":"JSON_DUPLICATE_KEY","target_record_id":"$","json_pointer":"","message":f"duplicate key: {exc}"}], args.json, 2)
    except Exception as exc:
        return report(args.input, False, [{"severity":"error","check_id":"INPUT_INVALID","target_record_id":"$","json_pointer":"","message":str(exc)}], args.json, 2)
    try:
        schema_path = Path(__file__).with_name("facility-record.schema.json")
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
        errors = sorted(jsonschema.Draft202012Validator(schema).iter_errors(data), key=lambda x: list(x.absolute_path))
        if errors:
            items=[]
            for err in errors: issue(items, "SCHEMA_INVALID", "$", err.message, "/" + "/".join(map(str, err.absolute_path)))
            return report(args.input, False, items, args.json, 1)
        issues = validate_semantics(data)
        return report(args.input, not issues, issues, args.json, 0 if not issues else 1)
    except Exception as exc:
        return report(args.input, False, [{"severity":"error","check_id":"VALIDATOR_INTERNAL_ERROR","target_record_id":"$","json_pointer":"","message":str(exc)}], args.json, 2)


if __name__ == "__main__":
    raise SystemExit(main())
