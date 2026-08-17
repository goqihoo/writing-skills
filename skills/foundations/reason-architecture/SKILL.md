---
name: reason-architecture
description: Apply the shared architecture reasoning method for domain facts, application ownership and contracts, governance authority and evidence, runtime failure and recovery, control traces, tradeoffs, and validation. Use with write-architecture-knowledge and write-technical-architecture.
disable-model-invocation: true
---

# Reason About Architecture

Reason about architecture consistently without choosing a document shape or making an unowned project decision.

## Workflow

1. Read `references/architecture-method.md` completely.
2. Frame confirmed context, constraints, stakeholders, unknowns, and the change under consideration.
3. Run the six-step reasoning loop across the four views. Revisit an earlier judgment only when new evidence invalidates it.
4. Trace every material control across views. Treat stale, duplicate, partial, conflicting, and unknown outcomes explicitly.
5. Separate constraints, qualities, principles, patterns, decisions, and validation.
6. Return the reasoning to the owning deliverable skill. Do not impose an output template or silently select a project-specific option.

## Completion

- Every authoritative fact has one application owner.
- Domain invariants survive governance and runtime constraints.
- Cross-boundary contracts state failure and recovery behavior.
- Material controls identify authority, enforcement, evidence, and validation.
- Every accepted tradeoff names its cost and review trigger.
