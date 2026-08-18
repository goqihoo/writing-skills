---
name: draw-diagram
description: Select, create, revise, or restyle one visual that best explains technical, architecture, product, or business-system knowledge. Use for an architecture diagram, context or ownership map, component view, flow, sequence, state model, deployment or failure view, technical illustration or 配图, matrix, chart, or interactive explanation.
disable-model-invocation: true
---

# Draw Diagram

Create or revise one visual per invocation. Make it answer one important question.

## Workflow

1. Read the source content, consuming artifact, supported facts, requested format, and established output conventions.
2. Read `../../methods/visual-production.md` and use its decision, routing, production, inspection, and semantic checks.
3. Select one reader question and one abstraction level. When the request contains several independent questions, complete the primary visual and identify the others as separate possible results.
4. Preserve supported meaning and exact labels. Do not invent architecture, product, technical, or business claims to make the visual look complete.
5. For an illustrated conceptual infographic, use the available ImageGen capability inside this workflow. For exact geometry delivered as PNG, create an exact editable source and export it.
6. Read `../../methods/prose-quality.md` for alt text, captions, and other natural-language passages. Keep exact diagram labels, Mermaid, SVG, code, commands, and structured data outside the prose pass.
7. Inspect the final render and verify that the consuming document can reference both the final asset and its editable source when applicable.

## Boundaries

- Own one visual's form, production, accessibility, and rendered quality.
- Let the consuming Public Skill or source artifact own meaning, facts, and decisions.
- Use the Shared Method directly when a consuming Public Skill needs a visual; no additional Draw Diagram invocation is required.

## Completion

The work is complete when the visual answers one question, adds supported information beyond nearby prose, remains readable at destination width, has no clipping or ambiguous direction, and is saved with meaningful alt text and editable source when applicable.
