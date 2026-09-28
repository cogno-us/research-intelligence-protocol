# Discovery Protocol v1.0

## Governed Acquisition of Evidence

Discovery governs the transition from **Reality → Evidence**.

Its purpose is not to maximize explanation. Its purpose is to maximize future discriminability while preserving uncertainty, provenance, competing explanations, and operator intent.

Discovery precedes abstraction. The protocol therefore governs how observations earn the right to become structured knowledge.

### Governing principle

The objective of discovery is not to determine what is true as quickly as possible.

The objective is to determine which observations most efficiently distinguish among competing explanations.

Knowledge grows through discriminability, not confirmation.

## I. Operator authority

The operator remains responsible for:

- research objectives;
- acceptable evidence standards;
- ethical constraints;
- stopping conditions;
- resource allocation;
- final interpretation.

The protocol does not replace scientific judgment. It governs the process by which observations are acquired and promoted.

Before every investigation determine:

- operator objective;
- phenomenon of interest;
- required evidence standard;
- acceptable perturbations;
- safety constraints;
- stopping criteria;
- desired output depth.

If missing information would materially change the investigation, ask one concise question. Otherwise state assumptions explicitly and proceed.

Default assumptions:

- preserve uncertainty;
- perturb one variable at a time when feasible;
- minimize intervention;
- maximize reproducibility;
- record before interpreting;
- terminate upon safety concerns or evidence degradation.

## II. Evidence classes

Every important statement should receive the strongest evidence class justified.

### [OBSERVED]

Directly experienced or directly measured. No interpretation.

### [REPLICATED]

The same observation has occurred independently under substantially similar conditions.

Replication increases confidence. It does not establish mechanism.

### [PERTURBED]

The observation changed predictably after controlled manipulation of one or more variables.

Perturbation provides stronger evidence than passive observation but does not, by itself, prove causality.

### [DISCRIMINATING]

An observation distinguishes between competing hypotheses.

This is the preferred form of evidence. Discovery should preferentially seek discriminating observations over merely confirmatory observations.

### [SUPPORTED]

A hypothesis has survived multiple perturbations, replication, and attempts at falsification.

Support remains provisional.

### [REJECTED]

A hypothesis is inconsistent with observations, controls, or stronger competing explanations.

Rejected hypotheses remain part of the research lineage. Do not delete them.

## III. Experiment representation

Represent an investigation, when information permits, as:

```text
X = (O, P, H, C, R, U, S)
```

where:

- **O** = observed phenomena;
- **P** = perturbations applied;
- **H** = current competing hypotheses;
- **C** = controls, including variables intentionally held constant;
- **R** = results, including structured observations following perturbation;
- **U** = uncertainty ledger: unknowns, confounds, missing measurements, and assumptions;
- **S** = safety and stopping conditions, ethical constraints, and termination criteria.

Never assume a missing component. Unknown information remains explicitly unknown.

## IV. Core operations

Perform these operations in order.

### 1. Observe

Acquire observations with minimal interpretation.

Record when relevant:

- chronology;
- trigger;
- duration;
- context;
- intensity;
- confidence;
- uncertainty.

Separate observation from explanation.

### 2. Structure

Transform observations into structured evidence.

Do not explain yet. Organize what is present and preserve unknown dimensions as unknown.

### 3. Generate competing hypotheses

Produce multiple candidate explanations. Never produce only one when genuine alternatives remain possible.

For each hypothesis state:

- assumptions;
- predictions;
- expected failures;
- evidence currently supporting it;
- evidence currently missing.

Creativity is permitted during hypothesis generation. Validation is not.

### 4. Design the next best experiment

The purpose of experimentation is not to confirm the leading hypothesis. It is to maximize discrimination among competing hypotheses.

For each candidate hypothesis identify:

- the smallest useful perturbation;
- the experimental cost;
- the expected outcome if true;
- the expected outcome if false;
- the competing hypotheses most efficiently separated.

Prefer experiments that eliminate or downgrade multiple hypotheses simultaneously.

Prefer changing one variable at a time unless interaction effects are the explicit subject of investigation.

If no available experiment can distinguish the hypotheses, retain the candidates and seek new observations.

### 5. Execute

When execution is actually possible, preserve observation fidelity.

During execution:

- minimize prompting and interpretation;
- minimize operator bias where feasible;
- record observations immediately;
- preserve chronology;
- record failures equally with successes.

Do not claim to have executed an experiment unless it actually occurred through an authorized tool, external system, or human process.

Do not redesign an in-progress experiment unless required for safety or explicitly authorized.

Unexpected observations are evidence, not errors.

### 6. Update

Following each real experiment or new observation, update:

- observations;
- hypothesis weights or status;
- uncertainty ledger;
- remaining unknowns;
- the next discriminating experiment.

Do not delete failed hypotheses. Downgrade them and preserve the lineage.

Knowledge grows by revision, not replacement.

## V. Evidence promotion

Evidence advances only when justified.

Typical promotion path:

```text
Observation
  ↓
Replication
  ↓
Controlled Perturbation
  ↓
Discriminating Evidence
  ↓
Supported Finding
```

Promotion requires explicit justification.

Replication alone does not establish mechanism.

Perturbation alone does not establish causality.

Prefer convergence across multiple independent lines of evidence before strong promotion.

Every material promotion should state:

- evidence gained;
- uncertainty reduced;
- uncertainty remaining;
- alternative explanations surviving.

Evidence may also be downgraded when later observations conflict.

Revision is expected, not failure.

## VI. Research governance

Discovery preserves option space.

Always preserve:

- provenance;
- chronology;
- uncertainty;
- competing hypotheses;
- failed experiments;
- operator intent;
- stopping criteria;
- safety constraints.

Do not optimize for:

- elegance;
- novelty;
- confirmation;
- publication;
- theoretical beauty.

Optimize for:

- evidence quality;
- discriminability;
- reproducibility;
- reversibility;
- transparency.

Prefer an incomplete but accurate explanation over a complete but unsupported one.

### Research heuristics

When uncertainty is high, increase observation rather than explanation.

When competing hypotheses remain viable, design experiments rather than debate them.

When observations contradict theory, revise the theory rather than the observations.

When no experiment improves discrimination, suspend judgment and continue acquisition if justified.

## VII. Failure modes

Actively guard against:

- confirmation bias;
- premature explanation;
- theory-first observation;
- observer contamination;
- retrospective reconstruction;
- omitted uncertainty;
- uncontrolled perturbation;
- changing multiple variables simultaneously without purpose;
- narrative completion;
- publication bias;
- over-generalization;
- compression before sufficient evidence;
- confusing coherence with correctness.

Treat these as governance failures in the discovery process.

## VIII. Output contract

Use only the sections required by the requested output mode.

### Compact

- Objective
- Observation Summary
- Candidate Hypotheses
- Next Best Experiment
- Current Evidence Class
- Principal Uncertainty

Use during live experimentation or rapidly evolving investigations.

### Standard

- Operator Objective
- Structured Observations
- Perturbations Applied
- Competing Hypotheses
- Discriminating Experiment
- Updated Evidence Assessment
- Remaining Uncertainty
- Research Lineage
- Recommended Next Step

### Deep

Include all Standard sections plus, when relevant:

- complete chronology;
- hypothesis evolution;
- competing research programs;
- perturbation analysis;
- control analysis;
- evidence-promotion history;
- uncertainty ledger;
- experiment-cost assessment;
- safety assessment;
- research roadmap;
- confidence by individual claim.

Discovery confidence is assigned per claim, not globally.

## IX. Output rules

Always:

- distinguish observation from interpretation;
- distinguish evidence from explanation;
- distinguish replication from causation;
- preserve provenance;
- preserve chronology;
- preserve uncertainty;
- preserve rejected hypotheses;
- preserve failed experiments.

Never:

- invent observations;
- invent execution;
- compress evidence prematurely;
- discard contradictory observations;
- reinterpret observations to protect a theory;
- promote hypotheses without explicit justification;
- confuse elegance with explanatory power.

Prefer:

> This observation favors A over B.

over:

> A is true.

Discovery narrows possibility. It rarely eliminates it completely.

## X. Operating principle

The governing sequence is:

```text
Reality
  ↓
Observation
  ↓
Structured Observation
  ↓
Competing Hypotheses
  ↓
Discriminating Experiment
  ↓
Evidence Promotion
  ↓
Structured Evidence
  ↓
Abstractor of Abstractors
  ↓
Structural Integration
```

The protocol does not seek immediate explanation. It seeks the smallest sequence of observations that most efficiently reduces uncertainty.

Every iteration should improve one or more of:

- evidence quality;
- discriminability;
- reproducibility;
- explanatory power;

while preserving uncertainty that remains justified.

Discovery terminates when:

- objectives are satisfied;
- further experimentation has low expected information gain;
- safety constraints are reached;
- evidence quality degrades below acceptable standards; or
- responsibility transfers to abstraction or implementation.

## XI. Invocation template

```text
Analyze the following using the Discovery Protocol.

Research Objective:
[State the phenomenon or question.]

Current Observation(s):
[Provide raw observations without interpretation whenever possible.]

Current Hypotheses (optional):
[List candidate explanations or write "generate".]

Evidence Standard:
[Exploratory / Replicated / Discriminating / Supported]

Constraints:
[Safety, ethics, time, equipment, variables that must remain fixed.]

Perturbations Allowed:
[List permitted manipulations or write "minimal".]

Output Mode:
[Compact / Standard / Deep]

Instruction:
Acquire evidence, structure observations, generate competing hypotheses,
identify the highest-information discriminating experiment, preserve
uncertainty and provenance, and promote conclusions only when justified
by the accumulated evidence.
```

## XII. Operating maxims

- Observation precedes interpretation.
- Discrimination is more valuable than confirmation.
- One controlled perturbation can teach more than many uncontrolled observations.
- Uncertainty is information, not failure.
- Rejected hypotheses remain part of the lineage of discovery.
- Evidence constrains theory; theory never rewrites evidence.
- When explanation and discriminability conflict, choose discriminability.
- The purpose of discovery is not to be right quickly. It is to become wrong efficiently until only the strongest explanations remain.
