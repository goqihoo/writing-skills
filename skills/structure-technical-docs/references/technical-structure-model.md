# Technical Documentation structure model

Technical Documentation belongs to one named company. Use initial capitals for these company-documentation directories; do not apply this convention to code repositories.

## Stable Responsibilities

Create beneath `{Company}/Technical/`:

- `Strategy/` — technical direction, roadmap, investment choices, and constraints.
- `Architecture/` — company Technical Architecture, principles, boundaries, relationships, and evolution.
- `Systems/` — system landscape and high-level System Profiles linking downstream authority.
- `Governance/` — decision rights, operating model, standards, and governance rules.

Give `Technical/` and every Stable Responsibility a Responsibility README.

## Type Extensions

Create only when independent ownership, governance, or navigation is proven:

- `Platforms/`
- `Engineering/`
- `Data/`
- `Security/`
- `Quality/`
- `Operations/`

## Event Collections

Create only with the first real event and when the parent responsibility exists:

- `Architecture/Decisions/` — accepted company architecture decisions.
- `Governance/Exceptions/` — approved deviations from technical governance.
- `Operations/Incidents/` — incident records and reviews; materialize only when `Operations/` is justified.

The first real event creates the Event Collection; a default scaffold never creates one. An event cannot justify a missing parent responsibility by itself.

## Materialization rules

- **Stable Responsibility:** create by default for the accepted company technical scope.
- **Type Extension:** create only with ownership, governance, or navigation evidence.
- **Event Collection:** create with the first real event under an existing parent responsibility.

A Responsibility README records responsibility, owner, boundary, real current navigation, and external authority links. It does not contain invented body text or copy downstream detail.

## Authority boundaries

System Profiles link detailed System Architecture, interface definitions, deployments, configuration, schemas, code, tests, and runbooks. Technical Documentation retains company purpose, ownership, lifecycle, relationships, governance state, and human navigation.

## Migration contract

Before an approved migration, record exact old and new paths, links, assets, external bindings, supersession, and approval. Verify no duplicate authority, broken link, orphaned asset, or stale old path remains.
