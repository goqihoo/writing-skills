#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
write_docs="$repo_root/skills/foundations/write-docs/SKILL.md"
write_knowledge="$repo_root/skills/knowledge/write-knowledge/SKILL.md"

forbidden_patterns=(
  "while planning, drafting, and revising"
  "Use it from the first sentence instead of treating expression as a separate polishing pass"
  "Use headings to advance the reader's questions"
)

for pattern in "${forbidden_patterns[@]}"; do
  if rg -Fq "$pattern" "$write_docs"; then
    printf 'FAIL: natural-writing guidance can change artifact planning or structure: %s\n' "$pattern" >&2
    exit 1
  fi
done

required_write_docs=(
  "Lock the artifact plan"
  "Do not add, remove, rename, or reorder sections"
  "Apply the natural writing guidance only after the artifact logic and substance are stable"
  "Compare the final heading sequence and section responsibilities with the locked artifact plan"
)

for pattern in "${required_write_docs[@]}"; do
  if ! rg -Fq "$pattern" "$write_docs"; then
    printf 'FAIL: write-docs is missing a structural guardrail: %s\n' "$pattern" >&2
    exit 1
  fi
done

if ! rg -Fq "Lock the reasoning path" "$write_knowledge"; then
  printf 'FAIL: write-knowledge does not lock the selected knowledge type before prose revision\n' >&2
  exit 1
fi

printf 'PASS: natural-writing guidance is structurally subordinate to the owning artifact skill\n'
