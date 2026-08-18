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


if __name__ == "__main__":
    unittest.main()
