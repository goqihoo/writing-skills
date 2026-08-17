# Scribe Repository

This repository contains composable skills for professional documents and technical visuals.

## Skill buckets

- `skills/foundations/` — the explicit Scribe guide and shared methods.
- `skills/knowledge/` — reusable knowledge artifacts.
- `skills/product/` — company Product Documentation artifacts and lifecycle assessment.
- `skills/technical/` — company Technical Documentation artifacts.
- `skills/visual/` — visual selection and production.

Every skill directory must contain `SKILL.md` and `agents/openai.yaml`. Add a resource only when the skill uses it.

## Invocation

Every skill is user-invoked. Set `disable-model-invocation: true` in every `SKILL.md` and `policy.allow_implicit_invocation: false` in every `agents/openai.yaml`.

The user must name every skill required by a composed workflow. `ask-scribe` explains Scribe's skills, boundaries, composition rules, and complete invocation choices; it never invokes another skill, performs its workflow, modifies files, or produces another skill's artifact.

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

- `write-doc` owns an optional general-purpose prose workflow for reader flow, concrete language, sentence movement, emphasis, and formatting. Artifact skills remain complete without it and retain genre, structure, facts, and technical meaning.
- `reason-architecture` owns the architecture method shared by architecture artifacts.
- `reason-domain` owns domain admission, boundaries, relationships, subdomain validity, high-level knowledge ownership, maturity, and the Domain Assessment handoff.
- `reason-product` owns product admission, boundaries, hierarchy, change and release authority, high-level knowledge ownership, and the Product Assessment handoff.
- `assess-product-lifecycle` owns product decision readiness, artifact coverage, evidence gaps, and the Product Lifecycle Assessment.
- `structure-docs` owns directory responsibilities, file placement, documentation navigation, and structure migrations.
- `structure-product-docs` owns the company Product core, accepted-product core, Type Extensions, Event Collections, navigation requirements, and product-structure migrations.
- `write-product-doc` owns the Product Internal Document Types; Product Strategy, Capability Map, Product Roadmap, PRD, and Product Metric System retain independent public skills.
- `reason-technical` owns company technical scope, Technical Landscape boundaries, responsibility admission, authority routing, and the Technical Assessment handoff.
- `structure-technical-docs` owns the Technical stable core, Type Extensions, Event Collections, navigation requirements, and technical-structure migrations.
- `write-technical-doc` owns standard Technical Internal Document Types.
- `write-technical-architecture` owns company Technical Architecture across the Technical Landscape.
- Each deliverable skill owns one artifact boundary, workflow, completion test, and output template.
- `draw-diagram` owns one visual's routing and quality, not architecture meaning.
- `ask-scribe` explains and recommends; the user retains control of every subsequent invocation and execution.

Keep each rule in one place. Compose an optional foundation when the user requests its additional workflow instead of copying it. Store output templates under `assets/`; disclose branch-specific guidance through one-level `references/`.

## Repository updates

When adding, renaming, or removing a skill:

1. Update its bucket README and the root README.
2. Update `.claude-plugin/plugin.json` and marketplace metadata.
3. Re-read and update `ask-scribe`.
4. Give every Public Skill a unique `interface.display_name`, recommend that exact display name in user-facing invocations, and preserve the canonical Skill ID for machine structure.
5. Validate every changed skill.
6. Run the test suite, `bash -n scripts/*.sh`, and `git diff --check`.

Write agent instructions in imperative form. End every workflow with a checkable completion condition. Keep `SKILL.md` concise and move conditional detail behind direct pointers.
