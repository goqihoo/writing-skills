import re
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "skills/draw-diagram/scripts"))
from apply_theme import SLOT_RE, apply_theme
from theme_tokens import read_theme_tokens

DRAW_DIAGRAM = REPO_ROOT / "skills" / "draw-diagram" / "SKILL.md"
VISUAL_METHOD = REPO_ROOT / "methods" / "visual-production.md"
STYLE_GUIDE = REPO_ROOT / "methods" / "visual-production" / "style-guide.md"
DEFAULT_THEME = (
    REPO_ROOT
    / "methods"
    / "visual-production"
    / "themes"
    / "scribe-plotly.md"
)
SCRIBE_PROFILE = REPO_ROOT / "methods" / "visual-production" / "scribe-profile.md"
CONTENT_PREPARATION = (
    REPO_ROOT / "methods" / "visual-production" / "content-preparation.md"
)
ANNOTATION_PRIMITIVE = (
    REPO_ROOT / "methods" / "visual-production" / "primitive-annotation.md"
)
SVG_GUIDE = REPO_ROOT / "methods" / "visual-production" / "svg-guide.md"
SVG_TEMPLATE = (
    REPO_ROOT / "skills" / "draw-diagram" / "assets" / "editorial-diagram-template.svg"
)
FLOW_TEMPLATE = (
    REPO_ROOT / "skills" / "draw-diagram" / "assets" / "editorial-flow-template.mmd"
)
HTML_TEMPLATE = (
    REPO_ROOT / "skills" / "draw-diagram" / "assets" / "editorial-diagram-template.html"
)
PROCESS_REFERENCE = (
    REPO_ROOT / "methods" / "visual-production" / "types" / "type-process.md"
)
ARCHITECTURE_REFERENCE = (
    REPO_ROOT / "methods" / "visual-production" / "types" / "type-architecture.md"
)
PROCESS_SPECIMEN = (
    REPO_ROOT / "skills" / "draw-diagram" / "assets" / "examples" / "example-process.html"
)


def class_fill(svg: str, class_name: str) -> str:
    svg = SLOT_RE.sub(lambda m: m.group(2), svg)
    rule = re.search(rf"\.{re.escape(class_name)}\s*\{{([^}}]+)\}}", svg)
    if rule is None:
        raise AssertionError(f"Missing SVG class: {class_name}")
    fill = re.search(r"(?:^|;)\s*fill:\s*([^;]+)", rule.group(1))
    if fill is None:
        raise AssertionError(f"Missing fill for SVG class: {class_name}")
    return fill.group(1).strip()


def theme_token(theme: str, token: str) -> str:
    row = re.search(
        rf"^\| `{re.escape(token)}` \| `([^`]+)` \|",
        theme,
        flags=re.MULTILINE,
    )
    if row is None:
        raise AssertionError(f"Missing theme token: {token}")
    return row.group(1)


class DrawDiagramContractTest(unittest.TestCase):
    def test_default_skin_is_a_replaceable_adapter_with_distinct_surfaces(self) -> None:
        style = STYLE_GUIDE.read_text(encoding="utf-8")
        theme = DEFAULT_THEME.read_text(encoding="utf-8")
        svg_template = SVG_TEMPLATE.read_text(encoding="utf-8")

        self.assertIn("themes/scribe-plotly.md", style)
        self.assertIn("Rebind every bundled specimen", style)
        self.assertNotRegex(style, r"#[0-9A-Fa-f]{6}")
        self.assertEqual("#FFFFFF", theme_token(theme, "paper"))
        self.assertEqual("#F7F8FC", theme_token(theme, "object"))
        self.assertNotEqual(
            theme_token(theme, "paper"),
            theme_token(theme, "object"),
        )
        self.assertEqual("none", theme_token(theme, "connector-label-surface"))
        for index in range(1, 6):
            self.assertNotEqual(
                theme_token(theme, "accent"),
                theme_token(theme, f"series-{index}"),
            )
        self.assertEqual(theme_token(theme, "object"), class_fill(svg_template, "node"))

    def test_content_is_prepared_before_type_selection(self) -> None:
        profile = SCRIBE_PROFILE.read_text(encoding="utf-8")
        preparation = CONTENT_PREPARATION.read_text(encoding="utf-8")
        method = VISUAL_METHOD.read_text(encoding="utf-8")
        skill = DRAW_DIAGRAM.read_text(encoding="utf-8")
        type_contracts = [
            path.read_text(encoding="utf-8")
            for path in sorted((STYLE_GUIDE.parent / "types").glob("type-*.md"))
        ]

        self.assertIn("scribe-profile.md", method)
        self.assertIn("scribe-profile.md", skill)
        self.assertIn("Do not invent focus", profile)
        self.assertIn("Clear every specimen-supplied", profile)
        self.assertNotIn("Concise object content", profile)
        self.assertNotIn("one optional short detail", profile)
        self.assertIn("name is the only required content", preparation)
        self.assertIn("one optional short detail", preparation)
        self.assertIn("before selecting a visual type", preparation)
        self.assertIn("content-preparation.md", method)
        self.assertLess(
            method.index("content-preparation.md"),
            method.index("Select exactly one of the 39 Diagram Design visual types"),
        )
        self.assertIn("source-defined semantic categories", profile)
        self.assertNotIn("When another theme is selected", skill)
        self.assertNotIn(
            "Use the bundled Scribe Plotly theme only when",
            method,
        )
        self.assertTrue(
            all("Start with zero focal elements" not in text for text in type_contracts)
        )
        self.assertTrue(
            all("Use `../style-guide.md` for every color" not in text for text in type_contracts)
        )
        self.assertNotIn("### Node text budget", ARCHITECTURE_REFERENCE.read_text(encoding="utf-8"))
        self.assertNotIn(
            "apply that category token to every enclosed categorized object",
            ARCHITECTURE_REFERENCE.read_text(encoding="utf-8"),
        )

    def test_new_svg_color_contract_is_machine_validated(self) -> None:
        skill = DRAW_DIAGRAM.read_text(encoding="utf-8")
        profile = SCRIBE_PROFILE.read_text(encoding="utf-8")
        svg = SVG_GUIDE.read_text(encoding="utf-8")

        self.assertIn("validate_svg.py SOURCE.svg --scribe", skill)
        self.assertIn("data-scribe-color-mode", profile)
        self.assertIn("Palette declarations inside `<defs>` are not visible paint.", profile)
        self.assertIn("validate_svg.py source.svg --scribe", svg)
        for template in (SVG_TEMPLATE, SVG_TEMPLATE.parent / "editorial-grouped-template.svg"):
            with self.subTest(template=template.name):
                root = ET.fromstring(template.read_text(encoding="utf-8"))
                self.assertEqual("categorical", root.get("data-scribe-color-mode"))

    def test_draw_diagram_skill_defers_content_rules_to_the_shared_method(self) -> None:
        skill = DRAW_DIAGRAM.read_text(encoding="utf-8")

        self.assertLess(
            skill.index("Select one reader question and one abstraction level"),
            skill.index("Read `../../methods/visual-production.md`"),
        )
        self.assertNotIn("Prepare the source-supported content", skill)
        self.assertNotIn("Condense explanatory prose", skill)

    def test_connector_label_surface_is_theme_owned_but_geometry_is_preserved(self) -> None:
        theme = DEFAULT_THEME.read_text(encoding="utf-8")
        svg = SVG_GUIDE.read_text(encoding="utf-8")

        self.assertEqual("none", theme_token(theme, "connector-label-surface"))
        self.assertIn("`connector-label-surface`", svg)
        self.assertIn("6–10 px", svg)
        self.assertNotIn("4–8 px", svg)
        self.assertNotIn("Connector labels use transparent fill by default", svg)

    def test_owns_one_visual_per_invocation(self) -> None:
        instructions = DRAW_DIAGRAM.read_text(encoding="utf-8")

        self.assertIn("Create or revise one visual per invocation.", instructions)

    def test_defaults_file_outputs_to_document_assets_directory(self) -> None:
        instructions = VISUAL_METHOD.read_text(encoding="utf-8")

        self.assertIn(
            "use the consuming document's sibling `_assets/` directory by default",
            instructions,
        )
        self.assertIn(
            "Keep the skill's bundled `assets/` directory for templates and specimens only",
            instructions,
        )

    def test_consuming_skill_decides_need_then_defaults_to_draw_diagram_contract(self) -> None:
        instructions = VISUAL_METHOD.read_text(encoding="utf-8")

        self.assertIn(
            "Let the consuming Public Skill and selected template decide whether a visual is needed",
            instructions,
        )
        self.assertIn(
            "use this Shared Method as the Draw Diagram production contract by default",
            instructions,
        )
        self.assertIn(
            "Depart from this contract only when the user explicitly requests another production contract or a binding destination convention requires one",
            instructions,
        )

    def test_templates_start_without_a_default_focus_state(self) -> None:
        profile = SCRIBE_PROFILE.read_text(encoding="utf-8")
        svg_template = SVG_TEMPLATE.read_text(encoding="utf-8")
        flow_template = FLOW_TEMPLATE.read_text(encoding="utf-8")
        html_template = HTML_TEMPLATE.read_text(encoding="utf-8")

        self.assertIn("Do not invent focus", profile)
        self.assertNotIn(".focus", svg_template)
        self.assertNotIn('class="focus"', svg_template)
        self.assertNotIn("Focal component", svg_template)
        self.assertEqual(2, svg_template.count('class="node category-1"'))
        self.assertNotIn("Focal component", flow_template)
        self.assertNotIn("classDef primary", flow_template)
        self.assertNotIn("class target primary", flow_template)
        self.assertNotIn("focal", html_template.casefold())

    def test_process_specimen_applies_the_scribe_profile_without_rewriting_the_type(self) -> None:
        profile = SCRIBE_PROFILE.read_text(encoding="utf-8")
        preparation = CONTENT_PREPARATION.read_text(encoding="utf-8")
        specimen = PROCESS_SPECIMEN.read_text(encoding="utf-8")

        self.assertIn("one optional short detail", preparation)
        self.assertIn("source-defined semantic categories", profile)
        self.assertIn("color-only restyle", profile)
        self.assertIn("var(--dd-", specimen)

    def test_default_skin_keeps_groups_unfilled_and_nodes_filled(self) -> None:
        style = STYLE_GUIDE.read_text(encoding="utf-8")
        theme = DEFAULT_THEME.read_text(encoding="utf-8")
        svg_template = SVG_TEMPLATE.read_text(encoding="utf-8")
        flow_template = FLOW_TEMPLATE.read_text(encoding="utf-8")
        html_template = HTML_TEMPLATE.read_text(encoding="utf-8")

        group_surface = theme_token(theme, "group-surface")
        node_surface = theme_token(theme, "object")

        self.assertEqual("none", group_surface)
        self.assertEqual(group_surface, class_fill(svg_template, "group"))
        self.assertNotIn(node_surface, (group_surface, theme_token(theme, "paper")))
        self.assertEqual(node_surface, class_fill(svg_template, "node"))
        for index in range(1, 6):
            tint = theme_token(theme, f"category-{index}-tint")
            self.assertNotIn(tint, (group_surface, theme_token(theme, "paper")))
            self.assertEqual(tint, class_fill(svg_template, f"category-{index}"))
        self.assertEqual("rgba(34,38,58,0.02)", class_fill(svg_template, "deemphasized"))
        self.assertEqual("#EEF1F7", theme_token(theme, "paper-2"))
        self.assertIn("| Backend / ordinary object | `object` | `ink` |", style)
        self.assertIn("| Group / boundary | `group-surface` |", style)
        self.assertIn("| Store | `ink @ 0.05` | `muted` |", style)
        self.assertIn("var(--dd-paper,", html_template)
        # Mermaid uses the CSS transparent color for the theme's unpainted surface.
        self.assertIn('"clusterBkg": "transparent"', flow_template)
        self.assertIn(f'"primaryColor": "{node_surface}"', flow_template)
        self.assertIn(f"classDef normal fill:{node_surface},", flow_template)

    def test_annotation_primitive_resolves_style_through_theme_roles(self) -> None:
        style = STYLE_GUIDE.read_text(encoding="utf-8")
        theme = DEFAULT_THEME.read_text(encoding="utf-8")
        annotation = ANNOTATION_PRIMITIVE.read_text(encoding="utf-8")

        for token in (
            "annotation-neutral-leader",
            "annotation-accent-leader",
            "annotation-muted-leader",
        ):
            self.assertIn(f"`{token}`", style)
            self.assertRegex(theme_token(theme, token), r"^rgba\(")
            self.assertIn(token, annotation)
        self.assertIn("var(--annotation-neutral-leader)", annotation)
        self.assertIn("var(--font-title)", annotation)
        self.assertNotRegex(annotation, r"#[0-9A-Fa-f]{6}")
        self.assertNotIn("rgba(", annotation)
        self.assertNotIn("Instrument Serif", annotation)

    def test_plotly_is_the_default_skin_not_the_only_allowed_skin(self) -> None:
        style = STYLE_GUIDE.read_text(encoding="utf-8")
        method = VISUAL_METHOD.read_text(encoding="utf-8")
        svg = SVG_GUIDE.read_text(encoding="utf-8")
        svg_template = SVG_TEMPLATE.read_text(encoding="utf-8")
        flow_template = FLOW_TEMPLATE.read_text(encoding="utf-8")

        self.assertIn("Use Diagram Design as four layers:", style)
        self.assertIn(
            "Scribe Plotly is the bundled default theme, not the only permitted theme.",
            style,
        )
        self.assertIn("an explicit user-supplied theme", style)
        self.assertIn("the consuming artifact's or project's established theme", style)
        self.assertIn("colors only", style)
        self.assertIn(
            "Literal colors in adapted type references describe the upstream skin",
            style,
        )
        self.assertNotRegex(style, r"#[0-9A-Fa-f]{6}")
        self.assertIn("theme interface and selected theme", method)
        self.assertIn("the selected theme is the only color system", svg)
        self.assertNotIn("the Plotly theme is the only color system", svg)
        svg_template = SLOT_RE.sub(lambda m: m.group(2), svg_template)
        self.assertIn(
            ".category-1 { fill: #E9EBFE; stroke: #4F5BD5; }",
            svg_template,
        )
        self.assertIn(
            '<rect id="canvas" width="1000" height="600" fill="#FFFFFF"/>',
            svg_template,
        )
        self.assertIn(
            "classDef category1 fill:#E9EBFE,stroke:#4F5BD5",
            flow_template,
        )

    def test_default_nodes_keep_upstream_visual_weight(self) -> None:
        theme = DEFAULT_THEME.read_text(encoding="utf-8")
        ink = theme_token(theme, "ink")
        with self.subTest(surface="theme"):
            self.assertEqual(ink, theme_token(theme, "object-border"))

        svg = apply_theme(SVG_TEMPLATE.read_text(encoding="utf-8"), read_theme_tokens(DEFAULT_THEME), resolve=True)
        rule = re.search(r"\.node\s*\{([^}]+)\}", svg)
        self.assertIsNotNone(rule)
        properties = dict(
            declaration.strip().split(":", 1)
            for declaration in rule.group(1).split(";")
            if declaration.strip()
        )
        with self.subTest(surface="svg-border"):
            self.assertEqual(ink, properties["stroke"].strip())
            self.assertEqual(1, float(properties["stroke-width"]))

        nodes = [
            rect for rect in ET.fromstring(svg).findall(".//{http://www.w3.org/2000/svg}rect")
            if "node" in rect.get("class", "").split()
        ]
        self.assertTrue(nodes)
        for index, node in enumerate(nodes):
            with self.subTest(surface="svg-proportions", node=index):
                # Preserve the upstream compact node's radius and stroke proportions.
                # This guards the starter, not the dimensions of arbitrary diagrams.
                height = float(node.attrib["height"])
                self.assertAlmostEqual(6 / 64, float(node.attrib["rx"]) / height)
                self.assertAlmostEqual(1 / 64, float(properties["stroke-width"]) / height)

        for template in sorted(SVG_TEMPLATE.parent.glob("editorial-*-template.mmd")):
            source = template.read_text(encoding="utf-8")
            with self.subTest(surface=template.name):
                self.assertIn(f'"primaryBorderColor": "{ink}"', source)
                if template == FLOW_TEMPLATE:
                    self.assertRegex(source, rf"classDef normal [^;]*stroke:{re.escape(ink)},")

    def test_diagram_design_component_system_is_preserved(self) -> None:
        style = STYLE_GUIDE.read_text(encoding="utf-8")
        theme = DEFAULT_THEME.read_text(encoding="utf-8")
        svg_template = SVG_TEMPLATE.read_text(encoding="utf-8")

        typography = (STYLE_GUIDE.parent / "typography.md").read_text(encoding="utf-8")
        self.assertIn("typography.md", style)
        self.assertIn("Instrument Serif", typography)
        self.assertIn("Geist Mono", typography)
        self.assertNotIn("font-sans", theme)
        self.assertIn("Keep every coordinate, width, height, padding, and gap on the 4 px grid", style)
        self.assertIn("Use no shadows.", style)
        self.assertIn('rx="6"', svg_template)
        self.assertIn('font: 400 28px "Instrument Serif"', svg_template)


if __name__ == "__main__":
    unittest.main()
