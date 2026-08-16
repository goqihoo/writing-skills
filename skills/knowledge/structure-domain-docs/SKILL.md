---
name: structure-domain-docs
description: Plan, audit, scaffold, or migrate the directory, coverage map, navigation, and materialization of one reusable domain knowledge set after its domain boundary has been assessed.
disable-model-invocation: true
---

# Structure Domain Docs

Turn an accepted domain boundary and real material into a knowledge map that can grow without changing its organizing logic.

## Workflow

1. Apply `$reason-domain`, `$structure-docs`, and `$write-doc`.
2. **Confirm the action and authority.** Classify the request as a proposal, audit, scaffold, or approved migration. Planning and audit are read-only. Obtain confirmation before moving, renaming, merging, deleting, or overwriting existing knowledge.
3. **Read the local system.** Read repository instructions, the domain-root README, the target README when present, and one or two healthy sibling domains. Record naming, link, numbering, language, and navigation conventions that the result must preserve.
4. **Consume the Domain Assessment.** Require an `Accept` decision with a supported boundary, exclusions and destinations, relationships, subdomain decisions, and unresolved questions from `$reason-domain`. For `Do not accept`, route cross-class restructuring to `$structure-docs`. For `Needs evidence` or an absent assessment, return a ready-to-type explicit invocation for `$reason-domain $write-doc` and stop before proposing a tree.
5. **Inventory before designing.** Read `references/domain-structure-model.md`, `../write-domain-doc/references/domain-document-types.md`, and `assets/domain-inventory-template.md`. Account for every existing and requested artifact by reader question, change authority, lifetime, content class, domain document type, current state, primary home, and structural issue.
6. **Choose the topology.** Use the assessed parent-or-child relationships and the topology tests in the structure model. Keep a valid small domain flat. Create subdomain directories only when both a real parent-child boundary and a current navigation need exist. Use links for related domains and handoffs.
7. **Choose materialization.** Create only files and directories required by current content or an explicit full-scaffold request. Record absent knowledge forms as planned coverage without linking to nonexistent files. Upgrade a file to a directory only when several independent documents or a stable internal reading path need it.
8. **Specify the map contract.** Read `../write-domain-doc/assets/domain-readme-template.md` when no healthy local README exists. Define the boundary statement, current and planned coverage, valid links, subdomain entries, default learning path, and task-based entry paths. Let `$write-domain-doc` own the README body.
9. **Present or apply the structure.** Use `assets/domain-structure-plan-template.md`. For an authorized scaffold, create the approved directories and files. When a README or document body is required and `$write-domain-doc` was not explicitly invoked, leave the body ungenerated and return a ready-to-type explicit invocation for `$write-domain-doc $reason-domain $write-doc`.
10. **Apply approved migrations atomically.** Record exact old-to-new paths, affected Markdown links, assets, and application bindings before editing. Update every approved path and reference in the same change.
11. **Verify the result.** Confirm one primary home per material, one organizing dimension per sibling level, no unsupported subdomain, no accidental duplicate authority, no unrequested empty directory, valid local links, no link to planned content, and no stale path after migration.

## Boundaries

- Own the structure of one accepted domain knowledge set: inventory, topology, materialization, coverage, navigation requirements, scaffolding, and approved migration.
- Let `$reason-domain` own admission, domain boundary, relationships, subdomain validity, high-level content ownership, maturity, and review triggers.
- Let `$write-domain-doc` own the internal structure and content of the domain README and every other common domain document.
- Let `$structure-docs` own repository-wide taxonomy and placement across business, domain, product, company, project, technical, and reference roots.
- Treat `{领域名称}本质.md` as a cognition anchor, not a container for every knowledge responsibility.

## Completion test

The work is complete only when every assessed material has a state and primary home, the topology follows evidenced relationships, every materialized path has a current purpose, the README contract exposes only valid links and honest planned coverage, destructive changes have explicit approval and complete path mappings, and the verification reports all unresolved gaps.
