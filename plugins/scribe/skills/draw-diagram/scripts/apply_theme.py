#!/usr/bin/env python3
"""Bind explicit color slots without rewriting diagram structure or typography.

Keep var(--dd-ROLE, COLOR) in editable source. Resolve it to literal paint for
standalone SVG consumers with --resolve. The compiler never guesses roles from
existing hex values; unmarked artwork needs an explicit role assignment first.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from theme_tokens import DEFAULT_THEME, read_theme_tokens


PAINT = r"(?:#[0-9a-fA-F]{3,8}\b|rgba?\([^()]*\)|none|transparent)"
SLOT_RE = re.compile(r"var\(--dd-([a-z][a-z0-9-]*),\s*(" + PAINT + r")\)")
ALPHA_ROLE_RE = re.compile(r"(.+)-a(\d{3}|1000)$")


def color_for(role: str, tokens: dict[str, str]) -> str:
    if role in tokens:
        return tokens[role]
    match = ALPHA_ROLE_RE.fullmatch(role)
    if match:
        base, amount = match.groups()
        color = tokens.get(base, "")
        if re.fullmatch(r"#[0-9a-fA-F]{6}", color):
            rgb = [int(color[i:i + 2], 16) for i in (1, 3, 5)]
            return "rgba(%d,%d,%d,%s)" % (*rgb, format(int(amount) / 1000, "g"))
    raise ValueError("missing color role or non-hex alpha base: %s" % role)


def apply_theme(source: str, tokens: dict[str, str], *, resolve: bool = False) -> str:
    def replace(match: re.Match) -> str:
        role = match.group(1)
        color = color_for(role, tokens)
        return color if resolve else "var(--dd-%s, %s)" % (role, color)

    # Reject malformed color slots rather than silently keeping a previous skin.
    if "var(--dd-" in SLOT_RE.sub("", source):
        raise ValueError("malformed --dd- color slot")
    if not SLOT_RE.search(source):
        raise ValueError("no --dd- color slots; assign semantic paint roles first")
    return SLOT_RE.sub(replace, source)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--theme", type=Path, default=DEFAULT_THEME)
    parser.add_argument("--resolve", action="store_true", help="materialize literal colors for SVG export")
    args = parser.parse_args()
    try:
        result = apply_theme(args.source.read_text(encoding="utf-8"), read_theme_tokens(args.theme), resolve=args.resolve)
        if args.resolve and args.source.resolve() == args.output.resolve():
            raise ValueError("keep editable color slots: resolve to a different output file")
        args.output.write_text(result, encoding="utf-8")
    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
