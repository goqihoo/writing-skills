# [Integration Architecture]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## Purpose and collaboration requirements

[Establish the interacting parties, trust and ownership boundaries, required business outcome and constraints. Identify the assumptions behind the model.]

## Interaction model

[Explain command, query, event or batch interactions as applicable, direction and synchronous or asynchronous choices. Show participants and meaningful exchanges; justify coupling and mediation choices.]

## Contract semantics

[Explain operation and payload meaning, identity and correlation, preconditions, completion, errors and unknown outcomes. Distinguish receipt from completed business effect; link the owning information model.]

## Consistency and delivery mechanisms

[Explain local transactions and cross-boundary coordination, ordering, duplicate handling, retries and reconciliation where needed. Identify the state and owner that make each guarantee possible.]

## Trust and dependency controls

[Explain caller identity, authorization, data protection, timeouts, resource limits and degraded dependency behavior where they affect the contract. Link detailed security and runtime mechanisms.]

## End-to-end exchange and recovery

[Walk a representative exchange from initiating state to observable effect, then trace a consequential partial or ambiguous outcome to resolution. State what each party may safely conclude at each boundary.]

## Compatibility and evolution

[Explain contract and event version changes, coexistence, consumer migration and removal conditions. Trace the effect of one meaningful change through dependent parties.]

## Alternatives, validation and adaptation

[Compare plausible interaction models under the same scenario. Define checks for semantic compatibility and failure behavior, evidence limits, adoption prerequisites and unsuitable contexts.]

## Related documents

[Link the overall scenario, data meaning, participating application contracts and runtime transport mechanisms. Keep a shared exchange definition in one owning document.]
