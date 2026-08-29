#!/usr/bin/env python3
"""Read semantic tokens from a Diagram Design Markdown theme."""

from __future__ import annotations

import re
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
PACKAGE_ROOT = SKILL_DIR.parents[1]
DEFAULT_THEME = PACKAGE_ROOT / "methods/visual-production/themes/scribe-plotly.md"

TOKEN_ROW_RE = re.compile(r"^\| `([^`]+)` \| `([^`]+)` \|", re.MULTILINE)
HEX_COLOR_RE = re.compile(r"#[0-9A-Fa-f]{6}")


def read_theme_tokens(path: Path) -> dict[str, str]:
    """Return all token/value pairs, failing closed on a missing theme."""
    if not path.is_file():
        raise ValueError("theme not found: %s" % path)
    source = path.read_text(encoding="utf-8")
    tokens = dict(TOKEN_ROW_RE.findall(source))
    if not tokens:
        raise ValueError("theme %s has no token table" % path.name)
    return tokens


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
