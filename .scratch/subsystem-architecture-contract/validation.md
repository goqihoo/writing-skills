# Validation — Subsystem architecture contract

Status: complete

## Scope and preservation

Updated the canonical Subsystem template and added its writing contract behind the shared architecture-method routing. Updated the family guide. The existing Writers reach the new branch through their already-required Shared Method, so no new Public Skill or type registration was created. The Overall template/contract, Module and Component templates were not edited in this turn. Preserved prior unrelated working-tree changes. No company document, installed plugin cache, commit or remote was changed.

Mapped old obligations in [spec.md](spec.md). Verified retention of allocation, external/internal contracts, style and strategy, state/transactions, concurrency, durable recovery, security, evidence, compatibility and migration. State definitions now precede full execution flows; constraints remain separate from local design choices.

## Full artifact exercise

Generated one full Chinese synthetic search-index Subsystem design with seven chapters and eight rendered figures. The fixture explicitly asks for Mermaid, exercising that format override rather than default SVG styling. It covers context, internal structure/organization, important state, rebuild/publish and query flows, shared-process runtime, transitional architecture and format cutover.

Inspected the prose and all rendered views. Self-review corrected a query diagram that had not explicitly branched when no active generation was available, and shortened a crowded rebuild message. The final views retain the failure branch, ownership and state distinctions. Checked that in-process placement was not turned into independent services, query lifetime constrained old-generation deletion, migration handled in-flight work, and unallocated budgets or unverified checks remained explicit.

Artifacts: `/var/folders/32/j8l0yn2s2x92jjs31z7v4xl80000gn/T/scribe-subsystem-validation-wichz11q`. Read `request.md`, `rendered.md`, `adaptation-review.md`, the eight `rendered-*.svg` files and three `inspection-*.png` sheets there.

Reviewed stateless/no-migration, parent-budget/evidence, pure logical reference and narrow-edit adaptations as bounded reasoning checks. They were not additional full document generations. This was implementing-agent self-review, not independent agent testing, and it does not prove production architecture correctness or future generation reliability. Default diagram styling was not validated by this Mermaid exercise.

## Repository checks

- All 150 existing tests passed in the temporary development environment with `requirements-dev.txt` installed during the preceding overall-template update.
- Canonical Claude marketplace and plugin validation passed.
- All 24 generated skills passed the skill validator.
- Rebuilt the generated package and passed source/package parity.
- Changed documentation links, new reference/template packaging, shell syntax and whitespace checks passed.
- The available Codex CLI exposes no dedicated plugin validator; generated-skill validation and package/tests are the available checks, not a substitute claim of dedicated validation.
