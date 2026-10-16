<!-- cognous-banner:start -->
```text
──────────────────────────────────────────────────
   __________  _______   ______  __  _______
  / ____/ __ \/ ____/ | / / __ \/ / / / ___/
 / /   / / / / / __/  |/ / / / / / / /\__ \
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

**Stack group: 06 · Reasoning & Human Oversight.** See the [six-group component map](#cognous-stack-components).

## Overview

A modular SKILL.md-based research workflow with two distinct components: Discovery structures observations, hypotheses and discriminating experiments; Abstractor of Abstractors (AoA) compares structure and proposes transferable invariants with explicit limits.

**Implementation status:** public reference work. The [current component lock](https://github.com/cogno-us/cognous-open-control-stack/blob/main/component-lock.json) defines the selected integration; a component merge does not automatically change that selection or approve deployment.

## Purpose and intended users

Research can fail by confirming the favorite explanation or by abstracting before evidence justifies transfer. A reusable workflow should preserve competing hypotheses, negative findings, source lineage and missing results instead of promoting a plausible analogy to a validated mechanism.

Engineers can inspect the reference contracts and examples; enterprise architecture, security and governance reviewers can examine the boundary and evidence. Evaluate this component for its named responsibility rather than as a complete governance platform.

## Key features

| Capability | Implemented or specified responsibility |
|---|---|
| **Discovery** | Separate observation from interpretation and prioritize experiments that distinguish competing explanations. |
| **Uncertainty ledger** | Retain assumptions, missing information, controls and safety/stopping conditions. |
| **AoA** | Compare entities, relations, functions, dynamics, boundaries, governance and context. |
| **Transfer discipline** | Distinguish surface resemblance from stronger structural equivalence; state where the comparison fails. |
| **Optional proposal profile** | Validate traceable unaccepted proposals for downstream review without submitting or accepting Index objects. |

## How it works

Use Discovery alone to choose the next discriminating observation. Use AoA alone when an existing evidence base is sufficient for structural comparison. In the combined workflow, Discovery produces structured evidence and AoA proposes abstractions; each candidate keeps uncertainty and provenance. The optional handoff remains explicitly unaccepted until a receiving system makes its own decision.

A valid signature, chain inclusion, message receipt, reasoning instruction or evidence-package digest does not authorize execution. Institutional authority must be supplied and evaluated through the appropriate trusted boundary.

## Getting started

Read [SKILL.md](SKILL.md) and [INSTALLATION.md](INSTALLATION.md). Ask explicitly for “Discovery only,” “AoA only” or the combined sequence. Keep Discovery and AoA operationally distinct. The commands below validate proposal examples and component tests; they do not execute research experiments or measure model behavior.

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_proposals.py
python -m unittest discover -s tests -v
```

## Scope and compatibility

The hub selects the instruction package as an optional layer. The [proposal handoff profile](docs/INDEX_HANDOFF_PROFILE.md) and its schema/tests are component artifacts, not automatic Index acceptance or hub-qualified downstream submission. Proposed or unexecuted experiments cannot contain invented results; executed experiments with unavailable results must preserve that missing information.

Test results, run commentary and historical qualification records are maintained in the [central test hub](https://github.com/cogno-us/cognous-stack-qualification/blob/main/results/readme-commentary/index.md). Read them against their recorded source revisions; source selection and deployment approval are separate decisions.

## Limitations and deployment decisions

The protocol does not run physical experiments, verify factual truth, supply missing findings or establish institutional authority. A valid proposal is not an accepted Index object. Behavioral benefits remain unmeasured in the hub; static/schema checks do not demonstrate scientific discovery or model efficacy.

Review original artifacts and their exact source revisions before extending a claim to a new environment. New dependencies, authority sources, destinations or enforcement mechanisms need their own compatibility and qualification. A passing reference case is not a certification of an enterprise deployment.

## Repository guide

Use these sources for details; their historical checkpoints retain the status and scope of the work they recorded:

- [SKILL.md](SKILL.md)
- [INSTALLATION.md](INSTALLATION.md)
- [docs/INDEX_HANDOFF_PROFILE.md](docs/INDEX_HANDOFF_PROFILE.md)
- [evaluations/README.md](evaluations/README.md)

For a nontechnical introduction, read the [business overview](collateral/business-collateral.md) and [one-page overview](collateral/one-page-overview.md). Both describe this component's role and evidence limits, not additional runtime features.

## Contributing and attribution

Propose focused changes through repository issues and pull requests. Keep evidence-linked claims, preserve historical records and separate proposed features from accepted implementation.

See [LICENSE](LICENSE) and [attribution](NOTICE) for the existing terms and third-party scope. Developed by [Cognous](https://cogno.us); no licensing change is part of this documentation update.

---

## Bibliography

Selected external sources from the October 2026 research review. These inform evaluation questions; they do not establish Cognous implementation, adoption, conformance or production qualification.

- [John W. Creswell and J. David Creswell. *Research Design: Qualitative, Quantitative, and Mixed Methods Approaches*, fifth edition. SAGE (2018)](https://edge.sagepub.com/creswellrd5e). Research-methods reference for explicit questions, comparison designs and interpretation limits.
- [Siddharth Gollapudi, Nilesh Gupta, Prasann Singhal and Sewon Min. *Can Language Models Actually Retrieve In-Context? Drowning in Documents at Million Token Scale*. arXiv:2607.01538v1 (2026)](https://arxiv.org/abs/2607.01538v1). Experimental retrieval research; useful context for testing source retrieval, not evidence of authorization correctness.
- [Mick Yang et al. *AI Epistemic Risks: Emerging Mechanisms & Evidence* (2026)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6873005). Research synthesis on persuasion, cognitive offloading and feedback loops; context for evidence quality and independent judgment.

See the [research bibliography](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/research-bibliography.md) for review scope and source-verification limits.

## Cognous stack components

The six groups organize component responsibilities. They are not an execution
sequence or a requirement to install every component. The [hub lock](https://github.com/cogno-us/cognous-open-control-stack/blob/main/component-lock.json)
defines the selected integration; [release status](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/release-status.md)
defines its evidence and limits.

| Group | Components |
| --- | --- |
| **01 · Knowledge & Provenance** | [The Index (Evidence Registry)](https://github.com/cogno-us/cognous-evidence-registry) · [BitRep (Evidence Attestation)](https://github.com/cogno-us/cognous-evidence-attestation) |
| **02 · Institutional Governance** | [Alvorada (Institutional Governance)](https://github.com/cogno-us/cognous-institutional-governance) · authority contracts |
| **03 · Declaration & Policy Control** | [Action Manifest](https://github.com/cogno-us/cognous-action-manifest) · [Control Plane](https://github.com/cogno-us/cognous-control-plane) |
| **04 · Constrained Execution** | [Execution Runtime (Moltbot Safe)](https://github.com/cogno-us/cognous-execution-runtime) |
| **05 · Replay & Evidence** | [Replay Bundle](https://github.com/cogno-us/cognous-replay-bundle) · [Governance Evidence Pack](https://github.com/cogno-us/cognous-governance-evidence-pack) · [ODES](https://github.com/cogno-us/open-decision-evidence-standard) |
| **06 · Reasoning & Human Oversight** | [PRP](https://github.com/cogno-us/portable-reasoning-protocol) · [Research Intelligence](https://github.com/cogno-us/research-intelligence-protocol) · [TFA](https://github.com/cogno-us/truth-freedom-agency-protocol) |

**Cross-cutting exchange:** [Governed Exchange (GAX/IMX)](https://github.com/cogno-us/cognous-governed-exchange) connects
governed messages, recipient assessment and continuity across the groups. It is
separate from Alvorada's institutional authority framework.

Execution Runtime and Moltbot Safe name the same repository here. The supported
Cognous Python execution boundary remains distinct from the retained upstream
application. PRP, Research Intelligence and TFA are optional behavioral
instructions; they do not enforce authorization or substitute for human oversight.
A signature, registry entry, message receipt or evidence summary does not grant
execution authority.


## Repository locations

See the [repository rename map and compatibility notes](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/repository-renames.md) for current component URLs. Existing package names, schema identifiers and retained producer identities are unchanged.

<!-- Retained anchors for existing documentation links. -->
<a id="evidence-and-supported-scope"></a>
