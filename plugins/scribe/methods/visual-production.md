# Visual production method

Let the consuming Public Skill and selected template decide whether a visual is needed and what it must explain. Once they select a visual, use this Shared Method as the Draw Diagram production contract by default; no additional public invocation is required. Depart from this contract only when the user explicitly requests another production contract or a binding destination convention requires one.

Apply this method when the user requests a visual or when the result would otherwise force readers to reconstruct a central relationship. Create the smallest visual that answers one important question, and retain prose or a table when either is clearer.

## Decision

Inspect a visual candidate when the content contains four or more meaningful nodes or relationships; three or more dependent stages with material intermediate state; branching, convergence, cycles, or bidirectional correspondence; one source affecting at least three consumers; or important timing, hierarchy, ownership, failure, or quantitative shape.

Use prose for one fact or two to three obvious linear steps. Use a Markdown table for compact repeated fields. A count triggers inspection, not decoration.

## Workflow

1. Read `visual-production/content-preparation.md` and establish the figure's context. State one reader question: locate, compare, follow, inspect, recognize, or explore.
2. Prepare the source-supported content model under that method before selecting a visual type or drawing geometry. Repeat this preparation for each figure in a document; retain shared names and facts while establishing each figure's own purpose.
3. When behavior, state, enforcement, or risk carries the meaning, read `visual-production/semantic-patterns.md` and select one primary semantic pattern before choosing layout.
4. Choose one production branch before selecting a visual form:
   - Use **Diagram Design** when exact relationships, direction, hierarchy, state, ownership, or quantitative encoding carry the meaning. Select exactly one of the 39 visual types below, read its linked reference completely, and choose one dominant visual axis.
   - Use **ImageGen** when the reader needs an illustrated conceptual explanation based on recognizable visual metaphors and the source does not require exact topology, sequence, or quantitative encoding. Do not select a Diagram Design type merely to satisfy the catalog.

   Keep a concise working note identifying the source section or request, reader question, scope, selected branch/type, and the relationship or behavior that justifies the choice. Select the type from that meaning, not the document title, node count, node names, or starter asset. Reuse a type across figures when their questions warrant it; choose different types when their explanatory tasks differ. Keep this note outside the reader-facing artifact unless requested.

5. For Diagram Design, read `visual-production/scribe-profile.md` for the small source-adaptation rules, `visual-production/style-guide.md` for the theme interface and selected theme, and `visual-production/svg-guide.md` for production, connector, accessibility, and inspection rules. For ImageGen, read the available ImageGen skill and its prompting guidance.
6. For Diagram Design, map the prepared objects and relationships to the selected type's node, boundary, connector, and quantitative primitives under **Component semantics** in `visual-production/svg-guide.md`. Establish the reading axis and required conditions before adapting a specimen. Apply the chosen type's complexity budget and split overview from detail when it cannot fit. For ImageGen, map each source concept to one recognizable visual cue, keep exact labels minimal, and avoid visual relationships that imply unsupported sequence, hierarchy, or causality.
7. In the Diagram Design branch, bind the chosen theme through explicit color slots using `visual-production/themes/README.md`; preserve component geometry and typography when switching colors. Use editable SVG by default. Use self-contained HTML with inline SVG when the destination needs a web wrapper or interaction. Export PNG from the editable source when raster output is requested. Use Mermaid only when the user explicitly requests Mermaid and state any type-specific fidelity loss. In the ImageGen branch, use its built-in generation workflow and save the inspected final raster into the consuming project's `_assets/` directory.
8. Create and inspect the actual render at full size and roughly 736–900 px wide. Apply **Completion** below against the figure's context as well as the selected type's checks. Fix clipping, overlap, crossings, unreadable labels, misaligned node text, false emphasis, and ambiguous direction.
9. For a file output, use the consuming document's sibling `_assets/` directory by default unless an explicit path or established project convention says otherwise. Keep editable source beside exports when practical. Keep the skill's bundled `assets/` directory for templates and specimens only.
10. Add only meaningful alt text by default. Do not append a visible title, caption, or explanation after the image unless requested or required by the consuming artifact.

## Visual-type routing

For behavior views, choose the diagram from the reader question rather than the document level. Prefer **Flowchart** when readers must choose among entry points, optional stages, independently runnable operations or composed paths, or follow conditions for reuse, waiting and completion. Use **Sequence** when message order, calls, responses or completion acknowledgments between participants carry the explanation. A sequence diagram may include branches, but a single end-to-end trace does not explain alternative routes. Split a routing overview from a local interaction view only when both answer distinct questions; do not require both types for every flow. Keep responsibility owners visible in process-node labels or explicit boundaries, and apply the selected type's reference below.

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

- ImageGen is a first-class production branch selected before Diagram Design type routing, not a fallback after an unsuitable type has been chosen.
- Use HTML or a visualization tool for adjustable exploration that cannot be expressed as a complete static frame.

## Semantic rules

- Treat containment, ownership, association, dependency, sequence, and data flow as different claims.
- Use arrows only for real direction or transition. Label a protocol, event, payload, or guarantee only when it matters.
- Show boundaries when ownership, trust, deployment, or failure isolation is part of the judgment.
- Match geometry, direction, labels, state, and color to supported claims.
- Preserve meaning without color alone and keep text readable at destination width.
- Inspect the final render for clipping, overlap, unintended crop, malformed text, or watermark.

## Completion

Compare the rendered figure with its working note and owning section or standalone request. Verify that a reader can recover the assigned structure, behavior, or quantitative comparison from the visual itself. Trace the material relationships or paths and check their participants, conditions, direction, boundaries, and outcomes against the source; use the selected type's defining encodings to make these visible. A correct nearby paragraph does not repair a misleading figure.

Repair the content mapping or reselect the type when its grammar cannot answer the reader question. Recheck affected figures when their source section or governing model changes; preserve geometry for an explicitly color-only restyle and report an existing semantic defect separately. Treat source validation and rendering checks as production evidence, not proof that the selected type or meaning is correct.

Complete when the context-based semantic review, selected branch/type checks, and actual render inspection pass, and the consuming artifact references the final asset with meaningful alt text and editable source when applicable.
