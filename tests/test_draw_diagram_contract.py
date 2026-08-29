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
            "Keep the skill's bundled `assets/` directory for templates only",
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

        self.assertNotIn("one blue focus", style)
        self.assertNotIn(".focus", svg_template)
        self.assertNotIn('class="focus"', svg_template)
        self.assertNotIn("Focal component", svg_template)
        self.assertEqual(2, svg_template.count('class="node"'))
        self.assertNotIn("Focal component", flow_template)
        self.assertNotIn("classDef primary", flow_template)
        self.assertNotIn("class target primary", flow_template)

    def test_container_fill_and_object_description_contract(self) -> None:
        style = STYLE_GUIDE.read_text(encoding="utf-8")
        svg_template = SVG_TEMPLATE.read_text(encoding="utf-8")

        self.assertIn(".node { fill: #FFFFFF;", svg_template)
        self.assertIn(".group { fill: #FFFFFF;", svg_template)
        self.assertIn(".deemphasized { fill: none;", svg_template)
        self.assertIn("Use the object name alone when it makes the role clear.", style)
        self.assertIn("one short responsibility phrase", style)


if __name__ == "__main__":
    unittest.main()
