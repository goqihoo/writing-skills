# Diagram Design provenance

The 39 type contracts, semantic patterns, icon primitive, annotation primitive, HTML starter, HTML validator, and type specimens in this directory and `skills/draw-diagram/` are adapted from [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) commit `ac490fd1ac4b4014100f93e729cb4ad198700bd4` (Diagram Design 2.6).

The upstream work is MIT-licensed. See `DIAGRAM_DESIGN_LICENSE.txt` and `THIRD_PARTY_LICENSES.md`.

Scribe keeps the upstream type contracts intact except for packaging adaptations: local links point at Scribe's shared method paths, bundled examples are discovered by type slug instead of repeated per-file sections, and verifier pointers resolve inside the packaged `draw-diagram` skill. Source adaptation lives in `scribe-profile.md`; the replaceable style interface lives in `style-guide.md`; and `themes/scribe-plotly.md` supplies the bundled default skin.

`UPSTREAM_TYPE_CONTRACTS.json` records the normalized SHA-256 snapshot for all 39 contracts. The routing test reverses only the packaging adaptations above before comparing each current contract with that fixed snapshot; any other contract edit must fail the test.

## Color-only specimen import

Import the 39 type specimens and HTML starter directly from the pinned source with `scripts/sync-diagram-design-skins.py`. Preserve every non-color byte, including labels, type tags, 7/9/12 px typography, markers, radii, stroke widths, layout, masks, and optional decorations. Store semantic color slots with Scribe fallbacks, then bind any palette with `apply_theme.py`. Specimen labels remain examples, not evidence about the user's system.

`UPSTREAM_VISUAL_CONTRACTS.json` records the original file hashes and hashes after removing color values only. Tests compare each shipped specimen with that fixed non-color snapshot and exercise palette round trips. Keep the original light/dark palettes selectable; also retain terminal colors as an opt-in palette. Keep font choices in `typography.md`, outside skins.

The standalone SVG starter uses the upstream node/mask and 8 × 6 arrowhead primitives. Its text content is a generic neutral example. Scribe retains source-supported content adaptation, editable SVG delivery, accessible labels, CJK fallbacks, and default transparent grouping/connector-label paints as explicit integration choices; these do not belong to a skin's geometry or typography.
