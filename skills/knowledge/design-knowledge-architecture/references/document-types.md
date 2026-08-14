# Architecture knowledge document types

Choose one primary type. Create separate notes when two types have independent readers, decisions, update cycles, or validation.

| Reader question | Type |
|---|---|
| What capability, lifecycle, and invariants define the problem? | Domain architecture |
| How is a whole system divided into authoritative owners? | Application architecture |
| How does one subsystem own state and collaborate? | Application subsystem |
| What stable responsibility and contracts define one component? | Component |
| How should a recurring hard engineering problem be handled? | Engineering strategy |
| Who may act, through what controlled path, with what evidence? | Governance architecture |
| How does the system deploy, fail, recover, observe, and scale? | Runtime architecture |
| How does one material control become enforceable across views? | Control architecture |
| How does a reusable technical mechanism work and vary? | System mechanism |

## Required questions by type

### Domain architecture

Define scope, actors, concepts, lifecycle, invariants, capability boundaries, cross-system scenarios, control implications, and evolution.

### Application architecture

Define subsystem boundaries, responsibilities, authoritative state, commands, events, queries, consistency, cross-system flows, and aggregate decisions.

### Application subsystem

Define owned and excluded responsibility, state model, components, contracts, success and failure flows, rules, evidence, validation, and evolution.

### Component

Define one stable responsibility, callers, dependencies, state, interface guarantees, failure behavior, validation, and replacement boundary.

### Engineering strategy

Define the recurring hard problem, conflicting drivers, option families, selected reusable guidance, unsafe failure modes, validation, and review triggers. Do not create strategy notes from an ordinary component list.

### Governance architecture

Define actors, authority, scope, controlled commands, approval, duty separation, policy version, evidence, exceptions, emergency behavior, bypass prevention, and validation.

### Runtime architecture

Define topology options, dependency shape, failure domains, degradation, observability, recovery, replay, rebuild, capacity, performance, data placement, and evolution.

### Control architecture

Trace one control objective through protected value, owners, control point, explicit failure behavior, evidence, validation, bypass paths, and projection into the four owning views.

### System mechanism

Define intended result, objects and state, preconditions, trigger, success and failure paths, guarantees, option families, limits, and validation independent of one business domain.

## Knowledge-base shape

Use an overview only when it provides navigation or aggregate judgments not owned by child notes:

```text
README or architecture overview
├── Domain notes
├── Application system and subsystem notes
│   ├── Component notes
│   └── Engineering strategy notes
├── Governance notes
└── Runtime notes
```

Split a note only when the child has its own reusable boundary, decisions, flows, validation, or evolution.
