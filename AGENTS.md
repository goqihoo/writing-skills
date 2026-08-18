# Scribe Repository

This repository contains composable skills for professional documents and technical visuals.

## Repository layout

- `skills/<skill-id>/` — flat Public Skill directories discovered directly by Codex and Claude Code.
- `methods/` — internal Shared Methods that Public Skills read directly.
- `plugins/scribe/` — generated Codex plugin package; never edit its copied skills or methods directly.

Describe the Foundations, Knowledge, Product Documentation, Technical Documentation, and Visual classifications in the catalog and architecture docs. Do not encode those classifications as intermediate directories under `skills/`.

Every skill directory must contain `SKILL.md` and `agents/openai.yaml`. Add a resource only when the skill uses it.

## Invocation

Every canonical Public Skill under `skills/` is user-invoked, independently valuable, and complete for its core result. Set `disable-model-invocation: true` in every canonical `SKILL.md` and `policy.allow_implicit_invocation: false` in every `agents/openai.yaml`. The generated Codex package removes the Claude-specific `disable-model-invocation` field while preserving the Codex policy.

Recommend one Public Skill for one requested result. Never require the user to invoke a reasoning, structure, prose, or visual skill so another Public Skill can work. Multiple named skills mean multiple independently requested results. `ask-scribe` explains Scribe's catalog and recommends a single end-to-end skill by default; it never invokes another skill, performs its workflow, modifies files, or produces another skill's artifact.

Store cross-skill implementation rules under `methods/`. Shared Methods are packaged with the public skills but are not skills themselves, have no skill metadata, and are never exposed as invocations. Public Skills apply the relevant Shared Methods internally.

Every Public Skill has a canonical **Skill ID** from its directory and `SKILL.md` frontmatter plus a unique **Skill Display Name** from `agents/openai.yaml` `interface.display_name`. The exact Skill ID and exact Skill Display Name are both valid invocation names. Preserve the Skill ID in paths, frontmatter, manifests, and code. Use the Skill Display Name for recommended user-facing invocations and introduce catalog entries as `Skill Display Name` (`skill-id`).

Use `$Ask Scribe` or `$ask-scribe` in Agent Skills clients and `/Ask Scribe` or `/ask-scribe` in Claude Code. Guarantee only the exact configured spelling, capitalization, and spacing; do not promise fuzzy matching or normalization.

## Agent skills

### Issue tracker

Issues and specifications are stored as local Markdown files under `.scratch/`. See `docs/agents/issue-tracker.md`.

### Triage labels

Use the five default triage labels recorded in `docs/agents/triage-labels.md`.

### Domain docs

This is a single-context repository using root `CONTEXT.md` and `docs/adr/`. See `docs/agents/domain.md`.

## Ownership

- `methods/prose-quality.md` owns the shared prose contract. Every Public Skill that creates, revises, reviews, or presents human-readable prose applies it proportionally.
- `methods/visual-production.md` owns shared visual routing and production. A Public Skill applies it internally when a visual is requested or materially improves the result.
- Domain, product, technical, architecture, and documentation-structure Shared Methods own their cross-skill reasoning rules.
- `write-doc` owns an optional general-purpose prose workflow as an independently valuable standalone result.
- `draw-diagram`, the four `reason-*` skills, and `structure-docs` expose their concerns only as independently valuable standalone workflows.
- `assess-product-lifecycle` owns product decision readiness, artifact coverage, evidence gaps, and the Product Lifecycle Assessment.
- `structure-docs` owns directory responsibilities, file placement, documentation navigation, and structure migrations.
- `structure-product-docs` owns the company Product core, accepted-product core, Type Extensions, Event Collections, navigation requirements, and product-structure migrations.
- `write-product-doc` owns the Product Internal Document Types; Product Strategy, Capability Map, Product Roadmap, PRD, and Product Metric System retain independent public skills.
- `reason-technical` owns company technical scope, Technical Landscape boundaries, responsibility admission, authority routing, and the Technical Assessment handoff.
- `structure-technical-docs` owns the Technical stable core, Type Extensions, Event Collections, navigation requirements, and technical-structure migrations.
- `write-technical-doc` owns standard Technical Internal Document Types.
- `write-technical-architecture` owns company Technical Architecture across the Technical Landscape.
- Each deliverable skill owns one artifact boundary, workflow, completion test, and output template.
- `draw-diagram` owns one independently requested visual, not architecture meaning.
- `ask-scribe` explains and recommends; the user retains control of every subsequent invocation and execution.

Keep each shared rule in one method. Apply Shared Methods internally instead of copying them or exposing them as dependencies. Store output templates under `assets/`; disclose branch-specific guidance through one-level `references/`.

## Repository updates

When adding, renaming, or removing a skill:

1. Update the classified catalog in the root README.
2. Update `.claude-plugin/plugin.json` and marketplace metadata when their shared paths or plugin metadata change.
3. Re-read and update `ask-scribe`.
4. Give every Public Skill a unique `interface.display_name`, recommend that exact display name in user-facing invocations, and preserve the canonical Skill ID for machine structure.
5. Rebuild the Codex package with `scripts/build-codex-plugin.sh` and verify it with `scripts/build-codex-plugin.sh --check`.
6. Validate canonical skills with `claude plugin validate .`; validate the generated Codex package with the Codex plugin validator. The generic Codex skill validator does not accept the Claude-only `disable-model-invocation` field in canonical sources.
7. Run the test suite, `bash -n scripts/*.sh`, and `git diff --check`.

Write agent instructions in imperative form. End every workflow with a checkable completion condition. Keep `SKILL.md` concise and move conditional detail behind direct pointers.
