# Diagram style

Use a calm technical-editorial system: warm canvas, neutral surfaces, slate text and structure, sparse semantic accents, flat geometry, and generous whitespace.

## Tokens

| Role | Value | Use |
|---|---:|---|
| Canvas | `#F8FAFC` | Default background |
| Surface | `#FFFFFF` | Default fill for objects, groups, and panels |
| De-emphasized surface | `none` | Supporting object or group; retain its border and label |
| Text | `#0F172A` | Titles and names |
| Secondary text | `#64748B` | Annotations |
| Border | `#CBD5E1` | Normal boundaries |
| Connector | `#94A3B8` | Ordinary relationships |
| Emphasis | `#2563EB` / `#EFF6FF` | Source-identified focal element or path only |
| Success | `#16A34A` / `#F0FDF4` | Verified or healthy state only |
| Warning | `#D97706` / `#FFF7ED` | Delay, retry, or degradation only |
| Error | `#DC2626` / `#FEF2F2` | Failure, rejection, or attack only |
| External | `#7C3AED` / `#F3E8FF` | External actor or platform |

Give object and group containers a Surface fill by default. For a deliberately de-emphasized object or group, use transparent fill while keeping its outline and label readable.

Do not color every peer differently by default. When color identifies real categories, retain labels and do not let category colors imply status.

## Typography and spacing

- Use `Inter`, `Noto Sans SC`, or `PingFang SC`; use `JetBrains Mono` for protocols or symbols.
- Use 20–24 px titles, 14–16 px node names, and at least 11–12 px annotations.
- Use the object name alone when it makes the role clear. Add one short responsibility phrase only when it changes interpretation; keep sentences and explanatory prose outside nodes.
- Use an 8 px spacing grid, 8–12 px corner radius, 1–1.5 px normal borders, and 2 px only for source-identified emphasis.
- Keep peer nodes aligned and equally sized when their roles are equal.

## Shape and connector meaning

| Form | Meaning |
|---|---|
| Rounded rectangle | Logical service, module, or application |
| Rectangle | Runtime unit or process |
| Cylinder | Durable storage or log |
| Pill or actor | User, client, or external actor |
| Solid container | Ownership, trust, domain, or deployment boundary |
| Dashed container | Optional, future, or logical scope |
| Solid arrow | Synchronous, gating, or definite flow |
| Dashed arrow | Asynchronous, delayed, optional, or eventual flow |
| Red arrow | Failure, rejection, or exceptional flow |

Name every boundary. Use a double-headed arrow only for a genuinely bidirectional interaction.

## Layout

- Use left-to-right for request, business, and data flows; top-to-bottom for layers and decision trees; outside-to-inside for trust; normal direction with failures branching downward.
- Keep one primary axis. Restructure or split when crossings remain.
- Separate context, component, deployment, sequence, and failure views rather than mixing them.
- Default to `1200 × 800` for documents and `1600 × 900` for wide presentation output.

## Grammar-specific composition

| Grammar | Composition | Completion test |
|---|---|---|
| Context map | Put the scoped subject inside a named boundary and arrange external actors around it. Show only relationships that cross the boundary. | The reader can identify the scope and each external dependency without reading an internal design. |
| Ownership or container map | Place each responsibility once inside named ownership, trust, or domain containers. Use nesting only when it carries real containment. | Ownership and separation are clear without implying a sequence. |
| Component or layer view | Keep peers at one abstraction level, align them by layer or responsibility, and direct only real dependencies. | The reader can see both responsibility decomposition and dependency direction. |
| Matrix | Use two independent dimensions as axes and one consistent meaning per cell. Include a legend when marks are not self-explanatory. | The reader can locate and compare every mapping without reconstructing it from prose. |
| Flow or lifecycle | Use one primary direction with an explicit entry and outcome. Make decisions branch, rejoin, or terminate visibly. | Every supported path can be followed without guessing where it starts, ends, or loops. |
| Sequence | Arrange participants across the top and time downward. Distinguish calls, responses, concurrency, retries, and acknowledgments only when they matter. | Message order and temporal behavior are unambiguous. |
| State diagram | Draw stable states as nodes and label transitions with the triggering event or guard. Include initial and terminal states only when supported. | Each allowed transition is clear and activities are not mistaken for states. |
| Deployment | Put runtime units inside named environment, host, network, or failure-domain boundaries and show placement or multiplicity when material. | The reader can tell where software runs and which isolation claims the topology makes. |
| Failure-mode view | Establish the ordinary path neutrally, then branch the supported rejection, timeout, degradation, or recovery path at its cause. | Cause, propagation, outcome, and recovery can be distinguished without treating the failure as the default state. |
| Chart | Choose an encoding that matches the comparison, label units and sources, and preserve an honest scale. | Values can be compared without visual distortion or missing quantitative context. |
| Illustrated conceptual infographic | Organize one mental model around a central idea and use a small number of concrete visual cues. | The cues clarify the concept without inventing relational or operational claims. |
| Interactive explanation | Bind each control to an explicit variable, show the current state, and provide a clear return to the base state. | The reader can explore effects and recover the starting view without losing context. |

## Accessibility and delivery

- Pair semantic colors with labels, shapes, or line styles; avoid red/green-only meaning.
- Add an accessible title and description to SVG or HTML and meaningful alt text to raster output.
- Retain editable source beside exports and use relative links from Markdown.
- Inspect both source and render; syntax validity alone is insufficient.
