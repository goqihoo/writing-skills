---
name: draw-diagram
description: Create, revise, or restyle one technical, architecture, product, business-system, process, planning, data, or quantitative visual using the Scribe Diagram Design profile.
disable-model-invocation: true
---

# Draw Diagram

Create or revise one visual per invocation. Make it answer one important question.

## Workflow

1. Read the source content, consuming artifact, supported facts, requested format, and established output conventions.
2. Select one reader question and one abstraction level. When the request contains several independent questions, complete the primary visual and identify the others as separate possible results.
3. Read `../../methods/visual-production.md` and apply its workflow in order, including the directly referenced Shared Methods. Select exactly one of its 39 Diagram Design visual types.
4. Read the selected type reference, `../../methods/visual-production/scribe-profile.md`, `../../methods/visual-production/style-guide.md`, the selected theme, and `../../methods/visual-production/svg-guide.md` completely. Load only the selected type's reference, not the other type files.
5. Preserve supported meaning, source-defined names, and exact technical identifiers. Do not invent architecture, product, technical, quantitative, or business claims to make the visual look complete.
6. Use the source profile's starting asset for grouped Architecture visuals; otherwise start from the bundled SVG template or the selected type's bundled specimen. Apply the profile's default category assignment, then bind explicit color slots using `scripts/apply_theme.py` and the selected theme; follow `../../methods/visual-production/themes/README.md`. For a color-only restyle, preserve all content, geometry, typography, component roles, and category assignments. For new content, replace specimen labels rather than treating them as source evidence. Retain editable source when exporting PNG.
7. For an illustrated conceptual infographic outside the 39 exact visual types, use the available ImageGen capability inside this workflow.
8. Read `../../methods/prose-quality.md` for alt text, captions, and other natural-language passages. Keep exact diagram labels, Mermaid, SVG, code, commands, and structured data outside the prose pass.
9. For new or redesigned SVG, run `scripts/validate_svg.py SOURCE.svg --scribe` before resolving the theme, then validate and inspect the resolved render. Use ordinary SVG validation for a color-only restyle and `scripts/validate_html.py` for self-contained HTML. Verify that the consuming document can reference both the final asset and its editable source when applicable.

## Boundaries

- Own one visual's form, production, accessibility, and rendered quality.
- Let the consuming Public Skill or source artifact own meaning, facts, and decisions.
- Use the Shared Method directly when a consuming Public Skill needs a visual; no additional Draw Diagram invocation is required.

## Completion

The work is complete when the visual answers one question, adds supported information beyond nearby prose, remains readable at destination width, has no clipping or ambiguous direction, and is saved with meaningful alt text and editable source when applicable.
