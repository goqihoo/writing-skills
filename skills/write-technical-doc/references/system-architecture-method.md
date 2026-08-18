# System Architecture method

Use this method for System Architecture and proportionally for Subsystem Architecture at the narrower Architecture Level. Keep the direct architecture document as the coherent entry point.

## Coverage contract

Address the relevant evidence for:

- purpose, scope, stable responsibilities, and non-goals;
- external actors, context, boundaries, Applications, Subsystems, and internal responsibility splits;
- authoritative state, data ownership, and consistency boundaries;
- interfaces, commands, events, queries, and cross-boundary contracts;
- normal flows and failure semantics, including duplicate, timeout, ordering, partial, and unknown outcomes;
- permissions, controlled commands, last responsible control points, and durable evidence;
- deployment responsibilities, runtime dependencies, failure domains, degradation, recovery, and observability;
- principles, constraints, material decisions, alternatives, and accepted costs;
- validation, operating evidence, fitness checks, and review triggers;
- current facts, accepted target direction, evaluated proposals, compatibility, migration, and evolution boundaries;
- downstream Subsystem Architecture, interface definitions, runbooks, code repositories, Project Technical Design, and Machine Authority links.

Omit an area only when it is genuinely irrelevant, and make material evidence gaps explicit.

## Supporting files

Split a supporting file only when it has an independent reader task, authority, change cycle, and navigation value. One invocation may update the main architecture document and directly affected supporting files; do not rewrite unrelated files.

## Completion

The architecture family is complete when the direct System or Subsystem Architecture remains a coherent entry point, relevant coverage is evidence-backed, authority links replace implementation duplication, and omissions, open decisions, validation, and evolution triggers are explicit.
