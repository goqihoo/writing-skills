# Technical reasoning method

Use this method inside any Public Skill that must decide what belongs in one company's Technical Documentation Set and which authority owns each fact.

## Company technical scope

Name the company, governance authority, and Technical Landscape in scope. The Technical Landscape is the company-specific view of technical capabilities, platforms, systems, ownership, dependencies, and lifecycle; it is not a code repository or one delivery project's design.

## Authority tests

| Candidate material | Primary authority |
| --- | --- |
| Reusable technical concept, pattern, or method not tied to one company | Technical Knowledge |
| Company strategy, landscape, governance, standards, and high-level system profiles | Technical Documentation |
| Detailed boundaries and behavior of one concrete system | System Architecture |
| Customer, contract, delivery plan, tasks, status, and acceptance | Project Documentation |
| Schemas, protocols, configuration, code behavior, migrations, and tests | Machine Authority |

Keep one canonical owner and link across boundaries.

## Responsibility classification

- **Stable Responsibility:** persists for the accepted company technical scope and receives a default directory and Responsibility README.
- **Type Extension:** appears only when independent ownership, governance, or navigation is proven.
- **Event Collection:** appears with the first real decision, exception, or incident and only beneath an existing parent responsibility.

The Stable Responsibilities are `Strategy/`, `Architecture/`, `Systems/`, and `Governance/`. The Type Extensions are `Platforms/`, `Engineering/`, `Data/`, `Security/`, `Quality/`, and `Operations/`. Event Collections are `Architecture/Decisions/`, `Governance/Exceptions/`, and `Operations/Incidents/`.

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
- Each directory decision is classified as Stable Responsibility, Type Extension, or Event Collection.
- Detailed Machine Authority and System Architecture are linked, not copied.
- Unresolved ownership and review triggers remain visible.
