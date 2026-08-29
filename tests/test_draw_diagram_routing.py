import re
import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DRAW_DIAGRAM = REPO_ROOT / "skills" / "draw-diagram" / "SKILL.md"
VISUAL_METHOD = REPO_ROOT / "methods" / "visual-production.md"
VISUAL_ROOT = REPO_ROOT / "methods" / "visual-production"
EXAMPLES_ROOT = REPO_ROOT / "skills" / "draw-diagram" / "assets" / "examples"

EXPECTED_TYPES = {
    "Architecture": "type-architecture.md",
    "IT current-state": "type-it-state.md",
    "Flowchart": "type-flowchart.md",
    "Sequence": "type-sequence.md",
    "State machine": "type-state.md",
    "ER / data model": "type-er.md",
    "Timeline": "type-timeline.md",
    "Swimlane": "type-swimlane.md",
    "Quadrant": "type-quadrant.md",
    "Radar / spider": "type-radar.md",
    "Polar chart": "type-polar.md",
    "Loop / flywheel": "type-loop.md",
    "Nested": "type-nested.md",
    "Tree": "type-tree.md",
    "Org chart": "type-org-chart.md",
    "Layer stack": "type-layers.md",
    "Venn": "type-venn.md",
    "Pyramid / funnel": "type-pyramid.md",
    "Bar chart": "type-bar.md",
    "Treemap": "type-treemap.md",
    "Line chart": "type-line.md",
    "Gantt": "type-gantt.md",
    "Scatter plot": "type-scatter.md",
    "High-Level": "type-high-level.md",
    "Process": "type-process.md",
    "Medallion": "type-medallion.md",
    "Data flow": "type-data-flow.md",
    "DP integration": "type-dp-integration.md",
    "DP security matrix": "type-dp-security-matrix.md",
    "Sankey": "type-sankey.md",
    "Fishbone": "type-fishbone.md",
    "Wardley map": "type-wardley.md",
    "Kanban": "type-kanban.md",
    "User journey": "type-journey.md",
    "Deployment": "type-deployment.md",
    "Dependency graph": "type-dependency.md",
    "UML class": "type-uml-class.md",
    "Story map": "type-story-map.md",
    "Database schema": "type-db-schema.md",
}

ALLOWED_THEME_COLORS = {
    "#FFFFFF",
    "#F5F6FB",
    "#22263A",
    "#596174",
    "#6F788C",
    "#DCE1EA",
    "#CBD2DF",
    "#C3CBD9",
    "#A6AFBF",
    "#4F5BD5",
    "#E9EBFE",
    "#007A59",
    "#DDF8F0",
    "#8240C9",
    "#F3E9FE",
    "#D43E26",
    "#FDE9E5",
    "#B95D18",
    "#FFF0E4",
}


def visual_type_rows(instructions: str) -> list[list[str]]:
    section = instructions.split("## Visual-type routing", maxsplit=1)[1]
    table = section.split("## Non-Diagram-Design outputs", maxsplit=1)[0]
    return [
        [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        for line in table.splitlines()
        if line.startswith("|")
        and "---" not in line
        and "reader needs" not in line.casefold()
    ]


def colors_in(paths: list[Path]) -> set[str]:
    colors: set[str] = set()
    for path in paths:
        source = path.read_text(encoding="utf-8")
        colors.update(
            match.upper()
            for match in re.findall(r"#[0-9A-Fa-f]{3,8}(?![0-9A-Fa-f])", source)
        )
    return colors


class DrawDiagramRoutingTest(unittest.TestCase):
    def setUp(self) -> None:
        self.instructions = VISUAL_METHOD.read_text(encoding="utf-8")
        self.rows = visual_type_rows(self.instructions)

    def test_routes_exactly_the_latest_39_diagram_design_types(self) -> None:
        routed = {diagram_type: Path(reference).name for _, diagram_type, reference in self.rows}

        self.assertEqual(39, len(self.rows))
        self.assertEqual(EXPECTED_TYPES, routed)
        self.assertIn("Polar chart", routed)

    def test_every_type_has_one_reference_and_one_plotly_specimen(self) -> None:
        for _, diagram_type, reference in self.rows:
            with self.subTest(diagram_type=diagram_type):
                reference_path = REPO_ROOT / "methods" / reference
                slug = reference_path.stem.removeprefix("type-")
                example_path = EXAMPLES_ROOT / f"example-{slug}.html"

                self.assertTrue(reference_path.is_file(), reference_path)
                self.assertTrue(example_path.is_file(), example_path)

                guidance = reference_path.read_text(encoding="utf-8")
                self.assertIn("Adapted from Diagram Design 2.6", guidance)
                self.assertIn("## Plotly specimen", guidance)
                self.assertIn(example_path.name, guidance)
                self.assertGreaterEqual(guidance.count("\n## "), 2)

                specimen = example_path.read_text(encoding="utf-8")
                self.assertIn("role=\"img\"", specimen)
                self.assertIn("aria-labelledby=", specimen)
                self.assertRegex(specimen, r"<title id=\"[^\"]+\">.+</title>")
                self.assertRegex(specimen, r"<desc id=\"[^\"]+\">.+</desc>")

    def test_progressive_disclosure_loads_only_the_selected_type(self) -> None:
        skill = DRAW_DIAGRAM.read_text(encoding="utf-8")

        self.assertIn("exactly one of its 39 Diagram Design visual types", skill)
        self.assertIn("Load only the selected type's reference", skill)
        self.assertNotIn("type-architecture.md", skill)

    def test_mermaid_remains_an_explicit_fidelity_limited_output(self) -> None:
        self.assertIn("Use Mermaid only when the user explicitly requests Mermaid", self.instructions)
        self.assertIn("state any type-specific fidelity loss", self.instructions)

    def test_non_relational_concept_routes_remain_available(self) -> None:
        self.assertIn("Use ImageGen for an illustrated conceptual explanation", self.instructions)
        self.assertIn("Use HTML or a visualization tool for adjustable exploration", self.instructions)

    def test_type_contracts_and_specimens_only_use_scribe_theme_colors(self) -> None:
        paths = sorted((VISUAL_ROOT / "types").glob("type-*.md"))
        paths += [VISUAL_ROOT / "semantic-patterns.md", VISUAL_ROOT / "primitive-annotation.md"]
        paths += sorted(EXAMPLES_ROOT.glob("example-*.html"))
        paths += [REPO_ROOT / "skills" / "draw-diagram" / "assets" / "editorial-diagram-template.html"]

        unexpected = colors_in(paths) - ALLOWED_THEME_COLORS
        self.assertEqual(set(), unexpected)

    def test_plotly_specimens_pass_the_packaged_html_validator(self) -> None:
        validator = REPO_ROOT / "skills" / "draw-diagram" / "scripts" / "validate_html.py"
        specimens = sorted(EXAMPLES_ROOT.glob("example-*.html"))
        result = subprocess.run(
            [sys.executable, str(validator), *map(str, specimens)],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_quantitative_variant_verifiers_ship_and_pass_representative_checks(self) -> None:
        scripts = REPO_ROOT / "skills" / "draw-diagram" / "scripts"
        expected = {
            "verify-bubble.py",
            "verify-dumbbell.py",
            "verify-ridgeline.py",
            "verify-slopegraph.py",
            "verify-treemap.py",
        }
        self.assertTrue(all((scripts / name).is_file() for name in expected))

        checks = [
            [sys.executable, str(scripts / "verify-dumbbell.py")],
            [
                sys.executable,
                str(scripts / "verify-treemap.py"),
                str(EXAMPLES_ROOT / "example-treemap.html"),
            ],
        ]
        for command in checks:
            with self.subTest(command=command[1]):
                result = subprocess.run(
                    command,
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_visual_method_markdown_links_and_verifier_pointers_resolve(self) -> None:
        missing: list[str] = []
        for path in VISUAL_ROOT.rglob("*.md"):
            source = path.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", source):
                target = target.strip().strip("<>")
                if "://" in target or target.startswith("#"):
                    continue
                local = target.split("#", maxsplit=1)[0]
                if local and not (path.parent / local).resolve().exists():
                    missing.append(f"{path}: {target}")
            for target in re.findall(
                r"`(\.\./\.\./\.\./skills/draw-diagram/scripts/verify-[^`]+\.py)`",
                source,
            ):
                if not (path.parent / target).resolve().is_file():
                    missing.append(f"{path}: {target}")

        self.assertEqual([], missing)

    def test_upstream_license_and_provenance_ship_with_the_method(self) -> None:
        provenance = (VISUAL_ROOT / "UPSTREAM.md").read_text(encoding="utf-8")
        license_text = (VISUAL_ROOT / "DIAGRAM_DESIGN_LICENSE.txt").read_text(
            encoding="utf-8"
        )

        self.assertIn("ac490fd1ac4b4014100f93e729cb4ad198700bd4", provenance)
        self.assertIn("Copyright (c) 2025 Cathryn Lavery", license_text)
        self.assertIn("MIT License", license_text)


if __name__ == "__main__":
    unittest.main()
