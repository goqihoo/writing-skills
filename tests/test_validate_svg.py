import importlib.util
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "skills" / "draw-diagram" / "scripts" / "validate_svg.py"

SPEC = importlib.util.spec_from_file_location("validate_svg", VALIDATOR_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load SVG validator: {VALIDATOR_PATH}")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


def write_svg(connector_y: int, mask_y: int) -> Path:
    handle = tempfile.NamedTemporaryFile(suffix=".svg", delete=False)
    path = Path(handle.name)
    handle.close()
    path.write_text(
        textwrap.dedent(
            f"""\
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100"
                 role="img" aria-labelledby="title desc">
              <title id="title">Connector label clearance</title>
              <desc id="desc">A minimal connector and edge label.</desc>
              <line class="connector" x1="20" y1="{connector_y}" x2="180" y2="{connector_y}"/>
              <rect class="label-mask" x="70" y="{mask_y}" width="60" height="20"/>
              <text class="edge-label" x="100" y="{mask_y + 15}" text-anchor="middle">label</text>
            </svg>
            """
        ),
        encoding="utf-8",
    )
    return path


def write_color_svg(
    mode: str | None,
    body: str,
    root_attributes: str = "",
) -> Path:
    handle = tempfile.NamedTemporaryFile(suffix=".svg", delete=False)
    path = Path(handle.name)
    handle.close()
    mode_attribute = f' data-scribe-color-mode="{mode}"' if mode else ""
    path.write_text(
        textwrap.dedent(
            f"""\
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100"
                 role="img" aria-labelledby="title desc"{mode_attribute} {root_attributes}>
              <title id="title">Color contract</title>
              <desc id="desc">A minimal Scribe color-contract fixture.</desc>
              <defs>
                <style>
                  .category-1 {{ fill: var(--dd-category-1-tint, #E9EBFE); stroke: var(--dd-category-1, #4F5BD5); }}
                  .series-2 {{ fill: var(--dd-series-2-tint, #F3E9FE); stroke: var(--dd-series-2, #8240C9); }}
                </style>
              </defs>
              {body}
            </svg>
            """
        ),
        encoding="utf-8",
    )
    return path


class ValidateSvgConnectorLabelTest(unittest.TestCase):
    def tearDown(self) -> None:
        for path in getattr(self, "paths", []):
            path.unlink(missing_ok=True)

    def test_rejects_label_mask_that_covers_a_connector(self) -> None:
        self.paths = [write_svg(connector_y=50, mask_y=40)]

        errors, _ = VALIDATOR.validate(self.paths[0])

        self.assertIn("connector label mask must stay at least 6px from every connector", errors)

    def test_accepts_label_mask_with_six_pixel_clearance(self) -> None:
        self.paths = [write_svg(connector_y=34, mask_y=40)]

        errors, _ = VALIDATOR.validate(self.paths[0])

        self.assertNotIn("connector label mask must stay at least 6px from every connector", errors)


class ValidateSvgScribeColorContractTest(unittest.TestCase):
    def tearDown(self) -> None:
        for path in getattr(self, "paths", []):
            path.unlink(missing_ok=True)

    def validate(self, path: Path) -> list[str]:
        errors, _warnings = VALIDATOR.validate(path, require_scribe_color=True)
        return errors

    def test_requires_an_explicit_color_mode(self) -> None:
        self.paths = [write_color_svg(None, '<rect class="category-1"/>')]

        errors = self.validate(self.paths[0])

        self.assertTrue(any("data-scribe-color-mode" in error for error in errors))

    def test_rejects_palette_definitions_without_visible_category_paint(self) -> None:
        self.paths = [write_color_svg("categorical", '<rect fill="var(--dd-object, #F7F8FC)"/>')]

        errors = self.validate(self.paths[0])

        self.assertIn(
            "categorical color mode needs visible category paint; palette definitions inside <defs> do not count",
            errors,
        )

    def test_accepts_visible_class_based_category_paint(self) -> None:
        self.paths = [write_color_svg("categorical", '<rect class="category-1"/>')]

        errors = self.validate(self.paths[0])

        self.assertEqual([], errors)

    def test_rejects_a_semantic_group_without_matching_category_paint(self) -> None:
        self.paths = [
            write_color_svg(
                "categorical",
                '<g data-category="2"><rect class="category-1"/></g>',
            )
        ]

        errors = self.validate(self.paths[0])

        self.assertIn("data-category=2 has no visible matching category paint", errors)

    def test_group_color_must_reach_every_node_consistently(self) -> None:
        self.paths = []
        for role, accepted in (
            ("object", False),
            ("category-2-tint", False),
            ("category-1-tint", True),
        ):
            with self.subTest(node_fill=role):
                path = write_color_svg(
                    "categorical",
                    f'''<g data-category="1">
                      <rect x="10" y="10" width="180" height="80"
                            fill="var(--dd-category-1-a020, rgba(79,91,213,0.02))"/>
                      <text x="20" y="25" fill="var(--dd-category-1, #4F5BD5)">Group A</text>
                      <rect class="node" x="20" y="35" width="70" height="40"
                            fill="var(--dd-category-1-tint, #E9EBFE)"
                            stroke="var(--dd-category-1, #4F5BD5)"/>
                      <rect class="node" x="110" y="35" width="70" height="40"
                            fill="var(--dd-{role}, #F7F8FC)"
                            stroke="var(--dd-category-1, #4F5BD5)"/>
                    </g>''',
                )
                self.paths.append(path)

                errors = self.validate(path)

                if accepted:
                    self.assertEqual([], errors)
                else:
                    self.assertTrue(errors, "a colored frame or border must not hide a gray or mismatched node")

    def test_accepts_visible_quantitative_series_paint(self) -> None:
        self.paths = [write_color_svg("quantitative", '<rect class="series-2"/>')]

        errors = self.validate(self.paths[0])

        self.assertEqual([], errors)

    def test_neutral_mode_requires_a_supported_reason(self) -> None:
        self.paths = [
            write_color_svg("neutral", '<rect fill="var(--dd-object, #F7F8FC)"/>'),
            write_color_svg(
                "neutral",
                '<rect fill="var(--dd-object, #F7F8FC)"/>',
                'data-scribe-neutral-reason="explicit-user-request"',
            ),
        ]

        missing_reason = self.validate(self.paths[0])
        supported_reason = self.validate(self.paths[1])

        self.assertTrue(any("data-scribe-neutral-reason" in error for error in missing_reason))
        self.assertEqual([], supported_reason)


if __name__ == "__main__":
    unittest.main()
