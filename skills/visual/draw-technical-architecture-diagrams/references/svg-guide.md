# Editable SVG production guide

Use SVG when exact coordinates, closed loops, aligned lanes, dense annotations, or publication composition require direct control.

## Contract

- Keep labels as `<text>` and related elements in stable named groups.
- Define shared colors, fonts, lines, and markers once in `<defs><style>`.
- Include `viewBox`, `<title>`, `<desc>`, `role="img"`, and `aria-labelledby`.
- Avoid scripts, animation, `foreignObject`, filters, external resources, and embedded raster images unless required.
- Put connectors before nodes so arrows pass behind surfaces; end arrows at node boundaries.
- Use editable geometry, consistent peer dimensions, and short labels.

Use this source order:

```xml
<svg ...>
  <title ...>...</title>
  <desc ...>...</desc>
  <defs>...</defs>
  <rect id="canvas" ... />
  <g id="boundaries">...</g>
  <g id="connectors">...</g>
  <g id="nodes">...</g>
  <g id="annotations">...</g>
</svg>
```

## Validation

Run:

```bash
python3 scripts/validate_svg.py path/to/diagram.svg
```

Render a preview when `rsvg-convert` is available:

```bash
python3 scripts/validate_svg.py path/to/diagram.svg --render /tmp/preview.png
```

Inspect clipping, overlap, arrowheads, label readability, semantic consistency, alignment, and whitespace. Keep SVG as the source of truth for PNG or PDF exports.
