# [Overall Architecture]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## 1. Design goals and scope

[Name the architecture object, scope and decision authority. Explain the problem, current baseline, intended outcomes, actors, external dependencies and non-goals; distinguish current and target design, proposals and accepted decisions, and planned and implemented behavior. Establish the critical scenarios, domain invariants, quality priorities, threats and operating constraints that drive the design. Cite requirements and evidence; keep missing budgets and applicability assumptions explicit. For reusable Knowledge, establish the intended context and applicability instead of inventing a delivery baseline.]

## 2. Overall solution and key tradeoffs

[Explain the selected, proposed or reference solution through a principal architecture figure showing the main participants, boundaries and relationships. Connect the organizing strategy and important technology choices to the goals and constraints. Compare plausible alternatives, explain accepted costs and name evidence that would change the choice. Establish how the combination can meet the requirements before expanding individual responsibilities; place each mechanism's detailed rationale beside its design in the following sections.]

## 3. System composition and responsibility boundaries

[Explain what each part owns, provides and depends on, and allocate important guarantees to accountable owners. Justify System boundaries by stable responsibility, state ownership where applicable, contracts and lifecycle; use Subsystems only where internal complexity warrants them. Keep peer functional responsibilities distinct from shared implementation mechanisms and runtime carriers. Map logical responsibilities to software modules, components, processes, stores and adapters at the document's scope. Explain dependency direction and local versus remote interaction. Link governing or detailed architectures at their owning boundaries, keeping the complete assembly intelligible here.]

## 4. Core data and state design

[Explain the core entities, identities, relationships, versions, lifecycle and state transitions. Identify authoritative and derived information, ownership, local transaction boundaries, cross-boundary consistency and reconstruction sources. Explain the mechanisms that preserve important invariants and protect sensitive information, including access, retention and audit consequences where material. Link detailed data models and executable schemas while retaining the meanings and state guarantees needed to understand the overall design.]

## 5. Critical flows and collaboration mechanisms

[Follow a critical end-to-end scenario through the same participants, identities and state changes defined above to an observable outcome. Explain the necessary interactions: operations or events and their meaning, callers and owners, synchronous or asynchronous coordination, completion conditions and architecture-significant failure semantics. Trace a consequential failure and recovery, including timeout, duplicate, partial or unknown outcomes where relevant; identify the mechanism and owner that preserve or restore the guarantee. Show authorization and control enforcement at the relevant boundaries and connect the flow to operating behavior in section 6. Keep detailed endpoints, field schemas, protocol formats and exhaustive error catalogs in their owning interface or Machine Authority; retain a detail here only when it materially determines the overall solution. For a static structural question, demonstrate a concrete dependency or change impact.]

## 6. Deployment and operational assurance

[Map logical responsibilities to deployment units, environments, placement, network relationships and failure domains. Explain runtime dependencies, workload and resource assumptions, capacity and performance mechanisms, observability, degradation, recovery and failover ownership. Explain trust boundaries, isolation, detection, response and durable evidence, connecting these protections to the data and action controls in sections 4 and 5. Distinguish deployment structure from operating behavior; link detailed deployment designs, configuration and runbooks while owning their combined consequences for the overall guarantees.]

## 7. Architecture validation and open questions

[Connect important requirements and guarantees to their design mechanisms, validation scenarios, sourced pass criteria and observed or planned evidence. Use the critical flow and failure above to assess whether the parts compose into the promised result. Distinguish an illustrative walkthrough from demonstrated behavior and verified acceptance. Identify contradictory views, unallocated responsibilities, unverified dependency assumptions and pending decisions; name the commitment each gap prevents, the evidence or decision required to close it and its owner where known. State residual risks and review triggers without inventing approval or unsupported thresholds.]

## 8. Evolution and compatible migration

[Explain which changes preserve the model and which invalidate it. For a concrete change, describe the baseline-to-target transition, intermediate states, sequencing dependencies, compatibility boundaries, state migration, cutover conditions, retirement and rollback limits; explain recovery after irreversible change. Link an existing migration design when it owns the detail. Keep task schedules and operational procedures in their owning artifacts. For reusable Knowledge, explain variants, adoption choices, adaptation prerequisites and unsuitable contexts. State the evidence and authority needed for a change without treating an unaccepted proposal as established technical truth.]
