#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
write_doc="$repo_root/skills/foundations/write-doc/SKILL.md"
write_knowledge="$repo_root/skills/knowledge/write-knowledge/SKILL.md"
knowledge_types="$repo_root/skills/knowledge/write-knowledge/references/knowledge-types.md"
write_architecture_knowledge="$repo_root/skills/knowledge/write-architecture-knowledge/SKILL.md"
write_technical_architecture="$repo_root/skills/technical/write-technical-architecture/SKILL.md"
draw_diagrams="$repo_root/skills/visual/draw-diagrams/SKILL.md"

forbidden_patterns=(
  "while planning, drafting, and revising"
  "Use it from the first sentence instead of treating expression as a separate polishing pass"
  "Use headings to advance the reader's questions"
)

for pattern in "${forbidden_patterns[@]}"; do
  if rg -Fq "$pattern" "$write_doc"; then
    printf 'FAIL: shared prose guidance can change artifact planning or structure: %s\n' "$pattern" >&2
    exit 1
  fi
done

required_write_doc=(
  "Lock the artifact plan"
  "Do not add, remove, rename, or reorder locked sections"
  "Run the shared reader-flow pass after the artifact logic and substance are stable"
  "Compare the final heading sequence and section responsibilities with the locked artifact plan"
)

for pattern in "${required_write_doc[@]}"; do
  if ! rg -Fq "$pattern" "$write_doc"; then
    printf 'FAIL: write-doc is missing a structural guardrail: %s\n' "$pattern" >&2
    exit 1
  fi
done

required_structure_ownership=(
  "$knowledge_types|reasoning obligations, not an outline or default heading sequence"
  "$knowledge_types|that template owns the heading names, order, hierarchy, and permitted branches"
  "$write_knowledge|Derive the subject-specific reasoning spine"
  "$write_knowledge|selected type's questions as a coverage checklist"
  "$write_doc|treat the template as the structure owner"
  "$write_architecture_knowledge|assets/architecture-knowledge-template.md"
  "$write_technical_architecture|assets/technical-architecture-template.md"
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
  "$write_doc|Route visual questions"
  "$write_doc|a model would otherwise require repeated arrows or indentation"
  "$draw_diagrams|a central model with four or more meaningful nodes or relationships"
  "$write_architecture_knowledge|When \`\$draw-diagrams\` was explicitly invoked by the user"
  "$write_technical_architecture|When \`\$draw-diagrams\` was explicitly invoked by the user"
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
