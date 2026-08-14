#!/usr/bin/env python3
"""Evaluate a generated Markdown document against a structural contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


HEADING_PATTERN = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
INLINE_LINK_PATTERN = re.compile(r"\]\((?:<([^>\n]+)>|([^\)\n]+))\)")
URI_SCHEME_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


class ContractError(ValueError):
    """Raised when an evaluation contract is invalid."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check a candidate Markdown document against a source and JSON contract."
    )
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument("--contract", required=True, type=Path)
    return parser.parse_args()


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as error:
        raise ContractError(f"cannot read {path}: {error}") from error


def read_contract(path: Path) -> dict[str, Any]:
    try:
        contract = json.loads(read_text(path))
    except json.JSONDecodeError as error:
        raise ContractError(f"invalid JSON in {path}: {error}") from error
    if not isinstance(contract, dict):
        raise ContractError("contract root must be a JSON object")
    return contract


def markdown_headings(text: str) -> list[str]:
    headings: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            continue
        if fence is not None:
            continue
        match = HEADING_PATTERN.match(line)
        if match:
            headings.append(f"{len(match.group(1))}:{match.group(2).strip()}")
    return headings


def heading_parts(heading: str) -> tuple[int, str]:
    level, title = heading.split(":", 1)
    return int(level), title


def object_field(contract: dict[str, Any], field: str) -> dict[str, Any] | None:
    value = contract.get(field)
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ContractError(f"{field} must be an object")
    return value


def boolean_option(config: dict[str, Any], field: str, default: bool) -> bool:
    value = config.get(field, default)
    if not isinstance(value, bool):
        raise ContractError(f"{field} must be a boolean")
    return value


def ordered_subsequence(expected: list[str], actual: list[str]) -> bool:
    expected_index = 0
    for heading in actual:
        while expected_index < len(expected) and expected[expected_index] != heading:
            expected_index += 1
        if expected_index == len(expected):
            return False
        expected_index += 1
    return True


def relative_markdown_links(text: str) -> Counter[str]:
    links: Counter[str] = Counter()
    for match in INLINE_LINK_PATTERN.finditer(text):
        target = (match.group(1) or match.group(2)).strip()
        if (
            not target
            or target.startswith(("#", "/"))
            or URI_SCHEME_PATTERN.match(target)
        ):
            continue
        links[target] += 1
    return links


def named_patterns(contract: dict[str, Any], field: str) -> list[tuple[str, str]]:
    raw_patterns = contract.get(field, [])
    if not isinstance(raw_patterns, list):
        raise ContractError(f"{field} must be a list")

    patterns: list[tuple[str, str]] = []
    for index, item in enumerate(raw_patterns):
        if not isinstance(item, dict):
            raise ContractError(f"{field}[{index}] must be an object")
        name = item.get("name")
        pattern = item.get("pattern")
        if not isinstance(name, str) or not name:
            raise ContractError(f"{field}[{index}].name must be a non-empty string")
        if not isinstance(pattern, str) or not pattern:
            raise ContractError(f"{field}[{index}].pattern must be a non-empty string")
        try:
            re.compile(pattern)
        except re.error as error:
            raise ContractError(f"invalid regex for {name}: {error}") from error
        patterns.append((name, pattern))
    return patterns


def evaluate(source: str, candidate: str, contract: dict[str, Any]) -> list[str]:
    failures: list[str] = []

    if contract.get("preserve_heading_sequence", False):
        expected_headings = markdown_headings(source)
        actual_headings = markdown_headings(candidate)
        if actual_headings != expected_headings:
            failures.append(
                "heading sequence changed\n"
                f"  expected: {expected_headings}\n"
                f"  actual:   {actual_headings}"
            )

    if contract.get("preserve_relative_links", False):
        expected_links = relative_markdown_links(source)
        actual_links = relative_markdown_links(candidate)
        if actual_links != expected_links:
            missing = list((expected_links - actual_links).elements())
            added = list((actual_links - expected_links).elements())
            failures.append(
                "relative Markdown links changed\n"
                f"  missing: {missing}\n"
                f"  added:   {added}"
            )

    heading_match_limit = object_field(contract, "heading_match_limit")
    if heading_match_limit is not None:
        reference_headings = heading_match_limit.get("headings")
        if not isinstance(reference_headings, list) or not all(
            isinstance(heading, str) and heading for heading in reference_headings
        ):
            raise ContractError(
                "heading_match_limit.headings must be a list of non-empty strings"
            )

        levels = heading_match_limit.get("levels", [2])
        if not isinstance(levels, list) or not levels or not all(
            isinstance(level, int) and not isinstance(level, bool) and 1 <= level <= 6
            for level in levels
        ):
            raise ContractError(
                "heading_match_limit.levels must be a non-empty list of levels 1-6"
            )

        max_matches = heading_match_limit.get("max_matches")
        if (
            not isinstance(max_matches, int)
            or isinstance(max_matches, bool)
            or max_matches < 0
        ):
            raise ContractError(
                "heading_match_limit.max_matches must be a non-negative integer"
            )

        references = set(reference_headings)
        level_set = set(levels)
        matches = [
            title
            for level, title in map(heading_parts, markdown_headings(candidate))
            if level in level_set and title in references
        ]
        if len(matches) > max_matches:
            failures.append(
                "heading match limit exceeded: "
                f"{len(matches)} matches, maximum {max_matches}\n"
                f"  matches: {matches}"
            )

    template_heading_sequence = object_field(
        contract, "template_heading_sequence"
    )
    if template_heading_sequence is not None:
        ignore_title = boolean_option(
            template_heading_sequence, "ignore_title", True
        )
        allow_omissions = boolean_option(
            template_heading_sequence, "allow_omissions", False
        )
        required_levels = template_heading_sequence.get("required_levels", [])
        if not isinstance(required_levels, list) or not all(
            isinstance(level, int) and not isinstance(level, bool) and 1 <= level <= 6
            for level in required_levels
        ):
            raise ContractError(
                "template_heading_sequence.required_levels must be a list of levels 1-6"
            )
        expected_headings = markdown_headings(source)
        actual_headings = markdown_headings(candidate)
        if ignore_title:
            expected_headings = [
                heading
                for heading in expected_headings
                if heading_parts(heading)[0] != 1
            ]
            actual_headings = [
                heading
                for heading in actual_headings
                if heading_parts(heading)[0] != 1
            ]

        required_level_set = set(required_levels)
        required_headings = Counter(
            heading
            for heading in expected_headings
            if heading_parts(heading)[0] in required_level_set
        )
        missing_required_headings = list(
            (required_headings - Counter(actual_headings)).elements()
        )
        if missing_required_headings:
            failures.append(
                "required template headings missing: "
                f"{missing_required_headings}"
            )

        sequence_matches = (
            ordered_subsequence(expected_headings, actual_headings)
            if allow_omissions
            else expected_headings == actual_headings
        )
        if not sequence_matches:
            failures.append(
                "template heading sequence changed\n"
                f"  template:  {expected_headings}\n"
                f"  candidate: {actual_headings}"
            )

    flags = re.MULTILINE | re.DOTALL
    for name, pattern in named_patterns(contract, "required_patterns"):
        if re.search(pattern, candidate, flags) is None:
            failures.append(f"required pattern missing: {name}")

    for name, pattern in named_patterns(contract, "forbidden_patterns"):
        if re.search(pattern, candidate, flags) is not None:
            failures.append(f"forbidden pattern present: {name}")

    return failures


def main() -> int:
    args = parse_args()
    try:
        source = read_text(args.source)
        candidate = read_text(args.candidate)
        contract = read_contract(args.contract)
        failures = evaluate(source, candidate, contract)
    except ContractError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: document contract satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
