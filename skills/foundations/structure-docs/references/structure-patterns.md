# Structure Patterns

## Use one dimension per level

Choose one stable question for siblings at the same level. Common dimensions include:

- fact ownership or content class at the repository root;
- business lifecycle inside a business directory;
- capability inside a product directory;
- system or subsystem inside a technical directory;
- customer or initiative inside a project directory;
- discipline or subject inside a domain directory.

Do not place a business process, professional discipline, software system, and company name as peers unless a documented local rule deliberately uses another coherent dimension.

## Choose directories and files

Create a directory when the collection has its own stable boundary, navigation need, or several independently useful children. Keep a file when one artifact answers one primary reader question and has no meaningful child navigation.

Use a directory README to state:

- what the directory owns;
- what it excludes and where that material belongs;
- how to decide whether new material belongs;
- links to its current children.

Do not use README as a holding area for unclassified material.

Split by independent change, not by length alone. Keep supporting examples with the artifact whose claim they explain unless the examples have their own reusable reader purpose.

## Name for stable retrieval

Follow local language, numbering, capitalization, and reserved-name conventions. Prefer names that identify the enduring subject or reader task. Preserve official product names and technical identifiers.

Avoid version labels such as `final`, `new`, or `v2` when lifecycle metadata or source control owns version history. Preserve source filenames when traceability is a stated requirement.

## Plan a migration

For every proposed move or rename, record:

- exact old path;
- exact new path;
- reason and boundary affected;
- inbound Markdown links and navigation entries;
- colocated assets or application bindings;
- terms or old paths to search after the move.

Propose first. Apply only when the request authorizes repository changes and the mapping is complete.

After applying a migration, verify that every local Markdown target and application binding exists, navigation exposes the new location, and searches find no stale path, retired term, or accidental duplicate source.
