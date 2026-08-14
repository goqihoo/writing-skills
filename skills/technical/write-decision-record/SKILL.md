---
name: write-decision-record
description: Create, revise, or review a product or technical decision record, including architecture decision records. Use when one material choice needs durable context, real alternatives, rationale, costs, consequences, status, validation, and triggerable review conditions; use a technical-design skill when the whole solution is the subject.
---

# Write Decision Record

Preserve enough context for a future reader to understand one decision without reopening the original discussion.

## Workflow

1. Apply the `/writing-foundations` skill.
2. Confirm that the document owns one material decision. Split independent choices into separate records.
3. Reconstruct the decision-time context: goal, constraints, evidence available, and consequences of delaying or avoiding the decision.
4. State the decision directly. Record its status and decision date.
5. Include only alternatives that were genuinely available. Compare them against the same drivers and constraints.
6. Explain why the chosen option fits better. Record costs, risks, operational burden, organizational effects, and lost options.
7. Define how the decision will be validated and what observable event, threshold, or date should trigger review.
8. Adapt `assets/decision-record-template.md`. Preserve unknown history as unknown; do not invent retrospective rationale.

## Boundaries

- Use `/write-technical-design` when several choices must form an implementation-ready solution.
- Use `/write-knowledge-document` when comparing a reusable family of patterns across many contexts.
- Record the decision actually made, not the decision a later reader wishes had been made.

## Completion criteria

- The context explains the constraint or conflict that forced a choice.
- The decision is specific enough to change behavior or design.
- Alternatives are real and compared against the same criteria.
- The rationale connects evidence and constraints to the selected option.
- Costs and consequences are explicit.
- Validation and review conditions can be observed and acted upon.
