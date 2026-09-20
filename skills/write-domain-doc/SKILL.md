---
name: write-domain-doc
description: Create, revise, or review one common document inside an accepted reusable domain knowledge set, selecting the matching internal module and template from the requested artifact.
disable-model-invocation: true
---

# Write Domain Doc

Use one public interface for domain writing while keeping each document type responsible for one reader question.

## Workflow

1. Read `../../methods/domain-reasoning.md` and apply it inside this workflow.
2. **Read the local set.** Read repository instructions, the Domain Assessment when persisted, the target domain README, the target file when present, and representative siblings. Preserve healthy terminology, links, title style, and navigation.
3. **Establish a usable boundary.** Confirm from the available evidence that the requested material belongs to an accepted domain boundary and has one primary home. Route `Do not accept` material to its owning content class. For `Needs evidence`, stop only when drafting would make an unsupported boundary authoritative; name the evidence gap instead of requiring another skill.
4. **Classify from the prompt.** Treat the user's explicit request as the highest-authority artifact signal. Use the target filename and title, target path, primary reader question, existing content, and sibling conventions only to confirm the request or infer a type when it is underspecified. Surface a rename or overwrite consequence before changing a conflicting target.
5. **Select one type.** Read `references/domain-document-types.md`. Select exactly one primary artifact type and its structure strength. Read its matching template and no unrelated template.
6. **Load only the selected branch.** For a domain essence document, read `references/essence-document-module.md` and `assets/essence-article-template.md`. For a domain README, read `assets/domain-readme-template.md` and `../structure-domain-docs/references/domain-structure-model.md` when coverage or reading order matters. When no common domain type fits, route to `$Write Knowledge`. When architecture ownership, contracts, controls, runtime failure, or evolution is primary, route to `$Write Arch Knowledge`.
7. **Lock the artifact plan.** State the reader question, included and excluded material, evidence needs, selected template, required section responsibilities, canonical sibling sources, and permitted adaptations. Preserve exact headings for a strict schema, required fields for a stable lookup schema, and reasoning order for a stable reasoning sequence.
8. **Ground the content.** Separate observed facts, external definitions, interpretation, choices, and open questions. Use preferred domain terms and link to canonical definitions. Mark a material evidence gap instead of inventing content.
9. **Draft in the owned structure.** Read `../../methods/prose-quality.md`, then fill every supported responsibility from the selected template. Read `../../methods/visual-production.md` when the request includes a visual or a central relationship is materially clearer as one. Keep terminology, object state, mechanisms, procedures, case evidence, reference data, and essence reasoning in their own artifacts instead of compressing the domain into one document.
10. **Connect the set.** Add or repair the relative link from the domain README when creating or renaming an artifact. Link to canonical siblings for prerequisites or deeper explanations. Keep planned nonexistent content unlinked.
11. **Verify the artifact.** Confirm the selected type still matches the reader question, its structure contract is intact, the Domain Assessment boundary is preserved, facts and interpretation remain distinct, links resolve, and no independent responsibility from another artifact has been absorbed.

## Routing guardrails

- The prompt owns the artifact type. A filename ending in `本质.md` selects the essence module only when the request asks for essence writing or leaves the type implicit.
- A domain README is written here; `$Structure Domain Docs` owns the surrounding directory plan and map requirements.
- A lifecycle document owns state and transitions. A mechanism owns why an outcome occurs. A method owns what a practitioner does. Split only for independent reader actions, change authorities, lifetimes, or citation needs.
- A capability-and-solution document maps reusable response families. Product commitments and project selections remain outside it.
- A case begins with observed facts. Interpretation, counterfactuals, and transferable lessons follow the evidence.
- A reference artifact optimizes lookup, version, and authority rather than narrative explanation.

## Boundaries

- Own one domain README, essence, terminology, object-lifecycle, participant-and-rule, mechanism, capability-and-solution, method-and-practice, case-and-failure, or reference artifact.
- Keep the ten artifact branches as internal modules and templates; do not expose one shallow public skill per document type.
- Use the shared Domain Reasoning Method for admission, boundary, relationships, subdomain validity, high-level content ownership, maturity, and review triggers.
- Let `$Structure Domain Docs` own inventory, topology, materialization, navigation requirements, scaffolding, and migration.
- Let `$Write Knowledge` own general durable knowledge outside the common domain artifact set, and architecture skills own architecture-primary material.

## Completion test

The work is complete only when one accepted domain boundary and one artifact type own the result, the matching template contract is satisfied, the document answers one primary reader question, evidence and interpretation remain distinguishable, canonical links replace duplicate definitions, the domain README exposes the artifact when appropriate, and no placeholder or foreign artifact responsibility remains.
