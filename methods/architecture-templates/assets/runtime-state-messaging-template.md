# [Runtime State and Messaging Architecture]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## Scope and guarantees

[State transport, durability, ordering, freshness and recovery questions]

## State taxonomy

[Explain authoritative facts, durable records and derived state, their lifetimes and reconstruction sources. Show why the distinctions change transport and recovery guarantees.]

## Messaging model

[Explain how writers, durable facts, streams and consumers cooperate. Trace a message across the acknowledgement boundary and explain precisely what the acknowledgement establishes and what failure can still leave unknown.]

[Figure: writers, durable facts, streams, consumers and projections]

## Ordering, partitioning and ownership

[Partition keys, sequencing, writers and ownership changes]

## Freshness and local snapshots

[Version, staleness, conflict and acceptance rules]

## Replay, rebuild and backfill

[Source, cursor, idempotency, compatibility and completion evidence]

## Failure and degradation

[Walk a repeated, lost or delayed message through the ownership and recovery rules. Explain how the model bounds inconsistency or uncertainty and when replay or reconciliation restores the intended state.]

## Patterns and tradeoffs

[Explain the relevant alternatives under the same scenario and assumptions: how each mechanism works, what it gains, what it costs and where it fails. Use a compact comparison table only when several choices share meaningful criteria; state the conditional selection and review trigger in prose.]

## Validation and review triggers

[Explain what evidence supports or challenges the operating guarantees under the stated assumptions. Link the relevant scenario or experiment and its limitations. State which workload, dependency or design changes require the model to be reconsidered.]

## Application and adaptation

[Explain the assumptions that make the design valid, the changes that require adaptation and the consequences for dependent owners. Identify prerequisites, compatibility or transition limits, and evidence needed before relying on the changed model. Bound reusable claims with an unsuitable context where relevant.]

## Related documents

[Link parent, child, cross-view and source documents with a short explanation of what each contributes. Keep a shared mechanism in its owning document and point to it from dependents.]
