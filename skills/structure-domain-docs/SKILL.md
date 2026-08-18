---
name: structure-domain-docs
description: Plan, audit, scaffold, or migrate the directory, coverage map, navigation, and materialization of one reusable domain knowledge set after its domain boundary has been assessed.
disable-model-invocation: true
---

# Structure Domain Docs

Turn an accepted domain boundary and real material into a knowledge map that can grow without changing its organizing logic.

## Workflow

1. Read `../../methods/domain-reasoning.md` and `../../methods/documentation-structure.md`. Apply both methods inside this workflow.
2. **Confirm the action and authority.** Classify the request as a proposal, audit, scaffold, or approved migration. Planning and audit are read-only. Obtain confirmation before moving, renaming, merging, deleting, or overwriting existing knowledge.
3. **Read the local system.** Read repository instructions, the domain-root README, the target README when present, and one or two healthy sibling domains. Record naming, link, numbering, language, and navigation conventions that the result must preserve.
4. **Establish the domain boundary.** Use a current Domain Assessment when present; otherwise derive the decision from the available evidence. For `Do not accept`, route the material to its owning content class. For `Needs evidence`, continue a read-only proposal or audit with explicit assumptions, but stop a scaffold or migration when it would make the unsupported boundary authoritative. Persist a Domain Assessment only when the decision needs durable traceability.
5. **Inventory before designing.** Read `references/domain-structure-model.md`, `../write-domain-doc/references/domain-document-types.md`, and `assets/domain-inventory-template.md`. Account for every existing and requested artifact by reader question, change authority, lifetime, content class, domain document type, current state, primary home, and structural issue.
6. **Choose the topology.** Use the assessed parent-or-child relationships and the topology tests in the structure model. Keep a valid small domain flat. Create subdomain directories only when both a real parent-child boundary and a current navigation need exist. Use links for related domains and handoffs.
7. **Choose materialization.** Create only files and directories required by current content or an explicit full-scaffold request. Record absent knowledge forms as planned coverage without linking to nonexistent files. Upgrade a file to a directory only when several independent documents or a stable internal reading path need it.
8. **Specify the map contract.** Read `../write-domain-doc/assets/domain-readme-template.md` when no healthy local README exists. Define the required boundary statement, current and planned coverage, valid links, subdomain entries, default learning path, and task-based entry paths without drafting the README body.
9. **Present or apply the structure.** Use `assets/domain-structure-plan-template.md`. For an authorized scaffold, create the approved directories and relocate or create supported non-README files. Do not create an empty or placeholder README. When a new or revised README body is needed, name `$Write Domain Doc` as a separate next result rather than a dependency of this structure result.
10. **Apply approved migrations atomically.** Record exact old-to-new paths, affected Markdown links, assets, and application bindings before editing. Update every approved path and reference in the same change.
11. **Verify the result.** Read `../../methods/prose-quality.md` before presenting reader-facing prose. Read `../../methods/visual-production.md` when the request includes a visual or the topology is materially clearer as one. Confirm one primary home per material, one organizing dimension per sibling level, no unsupported subdomain, no accidental duplicate authority, no unrequested empty directory, valid local links, no link to planned content, and no stale path after migration.

## Boundaries

- Own the structure of one accepted domain knowledge set: inventory, topology, materialization, coverage, navigation requirements, scaffolding, and approved migration.
- Use the shared Domain Reasoning Method for admission, relationships, subdomain validity, and high-level ownership without requiring a separate assessment workflow.
- Own the Responsibility README map contract, placement, and navigation requirements; `$Write Domain Doc` owns the README body and other domain document bodies.
- Use the shared Documentation Structure Method when placement crosses business, domain, product, company, project, technical, or reference roots.
- Treat `{领域名称}本质.md` as a cognition anchor, not a container for every knowledge responsibility.

## Completion test

The work is complete only when every assessed material has a state and primary home, the topology follows evidenced relationships, every materialized path has a current purpose, the README contract permits only valid links and honest planned coverage, every needed README body is identified as a separate result, destructive changes have explicit approval and complete path mappings, and the verification reports all unresolved gaps.
