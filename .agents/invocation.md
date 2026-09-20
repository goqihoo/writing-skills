# Skill invocation

Every Scribe skill is user-invoked. Set `disable-model-invocation: true` in `SKILL.md` and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.

Treat the directory and frontmatter `name` as the canonical Skill ID. Treat `agents/openai.yaml` `interface.display_name` as the authoritative Skill Display Name. Both exact names invoke the same skill; the display name is the recommended user-facing form.

Use `$Ask Scribe` or `$ask-scribe` in Agent Skills-compatible clients and `/Ask Scribe` or `/ask-scribe` in Claude Code. Preserve exact display-name capitalization and spacing. Keep Skill IDs in paths, manifests, code, and other machine-facing structures.

Recommend one Public Skill for one requested result. Every Public Skill completes its core workflow without requiring another invocation. Multiple named skills represent multiple independently requested results, never implementation dependencies.

Apply repository Shared Methods from `methods/` internally. Do not expose those methods as skills or ask the user to invoke a reasoning, structure, prose, or visual skill to unblock another skill. A skill owns its artifact-specific references and templates; Shared Methods own their cross-skill implementation rules and supporting guides.
