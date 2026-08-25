# System Architecture method

Use this method for System Architecture and proportionally for Subsystem Architecture. Lock the Architecture Object to the named System or Subsystem, set the Authority Level to System or Subsystem, and keep the direct architecture document as the coherent entry point.

## Coverage contract

Address the relevant evidence for:

- object, purpose, scope, stable responsibilities, and non-goals;
- linked Business and Product context, external actors, and reader-relevant journeys without redefining their authority;
- Data meaning, information authority, lifecycle, ownership, consistency, lineage, and retention where material;
- Application context, boundaries, Applications, Subsystems, internal responsibility splits, authoritative state, and dependency direction;
- interfaces, commands, events, queries, and cross-boundary contracts;
- normal flows and failure semantics, including duplicate, timeout, ordering, partial, stale, conflicting, and unknown outcomes;
- Technology platforms, infrastructure, storage, messaging, networks, environments, and constraints where they shape the System;
- Security assets, identities, trust boundaries, threats, protection, detection, response, and evidence where material;
- Governance permissions, controlled commands, last responsible control points, decision authority, exceptions, and durable evidence;
- Deployment Architecture responsibilities, deployment units, placement, network, topology, and failure domains where material;
- Runtime dependencies, load, degradation, observability, replay, recovery, and failover behavior;
- principles, constraints, material decisions, alternatives, and accepted costs;
- validation, operating evidence, fitness checks, and review triggers;
- current facts, accepted target direction, evaluated proposals, compatibility, migration, and evolution boundaries;
- downstream Subsystem Architecture, interface definitions, deployments, runbooks, code repositories, Project Technical Design, and Machine Authority links.

Use domain, application, governance, and runtime correctness as final checks. Omit an area only when it is genuinely irrelevant, and make material evidence gaps explicit. Do not force one heading or supporting file per domain or viewpoint.

## Supporting files

Split a supporting file only when it has an independent reader task, authority, change cycle, and navigation value. One invocation may update the main architecture document and directly affected supporting files; do not rewrite unrelated files.

## Completion

The architecture family is complete when the named Architecture Object and Scope are explicit, the direct System or Subsystem Architecture remains a coherent entry point, relevant domains and viewpoints are evidence-backed, Deployment Architecture and Runtime behavior are distinguishable, authority links replace implementation duplication, and omissions, open decisions, validation, and evolution triggers are explicit.
