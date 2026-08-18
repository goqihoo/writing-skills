# Visual production method

Apply this method inside a Public Skill when the user requests a visual or when the result would otherwise force readers to reconstruct a central relationship. Create the smallest visual that answers one important question, and retain prose or a table when either is clearer.

## Decision

Inspect a visual candidate when the content contains four or more meaningful nodes or relationships; three or more dependent stages with material intermediate state; branching, convergence, cycles, or bidirectional correspondence; one source affecting at least three consumers; or important timing, hierarchy, ownership, failure, or quantitative shape.

Use prose for one fact or two to three obvious linear steps. Use a Markdown table for compact repeated fields. A count triggers inspection, not decoration.

## Workflow

1. State one reader question: locate, compare, follow, inspect, recognize, or explore.
2. Select only the supported actors, boundaries, ownership, relationships, protocols, states, failure paths, labels, or data needed to answer it.
3. Choose the visual grammar before the file format. Preserve an explicit requested format.
4. Use editable SVG by default for exact relational diagrams. Use Mermaid only when the user explicitly requests Mermaid. Use an appropriate chart tool for verified quantitative comparison and ImageGen for an illustrated conceptual explanation.
5. Read `visual-production/style-guide.md`. Read `visual-production/svg-guide.md` for exact relational diagrams or `visual-production/mermaid-guide.md` for requested Mermaid.
6. Create and inspect the actual render at full size and roughly 736–900 px wide. Fix clipping, overlap, crossings, unreadable labels, false emphasis, and ambiguous direction.
7. For a file output, use the consuming document's sibling `_assets/` directory by default unless an explicit path or established project convention says otherwise. Keep editable source beside exports when practical. Keep the skill's bundled `assets/` directory for templates only.
8. Add only meaningful alt text by default. Do not append a visible title, caption, or explanation after the image unless requested or required by the consuming artifact.

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

## Semantic rules

- Treat containment, ownership, association, dependency, sequence, and data flow as different claims.
- Use arrows only for real direction or transition. Label a protocol, event, payload, or guarantee only when it matters.
- Keep peer relationships visually equal unless the source identifies a focal or failed path.
- Show boundaries when ownership, trust, deployment, or failure isolation is part of the judgment.
- Keep explanatory paragraphs outside nodes.
- Match geometry, direction, labels, state, and color to supported claims.
- Preserve meaning without color alone and keep text readable at destination width.
- Inspect the final render for clipping, overlap, unintended crop, malformed text, or watermark.
