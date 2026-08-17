---
name: structure-docs
description: Plan, review, or revise how a documentation set is divided into directories and files. Use when defining content boundaries, choosing where documents belong, designing a knowledge-base structure, proposing file and directory names, or detecting mixed responsibilities, taxonomy gaps, duplicate sources, and structural drift across business, domain, product, company, project, and technical content.
disable-model-invocation: true
---

# Structure Docs

Give every document one stable home and make each directory boundary explainable.

## Workflow

1. Apply `$write-doc` to the structure proposal and any README or navigation text produced.
2. Read repository instructions and the README, index, or map files that define the existing structure. Preserve explicit local rules over this skill's defaults.
3. Establish the scope and requested action: plan a new structure, place new material, review an existing structure, propose a migration, or apply an approved migration.
4. Read `references/content-boundaries.md`. Classify the relevant material by subject, change authority, lifetime, and reader action. Record a taxonomy gap when a valid class has no honest home instead of forcing it into the nearest directory.
5. Read `references/structure-patterns.md`. Identify the organizing dimension used at each level, then design the smallest directory and file structure that preserves those dimensions.
6. Give each directory a boundary contract: what it owns, what it excludes, where excluded material belongs, and the test used to decide placement.
7. Give each document one primary home. Use links for secondary relevance and split a document only when its parts have independently changing authority, lifetime, or reader purpose.
8. Present the proposed tree, important placement decisions, unresolved boundaries, and—for an existing structure—an exact old-to-new mapping. Separate observed structural facts from interpretation and recommendations.
9. Obtain confirmation before moving, renaming, merging, or deleting existing material. When authorized, update affected navigation, relative links, assets, and application bindings in the same change.
10. Verify every changed target, search for stale paths and names, and confirm that each affected document has one primary owner.

## Boundaries

- Own documentation-set information architecture: content classes, directory responsibilities, file placement, naming structure, navigation, and migration maps.
- Let the relevant artifact skill own document purpose and internal reasoning: `$write-knowledge` for reusable Knowledge, `$write-prd` for product requirements, `$write-architecture-knowledge` for reusable Architecture Knowledge, and `$write-technical-architecture` for company Technical Architecture.
- Treat software packages, runtime components, and deployment topology as technical architecture when the task is to design the system rather than organize its documentation.
- Preserve a healthy local taxonomy. Recommend a change only when evidence shows mixed dimensions, unclear ownership, duplication, an unrepresented content class, or a structure that prevents readers from finding the authoritative source.

## Output

Return only the forms needed for the request:

- a proposed directory tree with boundary explanations;
- a recommended path and filename for new material;
- a structure audit with observed problems and recommended corrections;
- an old-to-new mapping with affected links for a migration;
- applied changes and validation results when implementation was requested.

The work is complete when every item in scope has one explainable primary home, sibling directories use a coherent organizing dimension, taxonomy gaps and unresolved choices remain visible, and every applied move has valid navigation and links with no stale path left behind.
