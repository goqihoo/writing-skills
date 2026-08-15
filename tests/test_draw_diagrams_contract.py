import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DRAW_DIAGRAMS = REPO_ROOT / "skills" / "visual" / "draw-diagrams" / "SKILL.md"


class DrawDiagramsContractTest(unittest.TestCase):
    def test_defaults_file_outputs_to_document_assets_directory(self) -> None:
        instructions = DRAW_DIAGRAMS.read_text(encoding="utf-8")

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
