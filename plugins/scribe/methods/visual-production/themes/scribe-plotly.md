# Scribe Plotly theme

Use this as the zero-configuration **multicolor default skin** for the Diagram Design style interface. Apply its category palette through the [Scribe profile](../scribe-profile.md), including for architecture diagrams. It is a light theme; do not synthesize a dark variant from the upstream Diagram Design palette.

## Color tokens

| Token | Value | Use |
|---|---:|---|
| `inverse-ink` | `#FFFFFF` | Text on dark strong surfaces |
| `ink-strong` | `#22263A` | Strong filled bands |
| `paper` | `#FFFFFF` | Canvas |
| `paper-2` | `#EEF1F7` | Secondary surfaces, including durable stores |
| `group-surface` | `none` | Unpainted grouping containers and boundaries |
| `object` | `#F7F8FC` | Ordinary nodes and foreground panels |
| `ink` | `#22263A` | Primary text and strong strokes |
| `muted` | `#596174` | Secondary text and ordinary relationships |
| `soft` | `#6F788C` | Sublabels, boundary labels, and tertiary strokes |
| `rule` | `#DCE1EA` | Guides, grids, and hairlines |
| `rule-solid` | `#CBD2DF` | Group borders and stronger separators |
| `object-border` | `#22263A` | Ordinary object borders; alias of `ink` |
| `deemphasized-border` | `#A6AFBF` | Supporting objects and groups |
| `accent` | `#4F5BD5` | Source-identified focus |
| `accent-tint` | `#E9EBFE` | Focal surface |
| `link` | `#007A59` | External or protocol-bearing relationships |
| `success` | `#007A59` | Supported success state |
| `success-tint` | `#DDF8F0` | Success surface |
| `warning` | `#B95D18` | Supported warning state |
| `warning-tint` | `#FFF0E4` | Warning surface |
| `failure` | `#D43E26` | Supported failure or rejection state |
| `failure-tint` | `#FDE9E5` | Failure surface |
| `category-1` | `#4F5BD5` | Category or series stroke |
| `category-1-tint` | `#E9EBFE` | Category or series surface |
| `category-2` | `#007A59` | Category or series stroke |
| `category-2-tint` | `#DDF8F0` | Category or series surface |
| `category-3` | `#8240C9` | Category or series stroke |
| `category-3-tint` | `#F3E9FE` | Category or series surface |
| `category-4` | `#D43E26` | Category or series stroke |
| `category-4-tint` | `#FDE9E5` | Category or series surface |
| `category-5` | `#B95D18` | Category or series stroke |
| `category-5-tint` | `#FFF0E4` | Category or series surface |
| `series-1` | `#007A59` | Non-focal quantitative series stroke |
| `series-1-tint` | `#DDF8F0` | Non-focal quantitative series surface |
| `series-2` | `#8240C9` | Non-focal quantitative series stroke |
| `series-2-tint` | `#F3E9FE` | Non-focal quantitative series surface |
| `series-3` | `#B95D18` | Non-focal quantitative series stroke |
| `series-3-tint` | `#FFF0E4` | Non-focal quantitative series surface |
| `series-4` | `#D43E26` | Non-focal quantitative series stroke |
| `series-4-tint` | `#FDE9E5` | Non-focal quantitative series surface |
| `series-5` | `#6F788C` | Non-focal quantitative series stroke |
| `series-5-tint` | `#EEF1F7` | Non-focal quantitative series surface |
| `connector-label-surface` | `none` | Transparent connector-label background |
| `boundary-label-surface` | `#FFFFFF` | Boundary-label background |
| `annotation-neutral-leader` | `rgba(34,38,58,0.40)` | Neutral editorial-callout leader |
| `annotation-accent-leader` | `rgba(79,91,213,0.50)` | Focal editorial-callout leader |
| `annotation-muted-leader` | `rgba(34,38,58,0.30)` | Tertiary editorial-callout leader |
| `quantitative-connector-alpha` | `0.55` | Quantitative relationship-stroke opacity |

Keep non-focal series colors distinct from `accent`. Category is not status. Pair every category color with a label, shape, position, or line treatment, and use a status token only when the source establishes that state.

## Color scope

Use the shared component treatments in `../style-guide.md` and the default category assignment in `../scribe-profile.md`. Keep fonts, geometry, component roles, and category membership independent of the selected palette.
