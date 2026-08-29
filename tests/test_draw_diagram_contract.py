import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DRAW_DIAGRAM = REPO_ROOT / "skills" / "draw-diagram" / "SKILL.md"
VISUAL_METHOD = REPO_ROOT / "methods" / "visual-production.md"
STYLE_GUIDE = REPO_ROOT / "methods" / "visual-production" / "style-guide.md"
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


class DrawDiagramContractTest(unittest.TestCase):
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
        style = STYLE_GUIDE.read_text(encoding="utf-8")
        svg_template = SVG_TEMPLATE.read_text(encoding="utf-8")
        flow_template = FLOW_TEMPLATE.read_text(encoding="utf-8")
        html_template = HTML_TEMPLATE.read_text(encoding="utf-8")

        self.assertIn("Start every diagram with zero focal elements.", style)
        self.assertNotIn(".focus", svg_template)
        self.assertNotIn('class="focus"', svg_template)
        self.assertNotIn("Focal component", svg_template)
        self.assertEqual(2, svg_template.count('class="node"'))
        self.assertNotIn("Focal component", flow_template)
        self.assertNotIn("classDef primary", flow_template)
        self.assertNotIn("class target primary", flow_template)
        self.assertNotIn("focal", html_template.casefold())

    def test_process_defaults_to_compact_neutral_category_encoding(self) -> None:
        guidance = PROCESS_REFERENCE.read_text(encoding="utf-8")
        specimen = PROCESS_SPECIMEN.read_text(encoding="utf-8")

        self.assertIn("The node name is the only required visible text.", guidance)
        self.assertIn(
            "Give each source-defined lane category a distinct category token",
            guidance,
        )
        self.assertNotIn("exactly **one** focal", guidance.casefold())
        self.assertNotIn("focal", specimen.casefold())

    def test_container_fill_and_object_description_contract(self) -> None:
        style = STYLE_GUIDE.read_text(encoding="utf-8")
        svg_template = SVG_TEMPLATE.read_text(encoding="utf-8")

        node_fill = class_fill(svg_template, "node")
        group_fill = class_fill(svg_template, "group")
        deemphasized_fill = class_fill(svg_template, "deemphasized")

        self.assertEqual("#FFFFFF", node_fill)
        self.assertEqual("#F5F6FB", group_fill)
        self.assertNotEqual(node_fill, group_fill)
        self.assertEqual("none", deemphasized_fill)
        self.assertIn("| Ordinary object | `object` | `object-border` |", style)
        self.assertIn("| Group or boundary | `paper-2` | `rule-solid` |", style)
        self.assertIn("Use the object name alone when it makes the role clear.", style)
        self.assertIn("one short responsibility phrase", style)

    def test_plotly_qualitative_is_the_default_color_layer(self) -> None:
        style = STYLE_GUIDE.read_text(encoding="utf-8")
        svg_template = SVG_TEMPLATE.read_text(encoding="utf-8")
        flow_template = FLOW_TEMPLATE.read_text(encoding="utf-8")

        self.assertIn("Use Diagram Design as four layers:", style)
        self.assertIn("Use the Scribe Plotly theme below for the fourth.", style)
        self.assertIn(
            "A theme change may rebind only color tokens",
            style,
        )
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
        svg_template = SVG_TEMPLATE.read_text(encoding="utf-8")

        self.assertIn("Instrument Serif", style)
        self.assertIn("Geist Mono", style)
        self.assertIn("Keep every coordinate, width, height, padding, and gap on the 4 px grid", style)
        self.assertIn("Use no shadows.", style)
        self.assertIn('rx="6"', svg_template)
        self.assertIn('font: 400 28px "Instrument Serif"', svg_template)


if __name__ == "__main__":
    unittest.main()
