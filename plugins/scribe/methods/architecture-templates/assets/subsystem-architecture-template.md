# [Subsystem Architecture]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## Responsibility and scope

[Owns, does not own, parent architecture, intended result]

## Drivers and architecture characteristics

[Explain inherited guarantees and local design pressures, their priority and the conditions under which they matter. Use a representative caller scenario to show what the subsystem must accomplish; keep local choices distinct from the parent model.]

## Boundary and contracts

[Explain the upstream and downstream relationships, what callers may rely on and what the subsystem assumes of dependencies. State externally visible guarantees and failure semantics before describing the internals.]

[Figure: subsystem context]

## State

[Explain authoritative and derived state, lifecycle and consistency boundaries. Show why these ownership choices are needed to uphold the external contracts and how state can be reconstructed.]

## Components

[Explain how internal components divide the work and collectively realize the external contracts. Name responsibility and state owners, give the boundary rationale and link detailed component mechanisms.]

[Figure: internal components and ownership]

## Contract realization and consistency mechanisms

[Explain how internal commands, entity relationships, transaction boundaries and asynchronous coordination realize the external guarantees. Work through the selected mechanism and a condition that breaks it, distinguishing invariant requirements from replaceable implementation choices.]

## Core flows

[Follow an external request or change through the internal components, state transitions and result. Explain how their collaboration delivers the guarantee stated at the boundary.]

[Figure: core interaction]

## Failure and recovery

[Use a consequential failed or unknown outcome to explain detection, containment, safe behavior and recovery. Identify the recovering owner and source of truth, then show which external guarantee remains valid or is temporarily weakened.]

## Decisions and rules

[Explain why the subsystem model assigns these contracts and owners, which rules preserve its guarantees and how alternative decompositions change the result. State the conditions that would justify a different design.]

## Cross-view relationships

[Governance controls enforced here and runtime assumptions; links to their full treatments]

## Validation

[Explain how the principal claims could be established or challenged. Connect a concrete example, experiment, review or operational observation to the claim it tests, the expected signal and the limits of the evidence. Distinguish illustrative reasoning, sourced observations and proposed checks.]

## Evolution and adaptation

[Explain which changes preserve the model and which invalidate its boundaries or guarantees. Explain compatibility, transition constraints and the choices or evidence needed for the changed design. Bound reusable claims with an unsuitable context where relevant.]

## Related documents

[Link parent, child, cross-view and source documents with a short explanation of what each contributes. Keep a shared mechanism in its owning document and point to it from dependents.]
