from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_proposals.py"
spec = importlib.util.spec_from_file_location("validate_proposals", MODULE_PATH)
vp = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(vp)

FIXTURES = ROOT / "examples" / "proposals"
SCHEMA = vp.load_schema()


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


class PublishedFixtureTests(unittest.TestCase):
    def test_all_five_published_fixtures_pass_schema_and_semantics(self):
        paths = sorted(FIXTURES.glob("*.json"))
        self.assertEqual(5, len(paths))
        for path in paths:
            with self.subTest(path=path.name):
                proposal = json.loads(path.read_text(encoding="utf-8"))
                vp.validate_schema(proposal, SCHEMA)
                vp.validate_semantics(proposal)


class SchemaRegressionTests(unittest.TestCase):
    def setUp(self):
        self.base = load_fixture("unexecuted-experiment.json")

    def assertSchemaRejects(self, proposal: dict):
        with self.assertRaises(vp.ProposalValidationError):
            vp.validate_schema(proposal, SCHEMA)

    def test_governor_reproduction_sources_must_be_array(self):
        proposal = copy.deepcopy(self.base)
        proposal["sources"] = "not an array"
        self.assertSchemaRejects(proposal)

    def test_governor_reproduction_unsupported_epistemic_enum(self):
        proposal = copy.deepcopy(self.base)
        proposal["epistemic_mode"] = "verified"
        self.assertSchemaRejects(proposal)

    def test_undeclared_top_level_field_rejected(self):
        proposal = copy.deepcopy(self.base)
        proposal["verification_result"] = "verified"
        self.assertSchemaRejects(proposal)

    def test_component_origin_kind_combination_rejected_by_schema(self):
        proposal = copy.deepcopy(self.base)
        proposal["component_origin"] = "aoa"
        self.assertSchemaRejects(proposal)

    def test_experiment_proposal_requires_experiment_metadata(self):
        proposal = copy.deepcopy(self.base)
        proposal["experiment"] = None
        self.assertSchemaRejects(proposal)

    def test_unexecuted_experiment_cannot_have_findings(self):
        proposal = copy.deepcopy(self.base)
        proposal["experiment"]["result_status"] = "reported"
        proposal["experiment"]["results"] = [{"result": "fabricated", "direction": "positive"}]
        self.assertSchemaRejects(proposal)

    def test_discovery_cannot_emit_abstraction_payload(self):
        proposal = copy.deepcopy(self.base)
        proposal["proposal_kind"] = "hypothesis"
        proposal["experiment"] = None
        proposal["abstraction"] = {
            "abstraction_level": "E1",
            "source_domain": "x",
            "target_domain": None,
            "transfer_assumptions": [],
            "transfer_limits": [],
            "counterexamples": [],
            "disposition": "candidate",
        }
        self.assertSchemaRejects(proposal)

    def test_aoa_abstraction_requires_abstraction_metadata(self):
        proposal = load_fixture("supported-unaccepted-proposal.json")
        proposal["abstraction"] = None
        self.assertSchemaRejects(proposal)


class SemanticRegressionTests(unittest.TestCase):
    def test_executed_results_unavailable_is_valid_when_missing_is_explicit(self):
        proposal = load_fixture("unexecuted-experiment.json")
        proposal["experiment"] = {
            "status": "executed",
            "description": "Experiment execution is known, but the result artifact is unavailable.",
            "result_status": "unavailable",
            "results": [],
        }
        proposal["missing_information"] = [
            {
                "field": "experiment.results",
                "reason": "Execution was recorded, but the result artifact is unavailable to this handoff.",
            }
        ]
        vp.validate_proposal(proposal, "executed-unavailable", SCHEMA)

    def test_executed_results_unavailable_requires_explicit_missing_information(self):
        proposal = load_fixture("unexecuted-experiment.json")
        proposal["experiment"] = {
            "status": "executed",
            "description": "Experiment execution is known, but the result artifact is unavailable.",
            "result_status": "unavailable",
            "results": [],
        }
        proposal["missing_information"] = []
        with self.assertRaises(vp.ProposalValidationError):
            vp.validate_proposal(proposal, "executed-unavailable", SCHEMA)

    def test_semantic_guard_rejects_nonexecuted_findings_even_if_called_directly(self):
        proposal = load_fixture("unexecuted-experiment.json")
        proposal["experiment"]["result_status"] = "reported"
        proposal["experiment"]["results"] = [{"result": "fabricated", "direction": "positive"}]
        with self.assertRaises(vp.ProposalValidationError):
            vp.validate_semantics(proposal)

    def test_semantic_guard_rejects_invalid_component_kind_even_if_called_directly(self):
        proposal = load_fixture("unexecuted-experiment.json")
        proposal["component_origin"] = "aoa"
        with self.assertRaises(vp.ProposalValidationError):
            vp.validate_semantics(proposal)


if __name__ == "__main__":
    unittest.main()
