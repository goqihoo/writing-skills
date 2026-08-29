# Diagram Design style interface

Use Diagram Design as four layers:

1. Diagram semantics select the visual type and preserve the meaning of nodes, boundaries, relationships, and quantitative encodings.
2. Composition applies the selected type's hierarchy, direction, routing, alignment, density, and whitespace rules.
3. Components define shapes, typography roles, spacing, border weight, labels, icons, and connector forms.
4. A selected theme binds those semantic roles to colors and font families.

The type references and this interface own the first three layers. A theme may rebind semantic color tokens and font-family tokens, their conservative measurement estimates, and explicitly theme-owned opacity values; it must not change the visual type, composition, component geometry, typography roles or sizes, label geometry, or emphasis meaning.

## Theme selection

Resolve one theme before drawing, in this order:

1. an explicit user-supplied theme or token set;
2. the consuming artifact's or project's established theme or design system;
3. the bundled [Scribe Plotly theme](themes/scribe-plotly.md).

Do not interrupt the workflow with a theme question when the first two sources are absent. Scribe Plotly is the bundled default theme, not the only permitted theme.

Rebind every bundled specimen's semantic visual roles to the resolved theme before using it, including when the resolved theme is the bundled default. Treat specimen literals as a historical snapshot, not as current theme authority.

Map every role used by the selected visual to one coherent theme. Derive missing tints, borders, and muted variants from the selected palette and record the mapping in generated source; do not mix values from two themes. Preserve readable contrast and keep focus, status, and category as separate semantic axes. Render a light or dark variant only when the selected theme supplies a complete token set for it.

## Theme interface

A complete theme provides the roles the selected visual uses:

| Role | Use |
|---|---|
| `paper` | Canvas |
| `paper-2` | Grouping containers and secondary surfaces |
| `object` | Ordinary nodes and foreground panels |
| `ink` | Primary text and strong strokes |
| `muted` | Secondary text and ordinary relationships |
| `soft` | Sublabels, boundary labels, and tertiary strokes |
| `rule` | Guides, grids, and hairlines |
| `rule-solid` | Group borders and stronger separators |
| `object-border` | Ordinary object borders |
| `deemphasized-border` | Supporting objects and groups |
| `accent` / `accent-tint` | Source-identified focus |
| `link` | External or protocol-bearing relationships |
| `success` / `success-tint` | Supported success state |
| `warning` / `warning-tint` | Supported warning state |
| `failure` / `failure-tint` | Supported failure or rejection state |
| `category-1..5` / matching tints | Peer categories |
| `series-1..5` / matching tints | Quantitative series; may alias the matching category pair |
| `connector-label-surface` | Connector-label background; may be `none` |
| `boundary-label-surface` | Boundary-label background |
| `annotation-neutral-leader` | Neutral editorial-callout leader |
| `annotation-accent-leader` | Source-supported focal editorial-callout leader |
| `annotation-muted-leader` | Tertiary editorial-callout leader |
| `quantitative-connector-alpha` | Opacity for quantitative relationship strokes |
| `font-title` | Diagram title and display callouts |
| `font-sans` | Human-readable names and descriptions |
| `font-mono` | Technical labels, ports, URLs, and types |
| `font-sans-advance` | Conservative narrow-glyph advance used by static label-fit verification |
| `font-mono-advance` | Conservative mono-glyph advance used by static label-fit verification |
| `font-wide-advance` | Conservative wide/full-width glyph advance used by static label-fit verification |
| `font-ascent` | Conservative ascent used by static label-fit verification |

Literal family names and color values retained in adapted Diagram Design type references describe the upstream skin. Resolve them through the selected theme's semantic role rather than treating them as mandatory output values.

## Typography roles

Preserve these roles and sizes when a theme replaces their font families:

| Role | Size | Weight | Use |
|---|---:|---:|---|
| Title | 28 px | 400 | Diagram title only |
| Node name | 12 px | 600 | Human-readable names |
| Sublabel | 8–9 px | 400 | Ports, URLs, types, and compact technical data |
| Eyebrow or tag | 8 px | 500 | Type tags and axes |
| Connector label | 8 px | 400 | Short relationship labels |
| Callout | 16 px | 400 italic | Optional editorial aside |

Keep names in `font-sans` and reserve `font-mono` for genuinely technical content. A selected theme must provide suitable CJK fallbacks when labels require them.

Bind the four font measurement tokens to the selected font families rather than copying the bundled values into a verifier. They are conservative layout estimates for browser-free inspection, not typography-role or geometry changes.

## Stroke, radius, and grid

| Token | Value | Use |
|---|---:|---|
| `stroke-thin` | `0.8` | Tag outlines and leaf nodes |
| `stroke-default` | `1` | Ordinary strokes |
| `stroke-strong` | `1.2` | Supported emphasis |
| `radius-sm` | `4` | Tags |
| `radius-md` | `6` | Nodes |
| `radius-lg` | `8` | Containers |
| `grid` | `4` | Coordinates, dimensions, and gaps |

Use no shadows. Keep every coordinate, width, height, padding, and gap on the 4 px grid. Use rectangular tags with small radii rather than pills. Keep peer nodes aligned and equally sized when their roles are equal.

## Component treatments

| Component | Fill | Stroke |
|---|---|---|
| Ordinary object | `object` | `object-border` |
| Group or boundary | `paper-2` | `rule-solid` |
| Categorized object | matching category tint | matching category deep color |
| Supporting object | `none` | `deemphasized-border` |
| Durable store | `paper-2` | `muted` |
| External actor or system | `none` | `soft` |
| Optional or future object | `none` | `deemphasized-border`, dashed `4,3` |
| Source-identified focal object | `accent-tint` | `accent` |

Give grouping containers and nested objects different surfaces so both levels remain visible. Name every semantic boundary. Do not use a background rectangle merely to decorate a cluster that has no containment meaning.

## Shape meaning

| Form | Meaning |
|---|---|
| Rounded rectangle | Logical service, module, application, or step |
| Rectangle | Runtime unit or process |
| Cylinder | Durable storage or log |
| Pill or actor | User, client, or external actor |
| Solid container | Ownership, trust, domain, or deployment boundary |
| Dashed container | Optional, future, or logical scope |
| Solid arrow | Synchronous, gating, or definite flow |
| Dashed arrow | Asynchronous, delayed, optional, or eventual flow |
| Failure-colored arrow | Rejection or exceptional flow supported by the source |

Use a double-headed arrow only for a genuinely bidirectional relationship.
