---
name: write-solution-definition
description: Create, revise, or review a reusable product solution definition for one class of customer or partner scenario, covering roles, outcomes, end-to-end flow, capability composition, scenario rules, external authority, scope, success, and risks.
disable-model-invocation: true
---

# Write Solution Definition

Define how shared product capabilities solve a repeatable scenario without turning one customer delivery into a product.

## Workflow

1. Apply `$reason-product` and `$write-doc`.
2. Read the Product Assessment, product strategy, capability map, user and role model, available scenario evidence, existing solutions, and relevant product rules.
3. Require an accepted product boundary. For a missing, routed, or disputed Product Assessment, return `$reason-product $write-doc` and stop.
4. Confirm that the scenario is reusable across a class of customers, partners, or contexts. Route a single contract's scope and acceptance to its project location.
5. Separate shared product behavior, scenario-specific product behavior, customer-specific configuration, external authority, and unresolved delivery choices.
6. Define participants, problem and outcome, representative end-to-end scenario, capability composition, rules, interfaces visible at the product boundary, data meaning, and decision authority.
7. State scope, non-goals, variation points, success criteria, risks, evidence, and review triggers.
8. Use `assets/solution-definition-template.md` as the structure owner. Preserve its H2 headings, order, and responsibilities.
9. Link capability definitions and external project or technical owners rather than copying them.
10. Verify that the solution remains reusable, does not redefine the product, and gives a later PRD enough product context without committing technical design.

## Boundaries

- Own one reusable product solution for a class of scenarios.
- Keep customer-specific commercial scope, mappings, acceptance, and delivery choices in the project.
- Let `$map-product-capabilities` own the reusable capability model and `$write-prd` own one initiative's behavior and acceptance.
- Keep technical component, interface, data, and deployment design externally owned.

## Completion

The work is complete when the target scenario and reuse class are explicit, participants and authority are clear, the end-to-end outcome maps to existing or proposed capabilities, shared and scenario-specific behavior remain distinct, customer-specific work is excluded, and success, risks, variants, and unresolved decisions are visible.
