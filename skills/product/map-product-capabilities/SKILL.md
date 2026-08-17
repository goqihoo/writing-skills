---
name: map-product-capabilities
description: Create, revise, or review a product capability map that defines durable capabilities, relationships, responsibility and authority boundaries, reusable solution composition, gaps, and evolution triggers without becoming a feature, module, team, or roadmap map.
disable-model-invocation: true
---

# Map Product Capabilities

Connect product strategy to reusable product responsibilities without prescribing implementation or delivery order.

## Workflow

1. Apply `$Reason Product`.
2. Read the Product Assessment, product strategy, existing capabilities, reusable solutions, user journeys, product decisions, and authoritative business or domain constraints.
3. Require an accepted product boundary. Return `$Reason Product` when the boundary is missing or materially disputed.
4. Define capability as a durable ability the product must provide to achieve a user or product outcome. Reject features, pages, systems, teams, projects, and roadmap themes as capability candidates unless their underlying responsibility is stated.
5. Group capabilities by one stable product-responsibility dimension. Limit hierarchy depth to what current decisions and navigation require.
6. Record capability outcomes, relationships, owned responsibility, integrated responsibility, external authority, and boundary handoffs.
7. Show how reusable solutions compose capabilities without treating a solution or customer project as a capability.
8. Record current coverage, gaps, evidence, and evolution triggers. Keep construction order in the roadmap.
9. Use `assets/product-capability-map-template.md` as the structure owner. Preserve its H2 headings, order, and responsibilities.
10. When relationships need a visual and `$Draw Diagram` was explicitly included, define the capability meaning before drawing; otherwise retain the smallest useful table or prose model.
11. Verify that every capability expresses a product responsibility, every boundary has one authority, and no implementation or schedule has become the organizing model.

## Boundaries

- Own the whole-product capability model, not every capability detail; route an individual detail to `$Write Product Doc $Reason Product`.
- Let product strategy own why the product chooses the direction and the roadmap own when gaps are addressed.
- Keep application, system, component, data, and deployment structure in technical documentation.

## Completion

The work is complete when capabilities cover the accepted product outcome without mirroring features or systems, relationships and authority are explicit, solutions can compose the model, gaps and external dependencies are visible, and readers can map a new initiative to an existing capability or justify a new one.
