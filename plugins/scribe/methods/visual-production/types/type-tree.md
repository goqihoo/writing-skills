# Tree / Hierarchy

> Adapted from Diagram Design 2.6 at `ac490fd1` under MIT. Use `../style-guide.md` for every color. Start with zero focal elements. Any `focal: true` example or “exactly one focal” checklist item below is conditional on source-supplied focus; otherwise omit it and render peers neutrally.

**Best for:** org charts, dependency trees, taxonomy, file trees, decision breakdowns, skill trees.

## Layout conventions
- Root at top, children fan out below (or root at left, children to right).
- Nodes are small labeled rectangles (`rx=6`), Geist 12px 600 name + optional Geist Mono 9px sublabel. Width 120–180px, height 40–52px.
- **Connectors are orthogonal (elbow-style), never diagonal.** Parent drops a short vertical line, then a horizontal bus connects siblings, then each child has a short vertical drop into its top edge. 1px muted stroke.
- Leaf indicator: thinner stroke (0.8) or different fill — OR let terminal position do the work.
- Max depth: 4 (root + 3 tiers). Max breadth per level: 5.
- accent on **one** node: root OR critical leaf. Not both.
- Draw connectors before nodes.

## Anti-patterns
- Tree 5+ levels deep on a single page (illegible — split).
- Nodes of wildly varying widths — pick 2 widths max.
- Diagonal connector lines.
- Skipped levels (parent connected to grandchild with no middle).
- accent on root AND a leaf.

## Plotly specimen

- `../../../skills/draw-diagram/assets/examples/example-tree.html`
