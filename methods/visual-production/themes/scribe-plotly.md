# Scribe Plotly theme

Use this as the zero-configuration default adapter for the Diagram Design style interface. It is a light theme; do not synthesize a dark variant from the upstream Diagram Design palette.

## Color tokens

| Token | Value | Use |
|---|---:|---|
| `paper` | `#FFFFFF` | Canvas |
| `paper-2` | `#EEF1F7` | Grouping containers and secondary surfaces |
| `object` | `#F7F8FC` | Ordinary nodes and foreground panels |
| `ink` | `#22263A` | Primary text and strong strokes |
| `muted` | `#596174` | Secondary text and ordinary relationships |
| `soft` | `#6F788C` | Sublabels, boundary labels, and tertiary strokes |
| `rule` | `#DCE1EA` | Guides, grids, and hairlines |
| `rule-solid` | `#CBD2DF` | Group borders and stronger separators |
| `object-border` | `#C3CBD9` | Ordinary object borders |
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
| `series-1` | `#4F5BD5` | Quantitative series stroke; alias of `category-1` |
| `series-1-tint` | `#E9EBFE` | Quantitative series surface; alias of `category-1-tint` |
| `series-2` | `#007A59` | Quantitative series stroke; alias of `category-2` |
| `series-2-tint` | `#DDF8F0` | Quantitative series surface; alias of `category-2-tint` |
| `series-3` | `#8240C9` | Quantitative series stroke; alias of `category-3` |
| `series-3-tint` | `#F3E9FE` | Quantitative series surface; alias of `category-3-tint` |
| `series-4` | `#D43E26` | Quantitative series stroke; alias of `category-4` |
| `series-4-tint` | `#FDE9E5` | Quantitative series surface; alias of `category-4-tint` |
| `series-5` | `#B95D18` | Quantitative series stroke; alias of `category-5` |
| `series-5-tint` | `#FFF0E4` | Quantitative series surface; alias of `category-5-tint` |
| `connector-label-surface` | `none` | Transparent connector-label background |
| `boundary-label-surface` | `#FFFFFF` | Boundary-label background |
| `annotation-neutral-leader` | `rgba(34,38,58,0.40)` | Neutral editorial-callout leader |
| `annotation-accent-leader` | `rgba(79,91,213,0.50)` | Focal editorial-callout leader |
| `annotation-muted-leader` | `rgba(34,38,58,0.30)` | Tertiary editorial-callout leader |
| `quantitative-connector-alpha` | `0.55` | Quantitative relationship-stroke opacity |

Category is not status. Pair every category color with a label, shape, position, or line treatment, and use a status token only when the source establishes that state.

## Font-family tokens

| Token | Value | Use |
|---|---|---|
| `font-title` | `Instrument Serif` | Titles and editorial callouts |
| `font-sans` | `Geist, Noto Sans SC, PingFang SC, sans-serif` | Names and natural-language descriptions |
| `font-mono` | `Geist Mono, Noto Sans Mono CJK SC, monospace` | Technical labels and compact metadata |
| `font-sans-advance` | `0.60` | Conservative narrow-glyph advance in em for `font-sans` |
| `font-mono-advance` | `0.62` | Conservative mono-glyph advance in em for `font-mono` |
| `font-wide-advance` | `1.00` | Conservative wide/full-width glyph advance in em |
| `font-ascent` | `0.74` | Conservative ascent in em |
