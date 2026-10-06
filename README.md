# Research Intelligence Protocol v1.0

**A portable research-intelligence workflow for disciplined discovery and cross-domain structural abstraction.**

Developed by **[Cognous](https://cogno.us)**.

Research Intelligence Protocol v1.0 packages two complementary protocols as one reusable `SKILL.md`-based Skill while keeping them operationally distinct:

1. **Discovery Protocol** — governs the path from reality, observations, and experiments to structured evidence.
2. **Abstractor of Abstractors (AoA)** — governs the path from structured evidence to tested invariants, cross-domain transfer, and architecture-ready knowledge.

The components can be invoked independently or sequentially. Discovery is not folded into AoA, and AoA is not used as a substitute for evidence acquisition.

## What it is

Research Intelligence Protocol is an instruction-layer research workflow for general-purpose AI systems. It is designed for problems where ordinary summarization or brainstorming is insufficient: research questions, competing explanations, experiment design, causal uncertainty, structural comparison, technology transfer, and cross-domain reasoning.

The core sequence is:

```text
Reality
  ↓
Discovery Protocol
  ↓
Structured Evidence
  ↓
Abstractor of Abstractors
  ↓
Tested Invariants
  ↓
Transferable Knowledge
```

The bundle is deliberately modular. A task that only requires evidence acquisition should stop after Discovery. A task that begins with an existing evidence base can invoke AoA directly. A full research-intelligence workflow can run both in sequence.

## Component 1: Discovery Protocol

Discovery is designed to improve **evidence acquisition and hypothesis discrimination**.

Its governing principle is:

> Prefer observations and experiments that distinguish among competing explanations over observations that merely confirm the current favorite.

Discovery structures an investigation around:

```text
X = (O, P, H, C, R, U, S)
```

where:

- **O** = observed phenomena;
- **P** = perturbations;
- **H** = competing hypotheses;
- **C** = controls;
- **R** = results;
- **U** = uncertainty ledger;
- **S** = safety and stopping conditions.

Its workflow emphasizes observation before interpretation, multiple competing hypotheses, controlled perturbation, explicit uncertainty, research lineage, and evidence promotion only when justified.

## Component 2: Abstractor of Abstractors

AoA is designed to transform structured evidence into **reusable invariant structure** without confusing analogy with equivalence.

It represents systems, when information permits, as:

```text
S = (E, R, F, D, B, G, C)
```

where:

- **E** = entities;
- **R** = relations;
- **F** = functional roles;
- **D** = dynamics;
- **B** = boundaries;
- **G** = governance;
- **C** = context and substrate.

AoA uses an equivalence ladder:

| Level | Meaning |
|---|---|
| E0 | Surface resemblance |
| E1 | Relational correspondence |
| E2 | Functional equivalence |
| E3 | Dynamic correspondence |
| E4 | Governed structural equivalence |
| E5 | Formal isomorphism |

The protocol requires candidate abstractions to compete, survive structural discrimination, preserve provenance and uncertainty, and state transfer limits explicitly.

## Why the two components are separate

Discovery and AoA solve different epistemic problems.

**Discovery asks:** What evidence should we acquire next, and what does that evidence justify?

**AoA asks:** What reusable structure survives across the evidence, and how far can that structure legitimately transfer?

Keeping the components separate reduces a common failure mode in AI-assisted research: abstracting too early from observations that have not earned sufficient evidentiary status.

## Who it is for

Research Intelligence Protocol is intended for people and teams using AI in research-intensive or evidence-sensitive work, including:

- scientific and technical researchers;
- R&D organizations;
- engineering teams;
- product and systems architects;
- strategy and management consultants;
- due-diligence and investment teams;
- technology-transfer teams;
- patent and prior-art researchers;
- root-cause and incident-analysis teams;
- interdisciplinary research groups;
- founders and executives evaluating unfamiliar technical domains;
- analysts working across heterogeneous evidence sources.

It is especially useful when a task involves competing hypotheses, weak or incomplete evidence, cross-domain analogy, causal uncertainty, or the temptation to compress a complex system too early.

## Core benefits

### Better hypothesis discrimination

Discovery prioritizes experiments and observations that separate competing explanations rather than accumulating supportive examples for one favored theory.

### Explicit uncertainty

Unknowns, confounds, assumptions, missing measurements, and surviving alternatives remain visible instead of being silently collapsed into a single narrative.

### Stronger research lineage

Rejected hypotheses and failed experiments remain part of the record. Conclusions can be revised without rewriting the history of how they were reached.

### More disciplined abstraction

AoA distinguishes observed material, derived structure, candidate abstractions, supported invariants, speculation, and rejected mappings.

### Safer cross-domain transfer

The equivalence ladder prevents superficial resemblance from being presented as functional, dynamic, governed, or formal equivalence.

### Provenance-preserving compression

AoA separates the reusable invariant core from a lineage sidecar containing source support, discarded structure, assumptions, uncertainty, and transformation history.

### Modular use

Use Discovery alone, AoA alone, or both sequentially. The Skill should not run the full pipeline when the user's task only requires one component.

## Typical use cases

### Scientific or technical investigation

Use Discovery to structure observations, generate competing explanations, and identify the next experiment with the highest discriminatory value.

### Root-cause analysis

Use Discovery to distinguish plausible mechanisms with controlled tests rather than arguing from narrative coherence.

### Cross-domain research

Use AoA to determine whether structures in one domain transfer to another at the relational, functional, dynamic, governance, or formal level.

### Technology transfer

Use AoA to map source roles, target roles, preserved relations, known mismatches, transfer assumptions, and falsifiers.

### Patent and architecture research

Use AoA to identify structural invariants while preserving what is observed versus derived and avoiding unsupported equivalence claims.

### Full research-intelligence workflow

Use Discovery first to produce a structured evidence corpus, then AoA to test which structures deserve compression and transfer.

## What it does not do

Research Intelligence Protocol does **not**:

- guarantee factual correctness;
- replace domain experts or scientific judgment;
- create experimental evidence that was not observed;
- make a model capable of performing physical experiments without tools or human execution;
- turn correlation into causation;
- turn analogy into equivalence;
- guarantee formal proof;
- replace primary-source verification;
- replace legal, medical, safety, regulatory, or institutional authority;
- expose or require private chain-of-thought;
- eliminate model variability across platforms and model versions.

It is an instruction-layer discipline for improving research process and structural reasoning.

## Repository structure

```text
research-intelligence-protocol/
├── SKILL.md
├── README.md
├── INSTALLATION.md
├── CHANGELOG.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── discovery-protocol.md
│   └── abstractor-of-abstractors.md
├── docs/
│   └── INDEX_HANDOFF_PROFILE.md
├── schemas/
│   └── research-intelligence-proposal-v1.schema.json
├── examples/
│   └── proposals/
├── evaluations/
│   └── README.md
└── scripts/
    └── validate_proposals.py
```

`SKILL.md` is the runtime control plane. The two protocols remain separate reference components and are loaded only when relevant.

## Installation

See **[INSTALLATION.md](INSTALLATION.md)** for platform-specific instructions for:

- ChatGPT
- Claude
- Gemini
- GitHub Copilot

The guide distinguishes native Agent Skill support from compatibility methods on platforms that use different customization mechanisms.

## How to use it

### Discovery only

```text
Use the Discovery Protocol.

Objective: determine why this system intermittently fails under load.
Generate competing hypotheses, identify the smallest discriminating tests,
preserve uncertainty, and recommend the next best experiment.
```

### AoA only

```text
Use Abstractor of Abstractors on this evidence set.

Identify candidate invariant structures, discriminate among them,
assign the strongest supported equivalence level, and test transfer
into the target domain without treating analogy as identity.
```

### Full sequence

```text
Run the Research Intelligence Protocol end to end.

First use Discovery to structure the evidence and identify unresolved
hypotheses. Then, only when the evidence is sufficient, use AoA to
extract and test transferable invariants.
```

## Output modes

Both components support compact, standard, and deeper output modes.

Use **Compact** for live investigations and rapid iteration.

Use **Standard** for most research, analysis, and transfer work.

Use **Deep** when lineage, controls, counterfactuals, competing abstractions, evidence-promotion history, reversibility, or architecture implications materially affect the result.

Depth should be driven by the research problem, not by a desire for longer prose.

## Design principles

The bundle follows several shared principles:

1. **Observation precedes interpretation.**
2. **Discrimination is more valuable than confirmation.**
3. **Uncertainty is preserved until evidence justifies reduction.**
4. **Competing hypotheses and competing abstractions remain visible.**
5. **Compression must not erase provenance or boundary conditions.**
6. **Analogy must not be promoted into equivalence without structural support.**
7. **Evidence constrains theory; theory does not rewrite evidence.**
8. **Transfer requires explicit mappings, mismatches, assumptions, and falsifiers.**
9. **The operator retains responsibility for objectives, constraints, evidence standards, and final interpretation.**

## Versioning

This repository is **Research Intelligence Protocol v1.0**, the first public Skill release of the combined package.

The component references preserve the substance and lineage of the supplied Discovery Protocol and Abstractor of Abstractors specifications while presenting them as two components within the v1.0 public bundle.

Future changes should distinguish:

- editorial changes;
- implementation changes;
- behavioral changes;
- changes to evidence classes or promotion rules;
- changes to abstraction tests or equivalence semantics.

Material behavioral changes should receive explicit version increments and testing.

## Testing and contribution ideas

Useful tests include:

- whether Discovery generates genuinely competing hypotheses rather than cosmetic variants;
- whether proposed experiments discriminate between hypotheses;
- whether the system preserves negative results and rejected hypotheses;
- whether AoA distinguishes analogy from stronger equivalence;
- whether cross-domain mappings preserve roles, dynamics, governance, and boundaries;
- whether counterexamples downgrade an abstraction appropriately;
- whether uncertainty increases when evidence weakens;
- whether the system knows when to stop Discovery and when to hand off to AoA;
- whether it avoids invoking AoA when the evidence base is too weak.

A useful benchmark should test whether the protocol changes research quality, not merely whether it produces more structured prose.

## Important limitation

Model behavior can vary with model version, host instructions, available tools, retrieval quality, context, and decoding behavior. A protocol can discipline reasoning but cannot certify that a model output is true.

Use the protocol to improve the structure and inspectability of research work, then verify consequential claims against appropriate evidence.


## Optional downstream proposal handoff

Research Intelligence remains standalone. When a user or downstream system explicitly needs a traceable export, outputs may be represented with the optional **Research Intelligence → Index Proposal Handoff Profile v1.0**.

See **[docs/INDEX_HANDOFF_PROFILE.md](docs/INDEX_HANDOFF_PROFILE.md)**.

The profile preserves source references, uncertainty, competing hypotheses, contradictory evidence, experiment execution status and actual results, abstraction/transfer limits, lineage, and explicit missing information. Every exported object remains `proposed_unaccepted`.

The profile does **not** make The Index a dependency, does not submit blockchain transactions, and does not treat signatures, commitments, or Research Intelligence support labels as factual truth or recipient acceptance.

Machine-readable contract and fixtures:

- [schemas/research-intelligence-proposal-v1.schema.json](schemas/research-intelligence-proposal-v1.schema.json)
- [examples/proposals/](examples/proposals/)
- [evaluations/README.md](evaluations/README.md)

Static validation:

```bash
python scripts/validate_proposals.py
```

This checks proposal/example consistency and local links. It is not a behavioral evaluation of the protocols.


---

**Research Intelligence Protocol v1.0**  
Discovery Protocol + Abstractor of Abstractors  
Developed by **[Cognous](https://cogno.us)**  
Research infrastructure for evidence acquisition, structural abstraction, and cross-domain transfer.
