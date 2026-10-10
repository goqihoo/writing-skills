import hashlib
import json
import re
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skills/draw-diagram/scripts"
ASSETS = SCRIPTS.parent / "assets"
VISUAL = ROOT / "methods/visual-production"
sys.path.insert(0, str(SCRIPTS))
from apply_theme import SLOT_RE, apply_theme
from theme_tokens import COLOR_ROLES, DEFAULT_THEME, read_theme_tokens


def non_color_source(source):
    source = SLOT_RE.sub("COLOR", source)
    return re.sub(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^()]*\)", "COLOR", source)


class DiagramSkinTest(unittest.TestCase):
    def test_grouped_starter_renders_distinct_default_colors_without_focal_state(self):
        # Exercise the actual grouped starting asset and export path. Merely
        # defining unused category colors in a palette did not catch the bug.
        source = (ASSETS / "editorial-grouped-template.svg").read_text()
        default = read_theme_tokens(DEFAULT_THEME)
        rendered = apply_theme(source, default, resolve=True)
        svg = ET.fromstring(rendered)
        ns = "{http://www.w3.org/2000/svg}"
        groups = svg.findall(f"{ns}g[@data-category]")
        paints = set()
        self.assertEqual(3, len(groups))
        for group in groups:
            category = group.get("data-category")
            nodes = group.findall(f"{ns}g[@class='component']/{ns}rect[@class='node']")
            self.assertEqual(2, len(nodes))
            for node in nodes:
                self.assertEqual(default[f"category-{category}"], node.get("stroke"))
                self.assertEqual(default[f"category-{category}-tint"], node.get("fill"))
                self.assertEqual(("160", "64", "6", "1"), tuple(node.get(k) for k in ("width", "height", "rx", "stroke-width")))
                paints.add(node.get("stroke"))
        self.assertEqual(3, len(paints))
        self.assertNotIn("--dd-accent", source)
        self.assertNotIn("--dd-success", source)
        for skin in ("diagram-design", "diagram-design-dark", "diagram-design-terminal"):
            themed = apply_theme(source, read_theme_tokens(skin))
            self.assertEqual(non_color_source(source), non_color_source(themed))
            self.assertEqual(rendered, apply_theme(themed, default, resolve=True))

    def test_all_upstream_non_color_bytes_are_preserved(self):
        snapshot = json.loads((VISUAL / "UPSTREAM_VISUAL_CONTRACTS.json").read_text())
        self.assertEqual("ac490fd1ac4b4014100f93e729cb4ad198700bd4", snapshot["upstream_commit"])
        self.assertEqual(40, len(snapshot["assets"]))
        for name, record in snapshot["assets"].items():
            with self.subTest(asset=name):
                normalized = non_color_source((ASSETS / name).read_text())
                self.assertEqual(record["non_color_sha256"], hashlib.sha256(normalized.encode()).hexdigest())

    def test_all_bundled_skins_round_trip_without_component_changes(self):
        default = read_theme_tokens(DEFAULT_THEME)
        specimens = sorted((ASSETS / "examples").glob("*.html"))
        specimens += sorted(ASSETS.glob("editorial-diagram-template.*"))
        for path in sorted((VISUAL / "themes").glob("*.md")):
            if path.name == "README.md":
                continue
            tokens = read_theme_tokens(path)
            self.assertEqual(COLOR_ROLES | {"quantitative-connector-alpha"}, tokens.keys())
            for specimen in specimens:
                with self.subTest(theme=path.name, specimen=specimen.name):
                    source = specimen.read_text()
                    themed = apply_theme(source, tokens)
                    self.assertEqual(non_color_source(source), non_color_source(themed))
                    self.assertEqual(source, apply_theme(themed, default))
                    self.assertNotIn("var(--dd-", apply_theme(source, tokens, resolve=True))

    def test_svg_starter_keeps_full_upstream_component_hierarchy(self):
        source = apply_theme((ASSETS / "editorial-diagram-template.svg").read_text(), read_theme_tokens(DEFAULT_THEME), resolve=True)
        svg = ET.fromstring(source)
        ns = "{http://www.w3.org/2000/svg}"
        style = svg.find(f"{ns}defs/{ns}style").text
        self.assertRegex(style, r"\.node-title\s*\{\s*font: 600 12px")
        self.assertRegex(style, r"\.detail\s*\{\s*font: 400 9px")
        self.assertRegex(style, r"\.technical\s*\{\s*font: 400 9px")
        self.assertRegex(style, r"\.node\s*\{[^}]*stroke-width: 1;")
        groups = svg.findall(f"{ns}g[@id='nodes']/{ns}g")
        self.assertEqual(2, len(groups))
        for group in groups:
            mask, node = group.findall(f"{ns}rect")
            self.assertEqual("mask", mask.get("class"))
            self.assertEqual("node category-1", node.get("class"))
            for key in ("x", "y", "width", "height", "rx"):
                self.assertEqual(mask.get(key), node.get(key))
            self.assertEqual(("160", "64", "6"), tuple(node.get(k) for k in ("width", "height", "rx")))
        for marker in svg.findall(f"{ns}defs/{ns}marker"):
            self.assertEqual(("8", "6", "7", "3"), tuple(marker.get(k) for k in ("markerWidth", "markerHeight", "refX", "refY")))

    def test_original_palette_restores_architecture_semantic_roles(self):
        source = (ASSETS / "examples/example-architecture.html").read_text()
        native = apply_theme(source, read_theme_tokens("diagram-design"), resolve=True)
        svg = ET.fromstring(re.search(r"<svg\b.*?</svg>", native, re.S).group())
        ns = "{http://www.w3.org/2000/svg}"
        nodes = {(r.get("x"), r.get("y")): r for r in svg.findall(f"{ns}rect") if r.get("height") == "64"}
        self.assertEqual("#2d3142", nodes[("628", "160")].get("stroke"))
        self.assertEqual("#ffffff", nodes[("628", "160")].get("fill"))
        self.assertEqual("rgba(45,49,66,0.3)", nodes[("220", "240")].get("stroke"))
        self.assertEqual("#eb6c36", nodes[("416", "240")].get("stroke"))
        self.assertEqual("#7a8399", nodes[("40", "240")].get("stroke"))
        self.assertIn('font-size="9"', native)
        self.assertIn('stroke-width="1.4"', native)  # Type-specific emphasis is not rounded away.

    def test_new_palette_needs_no_renderer_or_registry_edit(self):
        source = '<svg><title>#22263A stays in the title</title><path id="ink" d="M 12 9 H 64" stroke-width="1" stroke="var(--dd-ink, #22263A)"/></svg>'
        with tempfile.TemporaryDirectory() as tmp:
            palette = Path(tmp) / "new-skin.md"
            palette.write_text(DEFAULT_THEME.read_text().replace("#22263A", "#103040"))
            tokens = read_theme_tokens(palette)
            result = apply_theme(source, tokens, resolve=True)
        self.assertEqual(source.replace('var(--dd-ink, #22263A)', '#103040'), result)

    def test_invalid_palettes_fail_instead_of_restyling_components(self):
        for key, value in [("font-sans", "Other Font"), ("stroke-width", "2"), ("radius", "12"), ("ink", "url(remote)"), ("ink", "rgba(999,0,0,0.5)"), ("quantitative-connector-alpha", "nan")]:
            with self.subTest(key=key, value=value), tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / "invalid.md"
                path.write_text(f"| `{key}` | `{value}` |\n")
                with self.assertRaises(ValueError):
                    read_theme_tokens(path)
        with self.assertRaises(ValueError):
            apply_theme('fill="var(--dd-unknown, #FFFFFF)"', read_theme_tokens(DEFAULT_THEME))
        with self.assertRaises(ValueError):
            apply_theme('fill="var(--dd-ink)"', read_theme_tokens(DEFAULT_THEME))

    def test_cli_keeps_editable_source_and_resolves_export(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "source.svg"
            output = Path(tmp) / "output.svg"
            original = (ASSETS / "editorial-diagram-template.svg").read_text()
            source.write_text(original)
            command = [sys.executable, str(SCRIPTS / "apply_theme.py"), str(source)]
            completed = subprocess.run(command + [str(output), "--theme", "diagram-design-dark", "--resolve"], capture_output=True, text=True)
            self.assertEqual(0, completed.returncode, completed.stderr)
            ET.fromstring(output.read_text())
            self.assertNotIn("var(--dd-", output.read_text())
            self.assertEqual(original, source.read_text())
            completed = subprocess.run(command + [str(source), "--resolve"], capture_output=True, text=True)
            self.assertNotEqual(0, completed.returncode)
            self.assertEqual(original, source.read_text())


if __name__ == "__main__":
    unittest.main()
