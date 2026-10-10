# Architecture reasoning method

Use this method inside any Public Skill that must reason about architectural scope, ownership, controls, failure, options, evolution, or validation.

## Architecture model

Keep the design object, viewpoint and document structure separate:

| Axis | Meaning | Examples |
| --- | --- | --- |
| Architecture Object | The entity being designed | Company Technical Landscape, System, Subsystem, Functional Module, Component |
| Architecture Scope | The selected responsibility and environment boundary | One service and its dependencies, one company landscape |
| Architecture Viewpoint | One of Scribe's four design-reasoning and completeness perspectives | Domain, Application, Governance, Runtime |
| Architecture View | A concrete explanation of an object through a viewpoint | A service's application structure, its runtime behavior |
| Authority Level | The scope owning a decision or technical artifact | Company, System, Subsystem |

Use Domain, Application, Governance and Runtime to derive design decisions and check completeness. Apply them to both Architecture Knowledge and Concrete Design at the object's scope. Let purpose and document responsibility govern expression through the Architecture Documents Method; viewpoints do not select templates or require headings, documents or directories. This is Scribe's working framework, not a universal architecture taxonomy.

## Responsibility decomposition

When designing or reviewing internal structure, choose the decomposition by responsibility before drawing nodes. Use the following distinctions; they are optional levels, not a mandatory System → Subsystem → Module → Component tree.

| Element | Boundary evidence | Design obligation |
| --- | --- | --- |
| System | Stable business or technical responsibility, lifecycle and externally meaningful contracts | Identify accountable ownership, authoritative state where applicable, external guarantees and evolution boundary |
| Subsystem | A cohesive group of responsibilities within a System whose complexity warrants independent design and maintenance | Explain its parent allocation, internal autonomy, contracts and why ordinary modules are insufficient |
| Functional module | A cohesive function with identifiable operations, rules, outputs and state responsibility where applicable | Name the function and explain its collaboration with peer functions |
| Implementation component | An encapsulated mechanism behind an explicit interface | Name its consumers, guarantees, owned or derived state and replacement constraints; it may be private to one module or shared |

A System or Application can contain functional modules directly. A module may use several components, and several modules may share one component. Code repositories, API endpoints, Agents, Workers, databases and deployment instances are implementation evidence, not automatic System or Subsystem boundaries. Separate deployment is neither required nor sufficient for a logical split. A platform mechanism can itself justify a System when it has an independently governed technical responsibility; its technical name alone neither admits nor excludes it.

For each proposed boundary, identify the outcome or technical service, operations and invariants, state and decision owner, callers and dependencies, and meaningful contract. Compare keeping it inside the parent with splitting it: explain the cohesion or independent evolution gained, the coordination and consistency cost, and the evidence that would change the decision. Prefer fewer boundaries when a split only renames a capability, table, process or team without changing responsibility. Use Product capabilities as requirements; preserve many-to-many mappings rather than converting each capability into a System.

For a functional decomposition view, put peer functions at the same level. Place cross-cutting mechanisms such as versioning, authorization, idempotency, storage adapters and notification delivery in shared-component explanations, and place API processes, Workers and stores in realization or runtime views. Functional responsibilities may use those mechanisms without becoming subordinate to a technical pipeline. For example, Report Generation is a function; a model adapter is a component, and a report Worker is its runtime carrier. An Agent may implement planning and orchestration across functions; treat it as a functional module only when a distinct responsibility and contract justify that choice.

An implementation view may show components and infrastructure together when their roles and boundaries are explicit. Keep each figure's chosen abstraction consistent and label any deliberate cross-level reference. Draw grouping boundaries when they distinguish responsibilities or internal from external participants; omit a redundant frame enclosing every node in a single group.

Before accepting the decomposition, verify that readers can identify who decides, who owns each state, and how a request crosses the boundaries. Apply Structure-to-flow traceability below; a separately deployed component must not silently become a new subsystem. Materialize a separate document only when its independent reader task and maintenance value justify it, following the Architecture Documents Method.

## Structure-to-flow traceability

Build each core flow from the responsibility owners established in the structural model. Use the decomposition justified for that object without adding intermediate levels. Preserve many-to-many relationships between flows and participants; select the participants needed for each outcome rather than visiting every structural element.

Choose the flow's question and expansion boundary by document responsibility. Reuse a scenario across levels when useful, but develop the contribution owned at each level:

| Document responsibility | Flow question and expansion boundary |
| --- | --- |
| Overall / System Architecture | Explain how the whole object's outcome follows from collaboration among its principal responsibility owners: Systems at company scope, or actual Subsystems/modules at System scope. Follow cross-boundary contracts, authoritative state changes, completion and coordinated failure/recovery. Treat each participant's internal processing as an operation with observable semantics. |
| Subsystem Architecture | Expand the responsibility allocated to this Subsystem into collaboration among its internal modules or components. Start and end at its external contract; retain callers and adjacent parts as context and dependencies. Explain local coordination, transaction boundaries and recovery that jointly realize that contract. |
| Module Design | Expand a supported operation into rule evaluation, decisions, internal processing, state transitions, atomic commits and dependency use. Show how the module's internal parts or cohesive processing steps realize its contract, including local failure and recovery. Keep peer modules at their dependency contracts. |
| Component Architecture | Expand a component operation into the algorithm, protocol or state/resource mechanism that establishes its usage guarantee. Keep consumer workflows at the interface and explain only the mechanism this component owns. |

Connect a child flow to the parent operation or handoff it realizes, using the same input and identity meaning, preconditions, completion, externally visible effects and failure semantics. Let one parent step expand into several child steps; add local rules and mechanisms while preserving the parent's observable promise. For example, a System's inventory-reservation handoff can expand in Module Design into duplicate detection, availability checks and an atomic reservation commit. Treat newly required caller duties or changed completion/failure behavior as a parent-contract decision rather than silently redefining them locally.

Keep internal details in the integrating flow only when they determine a cross-boundary guarantee or coordination decision; explain their consequence and leave the full local sequence to its owning explanation. When no child document exists, include necessary local detail in a clearly scoped subsection of the same document. Create neither extra levels nor supporting documents solely to separate flows.

Use consistent participant names in structure, contracts, flow prose and figures. Map any lower-level component or runtime carrier used in a flow to its logical responsibility owner, and make deliberate changes of abstraction explicit. When a flow reveals a new participant, add its responsibility and relationships to the structural model or identify it in the external context before using it.

Assign every architecturally significant action, decision and state change to a participant. Connect cross-boundary handoffs through the established command, event, query or other contract, including the receiving owner's responsibility and completion meaning. Trace consequential failures through detection, recovery ownership and the state or evidence that permits continuation. Use this collaboration to explain how the structure produces the scenario's observable outcome; a sequence of business activities alone is insufficient.

Complete this check when readers can locate every flow participant in the structure or external context, trace lower-level realizations to their owners, and follow actions, state changes, contract handoffs, completion and recovery without encountering unexplained participants or conflicting responsibilities. Verify that each flow answers its document-level question and, where parent and child explanations exist, the child adds the owned realization while preserving the parent contract. Revise repeated parent/child sequences or figures that add no local explanation. Resolve mismatches in the owning structural or contract definition and the affected flows together.

## Four viewpoints

| Viewpoint | Reader question and review responsibility |
| --- | --- |
| Domain | What concepts, facts, rules, lifecycle states and invariants define the problem? |
| Application | Which systems and modules own behavior and state, and how do their contracts and dependencies realize it? |
| Governance | Who may decide or act, under which constraints, with what review and evidence? |
| Runtime | How does the design operate under deployment conditions, load, failures and recovery? |

Link company Business and Product facts to their owning authorities. Explain their technical consequences without redefining their product meaning.

Do not introduce Data, Integration, Deployment or Security as additional peer viewpoints, predefined subcategories or recommended standalone documents. Their organization is deferred. Address necessary facts and mechanisms in the relevant explanation, allowing them to affect more than one viewpoint without imposing a fixed placement scheme. Preserve existing specialist templates as resources; use them for an explicitly requested specialist artifact, not to expand an ordinary architecture request.

## Correctness checks

Apply the four viewpoints throughout the reasoning loop below:

1. During Context and Drivers, identify the relevant rules and state invariants, behavior and information owners, controlled actions and evidence, and load or failure conditions. Turn them into sourced requirements or explicit assumptions; scale the questions to the object rather than repeating a company-wide checklist in each child.
2. During Scenarios, Risks and Decisions, trace one outcome and a consequential failure through the relevant concerns together. Derive boundaries, mechanisms and tradeoffs from those drivers. For example, cancellation requires a valid state transition, an owner coordinating the action, permission to request it and a safe result when execution is already in progress; develop one coherent design rather than four accounts of the same flow.
3. During Validation, check that the proposed mechanisms jointly uphold the claims and identify evidence gaps. Resolve each gap in the section or existing document that owns the affected decision. Keep this working coverage check internal unless the user requests it; report material uncertainty beside the claim.

Check domain validity, application ownership, governed authority and runtime behavior through the four viewpoints. An important action must remain authorized and traceable through failure and recovery; information must have clear meaning and ownership. These are coverage checks, not mandatory headings or a requirement for four files.

Use the selected template for the document sequence. A main architecture may combine all four viewpoints. Materialize a separate view only when the requested reader task and maintained content warrant it; do not split merely to complete a taxonomy. Keep object decomposition, viewpoints and document boundaries independent.

## Reasoning loop

Apply this loop across the relevant viewpoints:

```text
Context → Drivers → Scenarios and flows → Risks → Decisions → Validation
```

| Step | Required result |
| --- | --- |
| Context | Object, scope, authority, facts, stakeholders, unknowns, and change assumptions |
| Drivers | Invariants, information authority, ownership needs, constraints, control obligations, runtime conditions, and ranked qualities |
| Scenarios and flows | Concrete operations or change impacts that expose consequential guarantees, conditions and risks at this object's scope |
| Risks | Unsafe assumptions, bypasses, inconsistency, overload, unrecoverable states, and evidence gaps |
| Decisions | Boundaries, ownership, contracts, controls, deployment structure, patterns, and accepted costs |
| Validation | Tests, reviews, drills, operating evidence, and signals that prove or challenge each judgment |

Revisit an earlier judgment only when new evidence invalidates it, then trace the consequence forward again.

## Architecture judgment

Use these distinctions when deriving and explaining a design:

- **Constraint:** a boundary that cannot be violated in the stated context; identify its authority. Keep mandatory correctness and authorization obligations distinct from negotiable quality targets.
- **Architecture characteristic (quality):** a quality the object must exhibit. Prioritize it through a concrete operating or change scenario, an observable response and a sourced target or explicit unresolved target. Explain conflicts between qualities rather than promising all of them equally.
- **Architecture principle:** a durable rule guiding multiple choices. State its rationale, scope, practical consequence and exception authority where known; distinguish inherited principles from local proposals. A product name or a single mechanism is not a principle.
- **Architecture style:** an organizing form that constrains elements and relationships at a named scope. Explain the structural properties that justify the label, relevant alternatives, accepted costs and change triggers. Separate logical organization, deployment units and local interaction patterns; a queue alone does not make the entire architecture event-driven. Use a precise structural description when no established style fits.
- **Architecture strategy:** a coordinated approach to a significant problem or characteristic. Connect it to the principles and constraints it respects, the mechanisms that realize it, the cost it introduces and the scenario that tests it.
- **Pattern and mechanism:** a reusable response and its concrete realization. Explain how the selected transaction, algorithm, protocol or operating arrangement supports the strategy, rather than treating its name as proof.
- **Decision:** a scoped choice with evidence, alternatives, accepted cost and decision status. Distinguish an inherited choice, an interpretation of existing structure and a newly proposed choice.
- **Validation:** evidence that tests a named judgment and the conditions that would challenge it.

Trace significant choices from problem and constraints through prioritized characteristics and applicable principles to style or strategy, realizing mechanisms and validation. Revisit these relationships when a choice exposes a conflict; use the trace as a reasoning aid, not a forced linear process or a requirement for one document per concept. Apply the four viewpoints to discover and challenge these choices; viewpoints do not replace these design elements.

For Overall and Subsystem Architecture, explain the applicable style and major strategies explicitly. For Module and Component design, inherit the enclosing style and principles, then explain local quality scenarios, strategies and mechanism choices; propose a separate style only when the local structure warrants one. For Knowledge, explain conditions, variants and counterexamples; for Concrete Design, explain the object's actual or proposed choices and unresolved evidence. Pressure-test each choice for **fit**, **simplicity**, and **evolution**.

Complete the judgment when readers can identify the relevant characteristics, principles, organizing form and strategies, follow their consequences into mechanisms, and explain the cost and evidence that could change a material choice. A list of quality words or mechanisms alone does not satisfy this condition.

## Control trace

For every material control, trace:

```text
objective and unsafe outcome
→ protected value and capability
→ policy, decision, information, state, and execution owners
→ last responsible control point
→ allow, reject, hold, limit, degrade, repair, or fail-closed behavior
→ durable evidence
→ design and operating validation
```

Test missing, stale, conflicting, duplicate, delayed, partially applied, and unknown outcomes. “Log and continue” is not a safe default.

## Turn reasoning into an architecture document

Carry the structural model, scenario-derived mechanisms and Architecture judgment into the owning Writer's selected document. Use **Structure-to-flow traceability** to preserve responsibility and expansion boundaries. Keep sources, illustrative behavior, proposals and accepted decisions distinct; compare alternatives against the same drivers and scenarios. Use the section plan and explanation-and-repair loop in `architecture-documents.md` to turn this reasoning into a reader-usable account. Apply only the affected judgments for narrow edits and reviews.

## Reader verification

Apply **Make the design usable** and **Review before completion** in `architecture-documents.md` to the delivered artifact. That method owns the reader reconstruction, evidence comparison and repair loop; use this method's judgments and expansion boundaries to determine what must be understood. Treat viewpoint coverage as a way to find an overlooked commitment, not as evidence that its explanation works. Keep design validation distinct from verification that the document explains the design.

## Completion

Architecture reasoning is complete when the object and scope are explicit, the four viewpoints have been reviewed for relevant concerns, authoritative facts and state have one owner, material controls trace authority through evidence, failure and recovery behavior preserve invariants, the Architecture judgment completion condition is satisfied in the explanation, and every accepted tradeoff names its cost and review trigger.
