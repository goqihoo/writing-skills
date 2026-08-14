# Skill invocation

Use two invocation policies:

- **User-invoked:** only the human may select the skill. Set `disable-model-invocation: true` in `SKILL.md` and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
- **Model-invoked:** the model or the human may select the skill. Omit both settings and put every trigger branch in the description.

Use user invocation for explicit orchestration that must start only by direct request. Use model invocation for reusable writing disciplines, deliverable skills, and routers that should answer discovery questions automatically.

When giving a human a ready-to-type invocation, use `$skill-name` in Agent Skills-compatible clients and `/skill-name` in Claude Code. Keep bare skill names in cross-client maps and comparisons.

Express dependencies as prose invocation, such as “Apply the `/writing-foundations` skill.” Do not link across skill directories. A skill owns its own references and templates.
