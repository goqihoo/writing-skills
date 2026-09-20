#!/usr/bin/env python3

import argparse
import re
import sys
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = REPO_ROOT / "docs/internal-document-types.md"
OWNER_SKILLS = [
    "write-product-doc",
    "write-technical-architecture",
    "write-technical-doc",
]
REQUIRED_ENTRY_FIELDS = [
    "id",
    "name",
    "description",
    "reader_question",
    "authority",
    "completion",
]
ALLOWED_POLICIES = {"fixed", "sequence", "adaptive"}
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def registry_path(owner_skill: str) -> Path:
    return (
        REPO_ROOT
        / "skills"
        / owner_skill
        / "references/internal-document-types.yaml"
    )


def load_and_validate(owner_skill: str) -> dict:
    path = registry_path(owner_skill)
    registry = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(registry, dict):
        raise ValueError(f"{path}: registry must be a mapping")
    if registry.get("schema_version") != 1:
        raise ValueError(f"{path}: schema_version must be 1")
    if registry.get("owner_skill") != owner_skill:
        raise ValueError(f"{path}: owner_skill must be {owner_skill}")
    if not str(registry.get("model", "")).strip():
        raise ValueError(f"{path}: model is required")

    ids = set()
    names = set()
    templates = set()
    entries = registry.get("types")
    if not isinstance(entries, list):
        raise ValueError(f"{path}: types must be a list")

    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError(f"{path}: every type must be a mapping")
        for field in REQUIRED_ENTRY_FIELDS:
            value = entry.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(
                    f"{path}: {field} must be a non-empty string for every type"
                )
        type_id = entry["id"]
        if not ID_PATTERN.fullmatch(type_id):
            raise ValueError(f"{path}: invalid type id {type_id!r}")
        if type_id in ids or entry["name"] in names:
            raise ValueError(f"{path}: duplicate type id or name for {type_id}")
        ids.add(type_id)
        names.add(entry["name"])

        template = entry.get("template")
        if template is None:
            continue
        if not isinstance(template, dict):
            raise ValueError(f"{path}: template for {type_id} must be a mapping")
        policy = template.get("policy")
        if policy not in ALLOWED_POLICIES:
            raise ValueError(f"{path}: invalid template policy for {type_id}")
        relative_path = template.get("path")
        if not isinstance(relative_path, str) or not relative_path.strip():
            raise ValueError(f"{path}: template path is required for {type_id}")
        resolved = (path.parent / relative_path).resolve()
        if not resolved.is_file():
            raise ValueError(f"{path}: missing template for {type_id}: {resolved}")
        if resolved in templates:
            raise ValueError(f"{path}: template is assigned more than once: {resolved}")
        templates.add(resolved)

    bundled = {
        candidate.resolve()
        for candidate in (REPO_ROOT / "skills" / owner_skill / "assets").glob("*.md")
    }
    if bundled != templates:
        missing = sorted(str(path) for path in templates - bundled)
        dormant = sorted(str(path) for path in bundled - templates)
        raise ValueError(
            f"{path}: template mismatch; missing={missing}, dormant={dormant}"
        )
    return registry


def escape_cell(value: str) -> str:
    return " ".join(value.split()).replace("|", "\\|")


def render_catalog(registries: list[dict]) -> str:
    lines = [
        "# Internal Document Types",
        "",
        "This catalog is generated from the Product and Technical Writer registries. Edit the owning `references/internal-document-types.yaml` file, then regenerate this document.",
        "",
        "A missing template means **Freeform Structure**. A configured template reports its explicit `fixed`, `sequence`, or `adaptive` policy.",
        "",
    ]
    for registry in registries:
        lines.extend(
            [
                f"## {registry['model']}",
                "",
                f"Owner: `{registry['owner_skill']}`",
                "",
                "| Type | Description | Reader question | Authority | Mode | Completion |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        for entry in registry["types"]:
            template = entry.get("template")
            mode = (
                "Freeform Structure"
                if template is None
                else f"Templated / {template['policy']}"
            )
            cells = [
                f"**{entry['name']}** (`{entry['id']}`)",
                entry["description"],
                entry["reader_question"],
                entry["authority"],
                mode,
                entry["completion"],
            ]
            lines.append("| " + " | ".join(escape_cell(cell) for cell in cells) + " |")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    try:
        registries = [load_and_validate(owner) for owner in OWNER_SKILLS]
    except (OSError, ValueError, yaml.YAMLError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    rendered = render_catalog(registries)
    if args.check:
        if not CATALOG_PATH.is_file() or CATALOG_PATH.read_text(encoding="utf-8") != rendered:
            print(f"error: generated catalog is stale: {CATALOG_PATH}", file=sys.stderr)
            return 1
        print("PASS: Internal Document Type catalog matches canonical registries")
        return 0

    CATALOG_PATH.write_text(rendered, encoding="utf-8")
    print(f"Generated {CATALOG_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
