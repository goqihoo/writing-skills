#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
write_docs="$repo_root/skills/foundations/write-docs/SKILL.md"
write_knowledge="$repo_root/skills/knowledge/write-knowledge/SKILL.md"
knowledge_types="$repo_root/skills/knowledge/write-knowledge/references/knowledge-types.md"
study_architecture="$repo_root/skills/knowledge/study-architecture/SKILL.md"
design_architecture="$repo_root/skills/technical/design-architecture/SKILL.md"
draw_diagrams="$repo_root/skills/visual/draw-diagrams/SKILL.md"

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
  "Do not add, remove, rename, or reorder locked sections"
  "Apply the natural writing guidance only after the artifact logic and substance are stable"
  "Compare the final heading sequence and section responsibilities with the locked artifact plan"
)

for pattern in "${required_write_docs[@]}"; do
  if ! rg -Fq "$pattern" "$write_docs"; then
    printf 'FAIL: write-docs is missing a structural guardrail: %s\n' "$pattern" >&2
    exit 1
  fi
done

if ! rg -Fq "Lock the artifact plan" "$write_knowledge"; then
  printf 'FAIL: write-knowledge does not lock the subject-specific reasoning before prose revision\n' >&2
  exit 1
fi

required_structure_ownership=(
  "$knowledge_types|reasoning obligations, not an outline or default heading sequence"
  "$knowledge_types|that template owns the heading names, order, hierarchy, and permitted branches"
  "$write_knowledge|Derive the subject-specific reasoning spine"
  "$write_knowledge|selected type's questions as a coverage checklist"
  "$write_docs|treat the template as the structure owner"
  "$study_architecture|Preserve its H2 heading names, order, and hierarchy"
  "$design_architecture|Preserve its heading names, order, and hierarchy"
)

for requirement in "${required_structure_ownership[@]}"; do
  file="${requirement%%|*}"
  pattern="${requirement#*|}"
  if ! rg -Fq "$pattern" "$file"; then
    printf 'FAIL: structure ownership rule is missing: %s\n' "$pattern" >&2
    exit 1
  fi
done

if rg -Fq "primary use controls the main structure" "$knowledge_types"; then
  printf 'FAIL: knowledge type is still presented as the document outline owner\n' >&2
  exit 1
fi

required_visual_routing=(
  "$write_docs|Route visual questions"
  "$write_docs|a model would otherwise require repeated arrows or indentation"
  "$draw_diagrams|a central model with four or more meaningful nodes or relationships"
  "$draw_diagrams|Treat a central idea written as repeated arrows, nested indentation, or a prose tour through several relationships as a visual candidate"
  "$study_architecture|For each visual candidate identified by \`\$write-docs\`"
  "$design_architecture|For each visual candidate identified by \`\$write-docs\`"
)

for requirement in "${required_visual_routing[@]}"; do
  file="${requirement%%|*}"
  pattern="${requirement#*|}"
  if ! rg -Fq "$pattern" "$file"; then
    printf 'FAIL: visual routing rule is missing: %s\n' "$pattern" >&2
    exit 1
  fi
done

printf 'PASS: prose, subject reasoning, explicit templates, and visuals retain separate ownership\n'
