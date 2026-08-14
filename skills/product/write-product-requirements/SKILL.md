---
name: write-product-requirements
description: Create, revise, or review a product requirements document for a feature or product change. Use when stakeholders must align on the user problem, outcome, scope, observable behavior, business rules, edge states, measurement, and acceptance; use design-delivery-architecture when solution structure is the main subject.
---

# Write Product Requirements

Produce a PRD that lets product, design, engineering, and business stakeholders agree on the product behavior and verify the outcome.

## Workflow

1. Apply `$writing-docs`.
2. Establish the available inputs: problem evidence, affected users, desired outcome, business constraints, existing behavior, and known decisions.
3. Distinguish established facts from hypotheses. Preserve unresolved product decisions as open questions instead of inventing agreement.
4. Define the problem and measurable outcome before listing features.
5. Set scope and non-goals. Make each requirement traceable to the problem, target outcome, or binding constraint.
6. Describe representative user scenarios from trigger to observable result. Cover empty, failure, permission, cancellation, retry, and boundary states when they matter.
7. Write requirements as observable behavior. Add acceptance criteria that another person can verify.
8. Record business rules, data meaning, dependencies, risks, rollout, measurement, and remaining decisions.
9. Adapt `assets/prd-template.md`; remove sections that carry no decision or delivery value.

## Boundaries

- Keep product intent, behavior, and acceptance in the PRD.
- Move component structure, storage choices, protocols, topology, and implementation algorithms to `$design-delivery-architecture` unless a technical constraint changes product scope.
- Use `$write-decision-record` when one decision needs its own durable rationale and review trigger.

## Completion criteria

- The problem is supported by evidence or explicitly marked as a hypothesis.
- The intended outcome and success measures are observable.
- Scope, non-goals, users, scenarios, and requirements agree with one another.
- Every material requirement has a rationale or traceable source and a verifiable acceptance condition.
- Business rules and edge states do not depend on unstated interpretation.
- Dependencies, risks, rollout, measurement, and open decisions are visible.
- The PRD leaves implementation freedom where no product constraint requires a choice.
