#!/usr/bin/env python3
"""Import pinned upstream specimens, adding only semantic color slots.

Usage: python3 scripts/sync-diagram-design-skins.py /path/to/diagram-design
Review any upstream revision change before updating the pinned snapshot.
"""

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills/draw-diagram/scripts"))
from apply_theme import color_for  # noqa: E402
from theme_tokens import DEFAULT_THEME, read_theme_tokens  # noqa: E402

COMMIT = "ac490fd1ac4b4014100f93e729cb4ad198700bd4"
COLOR_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^()]*\)")
ROLES = {
    "#f5f5f5": "paper", "#ececec": "paper-2", "#ffffff": "object", "#fff": "object",
    "#2d3142": "ink", "#4f5d75": "muted", "#7a8399": "soft", "#eb6c36": "accent",
    "#2e5aa8": "link", "#3d4460": "ink-strong", "#bfc0c0": "rule-solid",
    "#7c8f6f": "series-1", "#5e7a9b": "series-2", "#b8915a": "series-3",
    "#9c6b50": "series-4", "#6e6479": "series-5",
}


def semantic_color(match: re.Match, source: str) -> str:
    value = match.group().lower()
    if value in ROLES:
        # White labels on filled bands are not ordinary node surfaces.
        tag = source[source.rfind("<", 0, match.start()):match.start()]
        if value in {"#fff", "#ffffff", "#f5f5f5"} and tag.startswith("<text "):
            return "inverse-ink"
        return ROLES[value]
    channels = value.removeprefix("rgba(").removesuffix(")").split(",")
    if len(channels) != 4:
        raise ValueError("unmapped upstream color: " + value)
    rgb = "#%02x%02x%02x" % tuple(int(c) for c in channels[:3])
    base, alpha = ROLES[rgb], float(channels[3])
    if base == "accent" and alpha == .08:
        return "accent-tint"
    tag = source[source.rfind("<", 0, match.start()):source.find(">", match.end())]
    if base == "ink" and alpha == .02 and tag.startswith("<rect ") and 'rx="8"' in tag:
        return "group-surface"
    return "%s-a%03d" % (base, round(alpha * 1000))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("upstream", type=Path)
    args = parser.parse_args()
    actual = subprocess.check_output(["git", "-C", str(args.upstream), "rev-parse", "HEAD"], text=True).strip()
    if actual != COMMIT:
        parser.error("expected upstream commit " + COMMIT)
    tokens = read_theme_tokens(DEFAULT_THEME)
    source_dir = args.upstream / "skills/diagram-design/assets"
    assets = ROOT / "skills/draw-diagram/assets"
    targets = {p: source_dir / p.name for p in sorted((assets / "examples").glob("example-*.html"))}
    targets[assets / "editorial-diagram-template.html"] = source_dir / "template.html"
    records = {}
    # Prepare every file before writing, so an unmapped color leaves assets intact.
    outputs = {}
    for target, upstream in targets.items():
        relative = str(upstream.relative_to(args.upstream))
        # Read the pinned commit, never uncommitted upstream modifications.
        source = subprocess.check_output(["git", "-C", str(args.upstream), "show", COMMIT + ":" + relative], text=True)
        result = COLOR_RE.sub(lambda m: "var(--dd-%s, %s)" % (semantic_color(m, source), color_for(semantic_color(m, source), tokens)), source)
        outputs[target] = result
        records[str(target.relative_to(assets))] = {
            "upstream_path": relative,
            "upstream_sha256": hashlib.sha256(source.encode()).hexdigest(),
            "non_color_sha256": hashlib.sha256(COLOR_RE.sub("COLOR", source).encode()).hexdigest(),
        }
    for target, source in outputs.items():
        target.write_text(source, encoding="utf-8")
    snapshot = {"upstream_commit": COMMIT, "normalization": "Replace only hex/RGBA paints (or an entire --dd- color slot) with COLOR; retain every other byte.", "assets": records}
    (ROOT / "methods/visual-production/UPSTREAM_VISUAL_CONTRACTS.json").write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    print("Imported %d upstream assets with color-only bindings" % len(outputs))


if __name__ == "__main__":
    main()
