# Scribe Diagram Design profile

Apply this small source-adaptation profile when populating a Diagram Design type with new source content. Skip content adaptation for a color-only restyle: retain every existing label, role, tag, and decoration. It changes how source material populates the type; it does not replace the type's semantics, composition, component geometry, connector grammar, or complexity budget.

Clear every specimen-supplied focus, status, category, subtitle, tool, chip, port, boundary, and detail before adapting its content. Preserve useful geometry, then repopulate semantic slots only from the source or user's explicit direction.

## Source-supported focus

Do not invent focus, active, selected, primary, success, warning, failure, or risk state from a template or specimen. Give peer objects equal emphasis while retaining their category colors. Treat focal fields, exact-one focal instructions, and focal examples in an adapted type reference as conditional input slots: use them only when the source or user establishes that meaning, and otherwise omit them without asking for a decorative focus.

For a view centered on a named System, Subsystem, Module or Component, establish the depicted responsibility boundary before assigning paint. Treat callers, peer modules, shared infrastructure and runtime carriers outside that boundary as supporting external participants. Apply this hierarchy to structure, flow and sequence views as well as context views. A parent module is external to its component's internal view; a private component remains internal to its owning module. Determine scope from responsibility and the reader question, not deployment location or an existing category number. Give peer objects equal emphasis when a landscape has no identified focal object.

Keep the focal object's internal parts in their meaningful category colors. Draw external nodes with quiet neutral surfaces and lighter borders, using theme roles such as `object` and `deemphasized-border`; keep their labels at readable size and contrast. Use neutral external group boundaries, lifelines and connecting relationships while retaining arrow direction, call/return styles and meaningful status or proposed-state markings. Preserve labels, geometry and topology during this emphasis-only adjustment. Avoid whole-node opacity, shrunken text or new dashed borders that obscure content or imply another protocol/state.

Mark supporting node containers with `data-scope="external"` in editable SVG. Remove their category-paint assignment, including inherited category paint, while preserving semantic identity in labels and boundaries. Keep category metadata only on elements that use category paint. External treatment takes precedence over the default multicolor palette; a bright alternative category does not count as de-emphasis. Keep the view's categorical mode when its internal parts remain categorical rather than making the whole diagram neutral.

## Source-defined categories

Use **multicolor categories by default** when generating or redesigning a visual. Treat existing groups, grouping boxes, layers, or lanes as the color groups; their membership is sufficient to assign paint. For an ungrouped visual, use its source-defined semantic categories, such as stages or object types. Reuse established category numbers; otherwise assign `category-1` through `category-5` in group reading order, using unused slots first and cycling only after all five are used. Record the assignments with `data-category` and retain them across edits and related figures. Select colors from the current skin without another classification pass or a user color request.

Use one category tint for all ordinary node surfaces in a group and its solid color for their borders; let group labels and related connectors echo the same color. Use the category at 2% opacity for a quiet group wash and at 35% for its border. Keep source-supported status and protocol encodings when they already carry meaning.

Apply category paint to the existing component: retain its shape, radius, border width, dash pattern, typography, ports, and hierarchy. Inherit the enclosing group's category through layout wrappers; assign a separate number only to an actual subgroup. Keep groups identifiable by labels and containment as well as color. Treat category as identity, not focus or status; use neutral paint for supporting detail or an explicitly requested neutral treatment. When the source has only one category, use one category color rather than inventing extra groups for variety.

For a new grouped Architecture visual, start from [the grouped SVG template](../../skills/draw-diagram/assets/editorial-grouped-template.svg). Replace its example groups, nodes, and links with the source model; adapt its composition to the selected type rather than forcing three groups or six nodes. Use the selected type's specimen for other visual types and retain their defining encodings. Preserve existing category assignments during a restyle; switching palettes changes their paint values, not which objects belong together.

## Machine-readable color contract

Give every new or redesigned editable SVG one `data-scribe-color-mode` on its root: `categorical` for qualitative categories, `quantitative` for series, or `status` when supported states carry the color meaning. Use `neutral` only for an explicit neutral-color request or a color-only restyle, and record that exception with `data-scribe-neutral-reason="explicit-user-request"` or `"color-only-restyle"`. Mark qualitative groups with `data-category="1"` through `"5"`; mark each node's styled shape with class `node`, leaving its mask, tag, and label separate. Bind matching category fill and any visible border to each ordinary node. A colored frame or label alone does not satisfy the group contract. Palette declarations inside `<defs>` are not visible paint.

Run `validate_svg.py --scribe` on the editable source before resolving its theme. Run ordinary SVG validation and render inspection on the resolved export.

## Completion check

The profile is satisfied when the declared color mode passes validation, internal source-defined groups visibly use their category colors, external supporting nodes are visibly quieter at destination size, the diagram contains no invented state, categories remain distinguishable without color alone, and the selected Diagram Design type still passes its original geometry and complexity checks. Check every external node against the depicted boundary and inspect actual surfaces, borders, labels and relationships; unused palette definitions or an “external” label with equally strong paint do not satisfy this check.
