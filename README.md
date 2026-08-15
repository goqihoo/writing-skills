# Scribe

Composable agent skills for professional documents, documentation structure, and technical visuals. Start with `ask-scribe` when you want to understand the available skills or plan how to combine them.

## Invocation

Use `$ask-scribe` in Agent Skills-compatible clients or `/ask-scribe` in Claude Code. Ask Scribe explains the plugin's skills and rules, then helps you choose an invocation or sequence without executing it.

## Installation

Choose one route. The Codex and Claude Code plugins install the complete bundle; [skills.sh](https://skills.sh/) lets other compatible agents select individual skills. Installing more than one route creates duplicates.

### Codex

```bash
codex plugin marketplace add goqihoo/writing-skills
codex plugin add scribe@goqihoo
```

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

### Other agents

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

- [ask-scribe](skills/foundations/ask-scribe/SKILL.md) — Explain Scribe's skills, boundaries, and useful combinations without executing them. Explicit invocation only.
- [structure-docs](skills/foundations/structure-docs/SKILL.md) — Plan directory boundaries, file placement, and documentation structure.
- [write-doc](skills/foundations/write-doc/SKILL.md) — Apply the shared method for one clear, grounded document.
- [reason-architecture](skills/foundations/reason-architecture/SKILL.md) — Reason about architecture across four views.

### Knowledge

- [structure-domain-docs](skills/knowledge/structure-domain-docs/SKILL.md) — Plan or scaffold one domain's directory, coverage map, and reading path.
- [write-domain-doc](skills/knowledge/write-domain-doc/SKILL.md) — Select and create any common domain document, including the README and fixed-structure essence article.
- [write-knowledge](skills/knowledge/write-knowledge/SKILL.md) — Create durable knowledge by reader use.
- [write-study-architecture](skills/knowledge/write-study-architecture/SKILL.md) — Build reusable architecture knowledge without making project commitments.

### Product

- [write-prd](skills/product/write-prd/SKILL.md) — Align product scope, behavior, and acceptance.

### Technical

- [write-delivery-architecture](skills/technical/write-delivery-architecture/SKILL.md) — Turn requirements into a project-specific architecture commitment.

### Visual

- [draw-diagrams](skills/visual/draw-diagrams/SKILL.md) — Select, create, and verify the smallest useful technical visual.

## Adding a skill

Add a deliverable skill only when an artifact has a distinct reader decision, stable structure, and completion test. Put shared writing or architecture method in the matching foundation instead of copying it.
