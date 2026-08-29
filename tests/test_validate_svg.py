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


if __name__ == "__main__":
    unittest.main()
