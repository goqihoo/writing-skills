# Shared Methods

Shared Methods are internal, non-invocable rule sets used by Public Skills. They have no Skill ID, display name, `SKILL.md`, or client metadata. A Public Skill points directly to only the methods its workflow needs and remains responsible for its user-visible result and completion condition.

Keep this directory beside the public skill buckets in every installation. `scripts/link-skills.sh` links it at the client root so flat skill installs can resolve `../../methods/` without exposing another invocation.

Keep a method here only when at least two Public Skills reuse it. Keep artifact-specific branches, templates, and production assets with their owning skill.
