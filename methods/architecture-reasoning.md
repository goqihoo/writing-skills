# Architecture reasoning method

Use this method inside any Public Skill that must reason about architectural boundaries, ownership, controls, failure, options, evolution, or validation.

## Levels and views

Separate the **Architecture Level** from the **Architecture View**:

- Company, System, and Subsystem are Architecture Levels.
- Domain, Application, Governance, and Runtime are Architecture Views that can be applied at any level.

Use the four views as coverage checks. Do not turn them into directory levels, mandatory documents, or fixed headings.

At System or Subsystem level, test responsibility and non-goals, context and boundaries, state and contracts, normal and failure behavior, authority and controls, runtime failure and recovery, decisions and accepted costs, validation, and evolution. Keep Project Technical Design and Machine Authority linked rather than copied.

## Reasoning loop

Apply this loop within each relevant view:

```text
Context → Drivers → Scenarios and flows → Risks → Decisions → Validation
```

| Step | Required result |
|---|---|
| Context | Facts, constraints, stakeholders, unknowns, and change assumptions |
| Drivers | Invariants, ownership needs, authority, runtime conditions, and ranked qualities |
| Scenarios and flows | Concrete success, failure, replay, recovery, and evolution paths |
| Risks | Unsafe assumptions, bypasses, inconsistency, overload, and evidence gaps |
| Decisions | Boundaries, ownership, contracts, controls, patterns, or option families |
| Validation | Tests, operating evidence, and signals that prove or challenge each judgment |

## Four Architecture Views

| View | Owns | Must not become |
|---|---|---|
| Domain | Capability meaning, facts, lifecycle, and invariants | Component or deployment design |
| Application | Authoritative state, subsystem responsibility, and contracts | Full domain meaning, governance platform, or topology |
| Governance | Authority, policy, controlled commands, evidence, and exceptions | Owner or executor of business state |
| Runtime | Deployment, failure domains, observability, recovery, and scale | Source of business rules or state ownership |

Use this dependency:

```text
Domain defines facts and invariants
→ Application owns state and contracts
↔ Governance constrains authority and evidence
↔ Runtime constrains failure and recovery
```

Application is the structural anchor. Introduce hard Governance and Runtime constraints early, then detail them after ownership stabilizes.

## Architecture judgment

Distinguish:

- **Constraint:** cannot be violated in the stated context.
- **Quality:** can improve or degrade and must be prioritized.
- **Principle:** guides later choices.
- **Pattern:** a reusable structural response.
- **Decision:** binds the current context and records accepted cost.
- **Validation:** evidence that tests a named judgment.

Pressure-test each choice for **fit**, **simplicity**, and **evolution**.

## Control trace

For every material control, trace:

```text
objective and unsafe outcome
→ protected value and capability
→ policy, decision, state, and execution owners
→ last responsible control point
→ allow, reject, hold, limit, degrade, repair, or fail-closed behavior
→ durable evidence
→ design and operating validation
```

Test missing, stale, conflicting, duplicate, delayed, partially applied, and unknown outcomes. “Log and continue” is not a safe default.
