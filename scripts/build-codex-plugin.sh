#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills_root="$repo_root/skills"
methods_root="$repo_root/methods"
plugin_root="$repo_root/plugins/scribe"

if [[ ! -f "$plugin_root/.codex-plugin/plugin.json" ]]; then
  printf 'error: missing Codex plugin manifest: %s\n' "$plugin_root/.codex-plugin/plugin.json" >&2
  exit 1
fi

build_snapshot() {
  local target_root="$1"
  local skill_dir
  local skill_file
  local rewritten

  mkdir -p "$target_root/skills"
  cp -R "$methods_root" "$target_root/methods"

  for skill_dir in "$skills_root"/*; do
    [[ -d "$skill_dir" ]] || continue
    if [[ ! -f "$skill_dir/SKILL.md" ]]; then
      printf 'error: non-skill directory under flat skill root: %s\n' "$skill_dir" >&2
      exit 1
    fi
    cp -R "$skill_dir" "$target_root/skills/"
  done

  while IFS= read -r skill_file; do
    rewritten="$skill_file.codex"
    awk '$0 != "disable-model-invocation: true"' "$skill_file" > "$rewritten"
    mv "$rewritten" "$skill_file"
  done < <(find "$target_root/skills" -mindepth 2 -maxdepth 2 -name SKILL.md -type f | sort)
}

staging_root="$(mktemp -d)"
backup_root="$(mktemp -d)"
cleanup() {
  rm -rf "$staging_root" "$backup_root"
}
trap cleanup EXIT

build_snapshot "$staging_root"

if [[ "${1:-}" == "--check" ]]; then
  diff -ru "$plugin_root/skills" "$staging_root/skills"
  diff -ru "$plugin_root/methods" "$staging_root/methods"
  printf 'PASS: Codex plugin package matches the canonical flat skills and Shared Methods\n'
  exit 0
fi

if [[ "$#" -ne 0 ]]; then
  printf 'usage: %s [--check]\n' "$0" >&2
  exit 2
fi

if [[ -e "$plugin_root/skills" ]]; then
  mv "$plugin_root/skills" "$backup_root/skills"
fi
if [[ -e "$plugin_root/methods" ]]; then
  mv "$plugin_root/methods" "$backup_root/methods"
fi

mv "$staging_root/skills" "$plugin_root/skills"
mv "$staging_root/methods" "$plugin_root/methods"

printf 'Built Codex plugin package at %s\n' "$plugin_root"
