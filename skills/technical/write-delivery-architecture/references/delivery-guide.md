# Architecture delivery guide

Select only sections that help stakeholders review, implement, or operate the architecture.

| Section | Decision value |
|---|---|
| Context and goals | Problem, scope, requirements, quality goals, and stakeholders |
| Constraints | Technical, organizational, business, security, and regulatory limits |
| System context | Boundary, external actors, dependencies, and exchanged information |
| Strategy | The few choices that explain the rest of the design |
| Building blocks | Responsibilities, authoritative state, and collaboration |
| Runtime | Success, failure, consistency, evidence, and recovery paths |
| Deployment | Placement, isolation, failure domains, and recovery when location matters |
| Cross-cutting concerns | Controls, security, observability, compatibility, and data handling |
| Decisions | Accepted choices, alternatives, rationale, costs, validation, status, and review triggers |
| Validation | Measurable quality scenarios and fitness checks |
| Risks | Trigger, impact, mitigation, and owner |

Minimum implementation handoff:

- system boundary and dependencies;
- top-level owners and authoritative state;
- command, event, query, and compatibility semantics;
- important success, failure, replay, and recovery behavior;
- authority, control points, evidence, and observability;
- accepted decisions, risks, rollout, rollback, and measurable validation.

Use prose for reasoning, tables for repeated fields, and diagrams only for relationships that prose cannot carry clearly. Do not leave empty template scaffolding.
