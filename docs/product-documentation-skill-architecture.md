# Product Documentation Skill Architecture

## Scope

Product Documentation is Company Documentation for how one company defines, organizes, governs, evolves, measures, and operates its commercial products. It is distinct from reusable Product Knowledge and from Project Documentation for customer or delivery work.

## Structure

The company Product Stable Responsibilities are:

```text
Product/
├── Portfolio/
├── Governance/
└── Products/
    └── {Product}/
        ├── Definition/
        ├── Capabilities/
        ├── Planning/
        └── Measurement/
```

Product lines are classification views inside Portfolio, not default parents of product directories. `Solutions/` and `Experience/` are Type Extensions. `Initiatives/`, `Evidence/`, `Releases/`, and `Decisions/` are Event Collections created with their first real entries.

## Public skills

| Skill | Ownership |
| --- | --- |
| **Reason Product** (`reason-product`) | Company portfolio, product line, product, responsibility admission, and Product Assessment decisions. |
| **Assess Product Lifecycle** (`assess-product-lifecycle`) | Product decision, evidence, and artifact coverage. |
| **Structure Product Docs** (`structure-product-docs`) | Product topology, materialization, navigation, scaffolding, audits, and approved migration. |
| **Write Product Doc** (`write-product-doc`) | Product Common Writer and its Internal Document Types. |
| **Write Product Strategy** (`write-product-strategy`) | Durable product direction and choices. |
| **Map Product Capabilities** (`map-product-capabilities`) | Product capability responsibilities and relationships. |
| **Write Product Roadmap** (`write-product-roadmap`) | Product outcome and decision sequence. |
| **Write PRD** (`write-prd`) | One product change's behavior and acceptance. |
| **Design Product Metrics** (`design-product-metrics`) | Metric semantics, hierarchy, guardrails, and governance. |

## Common Writer boundary

`write-product-doc` owns company navigation, Portfolio, Products Registry, Operating Model, Governance, product definition and reference documents, lifecycle maps, capability details, behavior, solutions, initiatives, evidence, decisions, release plans, release notes, and reviews. It routes Product Strategy, Capability Map, Product Roadmap, PRD, and Product Metric System to their Public Skills by returning a complete invocation and stopping.

## Lifecycle

Product Lifecycle is a governance view across existing authoritative documents, not another directory tree. Company Product scaffolding does not require a Product Lifecycle Assessment. Use the assessment when entering a specific product decision or evaluating its evidence and artifact coverage.

## Authority boundaries

Product Documentation links reusable Knowledge, Technical Documentation, Project Documentation, and Machine Authority. A Product Initiative changes shared product behavior; a delivery project coordinates customer, contract, plan, task, state, and acceptance.

## Explicit Skill Composition

Structure work explicitly includes `$Reason Product` and `$Structure Docs`; document work explicitly includes its artifact skill and `$Reason Product` when the artifact depends on an accepted product boundary. Add `$Write Doc` for a dedicated prose-quality pass or `$Draw Diagram` when the user requests one visual.

## Completion contract

The Product system is coherent when every accepted product appears directly below Products, Stable Responsibility homes exist, extensions and events are evidence-backed, each Internal Document Type has one completion profile, high-frequency artifacts retain public owners, and Product Knowledge is never presented as company commitment.
