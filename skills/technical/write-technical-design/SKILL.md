---
name: write-technical-design
description: Create, revise, or review an implementation-ready technical design or system design document. Use when agreed requirements must become a coherent solution across architecture, runtime flows, interfaces, data, failure handling, security, observability, rollout, and validation; use a decision-record skill when one decision is the whole subject.
---

# Write Technical Design

Produce a design that reviewers can challenge and implementers can follow without guessing about system behavior.

## Workflow

1. Apply the `/writing-foundations` skill.
2. Establish inputs: approved requirements, current system behavior, architecture constraints, quality goals, operational constraints, and unresolved decisions.
3. Separate current facts, proposed changes, accepted decisions, assumptions, and open questions.
4. Walk through one representative end-to-end scenario before decomposing the solution into components or layers.
5. Explain the proposed structure, responsibilities, interfaces, data ownership, state changes, and runtime interactions.
6. Trace failure, timeout, retry, partial success, concurrency, recovery, and degraded-operation paths where relevant.
7. Cover security, privacy, observability, deployment, migration, compatibility, testing, and rollback in proportion to risk.
8. Connect material choices to drivers and alternatives. Create a separate decision record when one choice needs independent lifecycle or review conditions.
9. Adapt `assets/technical-design-template.md`. Remove irrelevant sections and add domain-specific views only when they answer a review or implementation question.

## Boundaries

- A product requirements document defines needed behavior and acceptance. A technical design defines how the system will provide it.
- A decision record preserves one decision. A technical design combines many decisions into a working solution.
- A reusable mechanism explanation belongs in `/write-knowledge-document`; keep project constraints and implementation choices here.

## Completion criteria

- Every major requirement maps to a part of the proposed design or an explicit non-goal.
- A reader can trace the main scenario through components, interfaces, data, and state changes.
- Responsibilities and ownership have no silent gaps or unexplained overlap.
- Failure and recovery behavior is as explicit as the success path.
- Interfaces, data semantics, compatibility, rollout, rollback, and validation are implementable and testable.
- Risks, rejected alternatives, assumptions, and open questions remain visible.
