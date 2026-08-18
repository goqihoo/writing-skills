#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
if [ "$#" -gt 0 ]; then
  destinations=("$@")
else
  destinations=("$HOME/.claude/skills" "$HOME/.agents/skills")
fi

names=()
sources=()
methods_source="$repo_root/methods"
while IFS= read -r -d '' skill_file; do
  skill_dir="$(dirname "$skill_file")"
  names+=("$(basename "$skill_dir")")
  sources+=("$skill_dir")
done < <(find "$repo_root/skills" -name SKILL.md -not -path '*/deprecated/*' -print0)

for destination in "${destinations[@]}"; do
  methods_target="$(dirname "$destination")/methods"
  if [ -L "$destination" ]; then
    resolved="$(readlink -f "$destination")"
    case "$resolved" in
      "$repo_root"|"$repo_root"/*)
        echo "error: $destination resolves inside this repository: $resolved" >&2
        exit 1
        ;;
    esac
  fi

  if [ -e "$methods_target" ] && [ ! -L "$methods_target" ]; then
    echo "error: refusing to replace non-symlink Shared Methods: $methods_target" >&2
    exit 1
  fi

  for name in "${names[@]}"; do
    target="$destination/$name"
    if [ -e "$target" ] && [ ! -L "$target" ]; then
      echo "error: refusing to replace non-symlink skill: $target" >&2
      exit 1
    fi
  done
done

for destination in "${destinations[@]}"; do
  mkdir -p "$destination"
  methods_target="$(dirname "$destination")/methods"
  ln -sfn "$methods_source" "$methods_target"
  echo "linked Shared Methods -> $methods_source ($methods_target)"
  for index in "${!names[@]}"; do
    name="${names[$index]}"
    source_dir="${sources[$index]}"
    target="$destination/$name"
    ln -sfn "$source_dir" "$target"
    echo "linked $name -> $source_dir ($destination)"
  done
done
