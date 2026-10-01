# Architecture Knowledge systems

## Inventory and plan

For a request to organize or complete a knowledge system, inventory existing entry points, views, object documents, components, engineering strategies, shared mechanisms and their links before writing. Read representative content, not only filenames. Distinguish an actual file from a README's planned or stale link. Preserve substantive material and healthy local terminology.

Map each file to one reader question, subject, parent/view, and knowledge responsibility. Identify gaps, duplicate authority and misplaced content. Reuse documents that already answer the question. Use `architecture-templates.yaml` to select the entry, overview, index or substantive template for each needed artifact. Keep a coverage table in working notes; expose a gap in navigation only as an unlinked gap until its document exists.

Use the reference profile below when it fits the subject or the user requests it:

- Knowledge-set entry: purpose, boundaries, reading paths and view relationships.
- Domain: aggregate entry and concrete capability-domain documents.
- Application: overall reference architecture, subsystem documents, components, engineering strategies, and genuinely shared mechanisms.
- Governance: aggregate entry and independently useful security, compliance, risk, control-command and audit-evidence topics.
- Runtime: aggregate entry and deployment, network, runtime-state/messaging, observability, resilience, and capacity/performance topics.

Distinguish a navigational Runtime overview from substantive Runtime Architecture: the former owns the document map, the latter owns operating relationships and cross-topic judgments. Use the same distinction for other views. Keep shared mechanisms in one owning location and link them from specialized strategies.

## Materialize within the request

For one document, update only that document and directly affected navigation. For a system-building request, create the agreed or evidence-backed set end to end; do not require separate Public Skill invocations for each artifact. When a topology change is explicitly authorized, migrate with an old-to-new map and repair inbound/outbound links. Preserve unrequested content and avoid destructive replacement; if migration authorization is absent, report the proposed move while completing safe additions or revisions within scope.

Keep components below their owning subsystem when that convention exists. Add an engineering strategy for a recurring hard problem with real tradeoffs, not mechanically for every component. Put implications of another view next to the local design and link that view's governing explanation rather than copying it.

Adapt reference examples to the actual subject. Do not copy CEX-specific actors, stages, invariants, or folder names into unrelated knowledge systems. Treat data or integration topics not covered by a dedicated template as explicit extensions; use a relevant mechanism or architecture template only if its responsibilities fit, otherwise propose the missing template instead of silently misclassifying the topic.

## Completion

Complete a knowledge-system request when the requested scope has a coherent entry, each materialized file has a distinct responsibility and appropriate template, parent/child and cross-view links resolve, shared explanations have one owner, and unresolved coverage is explicit without empty placeholder documents. Complete a single-document request when it fits the set and its directly affected links are repaired, or stands alone when requested.
