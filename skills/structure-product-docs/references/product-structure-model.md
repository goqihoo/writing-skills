# Product Documentation structure model

Product Documentation belongs to one named company. Its directory names use initial capitals because they represent company documentation responsibilities, not code-repository conventions.

## Company Product stable core

Create these Stable Responsibilities beneath `{Company}/Product/`:

- `Portfolio/` — product admission, product-line classification views, investment relationships, ownership, and lifecycle across the portfolio.
- `Governance/` — product decision rights, operating rules, shared standards, and exceptions.
- `Products/` — the registry and direct parent of accepted product directories.

Give `Product/` and every Stable Responsibility a Responsibility README. A product line is a classification view inside `Portfolio/`, not a default physical parent below `Products/`.

## Accepted-product stable core

Create `Products/{Product}/` only after the product is accepted. Give the product root and each Stable Responsibility a Responsibility README:

- `Definition/` — boundary, users, terminology, current definition, and related products.
- `Capabilities/` — durable product abilities and their relationships.
- `Planning/` — accepted strategy, roadmap, and change planning.
- `Measurement/` — metric semantics, outcomes, and measurement governance.

## Type Extensions

Create only when independent ownership, governance, or navigation is proven:

- `Solutions/` — reusable capability compositions for classes of scenarios.
- `Experience/` — product-wide experience responsibilities and cross-capability behavior.

## Event Collections

Create with the first real event document, not during a default scaffold:

- `Initiatives/` — accepted activities changing shared product behavior.
- `Evidence/` — research, feedback, experiments, or other product evidence.
- `Releases/` — release plans, release notes, and release reviews.
- `Decisions/` — product decisions needing independent lookup or review.

## Materialization rules

- **Stable Responsibility:** create by default for an accepted scope and add a Responsibility README.
- **Type Extension:** create only with evidence of independent ownership, governance, or navigation.
- **Event Collection:** create only with the first real event document.

A Responsibility README states responsibility, owner, boundary, real current navigation, and external authority links. It is not placeholder body text or a duplicate of an authoritative document.

## Company root and independent materialization

`Product/` and `Technical/` may be materialized independently under a shared company root. When both exist, `{Company}/README.md` links both. Never create a missing sibling root merely for symmetry.

## Migration contract

Before an approved migration, record exact old and new paths, affected links, moved assets, external bindings, supersession relationships, and approval. Verify that no old path, duplicate authority, broken link, or orphaned asset remains.
