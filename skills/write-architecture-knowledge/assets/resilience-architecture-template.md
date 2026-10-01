# [Resilience Architecture]

**Status:** [Draft / Reviewed / Superseded]

**Verified:** [Date and evidence baseline]

## Scope and protected invariants

[Availability, recoverability, correctness and dependency assumptions]

## Lifecycle and admission

[Figure: startup, readiness, serving, degradation, drain and recovery]

## Failure and degradation model

| Failure | Blast radius | Admission / degradation | Invariant | Recovery owner |
| --- | --- | --- | --- | --- |
| [Failure] | [Blast radius] | [Admission / degradation] | [Invariant] | [Recovery owner] |

## Retry and unknown outcomes

[Retry boundaries, identity, pending outcomes and reconciliation]

## Recovery, replay and rebuild

[Authoritative sources, checkpoints, restore validation and resumption conditions]

## Failover and disaster recovery

[Ownership fencing, state loss limits, failover prerequisites and reversal]

## Patterns and tradeoffs

| Pattern / variant | Applies when | Benefit | Cost / failure limit | Review trigger |
| --- | --- | --- | --- | --- |
| [Pattern] | [Conditions] | [Benefit] | [Cost / limit] | [Trigger] |

## Validation and review triggers

| Judgment | Evidence or planned check | Pass / challenge signal | Evidence limits |
| --- | --- | --- | --- |
| [Judgment] | [Evidence or planned check] | [Pass / challenge signal] | [Evidence limits] |

## Project extraction

| Reusable conclusion | Applies when | Project must decide / verify | Unsuitable when |
| --- | --- | --- | --- |
| [Reusable conclusion] | [Applies when] | [Project must decide / verify] | [Unsuitable when] |

## Related documents

| Related document / source | Relationship | Link |
| --- | --- | --- |
| [Related document / source] | [Relationship] | [Link] |
