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

## Overview

A modular SKILL.md-based research workflow with two distinct components: Discovery structures observations, hypotheses and discriminating experiments; Abstractor of Abstractors (AoA) compares structure and proposes transferable invariants with explicit limits.

**Implementation status:** this README describes merged public reference work. Component acceptance, selection in the hub and execution of a qualification are separate facts. The selected revision for this component is `30c7274b49c07a0df4c8ca7b281f2e3f8ae68dee`; the [hub lock](https://github.com/cogno-us/cognous-open-control-stack/blob/5737267d94d2b445735c95e8480a31de73a2abe8/component-lock.json) is the source of that integration choice.

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

## Evidence and supported scope

The hub selects the instruction package as an optional layer. The [proposal handoff profile](docs/INDEX_HANDOFF_PROFILE.md) and its schema/tests are component artifacts, not automatic Index acceptance or hub-qualified downstream submission. Proposed or unexecuted experiments cannot contain invented results; executed experiments with unavailable results must preserve that missing information.

The accepted [hub persistence-generation evidence](https://github.com/cogno-us/cognous-open-control-stack/blob/5737267d94d2b445735c95e8480a31de73a2abe8/examples/control-plane-store-adoption/qualification-summary.json) records 915 Python tests in each of two repetitions, 35 matrix entries satisfying their gates and 120 separate mocked OpenShell tests. Those are aggregate hub results, not a per-component test count or a claim of production readiness. Optional behavioral layers receive static checks only. The [support ledger](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/release-status.md) separates implementation, execution and adoption.

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

[Stack hub](https://github.com/cogno-us/cognous-open-control-stack) · [Selected pins](https://github.com/cogno-us/cognous-open-control-stack/blob/main/component-lock.json) · [Evidence and limits](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/release-status.md)

Component links are navigation, not a requirement to install every component. The hub lock determines its supported integration.

| Component | Responsibility |
|---|---|
| [Cognous Action Manifest](https://github.com/cogno-us/cognous-action-manifest) | Declare the action before evaluating permission |
| [Cognous Control Plane](https://github.com/cogno-us/cognous-control-plane) | Evaluate proposals against authority and preserve the decision record |
| [Cognous Replay Bundle](https://github.com/cogno-us/cognous-replay-bundle) | Reconstruct what the retained records support |
| [Cognous Governance Evidence Pack](https://github.com/cogno-us/cognous-governance-evidence-pack) | Turn traceable runtime records into reviewable governance evidence |
| [Open Decision Evidence Standard](https://github.com/cogno-us/open-decision-evidence-standard) | Portable decision evidence across system and organizational boundaries |
| [Cognous Governed Exchange](https://github.com/cogno-us/cognous-governed-exchange) | Governed exchange and continuity for a bounded synthetic workflow |
| [Cognous Execution Runtime](https://github.com/cogno-us/cognous-execution-runtime) | Constrained execution beneath independent current authorization |
| [Cognous Evidence Attestation](https://github.com/cogno-us/cognous-evidence-attestation) | Verify issuer signatures under explicit trust assumptions |
| [Cognous Evidence Registry](https://github.com/cogno-us/cognous-evidence-registry) | A local blockchain reference for claims, evidence commitments and lifecycle history |
| [Portable Reasoning Protocol v1.0](https://github.com/cogno-us/portable-reasoning-protocol) | Portable instructions for evidence-bounded reasoning |
| [TFA Protocol (S43)](https://github.com/cogno-us/truth-freedom-agency-protocol) | Truth · Freedom · Agency |
| [Cognous Institutional Governance](https://github.com/cogno-us/cognous-institutional-governance) | Alvorada: authority, challenge and correction for institutions |

## Repository locations

See the [repository rename map and compatibility notes](https://github.com/cogno-us/cognous-open-control-stack/blob/main/docs/repository-renames.md) for current component URLs. Existing package names, schema identifiers and retained producer identities are unchanged.
