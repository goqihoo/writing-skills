# Timeline

> Adapted from Diagram Design 2.6 at `ac490fd1` under MIT. Use `../style-guide.md` for every color. Start with zero focal elements. Any `focal: true` example or “exactly one focal” checklist item below is conditional on source-supplied focus; otherwise omit it and render peers neutrally.

**Best for:** release history, project milestones, incident timelines, roadmaps, changelog visualizations.

## Layout conventions
- Horizontal hairline baseline across the middle (`stroke-width=1`).
- Tick marks at time boundaries (quarters, months, sprints) with date labels below in Geist Mono.
- Events: small filled circles (`r=4`) on the baseline. Labels alternate above and below to prevent collision, connected to the circle with a 1px hairline drop.
- Major milestones: accent circle (`r=6`) + bold Geist label.
- Time scale must be honest: if intervals are non-equal, space the circles non-equally. Don't fake linear spacing for aesthetics. Break the axis visibly if a region is too dense.

## Anti-patterns
- Equal-spacing events that aren't equally spaced in time.
- Missing axis labels ("what unit is this?").
- Crowded labels without vertical offset — illegible.

## Plotly specimen

- `../../../skills/draw-diagram/assets/examples/example-timeline.html`
