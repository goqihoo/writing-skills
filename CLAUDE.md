# Scribe Repository

This repository contains composable skills for professional documents and technical visuals.

## Skill buckets

- `skills/foundations/` — the explicit router and shared methods.
- `skills/knowledge/` — reusable knowledge artifacts.
- `skills/product/` — product work artifacts.
- `skills/technical/` — project delivery and decision artifacts.
- `skills/visual/` — visual selection and production.

Every skill directory must contain `SKILL.md` and `agents/openai.yaml`. Add a resource only when the skill uses it.

## Invocation

Classify every skill as user-invoked or model-invoked:

- User-invoked skills set `disable-model-invocation: true` in `SKILL.md` and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
- Model-invoked skills omit both settings and name every trigger branch in the description.

`ask-scribe` is the user-invoked plugin index, like Ask Matt. Foundations and deliverable skills are model-invoked so the model and other skills can reach them.

Use `$skill-name` for ready-to-type Agent Skills invocations and `/skill-name` for Claude Code.

## Ownership

- `writing-docs` owns the writing method shared by all documents.
- `architecture-foundations` owns the architecture method shared by architecture artifacts.
- Each deliverable skill owns one artifact boundary, workflow, completion test, and output template.
- `draw-technical-architecture-diagrams` owns visual routing and quality, not architecture meaning.
- `ask-scribe` recommends a route and stops.

Keep each rule in one place. Invoke a foundation instead of copying it. Store output templates under `assets/`; disclose branch-specific guidance through one-level `references/`.

## Repository updates

When adding, renaming, or removing a skill:

1. Update its bucket README and the root README.
2. Update `.claude-plugin/plugin.json` and marketplace metadata.
3. Re-read and update `ask-scribe`.
4. Validate every changed skill.
5. Run `bash -n scripts/*.sh` and `git diff --check`.

Write agent instructions in imperative form. End every workflow with a checkable completion condition. Keep `SKILL.md` concise and move conditional detail behind direct pointers.
