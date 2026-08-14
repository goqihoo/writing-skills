---
name: design-architecture
description: Create, revise, or review a project-specific software architecture commitment. Use for delivery architecture, solution architecture, system design, technical design, architecture proposals, arc42-style documents, and extraction from reusable architecture knowledge when stakeholders need aligned boundaries, ownership, contracts, controls, runtime behavior, rollout, and validation. Surface material unresolved decisions instead of silently choosing for the team.
---

# Design Architecture

Produce a concise architecture document that reviewers can challenge and implementers and operators can follow.

## Workflow

1. Apply `$write-docs` and `$reason-architecture`.
2. Read `references/delivery-guide.md`. Read `references/decision-questions.md` when missing facts or authority create a material fork.
3. Establish approved requirements, current behavior, constraints, ranked quality goals, operational conditions, reusable knowledge, and unresolved decisions.
4. Separate facts, external constraints, proposals, accepted decisions, assumptions, and open questions.
5. Walk one representative end-to-end scenario before decomposing the design. Then define boundaries, authoritative state, responsibilities, contracts, controls, runtime behavior, and recovery.
6. Compare material options against the same drivers. Ask the responsible stakeholder when the choice changes scope, ownership, contracts, controls, topology, cost, risk, or validation.
7. Cover security, observability, deployment, migration, compatibility, rollout, rollback, and testing in proportion to risk.
8. Use `assets/delivery-architecture-template.md` as the structure owner. Preserve its heading names, order, and hierarchy while replacing the title placeholder and filling each section. Keep a concise section and state why it is not applicable when no substantive content exists; do not delete, rename, reorder, or replace template sections.
9. For each visual candidate identified by `$write-docs`, define its architecture meaning first, then invoke `$draw-diagrams`; retain no visual when the routing result is prose or a table.
10. Verify the shared architecture completion checks and the delivery criteria below.

## Boundaries

- Product requirements define needed behavior; delivery architecture commits to how the project will provide it.
- A decision record owns one decision; delivery architecture combines related decisions into one solution.
- Invoke `$record-decision` when one accepted choice needs an independent lifecycle or review trigger.
- Reusable architecture knowledge retains options; this skill records what the project adopts, adapts, defers, or rejects.
- Stop before field-level schemas, class design, task plans, vendor configuration, and runbook procedures unless they change an architecture decision.

## Completion criteria

- Every major requirement maps to the design or an explicit non-goal.
- The main and failure paths are traceable through owners, contracts, state, controls, and recovery.
- Compatibility, rollout, rollback, operations, and validation are implementable.
- Accepted costs, risks, assumptions, and open decisions remain visible.
- The document retains the complete delivery-architecture template heading structure.
