# Restore Scribe's multicolor default

Status: resolved

## Intended behavior

Scribe is a multicolor default skin. New visuals use category paint for source-defined groups, layers, stages, or object types without an extra user request. Category identifies membership, not focal or risk state. Keep native geometry and typography. Keep the original light, dark, and terminal palettes selectable; switching palettes preserves category assignments. Do not recolor unrelated existing user assets as part of updating the plugin.

## Cause and evidence

Restoring native Diagram Design components accidentally restored a neutral-only generation policy as well. The source profile restricted category paint to an explicit user request, the style guide repeated that restriction, and the theme said selecting it did not assign architecture colors. A delivery generator consequently discarded supplied category classes. The installed palette still contained all five colors and matched the repository; resolving category-3 slots correctly produced purple. Thus the defect was category assignment, not missing tokens, export, or plugin cache.

The earlier differential loop found 34 changed category assignments out of 39 in six delivered figures. The minimal example was one node whose purple fill/border became ordinary object/ink. The user subsequently narrowed visual delivery to one panorama and explicitly confirmed multicolor as the default. That panorama is already corrected; the historical six figures are not rewritten in this plugin update.

## Fix

- Make the shared source profile own multicolor category assignment by default, including architecture and the single-category case.
- Separate category identity from emphasis and status; retain the native component under the paint.
- Replace contradictory style/theme prose with pointers to that authority.
- Supply a grouped starting asset with actual colored nodes and boundaries; route grouped Architecture generation to it.
- Give the general SVG starter category paint instead of neutral paint.
- Keep the original 40 upstream assets' non-color bytes and all alternative palettes unchanged.

## Verification

The grouped-template export regression was written first and failed because the colored starting asset was absent. It now checks six actual node paints across three groups, native dimensions/radius/stroke, absence of focal/status slots, and palette round trips. Existing component guards now recognize multi-class nodes instead of requiring an exact neutral class string. All 128 repository tests, canonical/generated plugin validators, shell syntax, and whitespace checks pass.

A template test cannot deterministically prove a language model follows prose. An independent forward check therefore receives only source content and the updated packaged skill, without color hints or the diagnosis; its generated artifact is inspected separately. Keep that limitation explicit rather than substituting keyword tests for behavioral validation.

No diagnostic logging was added to production scripts. The prior one-off differential checker is retained under the explicitly named debug/ directory. Do not treat neutral output as success merely because unused category tokens are present.

## Installed result

Installed `scribe@goqihoo` version `0.9.0+codex.20260831121752` through the supported CLI update flow. The installed six changed skill/asset/method files match the generated package byte for byte; relative asset links resolve, all three original skins remain present, and package synchronization passes.

The independent invocation, given source content without any color request, selected the default Scribe palette and produced six colored nodes across three distinct category colors. Actual node paints and native component attributes were inspected in the generated SVG. A feedback-target ambiguity found during visual review was corrected in that temporary check artifact. The final artifact retains six nodes and seven directed relationships with an explicit feedback target. That correction did not change the automatically selected default category colors or the shipped skill.
