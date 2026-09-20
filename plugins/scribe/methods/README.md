# Shared Methods

Shared Methods are internal, non-invocable rule sets used by Public Skills. They have no Skill ID, display name, `SKILL.md`, or client metadata. A Public Skill points directly to only the methods its workflow needs and remains responsible for its user-visible result and completion condition.

Keep this directory beside the flat `skills/` directory in every installation. `scripts/link-skills.sh` links it at the client root so standalone skill installs can resolve `../../methods/` without exposing another invocation. `scripts/build-codex-plugin.sh` copies it beside the Codex package's flat skill directory for the same reason.

Keep a method here only when at least two Public Skills reuse it. Keep artifact-specific branches, templates, and production assets with their owning skill.
