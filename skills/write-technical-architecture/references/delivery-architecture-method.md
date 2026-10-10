# Project delivery architecture

Use this branch for a concrete project, engagement or bounded delivery architecture request. Keep project authority distinct from the company Technical Landscape and governing System/Subsystem design. A project need not be a Registered System; identify its concrete object and baseline without inventing company registration.

## Select artifacts

Read the Writer registry and select `delivery-architecture` for a main architecture, `delivery-subsystem`, `delivery-module` or `delivery-component` for a detailed object, and `delivery-index` for a multi-file entry. Select `delivery-deployment` only for an explicitly requested deployment artifact; select `delivery-migration` or `delivery-validation` when the corresponding concern needs its own deliverable. A single architecture can own these sections without separate files. Keep a clear main entry and create only justified supporting artifacts.

Use an existing Architecture Decision record where its owning authority already maintains one; summarize and link it. For a standalone Company/System decision record, recommend `$Write Tech Doc`. Handle an occasional standalone Project decision record as a Project Freeform Artifact with its choice, status, governing scope, alternatives, rationale, costs, authority and validation explicit; link the affected delivery architecture. This does not require a duplicate permanent template or another invocation for decisions inside a delivery architecture.

## Use shared structure

Select `delivery-database-design` for a requested database design or independently useful database detail. Apply `../../../methods/references/database-design-writing.md` for its scope and placement, lightweight structure, conditional mechanisms and validation; embed small database concerns in their owning design.

Read `../../../methods/architecture-templates/concrete-design.md` with the assigned shared template. Use the same overall, subsystem, module and component structures as Architecture Knowledge; retain existing deployment resources for their explicit branch. Apply the four viewpoints through the shared Architecture Reasoning Method during driver identification, mechanism design and completeness checks. Keep an explicitly requested specialist artifact within this delivery's authority as a Freeform Artifact when no registered type applies. Integrate small topics in the main architecture rather than creating one file per view.

Retain delivery entry, migration and validation assets for their distinct navigation, transition and acceptance responsibilities. Merge their relevant content into a single deliverable when separate files add no reader value. Let the main architecture remain readable without following every supporting link.

## Establish design and evidence

Read actual requirements, baseline architecture, constraints, dependencies, accepted decisions and relevant reference knowledge. Record material knowledge adoption as Adopt, Adapt or Reject with reasons. Separate observed baseline, proposed target, accepted choice and implementation state. Develop a useful proposal under explicit assumptions when the scope is clear; ask only for missing information that materially blocks a responsible design.

Explain concrete responsibilities, interfaces, authoritative state, normal/failure behavior, deployment and controls. Trace the requirements to design responses and measurable validation criteria without fabricating thresholds. Record project-specific compatibility, migration, rollout and rollback architecture when needed; keep task schedules and operational procedures in their owning artifacts. Identify the authority needed for pending decisions without claiming approval.

Write project proposals in their project location and link stable company/System authorities. Update a stable authority only when the request authorizes it and the accepted change is supported. Do not silently promote a proposal into stable technical truth.

## Completion

Verify a complete main architecture or independently useful detail, coherent supporting links, explicit current/target and decision status, requirements-to-design-to-validation traceability, migration constraints where relevant, and honest residual risks. Mark acceptance only from actual evidence and authorized decisions. Templates produce architecture deliverables, not permission to deploy or operate the target.
