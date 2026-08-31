# Shared typography

Use Diagram Design’s Instrument Serif / Geist / Geist Mono families for every color skin. Add CJK fallbacks without changing the 12 px name / 9 px sublabel hierarchy. Typography is a separate, explicit user or destination override; color selection never changes these values.

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

Use these conservative measurement estimates for static label-fit verification; inspect the actual render with the chosen fonts before delivery.
