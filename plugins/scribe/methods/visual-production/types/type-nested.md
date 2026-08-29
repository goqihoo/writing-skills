# Nested Containment

> Adapted from Diagram Design 2.6 at `ac490fd1` under MIT. Use `../style-guide.md` for every color. Start with zero focal elements. Any `focal: true` example or “exactly one focal” checklist item below is conditional on source-supplied focus; otherwise omit it and render peers neutrally.

**Best for:** hierarchy through containment — scope boundaries, CLAUDE.md cascade, trust zones, folder nesting, blast radius. Outer = broader, inner = more specific.

## Layout conventions
- 3–5 rounded rectangles (`rx=8`), nested with consistent inset padding (24–32px horizontal, 32–36px vertical recommended).
- Each level labeled at the top-left in Geist Mono eyebrow style (7–8px, letter-spacing 0.14em). Labels sit on a paper-colored mask rect over the ring's top border.
- Stroke hierarchy: outer rings faint (`rgba(..,0.30–0.45)`), progressing to muted, to ink, to accent at the innermost focal.
- Fills step up in opacity from outer to inner: `rgba(..,0.015)` → `rgba(..,0.025)` → accent-tint on the innermost.
- Optional file-icon glyph (folded-corner rect) inside each level hints at scope content.
- Italic Instrument Serif callouts (see `../primitive-annotation.md`) — 1–2 max.

## Anti-patterns
- More than 6 levels (information disappears inward).
- Irregular padding between levels — unaligned nesting looks accidental.
- Content inside rings that isn't part of the hierarchy — use a sibling diagram.
- accent on multiple levels — hierarchy collapses.

## Plotly specimen

- `../../../skills/draw-diagram/assets/examples/example-nested.html`
