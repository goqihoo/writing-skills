---
name: reason-architecture
description: Apply architecture reasoning to an explicit object and scope across relevant architecture domains, cross-cutting viewpoints, correctness checks, control traces, tradeoffs, and validation.
disable-model-invocation: true
---

# Reason Arch

Reason about architecture consistently without choosing a document shape or making an unowned project decision.

## Workflow

1. Read `../../methods/architecture-reasoning.md` completely.
2. Frame confirmed context, constraints, stakeholders, unknowns, and the change under consideration.
3. Select the Business, Data, Application, and Technology domains and the Security, Governance, and Runtime viewpoints that materially affect the reader decision. Run the six-step reasoning loop across that selection, then apply the four correctness checks.
4. Trace every material control across its owning domains and viewpoints. Treat stale, duplicate, partial, conflicting, and unknown outcomes explicitly.
5. Separate constraints, qualities, principles, patterns, decisions, and validation.
6. Read `../../methods/prose-quality.md`, then present the reasoning without imposing an unrelated artifact template or silently selecting a project-specific option. Read `../../methods/visual-production.md` when the user requests a visual or the architecture relationships are materially clearer as one.

## Completion

- The Architecture Object and Scope are explicit.
- Every authoritative fact and state has one owning authority.
- Domain invariants survive application, governance, technology, and runtime constraints.
- Cross-boundary contracts state failure and recovery behavior.
- Material controls identify authority, enforcement, evidence, and validation.
- Every accepted tradeoff names its cost and review trigger.
