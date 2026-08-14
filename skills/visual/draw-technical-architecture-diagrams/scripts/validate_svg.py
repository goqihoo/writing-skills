#!/usr/bin/env python3
"""Validate portable editable SVGs and optionally render a preview."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


XLINK_HREF = "{http://www.w3.org/1999/xlink}href"
LOCAL_REF = re.compile(r"url\(#([^)]+)\)")


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def validate(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not path.is_file():
        return [f"file does not exist: {path}"], warnings

    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return [f"invalid XML: {exc}"], warnings

    if local_name(root.tag) != "svg":
        return ["root element must be <svg>"], warnings
    if not root.get("viewBox"):
        errors.append("missing viewBox")

    elements = list(root.iter())
    ids: dict[str, int] = {}
    for element in elements:
        if element_id := element.get("id"):
            ids[element_id] = ids.get(element_id, 0) + 1
    duplicates = sorted(key for key, count in ids.items() if count > 1)
    if duplicates:
        errors.append("duplicate ids: " + ", ".join(duplicates))

    title = next((e for e in elements if local_name(e.tag) == "title"), None)
    desc = next((e for e in elements if local_name(e.tag) == "desc"), None)
    if title is None or not "".join(title.itertext()).strip():
        errors.append("missing non-empty <title>")
    if desc is None or not "".join(desc.itertext()).strip():
        errors.append("missing non-empty <desc>")

    labelled = set((root.get("aria-labelledby") or "").split())
    if root.get("role") != "img":
        warnings.append('root should include role="img"')
    for element, label in ((title, "title"), (desc, "desc")):
        if element is not None and element.get("id") not in labelled:
            warnings.append(f"{label} id should appear in aria-labelledby")

    forbidden = {"foreignObject", "script", "animate", "animateMotion", "animateTransform"}
    found = sorted({local_name(e.tag) for e in elements} & forbidden)
    if found:
        warnings.append("portability risk: " + ", ".join(found))
    if not any(local_name(e.tag) == "text" for e in elements):
        warnings.append("no editable <text> labels found")
    if any(local_name(e.tag) == "image" for e in elements):
        warnings.append("embedded raster image found")

    for element in elements:
        href = element.get("href") or element.get(XLINK_HREF)
        if href and not href.startswith(("#", "data:")):
            warnings.append(f"external resource: {href}")
        for value in element.attrib.values():
            for reference in LOCAL_REF.findall(value):
                if reference not in ids:
                    errors.append(f"missing referenced id: {reference}")

    return sorted(set(errors)), sorted(set(warnings))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("svg", type=Path)
    parser.add_argument("--render", type=Path)
    args = parser.parse_args()

    errors, warnings = validate(args.svg)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1

    if args.render:
        renderer = shutil.which("rsvg-convert")
        if not renderer:
            print("ERROR: rsvg-convert is unavailable", file=sys.stderr)
            return 1
        args.render.parent.mkdir(parents=True, exist_ok=True)
        result = subprocess.run(
            [renderer, str(args.svg), "-o", str(args.render)],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode:
            print(result.stderr.strip() or "ERROR: render failed", file=sys.stderr)
            return 1
        print(f"Rendered preview: {args.render}")

    print(f"Valid editable SVG: {args.svg}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
