# <System or Change> Technical Design

## Document status

| Field | Value |
|---|---|
| Owner | <Name or role> |
| Status | Draft / In review / Approved / Superseded |
| Last updated | <Date> |
| Related requirements | <Link> |

## Context

Describe the current system behavior, the required change, and the evidence or decisions that establish the need.

## Goals and non-goals

### Goals

- <Required technical or product result>

### Non-goals

- <Explicitly excluded concern>

## Drivers and constraints

| Driver or constraint | Why it changes the design | Source |
|---|---|---|
| <Requirement, quality goal, policy, platform fact, or deadline> | <Structural effect> | <Link or decision> |

## Current state

Describe only the current behavior needed to understand the change.

## Representative end-to-end scenario

Trace one realistic request, event, or state change before introducing the component view.

1. <Actor or component receives an input>
2. <State or data changes>
3. <Another component observes or acts>
4. <Caller, user, or operator sees the result>

## Proposed design

### Responsibilities and boundaries

| Component or owner | Responsibility | Does not own |
|---|---|---|
| <Component> | <Behavior and state owned> | <Explicit boundary> |

### Runtime flows

Describe the main success path and link it to the representative scenario.

### Interfaces and contracts

| Interface | Caller and provider | Input | Output | Errors and guarantees |
|---|---|---|---|---|
| <API, event, job, or library boundary> | <Parties> | <Semantics> | <Semantics> | <Observable behavior> |

### Data and state

| Data or state | Owner | Source of truth | Lifecycle and invariants |
|---|---|---|---|
| <Object> | <Owner> | <System or store> | <Creation, change, retention, invariant> |

## Failure, recovery, and degraded operation

| Failure | Observable effect | Detection | Recovery or containment |
|---|---|---|---|
| <Timeout, retry, partial success, concurrency conflict, dependency failure, or corrupt state> | <Effect> | <Signal> | <Action> |

## Security and privacy

- <Trust boundary, access control, sensitive data, abuse case, or audit requirement>

## Observability and operations

- **Signals:** <Metrics, logs, traces, events>
- **Operational action:** <Diagnosis, repair, replay, reconciliation, or capacity change>

## Deployment, migration, and compatibility

1. <Safe rollout step>
2. <Migration or compatibility step>
3. <Cutover and cleanup>

**Rollback condition:** <Observable trigger>

**Rollback action:** <Recoverable action>

## Validation

| Claim or risk | Validation method | Acceptance threshold |
|---|---|---|
| <Behavior, performance, resilience, security, or migration claim> | <Test, experiment, review, or production signal> | <Pass condition> |

## Decisions and alternatives

| Decision | Selected option | Alternatives | Rationale | Separate record |
|---|---|---|---|---|
| <Decision> | <Choice> | <Real alternatives> | <Drivers and tradeoffs> | <Link if needed> |

## Risks, assumptions, and open questions

| Type | Item | Owner | Resolution or trigger |
|---|---|---|---|
| Risk / Assumption / Question | <Item> | <Role> | <Action, evidence, or date> |

## Review checklist

- [ ] Requirements map to the design or explicit non-goals.
- [ ] The main and failure paths are traceable through interfaces, data, and state.
- [ ] Ownership, rollout, rollback, observability, and validation are implementable.
