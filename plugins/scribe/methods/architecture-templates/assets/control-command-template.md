# [Control Command Architecture]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## Purpose and command taxonomy

[Explain which outcomes the commands protect, how command classes differ in their effects and scope, and which state owners carry them out. Introduce a representative controlled action that the lifecycle below will follow.]

## Actors and approval

[Explain who may originate, authorize and execute commands, how scope is constrained and why duties are separated. Describe the approval relationship before using a matrix for repeated permissions.]

## Command lifecycle

[Explain how a command moves from request through authorization, routing, local validation and execution to confirmation. State what each stage establishes and which outcome remains unknown until confirmation.]

[Figure: request, authorize, route, validate, execute and confirm]

## Routing and owning executor

[Explain how a command reaches the owner able to change the target state and why that owner is the last responsible enforcement point. Trace one illustrative command through routing and confirmation.]

## Control state and snapshots

[Version, scope, freshness, conflict and local interpretation]

## Ordering, expiry and failure

[Explain how repeated, reordered, expired or partially applied commands affect the lifecycle. State the mechanism for idempotency or ordering where required, safe behavior for unknown outcomes and the recovery owner.]

## Evidence model

[Explain how action identity, authority reference, policy version and outcome are linked durably enough to reconstruct the decision and effect. Distinguish a received command from a completed action.]

## Patterns and tradeoffs

[Explain the relevant alternatives under the same scenario and assumptions: how each mechanism works, what it gains, what it costs and where it fails. Use a compact comparison table only when several choices share meaningful criteria; state the conditional selection and review trigger in prose.]

## Validation

[Explain how the principal claims could be established or challenged. Connect a concrete example, experiment, review or operational observation to the claim it tests, the expected signal and the limits of the evidence. Distinguish illustrative reasoning, sourced observations and proposed checks.]

## Application and adaptation

[Explain the assumptions that make the design valid, the changes that require adaptation and the consequences for dependent owners. Identify prerequisites, compatibility or transition limits, and evidence needed before relying on the changed model. Bound reusable claims with an unsuitable context where relevant.]

## Related documents

[Link parent, child, cross-view and source documents with a short explanation of what each contributes. Keep a shared mechanism in its owning document and point to it from dependents.]
