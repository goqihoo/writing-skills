import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
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
            self.assertEqual(
                theme_token(theme, f"category-{index}"),
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
        self.assertIn("Start with neutral peers.", profile)
        self.assertNotIn(".focus", svg_template)
        self.assertNotIn('class="focus"', svg_template)
        self.assertNotIn("Focal component", svg_template)
        self.assertEqual(2, svg_template.count('class="node"'))
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
        self.assertNotIn("focal", specimen.casefold())

    def test_container_fill_and_object_description_contract(self) -> None:
        style = STYLE_GUIDE.read_text(encoding="utf-8")
        preparation = CONTENT_PREPARATION.read_text(encoding="utf-8")
        svg_template = SVG_TEMPLATE.read_text(encoding="utf-8")

        node_fill = class_fill(svg_template, "node")
        group_fill = class_fill(svg_template, "group")
        deemphasized_fill = class_fill(svg_template, "deemphasized")

        self.assertEqual("#F7F8FC", node_fill)
        self.assertEqual("#EEF1F7", group_fill)
        self.assertNotEqual(node_fill, group_fill)
        self.assertEqual("none", deemphasized_fill)
        self.assertIn("| Ordinary object | `object` | `object-border` |", style)
        self.assertIn("| Group or boundary | `paper-2` | `rule-solid` |", style)
        self.assertIn("name is the only required content", preparation)
        self.assertIn("one optional short detail", preparation)

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
        self.assertIn("semantic color tokens and font-family tokens", style)
        self.assertIn(
            "Literal family names and color values retained in adapted Diagram Design type references describe the upstream skin",
            style,
        )
        self.assertNotRegex(style, r"#[0-9A-Fa-f]{6}")
        self.assertIn("theme interface and selected theme", method)
        self.assertIn("the selected theme is the only color system", svg)
        self.assertNotIn("the Plotly theme is the only color system", svg)
        self.assertIn(
            ".category-1 { fill: #E9EBFE; stroke: #4F5BD5; }",
            svg_template,
        )
        self.assertIn(
            '<rect id="canvas" width="1200" height="800" fill="#FFFFFF"/>',
            svg_template,
        )
        self.assertIn(
            "classDef category1 fill:#E9EBFE,stroke:#4F5BD5",
            flow_template,
        )

    def test_diagram_design_component_system_is_preserved(self) -> None:
        style = STYLE_GUIDE.read_text(encoding="utf-8")
        theme = DEFAULT_THEME.read_text(encoding="utf-8")
        svg_template = SVG_TEMPLATE.read_text(encoding="utf-8")

        self.assertIn("`font-title`", style)
        self.assertIn("`font-mono`", style)
        self.assertIn("Instrument Serif", theme)
        self.assertIn("Geist Mono", theme)
        self.assertIn("Keep every coordinate, width, height, padding, and gap on the 4 px grid", style)
        self.assertIn("Use no shadows.", style)
        self.assertIn('rx="6"', svg_template)
        self.assertIn('font: 400 28px "Instrument Serif"', svg_template)


if __name__ == "__main__":
    unittest.main()
