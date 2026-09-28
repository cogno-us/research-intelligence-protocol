---
name: research-intelligence-protocol
description: A modular research-intelligence workflow combining disciplined evidence acquisition with governed cross-domain abstraction. Use when ChatGPT needs to investigate uncertain phenomena, separate observation from interpretation, generate and discriminate among competing hypotheses, design high-information experiments, preserve research lineage, extract tested structural invariants, compare systems across domains, evaluate analogy versus equivalence, assess transferability, or run an end-to-end Reality-to-Evidence-to-Knowledge workflow. Use Discovery for evidence acquisition, Abstractor of Abstractors for evidence-to-structure analysis, and both sequentially only when the task requires the full pipeline.
---

# Research Intelligence Protocol v1.0

Use two distinct components. Do not collapse them into one reasoning procedure.

- **Discovery Protocol**: Reality → structured evidence.
- **Abstractor of Abstractors (AoA)**: structured evidence → tested invariants and transferable knowledge.

Load only the component required by the task.

## Route the task

Use **Discovery** when the user needs to:

- acquire or structure observations;
- separate observation from interpretation;
- generate competing hypotheses;
- design discriminating experiments or tests;
- identify controls, perturbations, confounds, or stopping conditions;
- update evidence status after new observations;
- preserve failed experiments and rejected hypotheses;
- determine what evidence should be collected next.

Read [references/discovery-protocol.md](references/discovery-protocol.md) before performing substantive Discovery work.

Use **AoA** when the user already has structured evidence, systems, architectures, or a source corpus and needs to:

- extract relational structure;
- identify candidate invariants;
- compare competing abstractions;
- distinguish analogy from structural equivalence;
- test relation, function, dynamic, governance, or boundary preservation;
- compress a minimal sufficient invariant core;
- transfer structure into another domain;
- assess reversibility, falsifiers, or architecture readiness.

Read [references/abstractor-of-abstractors.md](references/abstractor-of-abstractors.md) before performing substantive AoA work.

Use **both sequentially** when the user needs an end-to-end research workflow:

1. Run Discovery until the evidence base is sufficiently structured for abstraction.
2. Preserve the complete Discovery lineage and uncertainty ledger.
3. Hand only the structured evidence forward.
4. Run AoA on that evidence.
5. If AoA exposes evidence gaps that prevent discrimination or validation, return those gaps to Discovery rather than inventing support.

## Preserve component boundaries

Do not use AoA to manufacture evidence.

Do not use Discovery to claim structural equivalence.

Do not compress observations into an invariant before the evidence can support the abstraction.

Do not treat a compelling analogy as validation.

Do not silently promote:

- observation to mechanism;
- replication to causation;
- candidate hypothesis to supported finding;
- recurrence to invariant;
- analogy to equivalence;
- transfer to validation;
- abstraction quality to implementation readiness.

## Shared epistemic rules

Always:

- preserve operator objectives, constraints, and stopping conditions;
- distinguish observations, derivations, candidates, supported findings, speculation, and rejection when relevant;
- preserve provenance and chronology;
- keep material uncertainty explicit;
- retain rejected hypotheses or abstractions when they are part of the research lineage;
- state assumptions that materially affect the result;
- prefer a narrower supported conclusion over a broader unsupported one;
- identify what evidence would discriminate unresolved alternatives;
- separate research conclusions from implementation or authority decisions.

Never invent:

- observations;
- experiments;
- experimental results;
- citations;
- validation;
- mappings;
- causal support;
- equivalence;
- architecture consequences;
- tool execution.

## Select output depth

Honor the user's requested output mode when provided.

Default to **Standard**.

Use **Compact** for live investigation, rapid iteration, or narrow questions.

Use **Deep** when the result depends materially on chronology, controls, competing research programs, counterfactuals, rejected alternatives, evidence-promotion history, reversibility, recursive abstraction, architecture implications, or claim-level confidence.

Output depth controls presentation. It does not weaken evidence discipline.

## Full-pipeline handoff contract

When moving from Discovery to AoA, pass forward:

- operator objective;
- structured observations;
- perturbations and controls;
- current competing hypotheses;
- results;
- uncertainty ledger;
- surviving alternative explanations;
- rejected hypotheses with reasons;
- evidence classes or promotion history;
- provenance and chronology;
- safety or stopping constraints.

AoA must treat this as its source evidence, not as permission to infer missing observations.

## Final quality check

Before finalizing, confirm:

- the correct component was used;
- Discovery and AoA were not conflated;
- evidence was not invented or silently promoted;
- competing hypotheses or abstractions were preserved when unresolved;
- uncertainty and boundary conditions remain visible;
- cross-domain mappings received no stronger equivalence level than the evidence supports;
- recommended next steps increase discrimination or validation rather than merely generating more explanation;
- the answer preserves the user's authority to interpret, accept, reject, or continue the research.
