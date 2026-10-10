# [Deployment Architecture]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## Scope and constraints

[Explain the placement problem, workload and quality assumptions, isolation needs and environmental constraints. State what this model can and cannot guarantee.]

## Runtime unit model

[Explain how logical responsibilities map to runtime units and owned state, and why release, scaling or isolation needs justify those boundaries.]

## Placement and isolation

[Explain how workload, shared dependencies and failure assumptions determine capacity, placement and isolation. State sizing assumptions, scaling triggers and limits with their evidence. Compare relevant deployment variants on the same assumptions, including resource and operational costs.]

[Figure: environments, units, zones and failure domains]

## Dependencies, connectivity and lifecycle

[Explain compute, persistence, messaging and execution dependencies and compatibility requirements. Trace relevant traffic across trust boundaries; name admission, startup, readiness, drain and recovery owners. Distinguish restart from restoration of correct service and connect diagnostic signals to operating decisions.]

## Failure domains

[Trace a shared-dependency or placement failure through affected units, containment and recovery. Explain which operating guarantees survive and what conditions are required to restore the others.]

## Release and rollback

[Explain how version coexistence, draining and state preservation allow a release to proceed safely. Distinguish release rollback from failure recovery and identify incompatibilities that make reversal unsafe.]

## Validation and review triggers

[Explain what evidence supports or challenges the operating guarantees under the stated assumptions. Link the relevant scenario or experiment and its limitations. State which workload, dependency or design changes require the model to be reconsidered.]

## Application and adaptation

[Explain the assumptions that make the design valid, the changes that require adaptation and the consequences for dependent owners. Identify prerequisites, compatibility or transition limits, and evidence needed before relying on the changed model. Bound reusable claims with an unsuitable context where relevant.]

## Related documents

[Link parent, child, cross-view and source documents with a short explanation of what each contributes. Keep a shared mechanism in its owning document and point to it from dependents.]
