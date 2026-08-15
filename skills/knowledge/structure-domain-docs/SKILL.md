---
name: structure-domain-docs
description: "Plan, scaffold, review, or revise the directory and navigation structure for one reusable domain knowledge set. Use for 领域知识目录, a new professional discipline or subject directory, a domain README and reading path, deciding which common domain documents and subdirectories are needed, splitting a large domain into subdomains, auditing coverage, or correcting mixed domain-document responsibilities without designing product, technical, company, business, or project structures."
---

# Structure Domain Docs

Give one domain a coherent knowledge map whose documents answer distinct reader questions and can grow without becoming a single monolith.

## Workflow

1. Apply `$structure-docs`.
2. Read repository instructions, the domain-root README, the target domain README when present, and representative sibling domains. Preserve healthy local naming, link, numbering, and navigation conventions.
3. **Confirm the domain boundary.** State the reusable professional subject, what changes its truth, and what it excludes. A domain claim should normally survive a company, product, implementation, customer, or project change. Surface a boundary conflict instead of silently absorbing business, product, technical, company, or project content.
4. Read `references/domain-structure-model.md`. Use its knowledge forms as a coverage model, not as a command to create every possible file.
5. **Inventory before designing.** Classify every existing or requested artifact by its primary reader question, change authority, and lifetime. Record missing knowledge forms, duplicate sources, mixed documents, broken reading paths, and unresolved placement choices.
6. **Choose the scale.** Keep a small domain flat by knowledge form. For a complex domain, keep shared scope, essence, and language at the root, then use stable subdomains as the next directory dimension. Within each subdomain, organize by knowledge form. Maintain one dimension per directory level.
7. **Choose what to materialize.** Create files and directories needed by current content or the user's explicit scaffold request. Do not create empty directories by default; show future knowledge forms as planned items in the domain README until content exists. If the user explicitly asks for a complete empty skeleton, create it without inventing document content.
8. **Build the map contract.** Read `../write-domain-doc/assets/domain-readme-template.md` when no healthy local README structure exists. Define the boundary, reading path, existing and planned knowledge, subdomain entries, and valid link targets, then route the README prose and every requested document body to `$write-domain-doc`.
9. **Present or apply the structure.** For a proposal, return the tree, each path's responsibility, planned versus existing items, and unresolved choices. For an authorized scaffold, create the directories and invoke `$write-domain-doc` for the README and requested document shells or bodies.
10. **Protect existing knowledge.** Obtain confirmation before moving, renaming, merging, or deleting existing files or directories. When authorized, update navigation, relative links, assets, and application bindings in the same change.
11. **Verify the result.** Confirm one primary home per artifact, coherent siblings at every level, valid local links, no accidental duplicate source, and no stale path after an applied migration.

## Boundaries

- Own the structure of one domain knowledge set: its root, subdomains, knowledge-form homes, coverage map, and reading-path requirements. Let `$write-domain-doc` own the domain README artifact.
- Let `$structure-docs` own repository-wide taxonomy, cross-class placement, and migrations involving domain, business, product, technical, project, or company roots.
- Let `$write-domain-doc` own the internal structure and content of common domain documents.
- Treat `{领域名称}本质.md` as the cognition anchor, not the container for every concept, mechanism, method, case, and reference.
- Preserve a smaller healthy structure. Expand only when a document has an independent reader question or several children need their own navigation boundary.

## Completion test

The work is complete only when:

- the domain boundary states what belongs, what does not, and what authority changes its truth;
- the structure distinguishes the domain map, cognition anchor, semantic model, causal explanations, reusable practices, evidence, and lookup material;
- small and complex domain rules have been applied deliberately;
- every created directory has current content or was explicitly requested as scaffold;
- the README exposes a valid reading path and does not link to nonexistent planned files;
- every artifact has one primary home and no sibling level mixes subdomains with knowledge forms without an explicit local rule;
- applied moves or renames have confirmation, updated links, and no stale paths.
