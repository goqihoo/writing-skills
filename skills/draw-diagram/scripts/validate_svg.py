#!/usr/bin/env python3
"""Validate editable SVG diagrams and optionally render a preview."""

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
PATH_TOKEN = re.compile(r"[A-Za-z]|-?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][+-]?\d+)?")
CONNECTOR_CLASSES = {"connector", "edge", "flow", "later", "link"}
CONNECTOR_LABEL_CLASSES = {"arrow-label", "connector-label", "edge-label"}
CONNECTOR_LABEL_CLEARANCE = 6.0
SCRIBE_COLOR_MODES = {"categorical", "quantitative", "status", "neutral"}
SCRIBE_NEUTRAL_REASONS = {"color-only-restyle", "explicit-user-request"}
COLOR_ROLE = re.compile(
    r"var\(--dd-(category-([1-5])(?:-tint|-a[0-9]{3})?"
    r"|series-([1-5])(?:-tint|-a[0-9]{3})?"
    r"|(success|warning|failure)(?:-tint|-a[0-9]{3})?)\b"
)
CSS_CLASS_RULE = re.compile(r"\.([A-Za-z_][\w-]*)\s*\{([^}]*)\}", re.DOTALL)


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def class_tokens(element: ET.Element) -> set[str]:
    return set((element.get("class") or "").split())


def color_roles(value: str) -> set[str]:
    return {match.group(1) for match in COLOR_ROLE.finditer(value)}


def class_color_roles(root: ET.Element) -> dict[str, set[str]]:
    roles: dict[str, set[str]] = {}
    for element in root.iter():
        if local_name(element.tag) != "style":
            continue
        source = "".join(element.itertext())
        for class_name, declarations in CSS_CLASS_RULE.findall(source):
            roles.setdefault(class_name, set()).update(color_roles(declarations))
    return roles


def visible_elements(root: ET.Element):
    def walk(element: ET.Element, hidden_definition: bool = False):
        hidden_definition = hidden_definition or local_name(element.tag) == "defs"
        if not hidden_definition:
            yield element
        for child in element:
            yield from walk(child, hidden_definition)

    yield from walk(root)


def element_color_roles(
    element: ET.Element,
    roles_by_class: dict[str, set[str]],
) -> set[str]:
    roles = {
        role
        for value in element.attrib.values()
        for role in color_roles(value)
    }
    for class_name in class_tokens(element):
        roles.update(roles_by_class.get(class_name, set()))
    return roles


def subtree_color_roles(
    element: ET.Element,
    roles_by_class: dict[str, set[str]],
) -> set[str]:
    return {
        role
        for descendant in element.iter()
        for role in element_color_roles(descendant, roles_by_class)
    }


def validate_group_node_paint(root: ET.Element) -> list[str]:
    """Check node surfaces, including inherited paint and the source's class rules."""
    def paint_declarations(source: str) -> dict[str, str]:
        return {
            name.strip(): value.strip()
            for declaration in source.split(";")
            if ":" in declaration
            for name, value in [declaration.split(":", 1)]
            if name.strip() in {"fill", "stroke"}
        }

    rules = [
        (name, paint_declarations(declarations))
        for element in root.iter()
        if local_name(element.tag) == "style"
        for name, declarations in CSS_CLASS_RULE.findall("".join(element.itertext()))
    ]
    errors: list[str] = []

    def walk(element: ET.Element, category: str, inherited: dict[str, str]):
        if local_name(element.tag) == "defs":
            return
        category = element.get("data-category", category)
        classes = class_tokens(element)
        paint = dict(inherited)
        paint.update({name: element.get(name) for name in ("fill", "stroke") if element.get(name) is not None})
        for name, declarations in rules:
            if name in classes:
                paint.update(declarations)
        paint.update(paint_declarations(element.get("style", "")))
        if category in {"1", "2", "3", "4", "5"} and "node" in classes:
            for name in ("fill", "stroke"):
                value = paint.get(name, "")
                if name == "stroke" and value in {"", "none"}:
                    continue
                roles = color_roles(value)
                if not roles or any(
                    not re.fullmatch(rf"category-{category}(?:-tint|-a[0-9]{{3}})?", role)
                    for role in roles
                ):
                    errors.append(f"node {element.get('id', '(unnamed)')} in data-category={category} needs matching category {name}")
        for child in element:
            walk(child, category, paint)

    walk(root, "", {})
    return errors


def validate_scribe_color_contract(root: ET.Element) -> list[str]:
    errors: list[str] = []
    mode = root.get("data-scribe-color-mode", "")
    if mode not in SCRIBE_COLOR_MODES:
        return [
            "data-scribe-color-mode must be one of "
            + ", ".join(sorted(SCRIBE_COLOR_MODES))
        ]

    roles_by_class = class_color_roles(root)
    visible_roles = {
        role
        for element in visible_elements(root)
        for role in element_color_roles(element, roles_by_class)
    }
    category_numbers = {
        match.group(1)
        for role in visible_roles
        if (match := re.fullmatch(r"category-([1-5])(?:-tint|-a[0-9]{3})?", role))
    }
    series_numbers = {
        match.group(1)
        for role in visible_roles
        if (match := re.fullmatch(r"series-([1-5])(?:-tint|-a[0-9]{3})?", role))
    }
    status_roles = {
        role.split("-", 1)[0]
        for role in visible_roles
        if role.split("-", 1)[0] in {"success", "warning", "failure"}
    }

    if mode == "categorical" and not category_numbers:
        errors.append(
            "categorical color mode needs visible category paint; "
            "palette definitions inside <defs> do not count"
        )
    elif mode == "quantitative" and not series_numbers:
        errors.append(
            "quantitative color mode needs visible series paint; "
            "palette definitions inside <defs> do not count"
        )
    elif mode == "status" and not status_roles:
        errors.append(
            "status color mode needs visible success, warning, or failure paint"
        )
    elif mode == "neutral":
        reason = root.get("data-scribe-neutral-reason", "")
        if reason not in SCRIBE_NEUTRAL_REASONS:
            errors.append(
                "neutral color mode needs data-scribe-neutral-reason="
                "color-only-restyle or explicit-user-request"
            )

    for element in root.iter():
        category = element.get("data-category")
        if category is None:
            continue
        if category not in {"1", "2", "3", "4", "5"}:
            errors.append(f"invalid data-category value: {category!r}")
            continue
        matching = {
            role
            for role in subtree_color_roles(element, roles_by_class)
            if re.fullmatch(rf"category-{category}(?:-tint|-a[0-9]{{3}})?", role)
        }
        if not matching:
            errors.append(
                f"data-category={category} has no visible matching category paint"
            )
    if mode == "categorical":
        errors.extend(validate_group_node_paint(root))
    return errors


def connector_segments(element: ET.Element) -> list[tuple[float, float, float, float]]:
    tag = local_name(element.tag)
    if not (class_tokens(element) & CONNECTOR_CLASSES):
        return []
    if tag == "line":
        try:
            return [
                (
                    float(element.get("x1", "0")),
                    float(element.get("y1", "0")),
                    float(element.get("x2", "0")),
                    float(element.get("y2", "0")),
                )
            ]
        except ValueError:
            return []
    if tag != "path":
        return []

    tokens = PATH_TOKEN.findall(element.get("d", ""))
    if any(token in "CcSsQqTtAa" for token in tokens):
        return []

    segments: list[tuple[float, float, float, float]] = []
    index = 0
    command = ""
    x = y = 0.0
    while index < len(tokens):
        if tokens[index].isalpha():
            command = tokens[index]
            index += 1
        try:
            if command in {"M", "m"}:
                next_x, next_y = map(float, tokens[index : index + 2])
                index += 2
                if command == "m":
                    next_x += x
                    next_y += y
                x, y = next_x, next_y
                command = "L" if command == "M" else "l"
            elif command in {"L", "l"}:
                next_x, next_y = map(float, tokens[index : index + 2])
                index += 2
                if command == "l":
                    next_x += x
                    next_y += y
                segments.append((x, y, next_x, next_y))
                x, y = next_x, next_y
            elif command in {"H", "h"}:
                next_x = float(tokens[index])
                index += 1
                if command == "h":
                    next_x += x
                segments.append((x, y, next_x, y))
                x = next_x
            elif command in {"V", "v"}:
                next_y = float(tokens[index])
                index += 1
                if command == "v":
                    next_y += y
                segments.append((x, y, x, next_y))
                y = next_y
            elif command in {"Z", "z"}:
                command = ""
            else:
                return []
        except (IndexError, ValueError):
            return []
    return segments


def connector_label_masks(root: ET.Element) -> list[ET.Element]:
    masks: list[ET.Element] = []
    for parent in root.iter():
        children = list(parent)
        for index, element in enumerate(children[:-1]):
            if local_name(element.tag) != "rect":
                continue
            if not any("mask" in token for token in class_tokens(element)):
                continue
            label = children[index + 1]
            if local_name(label.tag) != "text":
                continue
            if class_tokens(label) & CONNECTOR_LABEL_CLASSES:
                masks.append(element)
    return masks


def segment_nears_rect(
    segment: tuple[float, float, float, float],
    rect: tuple[float, float, float, float],
) -> bool:
    x1, y1, x2, y2 = segment
    rx, ry, width, height = rect
    margin = CONNECTOR_LABEL_CLEARANCE - 1e-9
    left, right = rx - margin, rx + width + margin
    top, bottom = ry - margin, ry + height + margin
    if y1 == y2:
        return top <= y1 <= bottom and max(x1, x2) >= left and min(x1, x2) <= right
    if x1 == x2:
        return left <= x1 <= right and max(y1, y2) >= top and min(y1, y2) <= bottom
    return False


def has_connector_label_collision(root: ET.Element) -> bool:
    segments = [
        segment
        for element in root.iter()
        for segment in connector_segments(element)
    ]
    for mask in connector_label_masks(root):
        try:
            rect = (
                float(mask.get("x", "0")),
                float(mask.get("y", "0")),
                float(mask.get("width", "0")),
                float(mask.get("height", "0")),
            )
        except ValueError:
            continue
        if any(segment_nears_rect(segment, rect) for segment in segments):
            return True
    return False


def validate(
    path: Path,
    require_scribe_color: bool = False,
) -> tuple[list[str], list[str]]:
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
    if has_connector_label_collision(root):
        errors.append("connector label mask must stay at least 6px from every connector")
    if require_scribe_color:
        errors.extend(validate_scribe_color_contract(root))

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
    parser.add_argument(
        "--scribe",
        action="store_true",
        help="enforce the Scribe visible-color contract on editable source",
    )
    args = parser.parse_args()

    errors, warnings = validate(args.svg, require_scribe_color=args.scribe)
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
