# [Runtime Architecture]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## Operating scope and drivers

[Runtime responsibilities, operating conditions and architectural constraints]

## Operating model

[Figure: runtime units, dependencies, control and data paths]

## Ownership and lifecycle

[Explain which runtime owners admit work, manage state and determine readiness, degradation or recovery. Show how their responsibilities preserve the operating guarantees across lifecycle changes.]

## Cross-topic relationships

[Explain how deployment, network, state, observability, resilience and capacity assumptions depend on one another. Link the owning topic for each mechanism; keep this substantive runtime architecture responsible for the aggregate operating judgment.]

## Critical operating scenarios

[Walk a representative workload or dependency-loss scenario through the runtime units, control and data paths to its observable result. Trace recovery and identify where an unsafe state must block normal service.]

## Patterns and tradeoffs

[Explain the relevant alternatives under the same scenario and assumptions: how each mechanism works, what it gains, what it costs and where it fails. Use a compact comparison table only when several choices share meaningful criteria; state the conditional selection and review trigger in prose.]

## Validation and review triggers

[Explain what evidence supports or challenges the operating guarantees under the stated assumptions. Link the relevant scenario or experiment and its limitations. State which workload, dependency or design changes require the model to be reconsidered.]

## Application and adaptation

[Explain the assumptions that make the design valid, the changes that require adaptation and the consequences for dependent owners. Identify prerequisites, compatibility or transition limits, and evidence needed before relying on the changed model. Bound reusable claims with an unsuitable context where relevant.]

## Related documents

[Link parent, child, cross-view and source documents with a short explanation of what each contributes. Keep a shared mechanism in its owning document and point to it from dependents.]
