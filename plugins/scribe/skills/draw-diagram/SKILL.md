---
name: draw-diagram
description: Create, revise, or restyle one technical, architecture, product, business-system, process, planning, data, or quantitative visual using the Scribe Diagram Design profile.
---

# Draw Diagram

Create or revise one visual per invocation. Make it answer one important question.

## Workflow

1. Read the source content, consuming artifact, supported facts, requested format, and established output conventions.
2. Select one reader question and one abstraction level. When the request contains several independent questions, complete the primary visual and identify the others as separate possible results.
3. Read `../../methods/visual-production.md` and apply its workflow in order, including the directly referenced Shared Methods. Choose its production branch before selecting a visual form; do not force conceptual content into a Diagram Design type.
4. For the Diagram Design branch, select exactly one of its 39 visual types and read the selected type reference, `../../methods/visual-production/scribe-profile.md`, `../../methods/visual-production/style-guide.md`, the selected theme, and `../../methods/visual-production/svg-guide.md` completely. Load only the selected type's reference, not the other type files. For the ImageGen branch, read the available ImageGen skill and its prompting guidance, then follow its built-in generation workflow.
5. Preserve supported meaning, source-defined names, and exact technical identifiers. Do not invent architecture, product, technical, quantitative, or business claims to make the visual look complete.
6. For Diagram Design, use the source profile's starting asset for grouped Architecture visuals; otherwise start from the bundled SVG template or the selected type's bundled specimen. Apply the profile's default category assignment, then bind explicit color slots using `scripts/apply_theme.py` and the selected theme; follow `../../methods/visual-production/themes/README.md`. For a color-only restyle, preserve all content, geometry, typography, component roles, and category assignments. For new content, replace specimen labels rather than treating them as source evidence. Retain editable source when exporting PNG. For ImageGen, map each source concept to one recognizable visual cue, keep exact labels minimal, and avoid visual relationships that imply unsupported sequence, hierarchy, or causality.
7. Read `../../methods/prose-quality.md` for alt text, captions, and other natural-language passages. Keep exact diagram labels, Mermaid, SVG, code, commands, and structured data outside the prose pass.
8. For new or redesigned SVG, run `scripts/validate_svg.py SOURCE.svg --scribe` before resolving the theme, then validate and inspect the resolved render. Use ordinary SVG validation for a color-only restyle and `scripts/validate_html.py` for self-contained HTML. For ImageGen output, inspect the actual raster for label accuracy, unsupported additions, artifacts, and readability at destination width. Verify that the consuming document references the final project asset and, for exported Diagram Design assets, its editable source when applicable.

## Boundaries

- Own one visual's form, production, accessibility, and rendered quality.
- Let the consuming Public Skill or source artifact own meaning, facts, and decisions.
- Use the Shared Method directly when a consuming Public Skill needs a visual; no additional Draw Diagram invocation is required.

## Completion

The work is complete when the visual answers one question, adds supported information beyond nearby prose, remains readable at destination width, has no clipping or ambiguous direction, and is saved with meaningful alt text and editable source when applicable.
