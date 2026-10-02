# [Subsystem Architecture]

**Purpose:** [Architecture Knowledge / Concrete Design]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## 1. Responsibility, scope and parent constraints

[Explain why this responsibility group warrants a Subsystem, what it owns and excludes, and the intended result. Link the parent architecture and identify the guarantees, invariants, quality priorities and operating constraints allocated to this Subsystem. Establish a representative caller scenario and relevant local design pressures. Keep inherited commitments, locally owned choices and changes requiring parent coordination distinct. Establish the relevant baseline, assumptions and decision status.]

## 2. External collaboration and key guarantees

[Explain callers, dependencies and upstream or downstream relationships. Describe the important operations or events, their meaning, preconditions, completion conditions and externally visible guarantees. Identify synchronous or asynchronous interaction and what callers can infer from success, rejection, timeout or an unknown outcome. Name the dependency assumptions needed to uphold these commitments and their owners where known. Keep detailed endpoints, executable field schemas and exhaustive interface specifications in their owning authority; retain the semantics needed to constrain the internal design here.]

[Figure: subsystem context]

## 3. Internal solution and responsibility boundaries

[Show the internal solution and explain how its parts collectively realize the external guarantees. Select functional modules or implementation components according to the reader task and Subsystem scope, keeping peer functions distinct from shared mechanisms and runtime carriers. Name responsibility and state owners, dependency direction and local versus remote interaction; map functions to software modules, components, processes, stores and adapters without forcing another nesting level. Explain important boundary and technology choices, plausible alternatives, costs and review triggers. Place rationale beside the affected design and link independently owned component or shared-mechanism explanations.]

[Figure: internal modules or components and ownership at the selected level]

## 4. Data and state design

[Explain the core entities, identities, relationships, versions, lifecycle and legal state transitions. Identify authoritative and derived state, owners, local transaction boundaries and cross-boundary consistency requirements. Connect these choices to the external guarantees and distinguish required invariants from replaceable storage choices. Identify reconstruction sources and relevant access, retention and audit rules. Link detailed data models and executable schemas while retaining the information meaning and state boundaries needed to implement the allocated responsibility.]

## 5. Critical flows and implementation mechanisms

[Follow the representative request or change through the named internal participants, state transitions and observable result. Explain how transaction, concurrency and coordination mechanisms uphold the boundary guarantees, including ordering, idempotency, retries or asynchronous completion where material. Trace a consequential failed or unknown outcome through safe behavior and recovery; identify the responsible owner, source of truth and guarantees that remain valid or are temporarily weakened. Show authorization and control enforcement at the relevant actions. Exercise the selected mechanism rather than repeating module descriptions, and link detailed component algorithms where they own the explanation. For a static structural question, trace a concrete dependency or change impact.]

[Figure: core interaction]

## 6. Deployment, operation and failure recovery

[Explain how the Subsystem's logical parts map to runtime and deployment units within the parent topology; a Subsystem need not be deployed separately. Identify placement, network and runtime dependencies, resource and workload assumptions, capacity limits and failure domains where material. Explain observability, health and completion signals, degradation, restart, replay, recovery and failover, connecting operating failures to the request and state guarantees above. Identify trust boundaries, isolation, detection, response and durable evidence. Distinguish inherited operating arrangements from local mechanisms and recovery responsibilities. Link detailed deployment designs, configuration and runbooks while retaining the combined operating consequences here.]

## 7. Validation and open questions

[Trace inherited and local guarantees to their implementation mechanisms, validation scenarios, sourced pass criteria and observed or planned evidence. Check that the internal parts compose into the externally promised behavior using the representative success and failure scenarios. Distinguish illustrative reasoning, observations, proposals and verified results. Identify unresolved choices, contradictory assumptions and missing evidence; name the affected commitment, the evidence or decision needed to close the gap and its owner where known. State residual risks and review triggers, keeping unverified acceptance explicit.]

## 8. Evolution and compatible migration

[Explain which internal changes preserve the model and which alter the Subsystem's boundaries, external guarantees or parent commitments. Identify effects on callers, dependencies and authoritative state, distinguishing local decisions from changes requiring parent coordination. For a concrete change, describe compatibility boundaries, intermediate states, migration dependencies, cutover conditions, rollback limits and recovery after irreversible change; link an existing migration design when it owns the detail. Keep task schedules and operating procedures in their owning artifacts. State the evidence and decision authority needed before relying on the changed design.]
