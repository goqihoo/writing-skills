# Diagram Design profile

Use Diagram Design as four layers:

1. Diagram semantics select the visual type and preserve the meaning of nodes, boundaries, relationships, and quantitative encodings.
2. Composition applies the selected type's hierarchy, direction, routing, alignment, density, and whitespace rules.
3. Components define shapes, typography, spacing, border weight, labels, icons, and connector forms.
4. The color theme binds canvas, surface, text, border, connector, status, and category tokens.

The type references and this profile own the first three layers. Use the Scribe Plotly theme below for the fourth. A theme change may rebind only color tokens; preserve visual type, composition, component geometry, typography roles, label treatment, and emphasis meaning.

## Scribe Plotly theme

Use semantic roles in instructions and generated source. The hex values below are the only bundled light-theme values.

The bundled Scribe theme is light only. Treat dark-mode subsections retained in an adapted type reference as dormant composition notes; do not render a dark variant until an explicit Scribe dark token set exists. Never restore the upstream palette to satisfy a dark-mode example.

| Role | Value | Use |
|---|---:|---|
| `paper` | `#FFFFFF` | Canvas and label masks |
| `paper-2` | `#F5F6FB` | Grouping containers and secondary surfaces |
| `object` | `#FFFFFF` | Ordinary nodes and foreground panels |
| `ink` | `#22263A` | Primary text and strong strokes |
| `muted` | `#596174` | Secondary text and ordinary relationships |
| `soft` | `#6F788C` | Sublabels, boundary labels, and tertiary strokes |
| `rule` | `#DCE1EA` | Guides, grids, and hairlines |
| `rule-solid` | `#CBD2DF` | Group borders and stronger separators |
| `object-border` | `#C3CBD9` | Ordinary object borders |
| `deemphasized-border` | `#A6AFBF` | Supporting objects and groups |
| `accent` | `#4F5BD5` | Source-identified focus; zero by default |
| `accent-tint` | `#E9EBFE` | Soft fill paired with `accent` stroke |
| `link` | `#007A59` | External or protocol-bearing relationships when distinction matters |
| `success` | `#007A59` / `#DDF8F0` | Supported success state only |
| `warning` | `#B95D18` / `#FFF0E4` | Supported warning state only |
| `failure` | `#D43E26` / `#FDE9E5` | Supported failure or rejection state only |

### Category palette

Use these pairs for peer categories and multi-series encodings. A deep color is the border, stroke, or mark; its matching tint is the surface. Category is not status.

| Token | Deep | Tint |
|---|---:|---:|
| `category-1` / `series-1` | `#4F5BD5` | `#E9EBFE` |
| `category-2` / `series-2` | `#007A59` | `#DDF8F0` |
| `category-3` / `series-3` | `#8240C9` | `#F3E9FE` |
| `category-4` / `series-4` | `#D43E26` | `#FDE9E5` |
| `category-5` / `series-5` | `#B95D18` | `#FFF0E4` |

Use the palette only when color distinguishes a real category or series. Pair it with a label, shape, position, or line treatment. Keep uncategorized peers neutral.

## Emphasis contract

Start every diagram with zero focal elements. Use one focal element, or at most two when comparison requires it, only when the source or user establishes focus. A generated template or specimen must not invent an active, selected, primary, risky, or successful state.

When focus is supported, use `accent-tint` fill with `accent` stroke. Do not use a category color as decoration, and do not reinterpret green, orange, or coral as status without source evidence.

## Typography

Preserve Diagram Design's typography roles.

| Role | Family | Size | Weight | Use |
|---|---|---:|---:|---|
| Title | Instrument Serif | 28 px | 400 | Diagram title only |
| Node name | Geist | 12 px | 600 | Human-readable names |
| Sublabel | Geist Mono | 8–9 px | 400 | Ports, URLs, types, and compact technical data |
| Eyebrow or tag | Geist Mono | 8 px | 500 | Type tags and axes |
| Connector label | Geist Mono | 8 px | 400 | Short relationship labels |
| Callout | Instrument Serif italic | 16 px | 400 | Optional editorial aside |

For Chinese labels, extend Geist with `Noto Sans SC`, `PingFang SC`, or the destination's established CJK sans. Extend Geist Mono with a CJK mono fallback for technical strings. Keep names in sans and reserve mono for genuinely technical content.

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

Use the object name alone when it makes the role clear. Add one short responsibility phrase only when it changes interpretation. Keep sentences and explanatory prose outside nodes.

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
