# Scribe

Scribe is a set of explicitly invoked skills for professional documents, presentation manuscripts, Company Documentation, reusable Knowledge, and technical visuals. Start with **Ask Scribe** (`ask-scribe`) when you want the current catalog and a complete invocation without executing another workflow.

## Documentation model

- **Knowledge** is reusable understanding not tied to one company. Domain, Product, Technical, and Architecture are possible Knowledge subjects.
- **Company Documentation** is owned and maintained by one named company. Scribe currently covers **Product Documentation** and **Technical Documentation**.
- **Project Documentation** belongs to one customer, contract, initiative, engagement, plan, or acceptance boundary. Its directory and artifact system is outside this release.

Company structures use **Stable Responsibility**, **Type Extension**, and **Event Collection** materialization rules. Repeated or audit-sensitive writer artifacts are registered as **Internal Document Types**; compatible occasional work remains a **Freeform Artifact**. The generated [Internal Document Type catalog](docs/internal-document-types.md) describes the current Product and Technical registries. Each Public Skill delivers one end-to-end result and applies cross-skill **Shared Methods** internally.

Use **Write Doc** (`write-doc`) for a general linear document or when prose improvement is itself the requested result. Use **Write Deck** (`write-deck`) for an audience-facing presentation manuscript in Markdown. Use **Draw Diagram** (`draw-diagram`) when one visual is itself the requested result. Other skills already apply prose quality and visual production when their own result needs them.

## Invocation

Every skill accepts its exact Skill Display Name and canonical Skill ID. Prefer the display name in user-facing calls: use `$Ask Scribe` or `$ask-scribe` in Agent Skills clients, and `/Ask Scribe` or `/ask-scribe` in Claude Code. Skill IDs remain stable in paths, manifests, and code. Invoke one skill for one result; naming multiple skills requests multiple independent results.

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
git clone https://github.com/goqihoo/writing-skills.git
bash writing-skills/scripts/link-skills.sh "$HOME/.agents/skills"
```

The link script installs the 24 Public Skills and their non-invocable Shared Methods together.

## Repository layout

All Public Skills use the standard flat `skills/<skill-id>/SKILL.md` layout. Foundations, Knowledge, Product Documentation, Technical Documentation, and Visual are catalog classifications rather than intermediate directories. Internal cross-skill rules live under `methods/`; the generated Codex package under `plugins/scribe/` adapts only platform-specific invocation metadata.

## Skills

### Entry and foundations

- [Ask Scribe](skills/ask-scribe/SKILL.md) (`ask-scribe`) — Explain the catalog, boundaries, and complete invocations without executing them.
- [Structure Docs](skills/structure-docs/SKILL.md) (`structure-docs`) — Plan documentation placement, boundaries, navigation, and approved migrations.
- [Write Doc](skills/write-doc/SKILL.md) (`write-doc`) — Apply an optional reader-flow and prose-quality workflow.
- [Write Deck](skills/write-deck/SKILL.md) (`write-deck`) — Create or revise an audience-facing presentation manuscript in Markdown.
- [Reason Arch](skills/reason-architecture/SKILL.md) (`reason-architecture`) — Apply the shared four-view architecture method.
- [Reason Domain](skills/reason-domain/SKILL.md) (`reason-domain`) — Assess reusable Domain Knowledge boundaries.
- [Reason Product](skills/reason-product/SKILL.md) (`reason-product`) — Assess company portfolios, product lines, products, and product responsibilities.
- [Reason Tech Docs](skills/reason-technical/SKILL.md) (`reason-technical`) — Assess company technical scope, ownership, authority, and responsibilities.

### Knowledge

- [Structure Domain Docs](skills/structure-domain-docs/SKILL.md) (`structure-domain-docs`) — Structure an accepted Domain Knowledge set.
- [Write Domain Doc](skills/write-domain-doc/SKILL.md) (`write-domain-doc`) — Write one common Domain Knowledge document.
- [Write Knowledge](skills/write-knowledge/SKILL.md) (`write-knowledge`) — Create durable reusable Knowledge.
- [Write Arch Knowledge](skills/write-architecture-knowledge/SKILL.md) (`write-architecture-knowledge`) — Create reusable Architecture Knowledge without a company commitment.

### Product Documentation

- [Assess Product Lifecycle](skills/assess-product-lifecycle/SKILL.md) (`assess-product-lifecycle`) — Assess a product decision, evidence, and artifact coverage.
- [Structure Product Docs](skills/structure-product-docs/SKILL.md) (`structure-product-docs`) — Propose, scaffold, audit, or migrate a company Product Documentation Set.
- [Write Product Doc](skills/write-product-doc/SKILL.md) (`write-product-doc`) — Write one registered or occasional Product artifact.
- [Write Product Strategy](skills/write-product-strategy/SKILL.md) (`write-product-strategy`) — Define product direction and durable choices.
- [Map Product Capabilities](skills/map-product-capabilities/SKILL.md) (`map-product-capabilities`) — Model durable product capabilities.
- [Write Product Roadmap](skills/write-product-roadmap/SKILL.md) (`write-product-roadmap`) — Sequence outcomes and decisions.
- [Write PRD](skills/write-prd/SKILL.md) (`write-prd`) — Define one product change's behavior and acceptance.
- [Design Product Metrics](skills/design-product-metrics/SKILL.md) (`design-product-metrics`) — Define outcome measures, semantics, and guardrails.

### Technical Documentation

- [Structure Tech Docs](skills/structure-technical-docs/SKILL.md) (`structure-technical-docs`) — Propose, scaffold, audit, or migrate a company Technical Documentation Set.
- [Write Tech Doc](skills/write-technical-doc/SKILL.md) (`write-technical-doc`) — Write one registered or occasional Technical artifact, including System or Subsystem Architecture.
- [Write Tech Arch](skills/write-technical-architecture/SKILL.md) (`write-technical-architecture`) — Define company-level Technical Architecture, Product-System mapping, or a cross-System topic.

### Visual

- [Draw Diagram](skills/draw-diagram/SKILL.md) (`draw-diagram`) — Select, create, and verify one of 39 Diagram Design diagram or chart types with the Scribe Plotly theme.

## Architecture guides

- [Scribe Skill Architecture](docs/scribe-skill-architecture.md)
- [Domain Knowledge Skill Architecture](docs/domain-knowledge-skill-architecture.md)
- [Product Documentation Skill Architecture](docs/product-documentation-skill-architecture.md)
- [Technical Documentation Skill Architecture](docs/technical-documentation-skill-architecture.md)
- [Scribe 0.7.0 migration notes](docs/releases/0.7.0.md)
- [Scribe 0.7.1 packaging notes](docs/releases/0.7.1.md)
- [Scribe 0.8.0 architecture and document-type notes](docs/releases/0.8.0.md)
- [Scribe 0.9.0 presentation-manuscript notes](docs/releases/0.9.0.md)
