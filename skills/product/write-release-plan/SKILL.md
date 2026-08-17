---
name: write-release-plan
description: Create, revise, or review a product release plan covering intent, scope, availability, product readiness, stakeholder coordination, communication, support, product rollout decisions, success signals, stop conditions, risks, owners, and open decisions.
disable-model-invocation: true
---

# Write Release Plan

Make the product release decision reviewable without copying technical deployment and operations procedures.

## Workflow

1. Apply `$reason-product` and `$write-doc`.
2. Read the Product Assessment, approved PRDs, current product behavior, roadmap commitment, metric definitions, user and market constraints, support needs, linked delivery readiness, and prior release evidence.
3. Require an accepted product boundary. For a missing, routed, or disputed Product Assessment, return `$reason-product $write-doc` and stop.
4. Identify release intent, product scope, eligible users, markets, channels, timing constraints, decision-maker, and required coordination.
5. Separate product readiness, technical readiness, commercial readiness, support readiness, and external authority. Link externally owned readiness evidence.
6. Define product-facing rollout, availability, communication, migration, support, success and guardrail signals, stop conditions, and product rollback or withdrawal decisions.
7. Record dependencies, risks, owners, decision gates, unresolved questions, and the exact evidence required for Go, Hold, Recycle, or Stop.
8. Use `assets/release-plan-template.md` as the structure owner. Preserve its H2 headings, order, and responsibilities.
9. Verify that every material readiness claim has an owner and evidence, and that technical execution remains in its owning record.

## Boundaries

- Own product release intent, availability, coordination, communication, support, measurement, and product decision criteria.
- Let technical owners retain deployment, migration execution, rollback commands, monitoring configuration, and runbooks.
- Let release notes describe what actually became available and `$write-product-review` evaluate the result.

## Completion

The work is complete when release scope and eligibility are explicit, every readiness dimension has evidence and an owner, communication and support are actionable, success and stop conditions are observable, dependencies and open decisions are visible, and the release decision can be made without treating linked technical procedures as product-plan content.
