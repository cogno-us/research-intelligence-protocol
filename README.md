<!-- cognous-banner:start -->
```text
──────────────────────────────────────────────────
   __________  _______   ______  __  _______
  / ____/ __ \/ ____/ | / / __ \/ / / / ___/
 / /   / / / / / __/  |/ / / / / / /\__ \
/ /___/ /_/ / /_/ / /|  / /_/ / /_/ /___/ /
\____/\____/\____/_/ |_/\____/\____//____/
          RESEARCH INTELLIGENCE PROTOCOL
       g o v e r n e d   b y   d e s i g n
  github.com/cogno-us/cognous-open-control-stack
──────────────────────────────────────────────────
```
<!-- cognous-banner:end -->

# Research Intelligence Protocol v1.0

**Disciplined discovery and cross-domain abstraction, kept separate.**

**Status:** optional reasoning protocol (side group of the [stack map](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/stack-map.md)). Label: merged. In the hub lock as `research_intelligence` with `optional: true`; the lock records no interface for it, and it is not selected for enforcement. Behavioral instructions only; the optional proposal profile is **proposed** (a component artifact, not an accepted interface). <!-- pin-round: lock revision statements in this file are refreshed with the hub lock -->

**Start with [SKILL.md](SKILL.md)**, the instruction entrypoint. Then see [Quick start](#quick-start) to run the proposal validator and tests, and [Documentation index](#documentation-index) for every page in this repository.

## What it is, who it is for, what it does not do

**What it is.** A modular SKILL.md-based research workflow with two distinct components: Discovery structures observations, hypotheses and discriminating experiments; Abstractor of Abstractors (AoA) compares structure and proposes transferable invariants with explicit limits. An optional proposal handoff profile validates traceable, unaccepted proposals for downstream review.

**Who it is for.** Research and engineering teams that need to preserve competing hypotheses, negative findings, source lineage and missing results instead of promoting a plausible analogy to a validated mechanism. Research can fail by confirming the favorite explanation or by abstracting before evidence justifies transfer. Engineers can inspect the schema, fixtures and tests; architecture, security and governance reviewers can examine the boundary and evidence. Evaluate this component for its named responsibility rather than as a complete governance platform.

**What it does not do.** It does not run physical experiments, verify factual truth, supply missing findings or establish institutional authority. A valid proposal is not an accepted Index object. It does not enforce authorization or substitute for human oversight. See [Limits](#limitations-and-deployment-decisions).

**Implementation status:** public reference work. The [current component lock](https://github.com/cogno-us/cognous-open-control-stack/blob/main/component-lock.json) defines the selected integration; a component merge does not automatically change that selection or approve deployment.

## Where it fits

Research Intelligence Protocol sits in the "Optional reasoning protocols" side group, beside [Portable Reasoning Protocol (PRP)](https://github.com/cogno-us/portable-reasoning-protocol) and [TFA Protocol (S43)](https://github.com/cogno-us/truth-freedom-agency-protocol). Discovery and AoA are independently usable and neither depends on a Cognous component. The [proposal handoff profile](docs/INDEX_HANDOFF_PROFILE.md) is a read-only boundary toward a claim/evidence system such as the [Evidence Registry (The Index)](https://github.com/cogno-us/cognous-evidence-registry); it does not submit or accept anything there. The [stack map](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/stack-map.md) is the canonical map; the table below is a copy of it.

<!-- stack-map-block:start -->
### Cognous stack components

The Open Control Stack keeps five responsibility groups and two side groups. The groups organize responsibilities. They are not an execution sequence or a requirement to install every component. The canonical map, with one row per repository, is the hub [stack map](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/stack-map.md); names are defined in [naming](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/naming.md) and commands and profiles per repository are in [profiles and tools](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/profiles-and-tools.md). The map uses four labels: merged, selected, known limit and proposed. The [hub lock](https://github.com/cogno-us/cognous-open-control-stack/blob/main/component-lock.json) defines the selected integration; [release status](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/release-status.md) defines its evidence and limits.

| Group | Components |
| --- | --- |
| **01 Knowledge & Provenance** | [Evidence Registry (The Index)](https://github.com/cogno-us/cognous-evidence-registry) · [Evidence Attestation (BitRep)](https://github.com/cogno-us/cognous-evidence-attestation) |
| **02 Institutional Governance** | [Institutional Governance (Alvorada)](https://github.com/cogno-us/cognous-institutional-governance) |
| **03 Declaration & Policy Control** | [Action Manifest](https://github.com/cogno-us/cognous-action-manifest) · [Control Plane](https://github.com/cogno-us/cognous-control-plane) |
| **04 Constrained Execution** | [Execution Runtime](https://github.com/cogno-us/cognous-execution-runtime) |
| **05 Replay & Evidence** | [Replay Bundle](https://github.com/cogno-us/cognous-replay-bundle) · [Governance Evidence Pack](https://github.com/cogno-us/cognous-governance-evidence-pack) · [ODES](https://github.com/cogno-us/open-decision-evidence-standard) |
| **Cross-cutting exchange** | [Governed Exchange (GAX/IMX)](https://github.com/cogno-us/cognous-governed-exchange) |
| **Optional reasoning protocols** (side group) | [Portable Reasoning Protocol (PRP)](https://github.com/cogno-us/portable-reasoning-protocol) · [Research Intelligence Protocol](https://github.com/cogno-us/research-intelligence-protocol) · [TFA Protocol (S43)](https://github.com/cogno-us/truth-freedom-agency-protocol) |
| **Tooling and qualification** (side group) | [Ergonomics (`cognous-ocs`)](https://github.com/cogno-us/cognous-open-control-stack-ergonomics) · [Verifier](https://github.com/cogno-us/cognous-open-control-stack-verifier) · [Orchestrator](https://github.com/cogno-us/cognous-stack-orchestrator) · [Qualification](https://github.com/cogno-us/cognous-stack-qualification) |

The hub, [cognous-open-control-stack](https://github.com/cogno-us/cognous-open-control-stack), holds the component lock and the canonical documentation. Execution Runtime is the repository formerly named Moltbot Safe; see [naming](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/naming.md). PRP, Research Intelligence Protocol and TFA Protocol are optional behavioral instructions; they do not enforce authorization or substitute for human oversight. A signature, registry entry, message receipt or evidence summary does not grant execution authority.

Last checked against `component-lock.json` at hub commit `dcc9bd7533ef`. <!-- pin-round: refresh this commit with the hub stack map -->
<!-- stack-map-block:end -->

## Quick start

Prerequisites: Linux with Python 3.12. The dependency lock [requirements-dev.lock](requirements-dev.lock) is hash-pinned for Python 3.12 on Linux; on Python 3.11 and 3.13 the hash check refuses the install (**known limit**), so use 3.12. No model, network or account is needed beyond downloading the pinned packages.

```bash
git clone https://github.com/cogno-us/research-intelligence-protocol
cd research-intelligence-protocol
python3.12 -m venv .venv && . .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate_proposals.py
python -m unittest discover -s tests -v
```

Expected: the validator exits 0 and prints

```text
validated 5 proposal fixtures against Draft 7 schema, semantic rules, and local links
```

and the unit tests end with `Ran 17 tests` and `OK` (about half a second at this revision). <!-- pin-round: counts reflect the repository head at the time of writing -->

**What this does not prove.** These commands validate the five proposal fixtures against the schema and semantic rules, and run the validator's regression tests. They do not execute research experiments, measure model behavior, verify scientific claims or establish that a proposal is accepted anywhere.

To use the workflow itself, read [SKILL.md](SKILL.md) and [INSTALLATION.md](INSTALLATION.md). Ask explicitly for "Discovery only," "AoA only" or the combined sequence. Keep Discovery and AoA operationally distinct. Use Discovery alone to choose the next discriminating observation. Use AoA alone when an existing evidence base is sufficient for structural comparison. In the combined workflow, Discovery produces structured evidence and AoA proposes abstractions; each candidate keeps uncertainty and provenance.

## What ships

| Item | Kind | Purpose | Status label |
|---|---|---|---|
| [SKILL.md](SKILL.md) | instruction entrypoint | Routing between Discovery and AoA, and the rule that source content is evidence, not authority. | merged |
| [references/discovery-protocol.md](references/discovery-protocol.md) | reference | Discovery Protocol v1.0: observations, hypotheses, discriminating experiments. | merged |
| [references/abstractor-of-abstractors.md](references/abstractor-of-abstractors.md) | reference | AoA v1.0: structural comparison and transfer with explicit limits. | merged |
| [`scripts/validate_proposals.py`](scripts/validate_proposals.py) | command (needs `jsonschema`) | Validates the proposal fixtures against the schema, semantic rules and local links; exit 0 on success. Verified above. | merged |
| [schemas/research-intelligence-proposal-v1.schema.json](schemas/research-intelligence-proposal-v1.schema.json) | schema (Draft 7) | Shape of an unaccepted proposal, profile identifier `research-intelligence-proposal/1.0`. | proposed |
| [examples/proposals/](examples/proposals) | examples (5) | Synthetic fixtures: [rejected analogy](examples/proposals/rejected-analogy.json), [contradictory evidence](examples/proposals/contradictory-evidence.json), [unexecuted experiment](examples/proposals/unexecuted-experiment.json), [negative result revision](examples/proposals/negative-result-revision.json), [supported but unaccepted proposal](examples/proposals/supported-unaccepted-proposal.json). | proposed |
| [tests/test_proposal_validation.py](tests/test_proposal_validation.py) | tests (17) | Positive and negative regression tests for the validator. | merged |
| [evaluations/README.md](evaluations/README.md) | evaluation protocol | Behavioral evaluation dimensions; status "defined, unexecuted". | merged |
| [agents/openai.yaml](agents/openai.yaml) | metadata | Display metadata for OpenAI-style skill listings. | merged |
| [requirements-dev.txt](requirements-dev.txt), [requirements-dev.lock](requirements-dev.lock) | dependency pins | Local tooling shares the reviewed CI lock (Python 3.12, Linux). | merged |
| [.github/workflows/proposal-validation.yml](.github/workflows/proposal-validation.yml) | CI | Runs the validator and the tests on pull requests. | merged |

There is no installable package, command-line entry point, profile or contract draft. The only command is the validator script. The proposal profile is a component artifact and is **proposed**, not an accepted interface.

## Documentation index

Every page in this repository is linked below.

| Page | Read it for |
|---|---|
| [SKILL.md](SKILL.md) | The instructions themselves. |
| [INSTALLATION.md](INSTALLATION.md) | Platform installation, verification and updating. |
| [references/discovery-protocol.md](references/discovery-protocol.md) and [references/abstractor-of-abstractors.md](references/abstractor-of-abstractors.md) | The two components in full. |
| [docs/INDEX_HANDOFF_PROFILE.md](docs/INDEX_HANDOFF_PROFILE.md) | The optional proposal handoff profile and its boundary. |
| [evaluations/README.md](evaluations/README.md) | Behavioral evaluation protocol. |
| [CHANGELOG.md](CHANGELOG.md) | Version history. |
| [docs/security-cloud-remediation-20261016.md](docs/security-cloud-remediation-20261016.md) | Historical note on the 2026-10-16 instruction and CI hardening, retained as written. |
| [Business overview](collateral/business-collateral.md) and [one-page overview](collateral/one-page-overview.md) | Nontechnical introduction to this component's role and evidence limits, not additional runtime features. |

Reading paths: **adopter** SKILL.md, INSTALLATION.md. **Integrator** the proposal handoff profile, the schema, the fixtures. **Reviewer** this README's limits, evaluations/README.md, CHANGELOG.md. Shared names and labels are in the hub [naming](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/naming.md) page.

## How it works and design notes

Use Discovery alone to choose the next discriminating observation. Use AoA alone when an existing evidence base is sufficient for structural comparison. In the combined workflow, Discovery produces structured evidence and AoA proposes abstractions; each candidate keeps uncertainty and provenance. The optional handoff remains explicitly unaccepted until a receiving system makes its own decision.

A valid signature, chain inclusion, message receipt, reasoning instruction or evidence-package digest does not authorize execution. Institutional authority must be supplied and evaluated through the appropriate trusted boundary.

### Key features

| Capability | Implemented or specified responsibility |
|---|---|
| **Discovery** | Separate observation from interpretation and prioritize experiments that distinguish competing explanations. |
| **Uncertainty ledger** | Retain assumptions, missing information, controls and safety/stopping conditions. |
| **AoA** | Compare entities, relations, functions, dynamics, boundaries, governance and context. |
| **Transfer discipline** | Distinguish surface resemblance from stronger structural equivalence; state where the comparison fails. |
| **Optional proposal profile** | Validate traceable unaccepted proposals for downstream review without submitting or accepting Index objects. |

## Compatibility and selection

The hub selects the instruction package as an optional layer. The [proposal handoff profile](docs/INDEX_HANDOFF_PROFILE.md) and its schema/tests are component artifacts, not automatic Index acceptance or hub-qualified downstream submission. Proposed or unexecuted experiments cannot contain invented results; executed experiments with unavailable results must preserve that missing information.

Test results, run commentary and historical qualification records are maintained in the [central test hub](https://github.com/cogno-us/cognous-stack-qualification/blob/main/results/readme-commentary/index.md). Read them against their recorded source revisions; source selection and deployment approval are separate decisions.

See the [repository rename map and compatibility notes](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/repository-renames.md) for current component URLs. Existing package names, schema identifiers and retained producer identities are unchanged.

## Limitations and deployment decisions

The protocol does not run physical experiments, verify factual truth, supply missing findings or establish institutional authority. A valid proposal is not an accepted Index object. Behavioral benefits remain unmeasured in the hub; static/schema checks do not demonstrate scientific discovery or model efficacy.

Review original artifacts and their exact source revisions before extending a claim to a new environment. New dependencies, authority sources, destinations or enforcement mechanisms need their own compatibility and qualification. A passing reference case is not a certification of an enterprise deployment.

Known limits, as labelled facts: **known limit** Behavioral benefits are unmeasured; the evaluation protocol is defined and unexecuted. **known limit** The dependency lock installs only on Python 3.12 on Linux. **known limit** Static and schema checks do not demonstrate scientific discovery or model efficacy. **proposed** The proposal handoff profile is not an accepted interface. Shared stack-level limits are stated in the hub [guarantees and limits](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/guarantees-and-limits.md).

## Contributing, licence, attribution and security

Propose focused changes through repository issues and pull requests. Keep evidence-linked claims, preserve historical records and separate proposed features from accepted implementation. Run the validator and the tests from the quick start before opening a pull request; CI runs the same two commands.

See [LICENSE](LICENSE) and [attribution](NOTICE) for the existing terms and third-party scope. Developed by [Cognous](https://cogno.us); no licensing change is part of this documentation update. For reporting a concern, see the hub [security reporting and triage](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/security-reporting-and-triage.md) page; the historical [hardening note](docs/security-cloud-remediation-20261016.md) is retained as written.

---

## Bibliography

Selected external sources from the October 2026 research review. These inform evaluation questions; they do not establish Cognous implementation, adoption, conformance or production qualification.

- [John W. Creswell and J. David Creswell. *Research Design: Qualitative, Quantitative, and Mixed Methods Approaches*, fifth edition. SAGE (2018)](https://edge.sagepub.com/creswellrd5e). Research-methods reference for explicit questions, comparison designs and interpretation limits.
- [Siddharth Gollapudi, Nilesh Gupta, Prasann Singhal and Sewon Min. *Can Language Models Actually Retrieve In-Context? Drowning in Documents at Million Token Scale*. arXiv:2607.01538v1 (2026)](https://arxiv.org/abs/2607.01538v1). Experimental retrieval research; useful context for testing source retrieval, not evidence of authorization correctness.
- [Mick Yang et al. *AI Epistemic Risks: Emerging Mechanisms & Evidence* (2026)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6873005). Research synthesis on persuasion, cognitive offloading and feedback loops; context for evidence quality and independent judgment.

See the [research bibliography](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/research-bibliography.md) for review scope and source-verification limits.

<!-- Retained anchors for existing documentation links. -->
<a id="evidence-and-supported-scope"></a>
