# Visual production method

Let the consuming Public Skill and selected template decide whether a visual is needed and what it must explain. Once they select a visual, use this Shared Method as the Draw Diagram production contract by default; no additional public invocation is required. Depart from this contract only when the user explicitly requests another production contract or a binding destination convention requires one.

Apply this method when the user requests a visual or when the result would otherwise force readers to reconstruct a central relationship. Create the smallest visual that answers one important question, and retain prose or a table when either is clearer.

## Decision

Inspect a visual candidate when the content contains four or more meaningful nodes or relationships; three or more dependent stages with material intermediate state; branching, convergence, cycles, or bidirectional correspondence; one source affecting at least three consumers; or important timing, hierarchy, ownership, failure, or quantitative shape.

Use prose for one fact or two to three obvious linear steps. Use a Markdown table for compact repeated fields. A count triggers inspection, not decoration.

## Workflow

1. State one reader question: locate, compare, follow, inspect, recognize, or explore.
2. Read `visual-production/content-preparation.md` and prepare the source-supported content model before selecting a visual type or drawing geometry.
3. When behavior, state, enforcement, or risk carries the meaning, read `visual-production/semantic-patterns.md` and select one primary semantic pattern before choosing layout.
4. Select exactly one of the 39 Diagram Design visual types below. Read its linked type reference completely before drawing. Choose the dominant visual axis instead of combining two layout grammars.
5. Read `visual-production/scribe-profile.md` for the small source-adaptation rules, `visual-production/style-guide.md` for the theme interface and selected theme, and `visual-production/svg-guide.md` for production, connector, accessibility, and inspection rules.
6. Map the prepared content into only the supported actors, boundaries, ownership, relationships, protocols, states, failure paths, labels, or data needed to answer the reader question. Apply the chosen type's complexity budget and split overview from detail when it cannot fit.
7. Use editable SVG by default. Use self-contained HTML with inline SVG when the destination needs a web wrapper or interaction. Export PNG from the editable source when raster output is requested. Use Mermaid only when the user explicitly requests Mermaid and state any type-specific fidelity loss.
8. Create and inspect the actual render at full size and roughly 736–900 px wide. Fix clipping, overlap, crossings, unreadable labels, false emphasis, and ambiguous direction.
9. For a file output, use the consuming document's sibling `_assets/` directory by default unless an explicit path or established project convention says otherwise. Keep editable source beside exports when practical. Keep the skill's bundled `assets/` directory for templates and specimens only.
10. Add only meaningful alt text by default. Do not append a visible title, caption, or explanation after the image unless requested or required by the consuming artifact.

## Visual-type routing

| If the reader needs to see… | Type | Read |
|---|---|---|
| Components and connections in a system | Architecture | `visual-production/types/type-architecture.md` |
| A legacy landscape grouped by phase or department | IT current-state | `visual-production/types/type-it-state.md` |
| Decision logic with branches | Flowchart | `visual-production/types/type-flowchart.md` |
| Time-ordered messages between actors | Sequence | `visual-production/types/type-sequence.md` |
| States, transitions, and guards | State machine | `visual-production/types/type-state.md` |
| Entities, fields, and logical relationships | ER / data model | `visual-production/types/type-er.md` |
| Events positioned in time | Timeline | `visual-production/types/type-timeline.md` |
| A cross-functional process with handoffs | Swimlane | `visual-production/types/type-swimlane.md` |
| Two-axis positioning or prioritization | Quadrant | `visual-production/types/type-quadrant.md` |
| Several entities scored across three to five criteria | Radar / spider | `visual-production/types/type-radar.md` |
| One quantitative series across cyclic categories | Polar chart | `visual-production/types/type-polar.md` |
| A reinforcing cycle with a shared accumulating hub | Loop / flywheel | `visual-production/types/type-loop.md` |
| Hierarchy through containment or scope | Nested | `visual-production/types/type-nested.md` |
| Parent-to-child relationships | Tree | `visual-production/types/type-tree.md` |
| Ownership, reporting, routing, or escalation | Org chart | `visual-production/types/type-org-chart.md` |
| Stacked abstraction levels | Layer stack | `visual-production/types/type-layers.md` |
| Overlap between sets | Venn | `visual-production/types/type-venn.md` |
| Ranked hierarchy or conversion drop-off | Pyramid / funnel | `visual-production/types/type-pyramid.md` |
| Quantitative comparison across categories | Bar chart | `visual-production/types/type-bar.md` |
| Part-to-whole relationships encoded by area | Treemap | `visual-production/types/type-treemap.md` |
| Trends over time, change between two states, or ridgelines | Line chart | `visual-production/types/type-line.md` |
| Tasks and phases on a calendar | Gantt | `visual-production/types/type-gantt.md` |
| Distribution and correlation between variables | Scatter plot | `visual-production/types/type-scatter.md` |
| An end-to-end data stack on a container cluster | High-Level | `visual-production/types/type-high-level.md` |
| A multi-actor sequential process with data handoffs | Process | `visual-production/types/type-process.md` |
| Multi-tier data storage, quality, and access policy | Medallion | `visual-production/types/type-medallion.md` |
| Who performs each pipeline step | Data flow | `visual-production/types/type-data-flow.md` |
| Data-platform sources, core, and consumers | DP integration | `visual-production/types/type-dp-integration.md` |
| Per-role or per-component access permissions | DP security matrix | `visual-production/types/type-dp-security-matrix.md` |
| Quantities that split and merge across stages | Sankey | `visual-production/types/type-sankey.md` |
| Grouped causes leading to one observed effect | Fishbone | `visual-production/types/type-fishbone.md` |
| A value chain positioned against evolution | Wardley map | `visual-production/types/type-wardley.md` |
| Work in progress by state and limit | Kanban | `visual-production/types/type-kanban.md` |
| Actions and sentiment across experience stages | User journey | `visual-production/types/type-journey.md` |
| Zones, hosts, artifacts, replicas, and ports | Deployment | `visual-production/types/type-deployment.md` |
| Fan-in, ranks, and cycles among dependencies | Dependency graph | `visual-production/types/type-dependency.md` |
| Classes, operations, and typed relationships | UML class | `visual-production/types/type-uml-class.md` |
| A narrative backbone sliced into releases | Story map | `visual-production/types/type-story-map.md` |
| Physical tables, column types, constraints, indexes, and foreign keys | Database schema | `visual-production/types/type-db-schema.md` |

Do not treat a generic `Chart`, `Flow`, `Matrix`, or `Architecture` umbrella as support for a specialized type. The selected type reference owns its quantitative encoding, geometry, complexity budget, and completion checks.

## Non-Diagram-Design outputs

- Use ImageGen for an illustrated conceptual explanation whose meaning depends on concrete visual cues rather than exact relationships.
- Use HTML or a visualization tool for adjustable exploration that cannot be expressed as a complete static frame.

## Semantic rules

- Treat containment, ownership, association, dependency, sequence, and data flow as different claims.
- Use arrows only for real direction or transition. Label a protocol, event, payload, or guarantee only when it matters.
- Show boundaries when ownership, trust, deployment, or failure isolation is part of the judgment.
- Match geometry, direction, labels, state, and color to supported claims.
- Preserve meaning without color alone and keep text readable at destination width.
- Inspect the final render for clipping, overlap, unintended crop, malformed text, or watermark.
