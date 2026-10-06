#!/usr/bin/env python3
"""Static contract checks for Research Intelligence proposal fixtures.

No third-party packages are required. This is deliberately narrower than a
full JSON Schema engine; it checks invariants that are easy to violate while
keeping package validation lightweight.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples" / "proposals"
SCHEMA = ROOT / "schemas" / "research-intelligence-proposal-v1.schema.json"

ALLOWED = {
    "discovery": {"observation", "hypothesis", "experiment"},
    "aoa": {"pattern", "abstraction", "transfer_hypothesis"},
}

def fail(msg: str) -> None:
    raise AssertionError(msg)

def validate_proposal(p: dict, path: Path) -> None:
    required = {
        "profile_version","proposal_id","component_origin","proposal_kind",
        "handoff_state","epistemic_mode","statement","sources","uncertainty",
        "assumptions","competing_hypotheses","contradictory_evidence",
        "experiment","abstraction","lineage","missing_information",
    }
    missing = required - set(p)
    if missing:
        fail(f"{path}: missing required keys: {sorted(missing)}")
    if p["profile_version"] != "research-intelligence-proposal/1.0":
        fail(f"{path}: wrong profile_version")
    if p["handoff_state"] != "proposed_unaccepted":
        fail(f"{path}: handoff_state must remain proposed_unaccepted")
    origin = p["component_origin"]
    kind = p["proposal_kind"]
    if origin not in ALLOWED or kind not in ALLOWED[origin]:
        fail(f"{path}: invalid component/kind combination {origin}/{kind}")
    if not isinstance(p["proposal_id"], str) or not p["proposal_id"]:
        fail(f"{path}: proposal_id must be non-empty")
    if not p.get("statement", {}).get("text"):
        fail(f"{path}: statement.text must be non-empty")
    if not isinstance(p["missing_information"], list):
        fail(f"{path}: missing_information must be explicit array")

    exp = p["experiment"]
    if exp is not None:
        status = exp.get("status")
        result_status = exp.get("result_status")
        results = exp.get("results")
        if status == "executed":
            if result_status != "reported" or not isinstance(results, list) or not results:
                fail(f"{path}: executed experiment must contain reported actual result(s)")
        elif status in {"proposed", "unexecuted"}:
            if result_status != "none" or results != []:
                fail(f"{path}: non-executed experiment must not contain findings")
        else:
            fail(f"{path}: invalid experiment status {status!r}")

    if origin == "discovery" and p["abstraction"] is not None:
        fail(f"{path}: Discovery fixture must not emit abstraction payload")
    if origin == "aoa" and kind in {"abstraction", "transfer_hypothesis"} and p["abstraction"] is None:
        fail(f"{path}: AoA abstraction/transfer fixture needs abstraction payload")

def validate_links() -> None:
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for rel in ["README.md", "SKILL.md"]:
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        for target in link_re.findall(text):
            if "://" in target or target.startswith("#") or target.startswith("mailto:"):
                continue
            clean = target.split("#", 1)[0]
            if clean and not (ROOT / clean).exists():
                fail(f"{rel}: broken local link {target}")

def main() -> int:
    json.loads(SCHEMA.read_text(encoding="utf-8"))
    files = sorted(EXAMPLES.glob("*.json"))
    if len(files) < 5:
        fail("expected at least five proposal fixtures")
    seen = set()
    for path in files:
        proposal = json.loads(path.read_text(encoding="utf-8"))
        validate_proposal(proposal, path)
        pid = proposal["proposal_id"]
        if pid in seen:
            fail(f"duplicate proposal_id: {pid}")
        seen.add(pid)
    validate_links()
    print(f"validated {len(files)} proposal fixtures, schema JSON, and local README/SKILL links")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
