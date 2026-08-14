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
- [writing-docs](skills/foundations/writing-docs/SKILL.md) — Shared discipline for clear, grounded documents.
- [architecture-foundations](skills/foundations/architecture-foundations/SKILL.md) — Shared architecture reasoning across four views.

### Knowledge

- [write-knowledge-document](skills/knowledge/write-knowledge-document/SKILL.md) — Create durable knowledge by reader use.
- [design-knowledge-architecture](skills/knowledge/design-knowledge-architecture/SKILL.md) — Build reusable architecture knowledge without making project commitments.

### Product

- [write-product-requirements](skills/product/write-product-requirements/SKILL.md) — Align product scope, behavior, and acceptance.

### Technical

- [design-delivery-architecture](skills/technical/design-delivery-architecture/SKILL.md) — Turn requirements into a project-specific architecture commitment. This replaces `write-technical-design`.
- [write-decision-record](skills/technical/write-decision-record/SKILL.md) — Preserve one material decision and its review triggers.

### Visual

- [draw-technical-architecture-diagrams](skills/visual/draw-technical-architecture-diagrams/SKILL.md) — Select, create, and verify the smallest useful technical visual.

## Adding a skill

Add a deliverable skill only when an artifact has a distinct reader decision, stable structure, and completion test. Put shared writing or architecture method in the matching foundation instead of copying it.
