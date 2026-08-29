---
name: draw-diagram
description: Create, revise, or restyle one technical, architecture, product, business-system, process, planning, data, or quantitative visual using the Scribe Diagram Design profile.
disable-model-invocation: true
---

# Draw Diagram

Create or revise one visual per invocation. Make it answer one important question.

## Workflow

1. Read the source content, consuming artifact, supported facts, requested format, and established output conventions.
2. Read `../../methods/visual-production.md`. Select one semantic pattern when routed and exactly one of its 39 Diagram Design visual types.
3. Read the selected type reference, `../../methods/visual-production/style-guide.md`, and `../../methods/visual-production/svg-guide.md` completely. Load only the selected type's reference, not the other type files.
4. Select one reader question and one abstraction level. When the request contains several independent questions, complete the primary visual and identify the others as separate possible results.
5. Preserve supported meaning and exact labels. Do not invent architecture, product, technical, quantitative, or business claims to make the visual look complete. Begin with zero focal elements.
6. Start from the bundled SVG template or the selected type's Plotly specimen. Replace specimen content rather than treating it as source evidence. For exact geometry delivered as PNG, retain the editable SVG source and export it.
7. For an illustrated conceptual infographic outside the 39 exact visual types, use the available ImageGen capability inside this workflow.
8. Read `../../methods/prose-quality.md` for alt text, captions, and other natural-language passages. Keep exact diagram labels, Mermaid, SVG, code, commands, and structured data outside the prose pass.
9. Run `scripts/validate_svg.py` on SVG output or `scripts/validate_html.py` on self-contained HTML output. Inspect the final render and verify that the consuming document can reference both the final asset and its editable source when applicable.

## Boundaries

- Own one visual's form, production, accessibility, and rendered quality.
- Let the consuming Public Skill or source artifact own meaning, facts, and decisions.
- Use the Shared Method directly when a consuming Public Skill needs a visual; no additional Draw Diagram invocation is required.

## Completion

The work is complete when the visual answers one question, adds supported information beyond nearby prose, remains readable at destination width, has no clipping or ambiguous direction, and is saved with meaningful alt text and editable source when applicable.
