# <System or Change> Delivery Architecture

## Document status

| Field | Value |
|---|---|
| Owner | <Name or role> |
| Status | Draft / In review / Approved / Superseded |
| Last updated | <Date> |
| Related requirements | <Link> |

## Context

Describe the current system behavior, the required change, and the evidence or decisions that establish the need.

## Goals, scope, and non-goals

### Goals

- <Required technical or product result>

### Non-goals

- <Explicitly excluded concern>

## Drivers and constraints

| Driver or constraint | Why it changes the design | Source |
|---|---|---|
| <Requirement, quality goal, policy, platform fact, or deadline> | <Structural effect> | <Link or decision> |

## Representative end-to-end scenario

Trace one realistic request, event, or state change before introducing the component view.

1. <Actor or component receives an input>
2. <State or data changes>
3. <Another component observes or acts>
4. <Caller, user, or operator sees the result>

## Architecture

### System context and boundaries

Describe users, the system boundary, external systems, and information crossing each boundary.

### Responsibilities and authoritative state

| Owner or subsystem | Responsibility | Authoritative state | Does not own |
|---|---|---|---|
| <Owner> | <Behavior> | <Facts or state> | <Boundary> |

### Interfaces and contracts

| Contract | Caller and owner | Semantics | Guarantees and failure behavior |
|---|---|---|---|
| <Command, event, query, or job> | <Parties> | <Meaning> | <Ordering, idempotency, timeout, compatibility, or recovery> |

### Main and failure flows

Trace the primary success path, then timeout, retry, duplicate, stale, partial, conflicting, and unknown outcomes that matter.

## Failure, recovery, and degraded operation

| Failure | Observable effect | Detection | Recovery or containment |
|---|---|---|---|
| <Timeout, retry, partial success, concurrency conflict, dependency failure, or corrupt state> | <Effect> | <Signal> | <Action> |

## Governance, security, and evidence

| Control objective | Authority and owner | Control point and failure behavior | Evidence and validation |
|---|---|---|---|
| <Unsafe outcome to prevent> | <Who decides and executes> | <Where and how enforced> | <Durable evidence and test> |

## Runtime and operations

- **Deployment and failure domains:** <Placement and isolation>
- **Signals:** <Metrics, logs, traces, and evidence>
- **Recovery:** <Repair, replay, reconciliation, failover, or restore>
- **Capacity and degradation:** <Limits and safe behavior>

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

## Delivery check

- [ ] Requirements map to the design or explicit non-goals.
- [ ] The main and failure paths are traceable through ownership, contracts, controls, and state.
- [ ] Rollout, rollback, operations, and validation are implementable.
