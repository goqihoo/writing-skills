# Applying and adding color skins

Use these instructions for a color-only restyle, after choosing the type and its component treatment. Use `../typography.md` for fonts independently of palette selection.

| ID | Palette |
|---|---|
| `scribe-plotly` | Scribe default, light |
| `diagram-design` | Original Diagram Design light |
| `diagram-design-dark` | Original Diagram Design dark |
| `diagram-design-terminal` | Original terminal colors; no automatic window chrome |

## Switch a skin

Run from the `skills/draw-diagram/` directory (the same relative layout ships in the plugin):

```sh
python3 scripts/apply_theme.py assets/examples/example-architecture.html /tmp/architecture.html --theme diagram-design
python3 scripts/apply_theme.py assets/editorial-diagram-template.svg /tmp/diagram.svg --theme scribe-plotly --resolve
```

Read only the selected type specimen. Preserve `var(--dd-ROLE, COLOR)` markers while adapting its source content. The fallback makes HTML specimens directly viewable in the default skin; `apply_theme.py` refreshes every marked color from the selected palette. It does not infer roles by replacing identical hex strings.

Use base slots such as `var(--dd-ink, #22263A)` and derived alpha slots such as `var(--dd-ink-a050, rgba(34,38,58,0.05))`. The suffix records opacity in thousandths (`a050` = 5%, `a400` = 40%). Use slots only for paint, never font, geometry, layout, or visible text. Use explicit roles for surfaces, focus, and series; preserve the type's alpha variants.

Keep tokenized SVG as editable source and use `--resolve` to create a second SVG with literal colors before validation, rendering, or embedding. Do not resolve over the editable source. HTML can retain slots. Preserve unmarked colors in third-party logos only when required by the source; otherwise assign roles to all paint before switching. For old unmarked diagrams, audit and assign roles once rather than guessing semantics from repeated hex values.

Keep names, descriptions, node types, tags, focus assignments, geometry, stroke widths, font properties, paths, and optional decorations identical for a color-only restyle. Do not run source-content adaptation or auto-layout as part of switching.

## Add a skin

1. Copy a bundled theme to a new Markdown file and give it a distinct name. Keep its token keys and replace color values only. Keep RGB channels in 0–255 and opacity in 0–1; keep `ink` and other alpha bases as six-digit hex colors.
2. Pass the new path with `--theme path/to/new-skin.md`. A file placed in this directory also resolves by its filename without `.md`; no registry or renderer code change is needed.
3. Run it against the selected specimen and inspect contrast at destination size. Check that only paint differs; unknown/non-color tokens and missing used roles must fail.
4. Document the new bundled name in this table and rebuild the plugin when shipping it.

Completion requires unchanged content and non-color source, readable contrast, and a validated render in the destination format.
