# Technical reasoning method

Use this method inside any Public Skill that must decide what belongs in one company's Technical Documentation Set and which authority owns each fact.

## Company technical scope

Name the company, governance authority, and Technical Landscape in scope. The Technical Landscape is the company-specific view of technical capabilities, platforms, systems, ownership, dependencies, and lifecycle; it is not a code repository or one delivery project's design.

## Authority tests

| Candidate material | Primary authority |
| --- | --- |
| Reusable technical concept, pattern, or method not tied to one company | Technical Knowledge |
| Company strategy, landscape, governance, standards, Registered System profiles, System Architecture, and Subsystem Architecture | Technical Documentation |
| Customer, contract, delivery plan, tasks, status, and acceptance | Project Documentation |
| Schemas, protocols, configuration, code behavior, migrations, and tests | Machine Authority |

Keep one canonical owner and link across boundaries.

## Responsibility classification

- **Stable Responsibility:** persists for the accepted company technical scope and receives a default directory and Responsibility README.
- **Type Extension:** appears only when independent ownership, governance, or navigation is proven.
- **Event Collection:** appears with the first real decision, exception, or incident and only beneath an existing parent responsibility.

The logical Stable Responsibilities are Strategy, Architecture, Systems, and Governance. Reuse the documentation set's language rather than imposing directory names. Type Extensions may include Platform, Engineering, Data, Security, Quality, and Operations when cross-System responsibility justifies them. Event Collections contain accepted Architecture Decisions, Governance Exceptions, or Operations Incidents beneath an existing parent.

## System admission and architecture ownership

Register a System only when evidence supports its stable name, responsibility boundary, owner, and lifecycle status. Preserve many-to-many Product-System relationships. Give every Registered System a System Responsibility README and System Architecture. Treat System Architecture and justified Subsystem Architecture as Technical Documentation; keep Project Technical Design and Machine Authority separate and linked.

Require an architecture family to distinguish current facts, accepted target direction, evaluated proposals, compatibility and migration boundaries, validation and operating evidence, and explicit review triggers. The direct architecture document remains the coherent entry point even when justified supporting files exist.

Use Company, System, and Subsystem as Architecture Levels. Place an Architecture Decision at the narrowest governing level and link it upward when needed.

## Ownership tests

For every responsibility, identify:

- accountable owner and decision authority;
- scope and exclusions;
- readers and decisions served;
- canonical sources and downstream authorities;
- independent governance or navigation need;
- review, split, merge, or retirement triggers.

Do not infer a company responsibility from a team name or tool category alone.

## Technical Assessment persistence

Persist a Technical Assessment only when disputed scope, a Type Extension, an audit finding, or an approved migration needs durable traceability. Do not create it as a default scaffold document.

## Completion checks

- Company technical scope and Technical Landscape are named.
- Every material has one authority scope and owner.
- Each materialization decision is classified as Stable Responsibility, Registered System, Type Extension, or Event Collection.
- System Architecture remains Technical Documentation; Project Technical Design and detailed Machine Authority are linked, not copied.
- Unresolved ownership and review triggers remain visible.
