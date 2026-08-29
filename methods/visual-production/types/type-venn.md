# Venn / Set Overlap

> Adapted from Diagram Design 2.6 at `ac490fd1` under MIT. Use `../style-guide.md` for every color. Start with zero focal elements. Any `focal: true` example or “exactly one focal” checklist item below is conditional on source-supplied focus; otherwise omit it and render peers neutrally.

**Best for:** intersection of concepts/domains, shared attributes between categories, "where A meets B", ikigai-style frames (desirable × feasible × viable).

## Layout conventions
- **Prefer 2 or 3 circles.** Avoid 4+ (unreadable — use a matrix instead).
- Circle stroke: 1px hairline, color per-set (ink, muted, soft).
- Circle fill: very low-opacity tint — `rgba(34,38,58,0.04)` for ink set, `rgba(89,97,116,0.05)` for muted. Tints compound naturally in overlap regions.
- Radii: equal when sets are comparable in size; proportional when sets are meaningfully different. Don't fake equal sizes for aesthetics.
- **Set labels** placed outside the circle, NEVER crossing the stroke. Geist 12–14px 600 for the set name, optional Geist Mono 9px sublabel.
- **Intersection labels** placed inside the overlap region, Geist 12px 600, centered. For small overlaps, use a leader line to a label in clear space.
- **accent accent** on the ONE focal intersection — the "sweet spot". Either accent label stroke OR clipPath-bounded accent fill tint (`rgba(79,91,213,0.10)`).
- Circle centers and radii divisible by 4.

## Anti-patterns
- Unlabeled regions — reader can't tell which set is which.
- Circles that don't overlap when overlap is the point.
- Equal-sized circles when sets are obviously different (dishonest).
- accent on multiple overlap regions (focal signal dies).
- Labels sitting on top of circle strokes (illegible).
- 4+ circles where 2–3 would do.

## Plotly specimen

- `../../../skills/draw-diagram/assets/examples/example-venn.html`
