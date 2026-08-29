# Diagram Design provenance

The 39 type contracts, semantic patterns, icon primitive, annotation primitive, HTML starter, HTML validator, and type specimens in this directory and `skills/draw-diagram/` are adapted from [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) commit `ac490fd1ac4b4014100f93e729cb4ad198700bd4` (Diagram Design 2.6).

The upstream work is MIT-licensed. See `DIAGRAM_DESIGN_LICENSE.txt` and `THIRD_PARTY_LICENSES.md`.

Scribe keeps the upstream type contracts intact except for packaging adaptations: local links point at Scribe's shared method paths, bundled examples are discovered by type slug instead of repeated per-file sections, and verifier pointers resolve inside the packaged `draw-diagram` skill. Source adaptation lives in `scribe-profile.md`; the replaceable style interface lives in `style-guide.md`; and `themes/scribe-plotly.md` supplies the bundled default skin.
