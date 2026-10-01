# [Component Reference Architecture]

**Status:** [Draft / Reviewed / Superseded]

**Verified:** [Date and evidence baseline]

## Responsibility and boundary

**Owns:** [Responsibilities]

**Does not own:** [Excluded responsibilities]

**Used by:** [Callers]

**Depends on:** [Dependencies]

## Inputs, outputs and contracts

| Contract | Direction | Source / target | Meaning | Failure / compatibility semantics |
| --- | --- | --- | --- | --- |
| [Contract] | [Direction] | [Source / target] | [Meaning] | [Failure / compatibility semantics] |

## Internal ownership model

[Figure: modules, owned state and dependencies]

| Internal element | Responsibility | State owner | Rebuild source |
| --- | --- | --- | --- |
| [Internal element] | [Responsibility] | [State owner] | [Rebuild source] |

## Lifecycle

[Figure: lifecycle transitions]

| Transition | Precondition | Effect | Completion condition |
| --- | --- | --- | --- |
| [Transition] | [Precondition] | [Effect] | [Completion condition] |

## Core behavior

[Algorithm or interaction, inputs, state transitions, result and invariant]

## Governed behavior

[Protected actions, enforcement points, authority and evidence]

## Failure and recovery

| Failure | Containment | Retry / replay semantics | Recovery evidence |
| --- | --- | --- | --- |
| [Failure] | [Containment] | [Retry / replay semantics] | [Recovery evidence] |

## Design variants

| Pattern / variant | Conditions | Benefits | Costs / failure limits | Change trigger |
| --- | --- | --- | --- | --- |
| [Pattern / variant] | [Conditions] | [Benefits] | [Costs / failure limits] | [Change trigger] |

## Validation

| Judgment | Evidence or planned check | Pass / challenge signal | Evidence limits |
| --- | --- | --- | --- |
| [Judgment] | [Evidence or planned check] | [Pass / challenge signal] | [Evidence limits] |

## Extension and replacement

[Extension points, compatibility, substitutability, replacement conditions]

## Project extraction

| Reusable conclusion | Applies when | Project must decide / verify | Unsuitable when |
| --- | --- | --- | --- |
| [Reusable conclusion] | [Applies when] | [Project must decide / verify] | [Unsuitable when] |

## Related documents

| Related document / source | Relationship | Link |
| --- | --- | --- |
| [Related document / source] | [Relationship] | [Link] |
