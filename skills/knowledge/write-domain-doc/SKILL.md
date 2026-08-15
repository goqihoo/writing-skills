---
name: write-domain-doc
description: "Create, revise, or review any common document in a reusable domain knowledge directory, including the domain README, `{领域名称}本质.md`, terminology and concept relationships, core objects and lifecycles, participants and rules, mechanisms, capability and solution space, methods and practices, cases and failures, and references. Use the user prompt as the primary artifact-type signal, then load the matching internal module and template when one exists."
---

# Write Domain Doc

Use one public entry point for domain writing: determine the artifact from the prompt, then load the structure that matches it.

## Workflow

1. Apply `$write-doc`.
2. Read repository instructions, the target domain's `README.md`, the target file when it exists, and representative sibling documents. Preserve healthy local terminology, links, title style, and navigation.
3. **Classify from the prompt.** Treat the user prompt and explicit instructions as the highest-authority type signal. Use the target filename and title, target directory, primary reader question, current content, and sibling conventions only to confirm the prompt or infer a type when the prompt is underspecified. When the prompt and an existing target disagree, follow the prompt for the intended artifact and surface any rename or overwrite consequence before changing the file.
4. Read `references/domain-document-types.md`. Select exactly one primary artifact type and its structure strength. When the selected type has a template, read and use that template. Read no unrelated type template.
5. **Load the selected module.** For a domain essence document, read `references/essence-document-module.md` and `assets/essence-article-template.md`; this module owns the fixed twelve-section reasoning contract. For a domain `README.md`, read `assets/domain-readme-template.md` and `../structure-domain-docs/references/domain-structure-model.md` when directory coverage or reading order matters. Apply `$write-knowledge` when no common template-backed domain type fits. Keep architecture ownership, contracts, controls, runtime failure, and evolution with `$study-architecture` when architecture is the primary subject rather than general domain knowledge.
6. **Lock the artifact plan.** State the primary reader question, included and excluded material, evidence needs, selected template, required section responsibilities, and permitted adaptations. A strict schema keeps exact headings and order. A stable lookup schema preserves required fields. A stable reasoning sequence preserves causal or procedural order while allowing subject-specific headings.
7. **Ground the content.** Separate observed facts, external definitions, interpretation, choices, and open questions. Use the domain's preferred terms and link to their canonical definitions. Introduce an abstract model only after a representative object, event, decision, or result makes its need concrete.
8. **Draft in the owned structure.** Use every applicable template selected in step 4; preserve its required headings, fields, or reasoning order according to its structure strength. If no template exists, derive a subject-specific structure through `$write-knowledge`. Fill every required section that the evidence supports and mark a material evidence gap instead of inventing content. Keep detailed terminology, object state, mechanism, procedure, case evidence, and lookup data in their owning artifacts rather than repeating the essence article.
9. **Connect the set.** Add or repair the relative link from the domain README when creating or renaming an artifact. Add links to canonical sibling explanations when readers need prerequisite or deeper material. Do not create links to planned files that do not exist.
10. **Verify the artifact.** Confirm the selected type still matches the reader question, its structure contract is intact, facts and interpretation remain distinct, links resolve, and the document does not mix another artifact's independent responsibility.

## Routing guardrails

- The prompt owns the artifact type. A filename ending in `本质.md` selects the essence module only when the prompt requests essence writing or leaves the type implicit. If the prompt requests another type, align the filename or target instead of silently applying the essence template.
- A domain `README.md` is a domain document written here; `$structure-domain-docs` may request or scaffold it while remaining responsible for the surrounding directory design.
- A document that defines several terms and their relationships is a concept artifact, even when one term dominates its title.
- A lifecycle document owns state and transitions; a mechanism document owns why one state causes or enables another; a method owns what a practitioner does. Split them only when they serve independent reader actions.
- A capability-and-solution document maps reusable response families. Product promises and project selections remain outside it.
- A case document begins with observed facts. Interpretation and transferable lessons follow the evidence.
- A reference document optimizes lookup and authority, not narrative explanation.

## Completion test

The work is complete only when:

- one artifact type owns the document and the evidence for that classification is clear;
- the matching internal module and every available type template were applied at the required structure strength;
- the document answers one primary reader question without becoming a compressed domain directory;
- canonical terminology and sibling links replace duplicate definitions where practical;
- factual claims, interpretations, choices, assumptions, and open questions are distinguishable;
- required examples, cases, failure conditions, validation, sources, or revision triggers for that artifact type are present;
- the domain README exposes the document through a valid relative link when appropriate;
- no placeholder or template instruction remains in a delivered document.
