# Scribe

Scribe is a set of explicitly invoked skills for professional documents, Company Documentation, reusable Knowledge, and technical visuals. Start with `ask-scribe` when you want the current catalog and a complete invocation without executing another workflow.

## Documentation model

- **Knowledge** is reusable understanding not tied to one company. Domain, Product, Technical, and Architecture are possible Knowledge subjects.
- **Company Documentation** is owned and maintained by one named company. Scribe currently covers **Product Documentation** and **Technical Documentation**.
- **Project Documentation** belongs to one customer, contract, initiative, engagement, plan, or acceptance boundary. Its directory and artifact system is outside this release.

Company structures use **Stable Responsibility**, **Type Extension**, and **Event Collection** materialization rules. Lower-frequency standard documents remain an **Internal Document Type** within a Common Writer. **Explicit Skill Composition** means the user names every required skill; no Scribe skill invokes another skill.

Every human-readable artifact explicitly includes `write-doc`. Add `draw-diagrams` only when a visual is requested.

## Invocation

Use `$skill-name` in Agent Skills clients or `/skill-name` in Claude Code. Name every coordination, structure, artifact, writing, and optional visual skill required by the workflow.

## Installation

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

### Other Agent Skills clients

```bash
npx skills@latest add goqihoo/writing-skills
```

## Skills

### Entry and foundations

- [ask-scribe](skills/foundations/ask-scribe/SKILL.md) — Explain the catalog, boundaries, and complete invocations without executing them.
- [structure-docs](skills/foundations/structure-docs/SKILL.md) — Plan documentation placement, boundaries, navigation, and approved migrations.
- [write-doc](skills/foundations/write-doc/SKILL.md) — Apply the shared prose contract.
- [reason-architecture](skills/foundations/reason-architecture/SKILL.md) — Apply the shared four-view architecture method.
- [reason-domain](skills/foundations/reason-domain/SKILL.md) — Assess reusable Domain Knowledge boundaries.
- [reason-product](skills/foundations/reason-product/SKILL.md) — Assess company portfolios, product lines, products, and product responsibilities.
- [reason-technical](skills/foundations/reason-technical/SKILL.md) — Assess company technical scope, ownership, authority, and responsibilities.

### Knowledge

- [structure-domain-docs](skills/knowledge/structure-domain-docs/SKILL.md) — Structure an accepted Domain Knowledge set.
- [write-domain-doc](skills/knowledge/write-domain-doc/SKILL.md) — Write one common Domain Knowledge document.
- [write-knowledge](skills/knowledge/write-knowledge/SKILL.md) — Create durable reusable Knowledge.
- [write-architecture-knowledge](skills/knowledge/write-architecture-knowledge/SKILL.md) — Create reusable Architecture Knowledge without a company commitment.

### Product Documentation

- [assess-product-lifecycle](skills/product/assess-product-lifecycle/SKILL.md) — Assess a product decision, evidence, and artifact coverage.
- [structure-product-docs](skills/product/structure-product-docs/SKILL.md) — Propose, scaffold, audit, or migrate a company Product Documentation Set.
- [write-product-doc](skills/product/write-product-doc/SKILL.md) — Write one standard Product Internal Document Type.
- [write-product-strategy](skills/product/write-product-strategy/SKILL.md) — Define product direction and durable choices.
- [map-product-capabilities](skills/product/map-product-capabilities/SKILL.md) — Model durable product capabilities.
- [write-product-roadmap](skills/product/write-product-roadmap/SKILL.md) — Sequence outcomes and decisions.
- [write-prd](skills/product/write-prd/SKILL.md) — Define one product change's behavior and acceptance.
- [design-product-metrics](skills/product/design-product-metrics/SKILL.md) — Define outcome measures, semantics, and guardrails.

### Technical Documentation

- [structure-technical-docs](skills/technical/structure-technical-docs/SKILL.md) — Propose, scaffold, audit, or migrate a company Technical Documentation Set.
- [write-technical-doc](skills/technical/write-technical-doc/SKILL.md) — Write one standard Technical Internal Document Type.
- [write-technical-architecture](skills/technical/write-technical-architecture/SKILL.md) — Define company Technical Architecture across its Technical Landscape.

### Visual

- [draw-diagrams](skills/visual/draw-diagrams/SKILL.md) — Select, create, and verify the smallest useful technical visual.

## Architecture guides

- [Scribe Skill Architecture](docs/scribe-skill-architecture.md)
- [Domain Knowledge Skill Architecture](docs/domain-knowledge-skill-architecture.md)
- [Product Documentation Skill Architecture](docs/product-documentation-skill-architecture.md)
- [Technical Documentation Skill Architecture](docs/technical-documentation-skill-architecture.md)
