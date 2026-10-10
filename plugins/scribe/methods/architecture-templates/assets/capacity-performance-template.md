# [Capacity and Performance Architecture]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## Scope and workload model

[Workload classes, distribution, bursts, data sizes and unverified assumptions]

## Critical paths and budgets

[Explain how the workload creates demand along the processing path, where shared bottlenecks form and how latency or resource budgets follow from the target. State the evidence and uncertainty behind the budget allocation.]

[Figure: processing path and shared bottlenecks]

## Scaling and partitioning

[Explain how the selected scaling or partitioning mechanism changes demand on the bottleneck, and its limits under skew or bursts. Compare alternatives on the same workload rather than assuming scaling is linear.]

## Backpressure and overload

[Admission, queue bounds, load shedding, fairness and safe degradation]

## Hotspots and dependency budgets

[Skew, burst isolation, shared resources and downstream limits]

## Performance experiments

[Explain the hypothesis, representative workload and measurements that could establish or challenge the claimed capacity. Separate predicted behavior from observed results and show the limits of the experiment.]

## Validation and review triggers

[Explain what evidence supports or challenges the operating guarantees under the stated assumptions. Link the relevant scenario or experiment and its limitations. State which workload, dependency or design changes require the model to be reconsidered.]

## Application and adaptation

[Explain the assumptions that make the design valid, the changes that require adaptation and the consequences for dependent owners. Identify prerequisites, compatibility or transition limits, and evidence needed before relying on the changed model. Bound reusable claims with an unsuitable context where relevant.]

## Related documents

[Link parent, child, cross-view and source documents with a short explanation of what each contributes. Keep a shared mechanism in its owning document and point to it from dependents.]
