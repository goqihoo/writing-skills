# [Module Design]

**Purpose:** [Architecture Knowledge / Concrete Design]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## 1. Functional responsibility and scope

[Name the cohesive function, intended result, callers and exclusions. Identify the parent System or Subsystem and the requirements, invariants and quality constraints allocated to this module. Explain why this function needs independent design detail. Distinguish locally owned rules from inherited commitments and changes requiring parent coordination; a module does not introduce a new authority level or require its own deployment.]

## 2. Operations, rules and external collaboration

[Explain the operations the module provides, their input and output meaning, preconditions, business or technical rules and completion conditions. Identify callers, dependencies, allowed actions and externally visible failure or unknown outcomes. State the guarantees required from dependencies and the assumptions under which this function is valid. Link complete interface specifications while retaining the semantics needed to implement and use the function.]

## 3. Internal design and dependency organization

[Explain how internal responsibilities, rule evaluation and coordination realize the function. Identify private or shared implementation components and why each is needed; keep peer functions distinct from the mechanisms they use. Explain dependency direction, important technology choices, alternatives and costs. Use a simple internal model when sufficient; create no child component merely to fill a hierarchy. Link independently owned component designs without repeating their algorithms.]

[Figure: internal responsibilities, dependencies and private or shared components]

## 4. Data, state and transaction boundaries

[Explain the entities, identities, relationships and state transitions relevant to the function. Identify authoritative state, derived information, owners and reconstruction sources. Specify local atomic changes, cross-boundary consistency requirements and the invariants that processing must preserve. Explain the data access, retention and evidence requirements that affect these choices. Link executable schemas rather than duplicating their complete definitions.]

## 5. Processing flows and coordination mechanisms

[Walk a representative operation from input through rule evaluation, participating owners, state changes and observable result. Explain how sequencing, transactions, concurrency and synchronous or asynchronous coordination uphold the functional guarantees. Trace a consequential exception, duplicate, partial or unknown outcome and its recovery, naming who decides and what evidence permits continuation. Explain local orchestration and the required behavior of dependencies; keep a component's independently owned algorithm in its design.]

[Figure: processing flow, decisions and state changes]

## 6. Failure handling and operating constraints

[Explain the module's behavior under dependency failure, cancellation, overload and resource limits where relevant. Identify timeouts, retry ownership, backpressure, degradation, reconciliation and completion signals, connecting them to the processing flow above. Locate control enforcement and durable evidence. State assumptions about the parent runtime, isolation and recovery arrangements, and identify the module's own responsibilities without inventing a separate deployment.]

## 7. Validation and open questions

[Connect the function's rules and inherited guarantees to scenario checks, sourced pass criteria and observed or planned evidence. Include boundary, failure and recovery behavior that could challenge the design. Identify unmet dependency assumptions and pending decisions with the affected guarantee, required evidence and owner where known. Distinguish illustrative examples from demonstrated behavior and keep unverified acceptance explicit.]

## 8. Evolution and compatibility

[Explain how rule, state, operation and dependency changes affect callers and parent commitments. Identify extension points, compatible changes, state-transition requirements and rollback or recovery limits. State which changes can be made locally and which require coordination. Compare relevant variants through their assumptions, costs and guarantees; identify conditions that require redesign or prevent reuse.]
