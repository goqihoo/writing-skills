# Scribe

Composable agent skills for professional documents and technical visuals. Start with `ask-scribe` when you do not know which skill owns the work.

## Invocation

Use `$ask-scribe` in Agent Skills-compatible clients or `/ask-scribe` in Claude Code. Ask Scribe recommends the smallest matching skill or short flow, then stops.

## Installation

Choose one route. The Claude Code plugin installs the complete bundle; [skills.sh](https://skills.sh/) lets Codex and other compatible agents select individual skills. Installing both creates duplicates.

### Claude Code

```bash
claude plugin marketplace add goqihoo/writing-skills
claude plugin install scribe@goqihoo
```

From Claude Code:

```text
/plugin marketplace add goqihoo/writing-skills
/plugin install scribe@goqihoo
```

### Codex and other agents

```bash
npx skills@latest add goqihoo/writing-skills
```

Run `npx skills@latest update` to receive later revisions.

## Maintainer setup

Expose every skill to local Claude Code and Agent Skills-compatible harnesses:

```bash
scripts/link-skills.sh
```

The linker refuses to replace a non-symlink with the same skill name.

## Skills

### Entry and foundations

- [ask-scribe](skills/foundations/ask-scribe/SKILL.md) — Route a document task to the right Scribe skill. Explicit invocation only.
- [write-docs](skills/foundations/write-docs/SKILL.md) — Apply the shared method for clear, grounded documents.
- [reason-architecture](skills/foundations/reason-architecture/SKILL.md) — Reason about architecture across four views.

### Knowledge

- [write-knowledge](skills/knowledge/write-knowledge/SKILL.md) — Create durable knowledge by reader use.
- [study-architecture](skills/knowledge/study-architecture/SKILL.md) — Build reusable architecture knowledge without making project commitments.

### Product

- [write-prd](skills/product/write-prd/SKILL.md) — Align product scope, behavior, and acceptance.

### Technical

- [design-architecture](skills/technical/design-architecture/SKILL.md) — Turn requirements into a project-specific architecture commitment.
- [record-decision](skills/technical/record-decision/SKILL.md) — Preserve one material decision and its review triggers.

### Visual

- [draw-diagrams](skills/visual/draw-diagrams/SKILL.md) — Select, create, and verify the smallest useful technical visual.

## Adding a skill

Add a deliverable skill only when an artifact has a distinct reader decision, stable structure, and completion test. Put shared writing or architecture method in the matching foundation instead of copying it.
