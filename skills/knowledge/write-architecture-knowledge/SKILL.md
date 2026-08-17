---
name: write-architecture-knowledge
description: Create, revise, or review reusable Architecture Knowledge that is not tied to one company, system implementation, or project commitment.
disable-model-invocation: true
---

# Write Arch Knowledge

Build reusable Architecture Knowledge about boundaries, ownership, contracts, controls, failure, validation, alternatives, and evolution without making one company's implementation commitment.

## Workflow

1. Apply `$Reason Arch`.
2. Read `references/architecture-knowledge-method.md`, relevant sources, the target knowledge set, navigation, and representative sibling documents.
3. Establish the reader decision, applicability, evidence, concepts, constraints, and reusable architecture question.
4. Separate general facts, principles, options, inference, examples, company decisions, and project commitments.
5. Analyze only the Domain, Application, Governance, and Runtime views needed for the question.
6. Compare material options against common drivers. State fit, cost, failure behavior, validation, transition conditions, and limits.
7. Use `assets/architecture-knowledge-template.md`. Adapt its branches to the subject without turning an example into a universal prescription.
8. When `$Draw Diagram` was explicitly invoked by the user, provide the architecture meaning and let it own visual form. Otherwise retain sufficient prose or a table.
9. Update existing Knowledge navigation when the artifact is created or renamed.
10. Verify applicability, sources, authority, option tradeoffs, failure behavior, validation, and separation from company or project commitments.

## Boundaries

- Own reusable Architecture Knowledge not tied to one company.
- Let `$Write Tech Arch` own one company's Technical Architecture.
- Keep detailed System Architecture and project Technical Design in their downstream authority scopes.
- Link examples and executable facts rather than treating them as general authority.

## Completion

The work is complete when readers can apply the knowledge without mistaking it for a company commitment, each option states fit and cost, failure and validation are explicit, applicability is bounded, sources and examples are distinguishable, and navigation exposes the artifact.
