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

## Completion

Architecture reasoning is complete when the object and scope are explicit, relevant domains and viewpoints are accounted for, authoritative facts and state have one owner, material controls trace authority through evidence, failure and recovery behavior preserve invariants, and every accepted tradeoff names its cost and review trigger.
