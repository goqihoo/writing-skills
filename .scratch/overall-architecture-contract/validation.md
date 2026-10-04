# Validation — overall architecture contract

Status: complete

## Scope and preservation

Updated the overall template, its shared writing contract and conditional routing in the existing three architecture Writers. Kept Skill IDs, type assignments and the other three canonical architecture templates unchanged in this turn. Existing unrelated working-tree edits were preserved. No company/business document, installed plugin cache, Git commit or remote was changed.

Mapped previous template obligations in [spec.md](spec.md). Reviewed the new scaffold and contract against every mapped obligation: data identity/ownership, transactions, contracts, security/authorization, recovery, evidence and transition obligations remain explicit at their new owners.

## Full artifact exercise

Generated one full Chinese synthetic equipment-slot reservation architecture through the new overall contract, with nine chapters and nine rendered diagrams. The synthetic request explicitly selects Mermaid; this tests the format-override branch, not default SVG styling. The main structure figure also expresses the actual organization, with the style subsection explicitly referring to it. The artifact exercises external context, ownership and state, creation/cancellation flows, shared technical concerns, deployment, release, evidence gaps and phased migration.

Self-review caught a release flow outside chapter 5 that needed its own diagram; the final fixture includes it. Inspected all nine rendered figures: context, shared overall/style, state, two business flows, deployment, release, transition architecture and cutover. Checked participant/state names, authority during migration, failure and retry semantics, actual image references, and readable labels. Preserved the distinction between diagram generation and the proposed system's validation: no system tests or architecture acceptance are claimed.

Reviewed simple stateless, logical-reference and narrow-edit adaptations separately. Those were reasoning checks, not additional full generations. No independent agent test was performed; this exercise does not establish reliability across all future architectures or validate default diagram styling.

Artifacts and inspection images: `/var/folders/32/j8l0yn2s2x92jjs31z7v4xl80000gn/T/scribe-overall-validation-uw7vzbzv`. Read `request.md`, `rendered.md`, `adaptation-review.md` and `inspection-1.png` through `inspection-3.png` there.

## Repository checks

- Created a fresh temporary Python environment and installed `requirements-dev.txt`.
- All 150 existing repository tests passed.
- Canonical Claude marketplace and plugin manifest validation passed.
- All 24 generated skills passed the skill validator; canonical skills were not passed to the Codex-only frontmatter validator.
- Rebuilt the generated Codex package and passed its source/package equality check.
- Changed documentation links, template/reference packaging, shell syntax and whitespace checks passed.
- The available Codex CLI has no dedicated plugin validation command. Generated-skill validation, package parity and repository tests were used; dedicated Codex plugin validation remains unavailable.
