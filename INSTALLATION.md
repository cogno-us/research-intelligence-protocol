# Installing Research Intelligence Protocol v1.0

Research Intelligence Protocol is distributed as an open `SKILL.md`-based research workflow containing two separate reference components:

- **Discovery Protocol** — Reality → structured evidence
- **Abstractor of Abstractors (AoA)** — structured evidence → tested invariants and transferable knowledge

Repository: https://github.com/cogno-us/research-intelligence-protocol  
Developed by **[Cognous](https://cogno.us)**.

> **Important:** Platform capabilities change. The instructions below distinguish native Agent Skill support from compatibility methods rather than assuming every platform implements the same Skill standard.

---

## 1. Required package structure

Keep the files together:

```text
research-intelligence-protocol/
├── SKILL.md
├── README.md
├── INSTALLATION.md
├── agents/
│   └── openai.yaml
└── references/
    ├── discovery-protocol.md
    └── abstractor-of-abstractors.md
```

Do not merge the two reference files. The Skill relies on progressive loading so that Discovery and AoA remain distinct components.

---

## 2. ChatGPT

### Recommended: upload as a Skill

For eligible ChatGPT workspaces with Skills enabled:

1. Open **ChatGPT**.
2. Open **Plugins** from the sidebar.
3. Open the **Skills** tab.
4. Select **Create**.
5. Choose **Upload from your computer**.
6. Upload a ZIP containing the complete directory shown above.
7. Review the Skill contents and complete installation.
8. Start a new chat and invoke the desired component.

Examples:

- `Use the Discovery Protocol to investigate this failure.`
- `Apply Abstractor of Abstractors to this evidence set.`
- `Run the Research Intelligence Protocol end to end.`

ChatGPT may also select the Skill automatically when the description matches the task.

### Fallback when Skills are unavailable

Use the body of `SKILL.md` as persistent project/workspace instructions where available, and make both reference files available as project knowledge or attached files.

This preserves much of the behavior but does **not** provide native Skill discovery or progressive loading.

---

## 3. Claude

Claude supports Agent Skills built around `SKILL.md`.

### Claude Code — project installation

Place the Skill directory under:

```text
.claude/skills/research-intelligence-protocol/
```

Example:

```text
your-project/
└── .claude/
    └── skills/
        └── research-intelligence-protocol/
            ├── SKILL.md
            └── references/
                ├── discovery-protocol.md
                └── abstractor-of-abstractors.md
```

### Claude Code — personal installation

For use across projects:

```text
~/.claude/skills/research-intelligence-protocol/
```

Keep both reference files with the Skill.

### Invocation

Examples:

- `Use Discovery to identify the next discriminating test.`
- `Use AoA to test whether these systems share a structural invariant.`
- `Run Discovery first, then hand the structured evidence to AoA.`

Where a Claude surface does not expose direct Agent Skill installation, use project instructions and supporting files as a compatibility method.

---

## 4. Gemini

Gemini's end-user customization mechanism may use **Gems** rather than the same native `SKILL.md` installation model.

The recommended compatibility configuration is a **Research Intelligence Protocol Gem**.

### Create the Gem

1. Open Gemini.
2. Open **Gems**.
3. Create a new Gem named:
   ```text
   Research Intelligence Protocol
   ```
4. Copy the body of `SKILL.md` into the Gem's instructions.
5. Add both files under `references/` as knowledge files if supported.
6. Save the Gem.
7. Test Discovery and AoA independently before testing the combined pipeline.

Recommended configuration:

- **Instructions:** `SKILL.md`
- **Knowledge:** `references/discovery-protocol.md`
- **Knowledge:** `references/abstractor-of-abstractors.md`

A Gem is a compatibility implementation. Do not describe it as native installation of this Agent Skill package unless the relevant Gemini surface explicitly supports compatible Skills.

---

## 5. GitHub Copilot

GitHub Copilot supports Agent Skills in supported environments.

### Project installation

Create:

```text
.github/skills/research-intelligence-protocol/
```

and place the Skill files inside:

```text
your-repository/
└── .github/
    └── skills/
        └── research-intelligence-protocol/
            ├── SKILL.md
            └── references/
                ├── discovery-protocol.md
                └── abstractor-of-abstractors.md
```

Supported environments may also recognize compatible Skill locations such as `.claude/skills` or `.agents/skills`.

### Personal installation

Where supported, install under a personal skills directory such as:

```text
~/.copilot/skills/research-intelligence-protocol/
```

or:

```text
~/.agents/skills/research-intelligence-protocol/
```

### Alternative: repository custom instructions

If you intentionally want the routing rules to apply to essentially every Copilot interaction in a repository, adapt the control-plane rules into:

```text
.github/copilot-instructions.md
```

For conditional loading and modular references, the Agent Skill form is preferable.

---

## 6. Verify the installation

Test the components separately.

### Discovery test

```text
Use the Discovery Protocol.

Observation:
A service fails intermittently only during peak load.

Generate genuinely competing hypotheses, identify the smallest test that
would best discriminate among them, state controls and confounds, and
preserve unresolved uncertainty.
```

A working installation should not jump directly to one explanation.

### AoA test

```text
Use Abstractor of Abstractors.

Compare these two systems structurally. Distinguish surface resemblance
from relational, functional, dynamic, governed, or formal equivalence.
State the strongest justified equivalence level and its failure conditions.
```

A working installation should not promote analogy into equivalence without support.

### Full-pipeline test

```text
Run the Research Intelligence Protocol end to end.

Use Discovery first. Only after the evidence is structured, hand it to AoA.
If AoA requires evidence that does not exist, return the gap to Discovery.
```

Do not verify installation merely by checking whether the model says the Skill is active. Test whether component boundaries and research behavior actually change.

---

## 7. Updating

When a new version is released:

1. Replace the existing Skill directory with the new version.
2. Preserve the directory name `research-intelligence-protocol` unless release notes explicitly require migration.
3. Keep Discovery and AoA as separate reference files.
4. Restart or reload the relevant AI environment if necessary.
5. Re-run component and full-pipeline tests.

For compatibility configurations such as Gems, update the instructions and both knowledge files.

---

## 8. Security and trust

Agent Skills can contain instructions, resources, and in some ecosystems executable scripts. Review any Skill before installing it.

This distribution is intentionally instruction-centric and does not require executable code for its research behavior.

Use the canonical repository when possible:

https://github.com/cogno-us/research-intelligence-protocol

---

**Research Intelligence Protocol v1.0**  
Discovery Protocol + Abstractor of Abstractors  
Developed by **[Cognous](https://cogno.us)**.
