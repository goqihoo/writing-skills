# Scribe Repository

This repository contains composable skills for professional documents and technical visuals.

## Skill buckets

- `skills/foundations/` — the explicit Scribe guide and shared methods.
- `skills/knowledge/` — reusable knowledge artifacts.
- `skills/product/` — product work artifacts.
- `skills/technical/` — project delivery and decision artifacts.
- `skills/visual/` — visual selection and production.

Every skill directory must contain `SKILL.md` and `agents/openai.yaml`. Add a resource only when the skill uses it.

## Invocation

Every skill is user-invoked. Set `disable-model-invocation: true` in every `SKILL.md` and `policy.allow_implicit_invocation: false` in every `agents/openai.yaml`.

The user must name every skill required by a composed workflow. `ask-scribe` explains Scribe's skills, boundaries, composition rules, and complete invocation choices; it never invokes another skill, performs its workflow, modifies files, or produces another skill's artifact.

Use `$skill-name` for ready-to-type Agent Skills invocations and `/skill-name` for Claude Code.

## Ownership

- `write-doc` owns the single shared prose contract for all human-readable documents. It standardizes natural reader flow, concrete language, sentence movement, emphasis, and formatting while leaving genre, structure, facts, and technical meaning with the artifact skill.
- `reason-architecture` owns the architecture method shared by architecture artifacts.
- `reason-domain` owns domain admission, boundaries, relationships, subdomain validity, high-level knowledge ownership, maturity, and the Domain Assessment handoff.
- `reason-product` owns product admission, boundaries, hierarchy, change and release authority, high-level knowledge ownership, and the Product Assessment handoff.
- `assess-product-lifecycle` owns product decision readiness, artifact coverage, evidence gaps, and the Product Lifecycle Assessment.
- `structure-docs` owns directory responsibilities, file placement, documentation navigation, and structure migrations.
- `structure-product-docs` owns the seven-directory product core, product-type extensions, materialization, navigation requirements, and product-structure migrations.
- `write-product-doc` owns common product maps, reference, evidence, decision, behavior, and release-note documents; standard lifecycle artifacts retain their independent public skills.
- Each deliverable skill owns one artifact boundary, workflow, completion test, and output template.
- `draw-diagrams` owns visual routing and quality, not architecture meaning.
- `ask-scribe` explains and recommends; the user retains control of every subsequent invocation and execution.

Every explicit invocation that creates, revises, reviews, or presents human-readable prose must include `$write-doc` directly. A workflow may route a document body to another artifact skill only when the invocation includes `$write-doc`. Keep general prose and style rules exclusively in `write-doc`; artifact skills may add genre-specific requirements but must not copy or replace the shared prose contract.

Keep each rule in one place. Invoke a foundation instead of copying it. Store output templates under `assets/`; disclose branch-specific guidance through one-level `references/`.

## Repository updates

When adding, renaming, or removing a skill:

1. Update its bucket README and the root README.
2. Update `.claude-plugin/plugin.json` and marketplace metadata.
3. Re-read and update `ask-scribe`.
4. For every new prose-producing skill, require `$write-doc` in the skill and its recommended invocation; the shared-writing contract test discovers omissions automatically.
5. Validate every changed skill.
6. Run the test suite, `bash -n scripts/*.sh`, and `git diff --check`.

Write agent instructions in imperative form. End every workflow with a checkable completion condition. Keep `SKILL.md` concise and move conditional detail behind direct pointers.
