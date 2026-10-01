# [Resilience Architecture]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## Scope and protected invariants

[Availability, recoverability, correctness and dependency assumptions]

## Failure and degradation model

[Explain the relevant failures, blast radius and protected invariants. Trace a concrete failure through admission or degradation to the recovery owner and state why the response preserves the protected result.]

## Lifecycle and admission

[Figure: startup, readiness, serving, degradation, drain and recovery]

## Retry and unknown outcomes

[Retry boundaries, identity, pending outcomes and reconciliation]

## Recovery, replay and rebuild

[Authoritative sources, checkpoints, restore validation and resumption conditions]

## Failover and disaster recovery

[Ownership fencing, state loss limits, failover prerequisites and reversal]

## Patterns and tradeoffs

[Explain the relevant alternatives under the same scenario and assumptions: how each mechanism works, what it gains, what it costs and where it fails. Use a compact comparison table only when several choices share meaningful criteria; state the conditional selection and review trigger in prose.]

## Validation and review triggers

[Explain what evidence supports or challenges the operating guarantees under the stated assumptions. Link the relevant scenario or experiment and its limitations. State which workload, dependency or design changes require the model to be reconsidered.]

## Application and adaptation

[Explain the assumptions that make the design valid, the changes that require adaptation and the consequences for dependent owners. Identify prerequisites, compatibility or transition limits, and evidence needed before relying on the changed model. Bound reusable claims with an unsuitable context where relevant.]

## Related documents

[Link parent, child, cross-view and source documents with a short explanation of what each contributes. Keep a shared mechanism in its owning document and point to it from dependents.]
