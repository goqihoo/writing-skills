---
name: draw-diagrams
description: Select, create, revise, or restyle the visual that best explains technical, architecture, product, or business-system knowledge. Use for architecture diagrams, context and ownership maps, components, flows, sequences, states, deployment and failure views, technical illustrations or 配图, matrices, charts, and interactive explanations; choose among no visual, Markdown tables, Mermaid, editable SVG, raster ImageGen, charts, or HTML, then verify the rendered result.
---

# Draw Diagrams

Create the smallest visual that answers one important question. Own visual form and quality; let the source document or architecture skill own the meaning.

## Workflow

1. **Decide whether to draw.** Draw when a visual materially reduces the relationships readers must reconstruct: a central model with four or more meaningful nodes or relationships; three or more dependent stages whose intermediate state matters; branching, convergence, cycles, or bidirectional correspondence; one source affecting three or more downstream consumers; or important state, timing, hierarchy, ownership, failure, or quantitative shape. Treat a central idea written as repeated arrows, nested indentation, or a prose tour through several relationships as a visual candidate. Use prose for one fact or two to three obvious linear steps, and use a Markdown table for compact repeated fields.
2. **State one question.** Name the reader task: locate, compare, follow, inspect, recognize, or explore. Split visuals that mix questions or abstraction levels.
3. **Choose the grammar.** Use the routing table below before choosing a file format.
4. **Choose production and delivery formats.** Preserve an explicit requested output. If exact geometry matters but delivery must be PNG, create an exact diagram source and export it; do not generate it as conceptual artwork.
5. **Extract only supported content.** Include only the actors, boundaries, ownership, relationships, protocols, states, failure paths, labels, or data needed to answer the question. Do not invent architecture meaning.
6. **Load guidance.** Read `references/style-guide.md`. Then read only `references/mermaid-guide.md` or `references/svg-guide.md` for the selected format. For conceptual raster art, invoke the available `imagegen` skill instead.
7. **Create and inspect.** Render or preview at full size and roughly 736–900 px wide. Fix clipping, overlap, crossings, unreadable labels, false emphasis, and ambiguous direction.
8. **Write accompanying prose.** When the result needs a title, caption, alt text, or explanation, stabilize the visual meaning first. Then apply the natural writing guidance from `$write-docs` while drafting those elements, and run its semantic recheck afterward. Keep exact diagram labels, Mermaid, SVG, code, commands, and structured data outside that guidance.
9. **Deliver editable source.** Keep Mermaid, SVG, chart data, or HTML beside exports when practical. Use stable descriptive filenames and accessible alt text.

## Visual routing

| Reader needs | Grammar | Default production |
|---|---|---|
| External actors and dependencies | Context map | Mermaid |
| Responsibility, authority, or trust | Ownership or container map | Mermaid or SVG |
| Layers, modules, or hierarchy | Component or layer view | Mermaid |
| Repeated two-dimensional mappings | Matrix | Markdown table or SVG |
| Ordered business or data stages | Flow or lifecycle | Mermaid; SVG for a true closed loop |
| Timing, concurrency, retry, or acknowledgment | Sequence | Mermaid |
| Allowed states and transitions | State diagram | Mermaid |
| Runtime placement or failure domains | Deployment | Mermaid or SVG |
| Normal path plus rejection, timeout, or recovery | Failure-mode view | Mermaid or SVG |
| Verified quantitative comparison | Chart | Appropriate chart tool |
| Abstract role or mental model without exact geometry | Editorial illustration | ImageGen |
| Adjustable or layered exploration | Interactive explanation | HTML or visualization tool |

The count is a trigger for inspection, not a command to decorate. Keep prose when the relationships remain easier to understand linearly, and keep a table when exact repeated fields matter more than geometry.

## Semantic rules

- Treat containment, ownership, association, dependency, sequence, and data flow as different claims.
- Use arrows only for real direction or transition; label protocol, event, payload, or guarantee only when it matters.
- Keep peer relationships visually equal unless the source identifies a focal or failed path.
- Show boundaries when ownership, trust, deployment, or failure isolation is part of the judgment.
- Keep explanatory paragraphs outside nodes.

## Completion

- The visual answers one question and adds information beyond nearby prose.
- Geometry, direction, labels, state, and color match supported claims.
- Meaning does not depend on color alone, and text remains readable at destination width.
- Reader-facing prose remains consistent with the visual meaning and exact labels.
- The actual render has no clipping, overlap, unintended crop, malformed text, or watermark.
- The consuming document can reference the saved final asset and its editable source.
