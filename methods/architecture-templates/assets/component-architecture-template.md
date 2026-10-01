# [Component Architecture]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## Responsibility and boundary

[Explain the component responsibility, exclusions, callers and dependencies. State the inherited constraints and invariants that shape its mechanism, including relevant concurrency or resource assumptions.]

## Inputs, outputs and contracts

[Explain input and output meaning, direction, preconditions, guarantees and failure or compatibility semantics. Show what callers can infer from an outcome and what remains unknown.]

## Internal ownership model

[Explain how internal elements, state ownership and dependency boundaries realize the contract and why this decomposition is useful. Identify the source from which owned or derived state can be rebuilt.]

[Figure: modules, owned state and dependencies]

## Algorithm and concurrency model

[Explain the algorithm or protocol, input assumptions, atomic changes, ordering and concurrency where relevant. Show why the mechanism delivers the contract and how dependency failures or alternate implementations change its guarantees.]

## Lifecycle

[Explain meaningful lifecycle transitions, their preconditions, effects and completion conditions. Distinguish object-state transitions from process readiness when both matter.]

[Figure: lifecycle transitions]

## Core behavior

[Exercise the algorithm and lifecycle with a concrete input and observable result. Refer to their rules and show why the invariant holds at significant steps; merge this section with the mechanism when a separate example would repeat the same explanation.]

## Governed behavior

[Protected actions, enforcement points, authority and evidence]

## Failure and recovery

[Trace a relevant failure through containment, retry or replay and recovery. Explain duplicate or unknown outcomes where applicable and the evidence needed before normal behavior resumes.]

## Design variants

[Explain how an alternative component mechanism changes its contract, performance or recovery behavior under the same conditions. State its costs and substitution limits; use comparison only where it aids selection.]

## Validation

[Explain how the principal claims could be established or challenged. Connect a concrete example, experiment, review or operational observation to the claim it tests, the expected signal and the limits of the evidence. Distinguish illustrative reasoning, sourced observations and proposed checks.]

## Extension and replacement

[Extension points, compatibility, substitutability, replacement conditions]

## Application and adaptation

[Explain the assumptions that make the design valid, the changes that require adaptation and the consequences for dependent owners. Identify prerequisites, compatibility or transition limits, and evidence needed before relying on the changed model. Bound reusable claims with an unsuitable context where relevant.]

## Related documents

[Link parent, child, cross-view and source documents with a short explanation of what each contributes. Keep a shared mechanism in its owning document and point to it from dependents.]
