# Scribe

Composable agent skills for professional documents, documentation structure, and technical visuals. Start with `ask-scribe` when you want to understand the available skills or plan how to combine them.

Every human-readable artifact uses the shared `write-doc` prose contract. Artifact skills keep their own structure and technical responsibilities while inheriting the same reader-first standard for concrete language, natural sentence flow, proportionate emphasis, and clean formatting.

## Invocation

Every Scribe skill requires explicit invocation. Use `$skill-name` in Agent Skills-compatible clients or `/skill-name` in Claude Code. Name every foundation and artifact skill required by a composed workflow.

Start with `$ask-scribe` or `/ask-scribe` when you want Scribe to explain the available skills and return a complete invocation or sequence without executing it.

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

- [ask-scribe](skills/foundations/ask-scribe/SKILL.md) — Explain Scribe's skills, boundaries, and useful combinations without executing them.
- [structure-docs](skills/foundations/structure-docs/SKILL.md) — Plan directory boundaries, file placement, and documentation structure.
- [write-doc](skills/foundations/write-doc/SKILL.md) — Apply the shared method for one clear, grounded document.
- [reason-architecture](skills/foundations/reason-architecture/SKILL.md) — Reason about architecture across four views.
- [reason-domain](skills/foundations/reason-domain/SKILL.md) — Assess domain admission, boundaries, relationships, knowledge ownership, and maturity.
- [reason-product](skills/foundations/reason-product/SKILL.md) — Assess product admission, boundaries, hierarchy, authority, ownership, and lifecycle.

### Knowledge

- [structure-domain-docs](skills/knowledge/structure-domain-docs/SKILL.md) — Turn an accepted domain assessment into a directory, coverage map, reading path, scaffold, or migration.
- [write-domain-doc](skills/knowledge/write-domain-doc/SKILL.md) — Select and create one common document inside an accepted domain knowledge set.
- [write-knowledge](skills/knowledge/write-knowledge/SKILL.md) — Create durable knowledge by reader use.
- [write-study-architecture](skills/knowledge/write-study-architecture/SKILL.md) — Build reusable architecture knowledge without making project commitments.

### Product

- [assess-product-lifecycle](skills/product/assess-product-lifecycle/SKILL.md) — Assess product decision readiness, evidence, and artifact coverage.
- [structure-product-docs](skills/product/structure-product-docs/SKILL.md) — Plan, scaffold, audit, or migrate a product knowledge set.
- [write-product-doc](skills/product/write-product-doc/SKILL.md) — Create one common map, reference, behavior, evidence, decision, or release-notes document.
- [write-product-strategy](skills/product/write-product-strategy/SKILL.md) — Define product direction, choices, non-goals, and review triggers.
- [map-product-capabilities](skills/product/map-product-capabilities/SKILL.md) — Model durable product capabilities and responsibility boundaries.
- [write-solution-definition](skills/product/write-solution-definition/SKILL.md) — Define a reusable solution for a class of product scenarios.
- [write-product-roadmap](skills/product/write-product-roadmap/SKILL.md) — Sequence outcomes, bets, dependencies, and decision gates.
- [write-prd](skills/product/write-prd/SKILL.md) — Align one product change's scope, behavior, and acceptance.
- [design-product-metrics](skills/product/design-product-metrics/SKILL.md) — Define product outcome measures, metric semantics, and guardrails.
- [write-release-plan](skills/product/write-release-plan/SKILL.md) — Plan product release readiness, coordination, and decision criteria.
- [write-product-review](skills/product/write-product-review/SKILL.md) — Review evidence, outcomes, and next product decisions.

### Technical

- [write-delivery-architecture](skills/technical/write-delivery-architecture/SKILL.md) — Turn requirements into a project-specific architecture commitment.

### Visual

- [draw-diagrams](skills/visual/draw-diagrams/SKILL.md) — Select, create, and verify the smallest useful technical visual.

## Adding a skill

Add a deliverable skill only when an artifact has a distinct reader decision, stable structure, and completion test. Put shared writing or architecture method in the matching foundation instead of copying it.

The accepted designs are recorded in [Domain Knowledge Skill Architecture](docs/domain-knowledge-skill-architecture.md) and [Product Knowledge Skill Architecture](docs/product-knowledge-skill-architecture.md).
