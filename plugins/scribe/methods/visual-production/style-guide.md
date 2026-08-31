# Diagram Design style interface

Use Diagram Design as four layers:

1. Semantics select the visual type and preserve the meaning of nodes, boundaries, relationships, and quantities.
2. Composition applies the type's hierarchy, routing, alignment, density, and whitespace.
3. Components define shapes, typography, spacing, border weight, tags, labels, and connectors.
4. The selected theme supplies **colors only**.

Keep layers 1–3 unchanged when switching skins. Use the pinned Diagram Design type contracts, component primitives, and specimens as their authority. A skin must not change fonts, font sizes, radius, stroke width, node proportions, layout, labels, component roles, or emphasis assignments. Treat a requested typography or layout change as a separate operation.

## Theme selection

Resolve one theme in this order:

1. an explicit user-supplied theme, bundled skin name, or color token set;
2. the consuming artifact's or project's established theme or design system;
3. the bundled [Scribe Plotly theme](themes/scribe-plotly.md).

Scribe Plotly is the bundled default theme, not the only permitted theme. Keep the upstream skins available: [Diagram Design light](themes/diagram-design.md), [Diagram Design dark](themes/diagram-design-dark.md), and the opt-in [terminal palette](themes/diagram-design-terminal.md). Selecting terminal colors does not add terminal-window geometry. See [skin application](themes/README.md) for switching, export, and adding a palette.

Rebind every bundled specimen through its explicit color slots with `apply_theme.py`, including for the default. Keep the role markers in editable source; resolve colors to literals for standalone SVG export. Use a complete selected palette; fail on a missing role instead of silently keeping another skin's fallback. Render dark output only from an explicit dark palette.

Literal colors in adapted type references describe the upstream skin. Resolve them through the corresponding semantic role. Preserve their non-color values, including type-specific stroke and radius exceptions.

## Color interface

| Roles | Use |
|---|---|
| `paper`, `paper-2`, `object` | Canvas, secondary surfaces, ordinary foreground nodes |
| `ink`, `muted`, `soft` | Primary text/strokes, secondary text/relationships, tertiary labels |
| `ink-strong`, `inverse-ink` | Filled bands and readable text on those bands |
| `rule`, `rule-solid` | Hairlines and group borders |
| `group-surface` | Group background; may be `none` |
| `object-border`, `deemphasized-border` | Compatibility aliases for ordinary and supporting borders |
| `accent`, `accent-tint` | Source-supported focus |
| `link` | Protocol-bearing/external relationships |
| `success`, `warning`, `failure`, matching `-tint` | Source-supported states |
| `category-1..5`, `series-1..5`, matching `-tint` | Explicit categorical encodings and quantitative series |
| `connector-label-surface`, `boundary-label-surface` | Label masks; retain their geometry even for transparent paint |
| `annotation-neutral-leader`, `annotation-accent-leader`, `annotation-muted-leader` | Editorial leaders |
| `quantitative-connector-alpha` | Quantitative connector color opacity |

Derive `ink @ α`, `muted @ α`, and other alpha variants from the selected base color while preserving the component's specified alpha. Keep color opacity separate from stroke width. Pair category/status encodings with labels or other non-color cues.

## Typography

Use the shared [typography profile](typography.md), independently of theme selection.

| Role | Family | Size | Weight |
|---|---|---:|---:|
| Title | Instrument Serif | 28 px | 400 |
| Node name | Geist sans | 12 px | 600 |
| Sublabel / concise description | Geist Mono for technical content; Geist sans for prose | 9 px | 400 |
| Eyebrow / type tag | Geist Mono | 7–8 px | 500 |
| Connector label | Geist Mono for technical content; Geist sans for prose | 8 px | 400 |
| Editorial callout | Instrument Serif italic | 14 px | 400 |

Keep names in sans and reserve mono for technical content. Add appropriate CJK fallbacks without enlarging descriptions to title size. Keep short natural-language descriptions subordinate to names. Preserve explicit type-specific typography, such as 8.5 px legend text.

## Stroke, radius, and grid

| Token | Value | Use |
|---|---:|---|
| `stroke-thin` | 0.8 | Tag outlines, leaf nodes, quiet groups |
| `stroke-default` | 1 | Node borders and ordinary strokes |
| `stroke-strong` | 1.2 | Supported emphasis |
| `radius-sm` | 4 | Small components |
| `radius-md` | 6 | Node boxes |
| `radius-lg` | 8 | Containers |
| `grid` | 4 | General layout grid |

Use no shadows. Keep every coordinate, width, height, padding, and gap on the 4 px grid unless the chosen primitive specifies an exception. Preserve the upstream full node's 2 px tag radius, 7 px tag text, 9 px sublabel, and type-specific stroke widths; the general grid must not round those into different components.

Size boxes to their names and padding, using the selected type's proportions. The architecture specimen uses 128–160 × 64 px nodes; those are examples, not a universal fixed width. Keep peer nodes aligned and equally sized when their roles and content permit it. Keep the whole component's scale consistent at destination width; widening the canvas or boxes independently makes the same 1 px border look weak.

## Component treatments

Apply the upstream semantic treatments before binding any palette:

| Component | Fill | Stroke |
|---|---|---|
| Backend / ordinary object | `object` | `ink` |
| Store | `ink @ 0.05` | `muted` |
| External service | `ink @ 0.03` | `ink @ 0.30` |
| Input / reader | `muted @ 0.10` | `soft` |
| Optional / future object | `ink @ 0.02` | `ink @ 0.20`, dashed `4,3` |
| Security boundary | `accent @ 0.05` | `accent @ 0.50`, dashed `4,4` |
| Source-identified focal object | `accent-tint` | `accent` |
| Group / boundary | `group-surface` | `rule-solid` or the type's quieter ink-alpha border |

Use an opaque `paper` mask beneath translucent node fills. Retain the full component pattern in [the SVG guide](svg-guide.md), including a rectangular tag when the source supplies a useful type label. Preserve optional decoration when recoloring an existing visual; choose decoration separately when creating one.

Use these component treatments as the structural base, then apply the default category paint described in [the Scribe profile](scribe-profile.md). Keep component geometry and source-supported state treatments intact. Let the profile own category assignment and the palette own color values; selecting another skin must preserve the same category assignments.

The skin change is complete when only paint values differ and the diagram retains identical content, geometry, typography, component treatments, and visual hierarchy.
