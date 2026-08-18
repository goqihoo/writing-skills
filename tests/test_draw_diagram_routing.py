import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DRAW_DIAGRAM = REPO_ROOT / "skills" / "draw-diagram" / "SKILL.md"
VISUAL_METHOD = REPO_ROOT / "methods" / "visual-production.md"


def visual_routing_rows(instructions: str) -> list[list[str]]:
    section = instructions.split("## Visual routing", maxsplit=1)[1]
    table = section.split("## Semantic rules", maxsplit=1)[0]

    return [
        [cell.strip() for cell in line.strip().strip("|").split("|")]
        for line in table.splitlines()
        if line.startswith("|") and "---" not in line and "Reader needs" not in line
    ]


class DrawDiagramRoutingTest(unittest.TestCase):
    def setUp(self) -> None:
        self.instructions = VISUAL_METHOD.read_text(encoding="utf-8")

    def test_routes_concept_explanations_to_imagegen_infographics(self) -> None:
        rows = visual_routing_rows(self.instructions)

        self.assertIn(
            [
                "Definition, role, or mental model aided by concrete visual cues",
                "Illustrated conceptual infographic",
                "ImageGen",
            ],
            rows,
        )

    def test_routes_exact_relational_views_to_svg(self) -> None:
        rows_by_need = {
            reader_need: production
            for reader_need, _, production in visual_routing_rows(self.instructions)
        }

        for reader_need in (
            "External actors and dependencies",
            "Responsibility, authority, or trust",
            "Layers, modules, or hierarchy",
            "Ordered business or data stages",
            "Timing, concurrency, retry, or acknowledgment",
            "Allowed states and transitions",
            "Runtime placement or failure domains",
            "Normal path plus rejection, timeout, or recovery",
        ):
            with self.subTest(reader_need=reader_need):
                self.assertEqual("SVG", rows_by_need[reader_need])

    def test_mermaid_is_only_used_when_explicitly_requested(self) -> None:
        rows = visual_routing_rows(self.instructions)

        self.assertIn(
            "Use Mermaid only when the user explicitly requests Mermaid.",
            self.instructions,
        )
        self.assertFalse(
            any("Mermaid" in production for _, _, production in rows),
            "Mermaid must not appear as a default production format.",
        )

    def test_does_not_add_visible_post_image_description_by_default(self) -> None:
        self.assertIn("Add only meaningful alt text by default.", self.instructions)
        self.assertIn(
            "Do not append a visible title, caption, or explanation after the image",
            self.instructions,
        )


if __name__ == "__main__":
    unittest.main()
