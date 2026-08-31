#!/usr/bin/env python3
"""Read semantic tokens from a Diagram Design Markdown theme."""

from __future__ import annotations

import argparse
import math
import re
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
PACKAGE_ROOT = SKILL_DIR.parents[1]
DEFAULT_THEME = PACKAGE_ROOT / "methods/visual-production/themes/scribe-plotly.md"
THEME_DIR = DEFAULT_THEME.parent
TYPOGRAPHY = THEME_DIR.parent / "typography.md"

TOKEN_ROW_RE = re.compile(r"^\| `([^`]+)` \| `([^`]+)` \|", re.MULTILINE)
HEX_COLOR_RE = re.compile(r"#[0-9A-Fa-f]{6}")
COLOR_RE = re.compile(r"#[0-9A-Fa-f]{6}|none|transparent|rgba\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*(?:0(?:\.\d+)?|\.\d+|1(?:\.0+)?)\s*\)")
COLOR_ROLES = {
    "paper", "paper-2", "object", "ink", "muted", "soft", "rule", "rule-solid",
    "group-surface", "object-border", "deemphasized-border", "accent", "accent-tint",
    "link", "success", "success-tint", "warning", "warning-tint", "failure", "failure-tint",
    "connector-label-surface", "boundary-label-surface", "annotation-neutral-leader",
    "annotation-accent-leader", "annotation-muted-leader", "ink-strong", "inverse-ink",
} | {f"{kind}-{i}{suffix}" for kind in ("category", "series") for i in range(1, 6) for suffix in ("", "-tint")}


def resolve_theme(path: Path | str) -> Path:
    """Accept a bundled skin ID or an explicit Markdown palette path."""
    path = Path(path)
    if len(path.parts) == 1 and not path.suffix:
        return THEME_DIR / (path.name + ".md")
    return path


def add_theme_argument(parser: argparse.ArgumentParser) -> None:
    """Add the shared selected-theme option to a verifier CLI."""
    parser.add_argument(
        "--theme",
        type=Path,
        default=DEFAULT_THEME,
        help="bundled skin ID or theme Markdown path (default: scribe-plotly)",
    )


def read_theme_tokens(path: Path) -> dict[str, str]:
    """Return all token/value pairs, failing closed on a missing theme."""
    path = resolve_theme(path)
    if not path.is_file():
        raise ValueError("theme not found: %s" % path)
    source = path.read_text(encoding="utf-8")
    rows = TOKEN_ROW_RE.findall(source)
    tokens = dict(rows)
    if not tokens:
        raise ValueError("theme %s has no token table" % path.name)
    if len(tokens) != len(rows):
        raise ValueError("theme %s has duplicate tokens" % path.name)
    for key, value in tokens.items():
        if key == "quantitative-connector-alpha":
            if not re.fullmatch(r"0(?:\.\d+)?|1(?:\.0+)?", value):
                raise ValueError("invalid color opacity: %s" % value)
        elif key not in COLOR_ROLES or COLOR_RE.fullmatch(value) is None:
            raise ValueError("theme %s contains a non-color or invalid token: %s" % (path.name, key))
        elif value.startswith("rgba") and any(int(v) > 255 for v in re.findall(r"\d+", value)[:3]):
            raise ValueError("invalid RGB channel: %s" % value)
    return tokens


def read_typography_tokens(path: Path = TYPOGRAPHY) -> dict[str, str]:
    """Read font choices independently of color skins."""
    return dict(TOKEN_ROW_RE.findall(path.read_text(encoding="utf-8")))


def theme_token(path: Path, token: str) -> str:
    """Return one required token from a theme."""
    tokens = read_theme_tokens(path)
    try:
        return tokens[token]
    except KeyError as error:
        raise ValueError("theme %s has no %s token" % (path.name, token)) from error


def theme_color(path: Path, token: str) -> str:
    """Return one required six-digit hexadecimal color token."""
    value = theme_token(path, token)
    if HEX_COLOR_RE.fullmatch(value) is None:
        raise ValueError("theme %s token %s is not a hex color" % (path.name, token))
    return value


def theme_number(path: Path, token: str) -> float:
    """Return one required finite numeric token from a theme."""
    value = theme_token(path, token)
    try:
        number = float(value)
    except ValueError as error:
        raise ValueError(
            "theme %s token %s is not numeric" % (path.name, token)
        ) from error
    if not math.isfinite(number):
        raise ValueError("theme %s token %s is not finite" % (path.name, token))
    return number
