---
name: study-architecture
description: Create, revise, or review reusable architecture knowledge for a business, product, platform, or technical domain. Use for domain, application, subsystem, component, governance, runtime, control, engineering-strategy, system-mechanism, and reference-architecture documents that explain ownership, contracts, controls, failure, validation, options, and evolution without selecting one project's vendor, topology, schema, or implementation.
---

# Study Architecture

Build durable architecture knowledge that explains how to reason about a domain, not one project's final solution.

## Workflow

1. Apply `$write-docs` and `$reason-architecture`.
2. Read `references/document-types.md` and select exactly one primary document type by the question readers must answer.
3. Read `references/evolution-and-evidence.md` when comparing options, stages, sources, or validation. Read `references/transactional-patterns.md` only for distributed or transactional workflows.
4. Inspect the knowledge directory, its navigation, neighboring notes, sources, and existing conventions. Preserve healthy titles, links, structure, and tone.
5. Separate domain facts, invariants, constraints, principles, reusable options, architecture inference, project decisions, and examples. Cite externally verifiable claims; do not invent domain rules, scale, incidents, or implementation details.
6. Analyze only the views needed by the selected type. Keep Domain meaning, Application ownership, Governance authority, and Runtime operation in their owning views.
7. Compare options against common drivers. State fit, cost, failure behavior, validation, and transition triggers; do not present a later or more complex stage as automatically better.
8. Use `assets/architecture-knowledge-template.md` as the structure owner. Preserve its H2 heading names, order, and hierarchy. Within **Architecture model**, include only the Domain, Application, Governance, and Runtime H3 views required by the selected type, retain them in template order, and omit a view rather than renaming it. Fill the retained structure using the selected type's required questions; do not merge several primary types into one note.
9. For each visual candidate identified by `$write-docs`, define its architecture meaning first, then invoke `$draw-diagrams`; retain no visual when the routing result is prose or a table.
10. Update an existing README, MOC, or index when navigation changes. Verify links and the completion checks below.

## Boundaries

- Keep reusable facts, option families, principles, validation, and evolution here.
- Move selected project boundaries, contracts, controls, topology, rollout, and accepted costs to `$design-architecture`.
- Move general concepts and methods without architecture ownership or control concerns to `$write-knowledge`.

## Completion

- Each authoritative fact has one owner; controls do not become hidden business-state owners.
- Options state fit, costs, failure modes, validation, and selection conditions.
- Stable knowledge remains distinct from project choices and illustrative examples.
- The document retains the architecture-knowledge template's H2 structure and only its permitted H3 view branches.
- Readers can extract a delivery decision without treating the note as a ready-made project design.
