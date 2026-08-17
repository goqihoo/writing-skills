# Skill invocation

Every Scribe skill is user-invoked. Set `disable-model-invocation: true` in `SKILL.md` and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.

Treat the directory and frontmatter `name` as the canonical Skill ID. Treat `agents/openai.yaml` `interface.display_name` as the authoritative Skill Display Name. Both exact names invoke the same skill; the display name is the recommended user-facing form.

Use `$Ask Scribe` or `$ask-scribe` in Agent Skills-compatible clients and `/Ask Scribe` or `/ask-scribe` in Claude Code. Preserve exact display-name capitalization and spacing. Keep Skill IDs in paths, manifests, code, and other machine-facing structures.

Express required dependencies with their display-name invocation, such as “Apply `$Reason Domain`.” Present optional skills as additions rather than dependencies. Do not link across skill directories. A skill owns its own references and templates.
