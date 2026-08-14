# Skill invocation

Use two invocation policies:

- **User-invoked:** only the human may select the skill. Set `disable-model-invocation: true` in `SKILL.md` and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
- **Model-invoked:** the model or the human may select the skill. Omit both settings and put every trigger branch in the description.

Use user invocation for explicit routers and orchestration that must start only by direct request. Use model invocation for reusable foundations and deliverable skills that the model should reach on its own.

`ask-scribe` is user-invoked. It is the human-facing index for the Scribe plugin. `write-docs` and `reason-architecture` are model-invoked foundations and stay out of normal router recommendations unless the user needs their shared discipline directly.

When giving a human a ready-to-type invocation, use `$skill-name` in Agent Skills-compatible clients and `/skill-name` in Claude Code. Keep bare skill names in cross-client maps and comparisons.

Express dependencies as prose invocation, such as “Apply the `/write-docs` skill.” Do not link across skill directories. A skill owns its own references and templates.
