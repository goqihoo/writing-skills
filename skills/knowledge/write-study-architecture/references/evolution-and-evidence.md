# Architecture evolution and evidence

## Compare options

Evaluate every option on the same fields:

- context, stage, prerequisites, and constraints;
- ownership, consistency, control, and failure behavior;
- operational complexity, strengths, accepted costs, and common failures;
- validation and signals that make the option stop fitting.

Tie each tradeoff to a driver or scenario. Keep project choices open when fit depends on concrete scale, team, platform, cost, or regulation.

## Describe evolution

Use stages only when architecture pressure changes.

| Field | Required content |
|---|---|
| Context | Scale, risk, product scope, regulation, team, and platform maturity |
| Shape | Boundaries, ownership, contracts, controls, and runtime model |
| Fit | Drivers satisfied with acceptable complexity |
| Limits | Failure modes, bottlenecks, and unsafe assumptions |
| Trigger | Observable condition that justifies change |
| Migration | Compatibility, state transfer, replay, dual running, evidence, and rollback |

A simpler architecture may remain the correct endpoint.

## Use evidence

- Prefer primary and authoritative sources for rules, standards, regulation, and technical guarantees.
- Use incidents to prove a failure mode, then extract the reusable lesson instead of retelling the incident.
- Keep source-supported facts separate from architecture inference and examples.
- Tie validation to a named judgment: lifecycle and invariant review for Domain; ownership, contract, replay, and convergence tests for Application; bypass and evidence review for Governance; load, failure, restore, and recovery tests for Runtime.
