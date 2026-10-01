# [Runtime State and Messaging Architecture]

**Status:** [Draft / Reviewed / Superseded]

**Verified:** [Date and evidence baseline]

## Scope and guarantees

[State transport, durability, ordering, freshness and recovery questions]

## State taxonomy

| State type | Authority | Derived / durable | Lifetime | Rebuild source |
| --- | --- | --- | --- | --- |
| [State type] | [Authority] | [Derived / durable] | [Lifetime] | [Rebuild source] |

## Messaging model

[Figure: writers, durable facts, streams, consumers and projections]

| Pattern | Delivery semantics | Acknowledgement boundary | Failure behavior |
| --- | --- | --- | --- |
| [Pattern] | [Delivery semantics] | [Acknowledgement boundary] | [Failure behavior] |

## Ordering, partitioning and ownership

[Partition keys, sequencing, writers and ownership changes]

## Freshness and local snapshots

[Version, staleness, conflict and acceptance rules]

## Replay, rebuild and backfill

[Source, cursor, idempotency, compatibility and completion evidence]

## Failure and degradation

[Lost, repeated, delayed or unknown outcomes and bounded recovery]

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
