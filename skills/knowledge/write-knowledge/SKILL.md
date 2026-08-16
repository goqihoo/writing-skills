---
name: write-knowledge
description: "Create, revise, or review general durable knowledge documents: concept explanations, mechanism explanations, methods, pattern comparisons, mental models, case studies, and references. Use when understanding must remain useful beyond one project and no common domain-document or stricter artifact skill owns the requested format; use write-domain-doc for every common artifact inside a domain knowledge directory, including first-principles essence documents, and write-study-architecture for reusable architecture ownership, contracts, controls, failure, or evolution."
disable-model-invocation: true
---

# Write Knowledge

Turn understanding, experience, and source material into knowledge that readers can reuse.

## Workflow

1. Apply `$write-doc`.
2. Read `references/knowledge-types.md`.
3. **Infer the primary type from artifact signals.** Use, in order, the user's explicit description; the target's title, filename, and directory; its existing healthy structure; and project rules and established sibling-document conventions. Use the future reader action to validate the inferred type instead of discarding stronger artifact identity. For every common domain-directory artifact, including essence documents, stop and return a ready-to-type explicit invocation using `$write-domain-doc $reason-domain $write-doc`. Surface a material conflict among the strongest signals instead of silently choosing a different artifact type.
4. Define the scope and concrete question. Treat other knowledge types as supporting material.
5. **Derive the subject-specific reasoning spine.** State the central claim, the distinctions readers must preserve, the causal chain that supports the claim, the boundaries that limit it, and the role of any example or counterexample. Derive this spine from the subject rather than from the labels in the selected knowledge type.
6. **Build and audit the outline.** Use headings that express the subject's own claims, relationships, stages, or decisions. Then audit the outline against the selected type's questions as a coverage checklist. Combine, distribute, or reorder those questions when the subject's reasoning requires it.
7. **Lock the artifact plan.** Record the primary question, reasoning chain, section responsibilities, and example roles. For a new document, confirm that the outline is explainable from the subject and would not remain intact if only the title changed to an unrelated topic. For a revision, preserve the healthy outline unless the user explicitly asks for reorganization.
8. Draft within the locked plan. Use other knowledge types only as supporting material and omit material that does not serve the primary use.
9. Test the reasoning with one representative case and relevant counterexample or failure condition without letting the case replace the selected knowledge type's structure.
10. Verify the shared completion check and the selected type's completion test.

## Type boundary

A knowledge document remains useful after the immediate initiative ends. A work artifact coordinates a specific delivery, approval, implementation, or operational response. Preserve that distinction even when both contain similar facts.

Route reusable system ownership, contracts, control, failure, and evolution to `$write-study-architecture`. Route project commitments to `$write-delivery-architecture`.

The work is complete when the selected type's reasoning obligations are satisfied without copying its part labels into a default outline, and a reader can perform the intended action without reconstructing the author's research process.
