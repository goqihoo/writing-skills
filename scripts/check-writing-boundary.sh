#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills_root="$repo_root/skills"
methods_root="$repo_root/methods"
write_doc="$skills_root/write-doc/SKILL.md"
write_knowledge="$skills_root/write-knowledge/SKILL.md"
knowledge_types="$skills_root/write-knowledge/references/knowledge-types.md"
write_architecture_knowledge="$skills_root/write-architecture-knowledge/SKILL.md"
write_technical_architecture="$skills_root/write-technical-architecture/SKILL.md"
prose_method="$methods_root/prose-quality.md"
visual_method="$methods_root/visual-production.md"

for method in \
  domain-reasoning.md \
  product-reasoning.md \
  technical-reasoning.md \
  architecture-reasoning.md \
  internal-document-types.md \
  documentation-structure.md \
  prose-quality.md \
  visual-production.md; do
  if [[ ! -f "$methods_root/$method" ]]; then
    printf 'FAIL: missing Shared Method: %s\n' "$method" >&2
    exit 1
  fi
done

if find "$methods_root" -type f \( -name SKILL.md -o -name openai.yaml \) | rg -q .; then
  printf 'FAIL: Shared Methods must not expose skill metadata\n' >&2
  exit 1
fi

while IFS= read -r skill; do
  if ! rg -Fq 'methods/prose-quality.md' "$skill"; then
    printf 'FAIL: Public Skill does not apply Prose Quality: %s\n' "$skill" >&2
    exit 1
  fi

  for forbidden in 'Apply `$' 'required dependency' 'missing dependency' 'was not explicitly invoked'; do
    if rg -Fq "$forbidden" "$skill"; then
      printf 'FAIL: Public Skill exposes an implementation dependency: %s (%s)\n' "$skill" "$forbidden" >&2
      exit 1
    fi
  done
done < <(find "$skills_root" -mindepth 2 -maxdepth 2 -name SKILL.md -type f | sort)

required_prose_contract=(
  'Lock the artifact plan before prose work'
  'Revise reader-facing prose with the contract below after artifact logic and substance are stable'
  'The heading sequence, section responsibilities, and reasoning path match the artifact plan'
  '**Point first.**'
  '**Concrete before abstract.**'
  '**Causal movement.**'
)

for pattern in "${required_prose_contract[@]}"; do
  if ! rg -Fq "$pattern" "$prose_method"; then
    printf 'FAIL: Prose Quality is missing a shared contract rule: %s\n' "$pattern" >&2
    exit 1
  fi
done

required_structure_ownership=(
  "$knowledge_types|reasoning obligations, not an outline or default heading sequence"
  "$knowledge_types|that template owns the heading names, order, hierarchy, and permitted branches"
  "$write_knowledge|Derive the subject-specific reasoning spine"
  "$write_knowledge|selected type's questions as a coverage checklist"
  "$write_doc|Lock the artifact type, core question, reasoning path, outline, section responsibilities, and required material"
  "$write_architecture_knowledge|assets/architecture-knowledge-template.md"
  "$write_technical_architecture|references/internal-document-types.yaml"
  "$write_technical_architecture|Freeform Artifact"
)

for requirement in "${required_structure_ownership[@]}"; do
  file="${requirement%%|*}"
  pattern="${requirement#*|}"
  if ! rg -Fq "$pattern" "$file"; then
    printf 'FAIL: structure ownership rule is missing: %s\n' "$pattern" >&2
    exit 1
  fi
done

if rg -Fq 'primary use controls the main structure' "$knowledge_types"; then
  printf 'FAIL: knowledge type is still presented as the document outline owner\n' >&2
  exit 1
fi

required_visual_contract=(
  'when the user requests a visual or when the result would otherwise force readers to reconstruct a central relationship'
  'four or more meaningful nodes or relationships'
  'Choose the visual grammar before the file format'
  'Use Mermaid only when the user explicitly requests Mermaid'
  'Inspect the final render for clipping, overlap, unintended crop, malformed text, or watermark'
)

for pattern in "${required_visual_contract[@]}"; do
  if ! rg -Fq "$pattern" "$visual_method"; then
    printf 'FAIL: Visual Production is missing a shared contract rule: %s\n' "$pattern" >&2
    exit 1
  fi
done

printf 'PASS: Shared Methods, independent Public Skills, artifact structure, prose, and visuals retain separate ownership\n'
