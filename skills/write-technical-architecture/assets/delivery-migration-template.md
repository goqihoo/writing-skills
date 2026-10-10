# [Delivery Architecture Migration]

**Status:** [Draft / In review / Accepted / Superseded]

**Owner / decision authority:** [Known roles]

**Baseline:** [Date / version]

**Design state:** [Current / Target / Mixed]

## Baseline, target and transition obligations

[Explain why the baseline must change, target boundaries and exclusions; link the owning designs. State behavior and data invariants that must hold throughout the transition, downtime and loss constraints, dependencies and unresolved assumptions.]

## Coexistence and transition strategy

[Explain how old and new versions coexist, who owns reads and writes at each transition, and why the selected sequencing preserves the obligations.]

[Figure: transition states, coexistence boundaries and points of no return]

## State transfer and compatibility

[Explain schema or contract compatibility, data movement, reconciliation and how completeness and correctness will be established. Identify authoritative state during coexistence and the risk of divergent writers.]

## Transition consistency and reconciliation

[Specify which version owns writes and serves reads during each coexistence state, how changes are transferred, how conflicts or missing records are detected and how reconciliation establishes completion. Identify the exact boundary after which rollback cannot preserve new state.]

## Migration stages

[Explain the dependency order and why each stage is safe to enter and leave. Use the stage record for execution gates; link procedures separately.]

| Stage | Entry condition | Architecture change | Exit evidence | Owner |
| --- | --- | --- | --- | --- |
| [Stage reference] | [Prerequisite] | [Boundary or ownership change] | [Evidence reference] | [Role] |

## Cutover, rollback and forward recovery

[Identify the cutover authority, trigger, health gates and state-preservation checks. State the last safe rollback point. After irreversible writes or incompatible changes, explain forward recovery and reconciliation instead of promising an impossible reversal.]

## Acceptance and residual risks

[Trace transition obligations and stage gates to evidence and acceptance decisions. Explain gaps, owners and resolution conditions; distinguish a proposed migration from a completed one. State when temporary compatibility paths can be retired.]

## Sources and related documents

[Link governing requirements, architecture and evidence at their relevant claims. List remaining sources with their version and relationship to this design.]
