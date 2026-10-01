# Architecture Knowledge systems

## Inventory and plan

For a request to organize or complete a knowledge system, inventory existing entry points, views, object documents, components, engineering strategies, shared mechanisms and their links before writing. Read representative content, not only filenames. Distinguish an actual file from a README's planned or stale link. Preserve substantive material and healthy local terminology.

Map each file to one reader question, subject, parent/view, and knowledge responsibility. Identify gaps, duplicate authority and misplaced content. Reuse documents that already answer the question. Use `../../../methods/architecture-templates/templates.yaml` to select the entry, overview, index or substantive template for each needed artifact. Keep a coverage table in working notes; expose a gap in navigation only as an unlinked gap until its document exists.

Use the reference profile below when it fits the subject or the user requests it:

- Knowledge-set entry: purpose, boundaries, reading paths and view relationships.
- Domain: aggregate entry and concrete capability-domain documents.
- Overall reference architecture: integrated design and end-to-end consequences across the relevant views.
- Application: application structure, subsystem documents, components, engineering strategies, and genuinely shared mechanisms.
- Governance: decision authority, permitted actions, constraints, review and evidence.
- Runtime: operating conditions, load, failure and recovery behavior.

Assign navigation to knowledge-set entries, view overviews and collection indexes. Assign design conclusions to substantive architectures: the overall architecture owns cross-view consequences, an application architecture owns application decomposition, and a runtime architecture owns operating relationships. Let a combined navigation/design document use the substantive template and a short document map, with one location for each conclusion. Keep shared mechanisms in one owning location and link them from specialized strategies. Apply the cross-document scenario check in the Architecture Documents Method to establish that the views compose.

## Materialize within the request

For one document, update only that document and directly affected navigation. For a system-building request, create the agreed or evidence-backed set end to end; do not require separate Public Skill invocations for each artifact. When a topology change is explicitly authorized, migrate with an old-to-new map and repair inbound/outbound links. Preserve unrequested content and avoid destructive replacement; if migration authorization is absent, report the proposed move while completing safe additions or revisions within scope.

Keep components below their owning subsystem when that convention exists. Add an engineering strategy for a recurring hard problem with real tradeoffs, not mechanically for every component. Put implications of another view next to the local design and link that view's governing explanation rather than copying it.

Adapt reference examples to the actual subject. Do not copy CEX-specific actors, stages, invariants, or folder names into unrelated knowledge systems. Apply the shared Architecture Reasoning Method before selecting a specialist template; retained templates do not authorize a new category or unsolicited document split. Keep small topics within their parent architecture; create a separate document only for independently useful detail. Treat remaining uncovered responsibilities as explicit extensions instead of silently misclassifying them.

## Completion

Complete a knowledge-system request when the requested scope has a coherent entry, each materialized file has a distinct responsibility and appropriate template, parent/child and cross-view links resolve, shared explanations have one owner, and unresolved coverage is explicit without empty placeholder documents. Complete a single-document request when it fits the set and its directly affected links are repaired, or stands alone when requested.
