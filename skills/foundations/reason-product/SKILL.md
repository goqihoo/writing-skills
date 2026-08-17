---
name: reason-product
description: Assess a candidate product boundary and record its users, outcomes, value, relationships, change and release authority, content ownership, lifecycle, and review triggers in a Product Assessment.
disable-model-invocation: true
---

# Reason About Products

Establish what the product is before a directory, roadmap, or PRD makes an accidental boundary look authoritative.

## Workflow

1. Apply `$write-doc` to the Product Assessment.
2. Read repository instructions, the product or project root README, existing product definitions, and representative adjacent products or initiatives. Preserve healthy local terms and ownership decisions.
3. Read `references/product-reasoning-method.md` completely.
4. Establish the candidate product, intended users, offered outcome, available evidence, current owner, and decision being requested. Separate facts, hypotheses, accepted decisions, proposals, and missing evidence.
5. Test the minimum user outcome, users and context, offered value and capability, change authority, release boundary, and sustained lifecycle. Return `Accept`, `Route as product area or capability`, `Route to another content class`, or `Needs evidence`.
6. Resolve relationships among product line, product, subproduct, product area, capability, solution, peer product, dependency, and handoff. Test every proposed child independently.
7. Assign each material one primary content class and owner. Keep reusable method knowledge, company strategy, customer projects, and technical implementation in their owning locations.
8. Record lifecycle, maturity, evidence gaps, authority conflicts, and events that require review.
9. Adapt `assets/product-assessment-template.md`. Keep unsupported conclusions visible as unresolved instead of inventing a coherent product.
10. Verify that the decision, boundary, relationships, ownership, and review triggers agree with the evidence.

## Boundaries

- Own product admission, identity, boundary, hierarchy, relationships, change and release authority, high-level knowledge ownership, and the Product Assessment handoff.
- Let `$assess-product-lifecycle` own decision readiness and artifact coverage.
- Let `$structure-product-docs` own directory topology, materialization, navigation, scaffolding, and migration.
- Let product artifact skills own their document bodies.
- Treat a feature, team, customer, project, software component, or named solution as a product only when it passes the product tests.

## Completion

The work is complete when one evidence-backed decision names the product boundary or correct route, every supported relationship and material has one primary owner, change and release authority are explicit, unresolved questions remain visible, and downstream skills can consume the Product Assessment without inferring a different product.
