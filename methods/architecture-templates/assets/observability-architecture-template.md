# [Observability Architecture]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## Scope and diagnostic questions

[What readers must detect, explain and correlate; audit-evidence boundary]

## Signal taxonomy

[Explain which diagnostic questions require which signals, who produces and consumes them and what each signal cannot establish. Distinguish service health from audit evidence.]

## Flow and health coverage

[Follow a representative flow and explain how its signals expose healthy, degraded or unsafe behavior. Identify ownership and blind spots; use a coverage matrix only when several flows require systematic comparison.]

## Correlation model

[Figure: request, event, state, policy and evidence identifiers]

## Alerting and diagnosis

[Walk a consequential condition from impact detection through correlation and diagnosis to the responding owner. Explain why the available evidence supports that diagnosis and where the response authority ends.]

## Telemetry failure

[Missing signals, sampling limits, collection failure and instrumentation overhead]

## Patterns and tradeoffs

[Explain the relevant alternatives under the same scenario and assumptions: how each mechanism works, what it gains, what it costs and where it fails. Use a compact comparison table only when several choices share meaningful criteria; state the conditional selection and review trigger in prose.]

## Validation and review triggers

[Explain what evidence supports or challenges the operating guarantees under the stated assumptions. Link the relevant scenario or experiment and its limitations. State which workload, dependency or design changes require the model to be reconsidered.]

## Application and adaptation

[Explain the assumptions that make the design valid, the changes that require adaptation and the consequences for dependent owners. Identify prerequisites, compatibility or transition limits, and evidence needed before relying on the changed model. Bound reusable claims with an unsuitable context where relevant.]

## Related documents

[Link parent, child, cross-view and source documents with a short explanation of what each contributes. Keep a shared mechanism in its owning document and point to it from dependents.]
