# Writing Skills Repository

This repository contains composable skills for writing reusable knowledge and professional work artifacts.

## Skill buckets

- `skills/foundations/` — shared writing discipline and the repository router.
- `skills/knowledge/` — reusable knowledge documents.
- `skills/product/` — product work artifacts.
- `skills/technical/` — technical work artifacts.

Every skill directory must contain `SKILL.md` and `agents/openai.yaml`. Add assets or references only when the skill uses them.

## Invocation

Classify every skill as either user-invoked or model-invoked:

- User-invoked skills set `disable-model-invocation: true` in `SKILL.md` and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
- Model-invoked skills omit both settings and use a description that states all trigger branches.

`ask-writing` is model-invoked so it can answer skill-discovery and comparison questions without requiring the user to remember its name. Keep other writing and review skills model-invoked unless a concrete workflow requires explicit orchestration.

Use `$skill-name` for ready-to-type invocations in Agent Skills-compatible clients and `/skill-name` in Claude Code. Keep bare skill names in cross-client maps and comparisons.

## Ownership

- `writing-foundations` owns rules shared by every document: outcome, reader path, facts, reasoning, decisions, concrete language, boundaries, and completion checks.
- Each deliverable skill owns its document-specific workflow, structure, completion criteria, and template.
- Keep each rule in one place. Invoke `/writing-foundations` from deliverable skills instead of copying shared rules.
- Templates under `assets/` are output material. Detailed guidance under `references/` is loaded only when its branch applies.

## Repository updates

When adding, renaming, or removing a skill:

1. Update the matching bucket `README.md` and the top-level `README.md`.
2. Update `.claude-plugin/plugin.json`.
3. Re-read and update `ask-writing` so its routes stay accurate.
4. Run the skill validator on every changed skill.
5. Run `bash -n scripts/*.sh` and inspect `git diff --check`.

Write agent instructions in imperative form. Give every workflow step a checkable completion condition. Keep `SKILL.md` concise and disclose branch-specific detail through one-level references.
