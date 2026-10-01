# Architecture reasoning method

Use this method inside any Public Skill that must reason about architectural scope, ownership, controls, failure, options, evolution, or validation.

## Architecture model

Keep these axes distinct:

| Axis | Meaning | Canonical examples |
| --- | --- | --- |
| Architecture Object | The entity whose architecture is being described | Company, Product, Solution, Business Domain, System, Subsystem |
| Architecture Scope | The selected responsibility and environment boundary around the object | One company Technical Landscape, one System and its dependencies, one cross-System concern |
| Architecture Domain | A foundational family of concerns | Business, Data, Application, Technology |
| Architecture Viewpoint | A reusable way to examine cross-cutting stakeholder concerns | Security, Governance, Runtime |
| Architecture View | The concrete representation produced for one object and scope using a focused domain or viewpoint | Company Application View, System Governance View, System Runtime View |
| Authority Level | The Company, System, or Subsystem scope that owns a Technical Documentation artifact or decision | Company, System, Subsystem |

Authority Level is a Technical Documentation routing concept, not a substitute for Architecture Object or Scope. Use the object's proper name and explicit scope in every architecture artifact.

Select only the domains and viewpoints that materially change the reader decision. Use them as coverage, not as required directories, documents, or fixed headings.

## Foundational domains

| Domain | Owns |
| --- | --- |
| Business | Capabilities, actors, value, responsibilities, policies, concepts, lifecycle, rules, and invariants |
| Data | Information meaning, authority, lifecycle, lineage, quality, exchange, retention, residency, and privacy |
| Application | Applications, Systems, Subsystems, behavior and state ownership, contracts, orchestration, and dependencies |
| Technology | Platforms, infrastructure, storage, messaging, networks, environments, and deployment mechanisms |

Keep company Business and Product authority linked when a Technical artifact uses their facts. Technical Architecture may show their structural consequences without redefining them.

## Cross-cutting viewpoints

| Viewpoint | Examines |
| --- | --- |
| Security | Assets, threats, identities, trust boundaries, protection, detection, response, and evidence |
| Governance | Decision authority, policy, controlled commands, approval, assurance, exceptions, and evidence |
| Runtime | Load, failure, degradation, dependency behavior, observability, replay, recovery, failover, and operating responsibility |

Use **Deployment Architecture** for environments, deployment units, placement, network, cluster, and topology. Use a **Runtime View** for operating behavior, failure, degradation, observability, and recovery.

## Correctness checks

Use four questions as an exhaustiveness check, not as architecture taxonomy:

| Concern | Check |
| --- | --- |
| Domain correctness | Are the facts, concepts, lifecycle states, rules, and invariants valid? |
| Application correctness | Does one authoritative owner preserve each material state and behavior through explicit contracts? |
| Governance correctness | Can every material action be authorized, constrained, evidenced, reviewed, and protected from bypass? |
| Runtime correctness | Do ownership and invariants survive real deployment, load, failure, degradation, and recovery? |

## Reasoning loop

Apply this loop across every relevant domain and viewpoint:

```text
Context → Drivers → Scenarios and flows → Risks → Decisions → Validation
```

| Step | Required result |
| --- | --- |
| Context | Object, scope, authority, facts, stakeholders, unknowns, and change assumptions |
| Drivers | Invariants, information authority, ownership needs, constraints, control obligations, runtime conditions, and ranked qualities |
| Scenarios and flows | Concrete success, failure, duplicate, delayed, partial, unknown, replay, recovery, and evolution paths |
| Risks | Unsafe assumptions, bypasses, inconsistency, overload, unrecoverable states, and evidence gaps |
| Decisions | Boundaries, ownership, contracts, controls, deployment structure, patterns, and accepted costs |
| Validation | Tests, reviews, drills, operating evidence, and signals that prove or challenge each judgment |

Revisit an earlier judgment only when new evidence invalidates it, then trace the consequence forward again.

## Architecture judgment

Distinguish:

- **Constraint:** cannot be violated in the stated context.
- **Quality:** can improve or degrade and must be prioritized.
- **Principle:** guides later choices.
- **Pattern:** a reusable structural response.
- **Decision:** binds the current object and scope and records accepted cost.
- **Validation:** evidence that tests a named judgment.

Pressure-test each choice for **fit**, **simplicity**, and **evolution**.

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

For a full architecture artifact, establish a concrete structural model before expanding the prose. Name the participants, responsibility boundaries, authoritative information or state, and meaningful relationships at the requested scope. Explain why the important boundaries exist. Use a principal view when it materially helps the reader; keep its names and relationships consistent with the text through the shared visual production method.

Demonstrate the model with a representative scenario: follow an input or decision through the participating owners, state changes, observable result, and a consequential failure or exception. For a static structural question, trace a concrete dependency or change impact instead. State the mechanism that preserves or restores the relevant invariant; naming a quality such as reliability is not an explanation. Keep illustrative scenarios visibly distinct from observed behavior.

Connect each material recommendation to a driver, a structural consequence, an accepted cost, and evidence that could challenge it. Compare plausible alternatives on the same scenario and criteria. Report missing evidence at the affected claim; preserve a useful proposed model when the user requests design, labeling assumptions and unaccepted decisions explicitly.

Use coverage checks to find omissions after drafting. Express the result through subject-specific explanations, views, and comparisons that let the reader reconstruct the architecture. Apply this process only to affected content for narrow edits and reviews.

## Reader verification

Before delivery, verify that the artifact lets its intended reader:

- reconstruct the relevant structure, owners, and relationships without interpreting a taxonomy checklist;
- follow the representative scenario or change impact and explain a material failure or exception;
- understand why the proposed structure fits its drivers, what it costs, and what evidence would invalidate it;
- distinguish established facts, illustrative examples, proposals, and accepted decisions.

Revise the model or explanation when any relevant answer depends on an unexplained slogan, an empty section, or contradictory views. Use the owning Writer's template for the artifact-specific expression of these checks.

## Completion

Architecture reasoning is complete when the object and scope are explicit, relevant domains and viewpoints are accounted for, authoritative facts and state have one owner, material controls trace authority through evidence, failure and recovery behavior preserve invariants, and every accepted tradeoff names its cost and review trigger.
