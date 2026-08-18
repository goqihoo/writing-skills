---
name: assess-product-lifecycle
description: Assess a product's next decision, evidence sufficiency, authoritative artifact coverage, and readiness without treating lifecycle stages as directories or creating another skill's artifact.
disable-model-invocation: true
---

# Assess Product Lifecycle

Turn lifecycle activity into an explicit decision-readiness view over one accepted product.

## Workflow

1. Read `../../methods/product-reasoning.md` and apply it inside this workflow.
2. Read repository instructions, the Product Assessment when persisted, product README, lifecycle map, current strategy, capability map, roadmap, active initiatives, evidence, metrics, and recent releases when present.
3. Establish an accepted product boundary from the available evidence. If the boundary remains missing, stale, or disputed, stop because the assessment would lack a valid subject; name the evidence or decision required without demanding another skill.
4. Read `references/product-lifecycle-model.md` completely.
5. Identify the decision being prepared rather than assigning a stage from document names. Record the responsible decision-maker, cost of acting, cost of delay, and uncertainty that must be reduced.
6. Inventory the evidence and authoritative artifacts required for that decision. Distinguish absence, insufficiency, staleness, ownership conflict, and an artifact that is not yet applicable.
7. Assign the structure state, artifact acceptance and currency states, and decision-gate state independently. Do not use one completion mark for all three state groups.
8. Right-size the required artifacts to the decision and risk. Keep a missing decision visible instead of requiring every lifecycle template.
9. Read `../../methods/prose-quality.md`, then adapt `assets/product-lifecycle-assessment-template.md`. For each missing artifact, name its owning Public Skill as a possible next result without treating it as a dependency of this assessment.
10. Read `../../methods/visual-production.md` when the request includes a visual or the lifecycle states and gates are materially clearer as one.
11. Verify that every readiness conclusion points to evidence, an authoritative artifact, or a named gap.

## Boundaries

- Own the Product Lifecycle Assessment, decision-gate matrix, evidence sufficiency, artifact coverage, and single-skill next-result invocations.
- Treat stages as a navigation and governance view, not a product directory topology.
- Let `$Structure Product Docs` own paths, scaffolding, and migration.
- Let Product artifact skills own strategy, capabilities, roadmap, PRD, and metrics; let `$Write Product Doc` own Product Release Plan and Product Review as registered Internal Document Types and compatible Product Solution work as a Freeform Artifact.
- Route technical readiness to the owning technical location without modeling its internal structure.

## Completion

The work is complete when one current decision and decision-maker are explicit, every required artifact has an authoritative link or named gap, all three state groups and their fields are assigned independently, evidence insufficiency is distinguishable from missing files, and each blocked next step has a complete explicit invocation without another skill having been executed.
