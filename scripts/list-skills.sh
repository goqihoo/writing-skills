#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"

while IFS= read -r skill_file; do
  skill_dir="$(dirname "$skill_file")"
  printf '%s\t%s\n' "$(basename "$skill_dir")" "${skill_dir#"$repo_root"/}"
done < <(find "$repo_root/skills" -name SKILL.md -not -path '*/deprecated/*' | sort)
