---
name: reason-architecture
description: Apply architecture reasoning to domain facts, application ownership and contracts, governance authority and evidence, runtime failure and recovery, control traces, tradeoffs, and validation.
---

# Reason Arch

Reason about architecture consistently without choosing a document shape or making an unowned project decision.

## Workflow

1. Read `../../methods/architecture-reasoning.md` completely.
2. Frame confirmed context, constraints, stakeholders, unknowns, and the change under consideration.
3. Run the six-step reasoning loop across the four views. Revisit an earlier judgment only when new evidence invalidates it.
4. Trace every material control across views. Treat stale, duplicate, partial, conflicting, and unknown outcomes explicitly.
5. Separate constraints, qualities, principles, patterns, decisions, and validation.
6. Read `../../methods/prose-quality.md`, then present the reasoning without imposing an unrelated artifact template or silently selecting a project-specific option. Read `../../methods/visual-production.md` when the user requests a visual or the architecture relationships are materially clearer as one.

## Completion

- Every authoritative fact has one application owner.
- Domain invariants survive governance and runtime constraints.
- Cross-boundary contracts state failure and recovery behavior.
- Material controls identify authority, enforcement, evidence, and validation.
- Every accepted tradeoff names its cost and review trigger.
