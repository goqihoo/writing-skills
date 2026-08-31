# SVG production guide

Use this guide with the selected type reference and `style-guide.md`. The type reference may replace a universal primitive only when that exception is part of the type's defining grammar, such as Sankey ribbons, Fishbone bones, or Loop arcs.

## Output contract

- Use editable SVG as the default source. Use self-contained HTML only as a requested wrapper around inline SVG.
- Start with the selected type specimen’s viewBox; use the upstream `1000 × 600` starter when no type-specific canvas applies. Fit the active diagram rather than stretching nodes to fill a larger canvas. Scale the whole SVG to the destination, preserving component proportions.
- Put the Scribe profile's `data-scribe-color-mode` on new or redesigned editable SVG; keep its category, series, status, or documented neutral paint contract machine-checkable.
- Put `<title>` first inside `<svg>`, followed by `<desc>` and then `<defs>`. Give both IDs a diagram-specific prefix and resolve them from `role="img" aria-labelledby="…"`.
- Draw in this order: canvas, groups or zones, connectors and labels, nodes, annotations, legend.
- Keep a 40 px outer margin and reserve about 60 px below the active diagram when a legend is necessary.

## Core components

Use one `paper` canvas from the selected theme. Apply the group and node paint assignments from `scribe-profile.md` by default; reserve `group-surface` and `object` for neutral treatments. Supporting elements may use transparent fill. A node consists of an opaque mask, its styled shape, an optional small rectangular type tag, a short name, and a subordinate 9 px sublabel only when needed. Preserve the full upstream pattern below; the tag is conditional on source-supported content.

Define arrow markers for ordinary, accent, and external relationships using `muted`, `accent`, and `link`. Draw connectors before boxes so node surfaces mask the connector ends cleanly.

Every connector label retains a label-surface rectangle sized to its text and resolves that rectangle's fill through the selected theme's `connector-label-surface` token. A theme may make the surface transparent or opaque without changing label geometry. Keep the label surface 6–10 px from its connector, keep the label to 14 characters when practical, place labels beside vertical segments, and never use vertical writing mode.

Put a necessary legend in a horizontal strip below the diagram. Keep it out of the active node area and include only symbols that appear in the diagram.

### Full node primitive

For the upstream 160 × 64 px architecture example at (240, 240), keep this mask / shape / tag / name / sublabel hierarchy. Resolve paint slots using the selected theme. This example uses category 1; use the enclosing group's assigned number for a grouped node. Omit a tag or sublabel only for content reasons, never because of skin selection.

```svg
<rect x="240" y="240" width="160" height="64" rx="6" fill="var(--dd-paper, #FFFFFF)"/>
<rect class="node" data-category="1" x="240" y="240" width="160" height="64" rx="6"
      fill="var(--dd-category-1-tint, #E9EBFE)" stroke="var(--dd-category-1, #4F5BD5)" stroke-width="1"/>
<rect x="248" y="248" width="28" height="12" rx="2" fill="transparent"
      stroke="var(--dd-ink-a400, rgba(34,38,58,0.4))" stroke-width="0.8"/>
<text x="262" y="257" font-size="7" font-family="'Geist Mono', monospace"
      fill="var(--dd-ink, #22263A)" text-anchor="middle" letter-spacing="0.08em">API</text>
<text x="320" y="276" font-size="12" font-weight="600" font-family="'Geist', sans-serif"
      fill="var(--dd-ink, #22263A)" text-anchor="middle">Node Name</text>
<text x="320" y="292" font-size="9" font-family="'Geist Mono', monospace"
      fill="var(--dd-muted, #596174)" text-anchor="middle">tech:port</text>
```

Define the original arrowhead as `markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"`, with polygon `0 0, 8 3, 0 6`. Preserve the type's connector widths and rounded elbows. Keep optional dot patterns, indices, and callouts separate from theme selection.

## Connector grammar

Apply these six rules unless the selected type reference declares a defining exception.

1. Use straight lines only when endpoints share an x or y coordinate. Otherwise use rounded orthogonal connectors with 8 px corner arcs; diagonal slants fail review.
2. Keep 6–10 px of visible space between a connector and its label-surface rectangle. Retain that layout box when its selected fill is `none`; it must not touch or cover the stroke.
3. Keep every connector independently traceable. Do not overlap paths. Offset parallel routes by at least 12 px and use a bridge or hop when a crossing cannot be removed.
4. Fan multiple connectors along a shared node edge. For `N` connectors on an edge of length `L`, place connector `k` at `L × k / (N + 1)` and keep adjacent attach points at least 12 px apart.
5. Route around every non-endpoint object. When a geometrically unavoidable transit crosses behind a non-endpoint box, use a dashed line, keep its label at a visible end, and place the arrowhead only at the real destination.
6. Put connector labels on open canvas. A label-surface rectangle must not overlap a node drawn after it.

Use top or bottom ports for predominantly vertical relationships and left or right ports for predominantly horizontal ones. Give synchronous, asynchronous, optional, return, and failure paths distinct semantics only when the source supports the distinction.

## Layout and complexity

Use one dominant reading direction. Start with left-to-right for request, business, and data flows; top-to-bottom for layers, trees, and time; outside-to-inside for trust; and the selected type reference's geometry for specialized quantitative views.

The default budget is nine nodes and twelve connectors. A selected type reference may set a tighter or specialized budget. Apply `scribe-profile.md` when deciding whether supported content populates focal or metadata slots. Split into overview and detail when the supported content exceeds the budget; do not shrink text or stack connectors to force a fit.

Use the typography sizes in `style-guide.md`, including the upstream 7 px tag / 9 px sublabel / 14 px callout exceptions. Use 8, 12, or 16 px internal padding and 20, 24, 32, 40, or 48 px gaps unless the type specifies otherwise. Preserve primitive-specific offsets instead of rounding them to the general grid.

## Render inspection

Retain `var(--dd-ROLE, COLOR)` slots in editable source. Run `validate_svg.py source.svg --scribe`, then run `apply_theme.py source.svg output.svg --theme SKIN --resolve`; validate and inspect the resolved output, since SVG consumers differ in CSS-variable support. Use color-only switching instructions in `themes/README.md`.

Inspect source and render at full size and at the destination width. Check:

- the chosen type still answers one reader question;
- text remains readable and no label, tag, marker, or node is clipped;
- connectors have unambiguous direction, distinct routes, clean attach points, and visible labels;
- containment, sequence, hierarchy, status, and quantity are not implied accidentally;
- the selected theme is the only color system and meaning survives without color;
- the Scribe source-adaptation profile passes;
- CJK fallback fonts render and labels fit their boxes;
- the image has no unintended crop, malformed glyph, external asset, or watermark.

## Pre-output check

The diagram is complete only when the selected type reference has been applied, its complexity budget is met, every visible claim is supported, the accessible SVG contract resolves, the actual render passes inspection, and the consuming artifact can reference the final asset and editable source.
