---
name: write-prd
description: Create, revise, or review a product requirements document for one product change, covering the user problem, outcome, scope, observable behavior, business rules, edge states, measurement, and acceptance.
disable-model-invocation: true
---

# Write Product Requirements

Produce a PRD that lets product, design, engineering, and business stakeholders agree on the product behavior and verify the outcome.

## Workflow

1. Establish the available inputs: problem evidence, affected users, desired outcome, business constraints, existing behavior, and known decisions.
2. Distinguish established facts from hypotheses. Preserve unresolved product decisions as open questions instead of inventing agreement.
3. Define the problem and measurable outcome before listing features.
4. Set scope and non-goals. Make each requirement traceable to the problem, target outcome, or binding constraint.
5. Describe representative user scenarios from trigger to observable result. Cover empty, failure, permission, cancellation, retry, and boundary states when they matter.
6. Write requirements as observable behavior. Add acceptance criteria that another person can verify.
7. Record business rules, data meaning, dependencies, risks, rollout, measurement, and remaining decisions.
8. Adapt `assets/prd-template.md`; remove sections that carry no decision or delivery value.

## Boundaries

- Keep product intent, behavior, and acceptance in the PRD.
- Move component structure, storage choices, protocols, topology, and implementation algorithms to their downstream Technical or System Architecture authority unless a technical constraint changes product scope.
- Keep unresolved product decisions in **Open decisions** and link accepted architecture decisions from their owning authority.

## Completion criteria

- The problem is supported by evidence or explicitly marked as a hypothesis.
- The intended outcome and success measures are observable.
- Scope, non-goals, users, scenarios, and requirements agree with one another.
- Every material requirement has a rationale or traceable source and a verifiable acceptance condition.
- Business rules and edge states do not depend on unstated interpretation.
- Dependencies, risks, rollout, measurement, and open decisions are visible.
- The PRD leaves implementation freedom where no product constraint requires a choice.
