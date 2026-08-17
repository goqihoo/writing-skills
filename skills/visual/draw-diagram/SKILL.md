---
name: draw-diagram
description: Select, create, revise, or restyle one visual that best explains technical, architecture, product, or business-system knowledge. Use for an architecture diagram, context or ownership map, component view, flow, sequence, state model, deployment or failure view, technical illustration or 配图, matrix, chart, or interactive explanation; choose among no visual, Markdown table, Mermaid, editable SVG, raster ImageGen, chart, or HTML, then verify the rendered result.
disable-model-invocation: true
---

# Draw Diagram

Create the smallest visual that answers one important question. Own visual form and quality; let the source document or architecture skill own the meaning.

Create or revise one visual per invocation.

## Workflow

1. **Decide whether to draw.** Draw when a visual materially reduces the relationships readers must reconstruct: a central model with four or more meaningful nodes or relationships; three or more dependent stages whose intermediate state matters; branching, convergence, cycles, or bidirectional correspondence; one source affecting three or more downstream consumers; or important state, timing, hierarchy, ownership, failure, or quantitative shape. Treat a central idea written as repeated arrows, nested indentation, or a prose tour through several relationships as a visual candidate. Use prose for one fact or two to three obvious linear steps, and use a Markdown table for compact repeated fields.
2. **State one question.** Name the reader task: locate, compare, follow, inspect, recognize, or explore. When a request mixes questions or abstraction levels, select the primary visual and return separate follow-up invocations for the others.
3. **Choose the grammar.** Use the routing table below before choosing a file format.
4. **Choose production and delivery formats.** Preserve an explicit requested output. Use editable SVG as the default for exact relational diagrams. Use Mermaid only when the user explicitly requests Mermaid. If exact geometry matters but delivery must be PNG, create an exact diagram source and export it; do not generate it as conceptual artwork.
5. **Extract only supported content.** Include only the actors, boundaries, ownership, relationships, protocols, states, failure paths, labels, or data needed to answer the question. Do not invent architecture meaning.
6. **Load guidance.** Read `references/style-guide.md`. Read `references/svg-guide.md` for exact relational diagrams, or `references/mermaid-guide.md` when the user requested Mermaid. For an illustrated conceptual infographic, invoke the available `imagegen` skill instead.
7. **Create and inspect.** Render or preview at full size and roughly 736–900 px wide. Fix clipping, overlap, crossings, unreadable labels, false emphasis, and ambiguous direction.
8. **Add only requested prose.** Add only meaningful alt text by default. Do not append a visible title, caption, or explanation after the image unless the user requests it or the consuming document has an established caption convention. When `$Write Doc` was explicitly included, stabilize the visual meaning before applying its prose pass and run its semantic recheck afterward. Keep exact diagram labels, Mermaid, SVG, code, commands, and structured data outside that optional pass.
9. **Deliver file outputs.** For file-based output, use the consuming document's sibling `_assets/` directory by default. When no consuming document exists, use `_assets/` under the current output directory. Follow an explicit user path or an established project convention instead. Keep Mermaid, SVG, chart data, or HTML beside exports when practical. Use stable descriptive filenames and accessible alt text. Keep the skill's bundled `assets/` directory for templates only.

## Visual routing

| Reader needs | Grammar | Default production |
|---|---|---|
| External actors and dependencies | Context map | SVG |
| Responsibility, authority, or trust | Ownership or container map | SVG |
| Layers, modules, or hierarchy | Component or layer view | SVG |
| Repeated two-dimensional mappings | Matrix | Markdown table or SVG |
| Ordered business or data stages | Flow or lifecycle | SVG |
| Timing, concurrency, retry, or acknowledgment | Sequence | SVG |
| Allowed states and transitions | State diagram | SVG |
| Runtime placement or failure domains | Deployment | SVG |
| Normal path plus rejection, timeout, or recovery | Failure-mode view | SVG |
| Verified quantitative comparison | Chart | Appropriate chart tool |
| Definition, role, or mental model aided by concrete visual cues | Illustrated conceptual infographic | ImageGen |
| Adjustable or layered exploration | Interactive explanation | HTML or visualization tool |

Choose ImageGen for a “what is it?” explanation when concrete objects, visual metaphor, and spatial grouping make the concept easier to recognize, even if the image includes short labels and simple relationships. Choose SVG when correctness depends on exact entities, wording, topology, boundaries, direction, order, timing, states, or failure paths.

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
