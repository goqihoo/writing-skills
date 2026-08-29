# Swimlane

> Adapted from Diagram Design 2.6 at `ac490fd1` under MIT. Use `../style-guide.md` for every color. Start with zero focal elements. Any `focal: true` example or “exactly one focal” checklist item below is conditional on source-supplied focus; otherwise omit it and render peers neutrally.

**Best for:** cross-functional processes, RACI-style flows, vendor handoffs, multi-team shipping workflows.

## Layout conventions
- Horizontal lanes (or vertical columns) — one per actor/team. Label each lane in the left margin (or top) with a Geist Mono eyebrow.
- Lane dividers: 1px hairlines.
- Process steps are rectangles placed inside the lane of the actor performing them; arrows show flow.
- Handoffs (arrows crossing lane boundaries) are the most important edges — consider accent on the handoff that introduces the most coupling or latency.
- Don't force equal step count per lane; a lane with one step is fine.

## Anti-patterns
- Lanes without labels.
- A step drawn across two lanes (pick one owner).
- Arrows that snake back and forth — reorder steps so the flow is mostly straight.

## Plotly specimen

- `../../../skills/draw-diagram/assets/examples/example-swimlane.html`
