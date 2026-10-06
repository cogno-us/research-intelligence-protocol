#!/usr/bin/env python3
"""Schema and semantic validation for Research Intelligence proposal fixtures."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft7Validator

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples" / "proposals"
SCHEMA = ROOT / "schemas" / "research-intelligence-proposal-v1.schema.json"

ALLOWED = {
    "discovery": {"observation", "hypothesis", "experiment"},
    "aoa": {"pattern", "abstraction", "transfer_hypothesis"},
}


class ProposalValidationError(ValueError):
    """Raised when a proposal violates schema or profile semantics."""


def _path(error: Any) -> str:
    return ".".join(str(part) for part in error.absolute_path) or "<root>"


def load_schema() -> dict:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft7Validator.check_schema(schema)
    return schema


def validate_schema(proposal: dict, schema: dict | None = None) -> None:
    """Apply the actual Draft 7 JSON Schema and report all instance errors."""
    schema = schema or load_schema()
    validator = Draft7Validator(schema)
    errors = sorted(validator.iter_errors(proposal), key=lambda e: list(e.absolute_path))
    if errors:
        details = "; ".join(f"{_path(err)}: {err.message}" for err in errors)
        raise ProposalValidationError(f"JSON Schema validation failed: {details}")


def validate_semantics(proposal: dict) -> None:
    """Enforce profile invariants that require cross-field semantic interpretation."""
    origin = proposal["component_origin"]
    kind = proposal["proposal_kind"]

    if kind not in ALLOWED[origin]:
        raise ProposalValidationError(f"invalid component/kind combination {origin}/{kind}")

    experiment = proposal["experiment"]
    if kind == "experiment" and experiment is None:
        raise ProposalValidationError("experiment proposals require experiment metadata")

    if experiment is not None:
        status = experiment["status"]
        result_status = experiment["result_status"]
        results = experiment["results"]

        if status in {"proposed", "unexecuted"}:
            if result_status != "none" or results:
                raise ProposalValidationError(
                    "proposed/unexecuted experiments cannot contain findings"
                )
        elif status == "executed":
            if result_status == "reported":
                if not results:
                    raise ProposalValidationError(
                        "executed experiments with reported results require at least one actual result"
                    )
            elif result_status == "unavailable":
                if results:
                    raise ProposalValidationError(
                        "executed experiments with unavailable results must not fabricate results"
                    )
                missing_fields = {item["field"] for item in proposal["missing_information"]}
                if "experiment.results" not in missing_fields:
                    raise ProposalValidationError(
                        "executed experiments with unavailable results must explicitly record experiment.results in missing_information"
                    )
            else:
                raise ProposalValidationError(
                    "executed experiments require result_status reported or unavailable"
                )

    abstraction = proposal["abstraction"]
    if origin == "discovery" and abstraction is not None:
        raise ProposalValidationError("Discovery proposals must not emit abstraction payloads")
    if origin == "aoa" and kind in {"abstraction", "transfer_hypothesis"} and abstraction is None:
        raise ProposalValidationError("AoA abstraction/transfer proposals require abstraction metadata")


def validate_proposal(proposal: dict, source: str | Path = "<proposal>", schema: dict | None = None) -> None:
    """Validate one proposal against both JSON Schema and semantic rules."""
    try:
        validate_schema(proposal, schema)
        validate_semantics(proposal)
    except ProposalValidationError as exc:
        raise ProposalValidationError(f"{source}: {exc}") from exc


def validate_links() -> None:
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for rel in ["README.md", "SKILL.md"]:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for target in link_re.findall(text):
            if "://" in target or target.startswith("#") or target.startswith("mailto:"):
                continue
            clean = target.split("#", 1)[0]
            if clean and not (ROOT / clean).exists():
                raise ProposalValidationError(f"{rel}: broken local link {target}")


def main() -> int:
    schema = load_schema()
    files = sorted(EXAMPLES.glob("*.json"))
    if len(files) != 5:
        raise ProposalValidationError(f"expected exactly five published proposal fixtures, found {len(files)}")

    seen: set[str] = set()
    for path in files:
        proposal = json.loads(path.read_text(encoding="utf-8"))
        validate_proposal(proposal, path, schema)
        proposal_id = proposal["proposal_id"]
        if proposal_id in seen:
            raise ProposalValidationError(f"duplicate proposal_id: {proposal_id}")
        seen.add(proposal_id)

    validate_links()
    print(f"validated {len(files)} proposal fixtures against Draft 7 schema, semantic rules, and local links")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ProposalValidationError, json.JSONDecodeError) as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
