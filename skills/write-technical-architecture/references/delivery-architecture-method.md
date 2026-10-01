# Project delivery architecture

Use this branch for a concrete project, engagement or bounded delivery architecture request. Keep project authority distinct from the company Technical Landscape and governing System/Subsystem design. A project need not be a Registered System; identify its concrete object and baseline without inventing company registration.

## Select artifacts

Read the Writer registry and select `delivery-architecture` for a main architecture, `delivery-subsystem` or `delivery-component` for a detailed object, and `delivery-index` for a multi-file entry. Select `delivery-deployment`, `delivery-migration` or `delivery-validation` only when the corresponding concern needs its own deliverable. A single architecture can own these sections without separate files. Keep a clear main entry and create only justified supporting artifacts.

Use an existing Architecture Decision record where its owning authority already maintains one; summarize and link it. For a standalone Company/System decision record, recommend `$Write Tech Doc`. Handle an occasional standalone Project decision record as a Project Freeform Artifact with its choice, status, governing scope, alternatives, rationale, costs, authority and validation explicit; link the affected delivery architecture. This does not require a duplicate permanent template or another invocation for decisions inside a delivery architecture.

## Establish design and evidence

Read actual requirements, baseline architecture, constraints, dependencies, accepted decisions and relevant reference knowledge. Record material knowledge adoption as Adopt, Adapt or Reject with reasons. Separate observed baseline, proposed target, accepted choice and implementation state. Develop a useful proposal under explicit assumptions when the scope is clear; ask only for missing information that materially blocks a responsible design.

Explain concrete responsibilities, interfaces, authoritative state, normal/failure behavior, deployment and controls. Trace the requirements to design responses and measurable validation criteria without fabricating thresholds. Record project-specific compatibility, migration, rollout and rollback architecture when needed; keep task schedules and operational procedures in their owning artifacts. Identify the authority needed for pending decisions without claiming approval.

Write project proposals in their project location and link stable company/System authorities. Update a stable authority only when the request authorizes it and the accepted change is supported. Do not silently promote a proposal into stable technical truth.

## Completion

Verify a complete main architecture or independently useful detail, coherent supporting links, explicit current/target and decision status, requirements-to-design-to-validation traceability, migration constraints where relevant, and honest residual risks. Mark acceptance only from actual evidence and authorized decisions. Templates produce architecture deliverables, not permission to deploy or operate the target.
