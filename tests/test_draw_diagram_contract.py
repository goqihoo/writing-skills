import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DRAW_DIAGRAM = REPO_ROOT / "skills" / "draw-diagram" / "SKILL.md"
VISUAL_METHOD = REPO_ROOT / "methods" / "visual-production.md"


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


if __name__ == "__main__":
    unittest.main()
