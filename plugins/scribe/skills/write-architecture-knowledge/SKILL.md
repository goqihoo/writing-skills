---
name: write-architecture-knowledge
description: Create, revise, or review reusable Architecture Knowledge that is not tied to one company, system implementation, or project commitment.
---

# Write Arch Knowledge

Build reusable Architecture Knowledge about boundaries, ownership, contracts, controls, failure, validation, alternatives, and evolution without making one company's implementation commitment.

## Workflow

1. Read `../../methods/architecture-reasoning.md` and apply it inside this workflow.
2. Read `references/architecture-knowledge-method.md`, relevant sources, the target knowledge set, navigation, and representative sibling documents.
3. Establish the reader decision, applicability, evidence, Architecture Object or recurring problem, scope, concepts, constraints, and reusable architecture question.
4. Separate general facts, principles, options, inference, examples, company decisions, and project commitments.
5. Select only the Business, Data, Application, and Technology domains and the Security, Governance, and Runtime viewpoints that materially affect the question. Use the four correctness concerns as completion checks rather than output headings.
6. Compare material options against common drivers. State fit, cost, failure behavior, validation, transition conditions, and limits.
7. Use `assets/architecture-knowledge-template.md` adaptively. Preserve its content responsibilities while deriving subject-specific analysis headings; never materialize one heading per domain or viewpoint merely for coverage.
8. Read `../../methods/visual-production.md` when the request includes a visual or a central architecture relationship is materially clearer as one. Preserve architecture meaning while applying its visual form and quality rules.
9. Read `../../methods/prose-quality.md`, then update existing Knowledge navigation when the artifact is created or renamed.
10. Verify applicability, sources, authority, option tradeoffs, failure behavior, validation, and separation from company or project commitments.

## Boundaries

- Own reusable Architecture Knowledge not tied to one company.
- Let `$Write Tech Arch` own one company's Technical Architecture.
- Keep detailed System Architecture and project Technical Design in their downstream authority scopes.
- Link examples and executable facts rather than treating them as general authority.

## Completion

The work is complete when readers can apply the knowledge without mistaking it for a company commitment, the object or recurring problem and scope are explicit, relevant domains and viewpoints are accounted for, each option states fit and cost, failure and validation are explicit, sources and examples are distinguishable, and navigation exposes the artifact.
