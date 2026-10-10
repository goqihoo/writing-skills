# Validation — Module Design contract

Status: complete

## Scope and preservation

Updated the canonical Module Design template, added its branch writing contract, and connected it through the shared architecture-method routing and family guide. The existing Writers already read that method, so no new Public Skill, registry entry or invocation is required. Preserved Overall, Subsystem and Component source templates/contracts in this turn and retained unrelated working-tree changes. No business document, installed plugin cache, Git commit or remote was changed.

Mapped previous content obligations in [spec.md](spec.md). Reviewed the final scaffold for rule/interface semantics, internal ownership and state, transaction/concurrency, durable recovery, resource effects, compatibility and evidence. The final title is 规则与接口; the processing chapter now contains actual named flows and verification evidence has its own subsection.

## Full artifact exercise

Generated one full synthetic Chinese approval-request Module Design with five chapters and four rendered figures: implementation structure, important states, submission/retry flow and the shared conditional-update flow for approval/rejection/withdrawal. The fixture explicitly selects Mermaid; this exercises the format override and not default SVG styling.

Inspected the full text and rendered views for consistent roles, state names, guards, atomic audit/results, concurrency and uncertain outcomes. The example distinguishes historical request-result replay from current-state query, preserves unresolved reviewer-routing policy as a gap, keeps the module directly under a System, and adds no separate runtime platform or fabricated migration. Equivalent terminal-operation variants share a flow with explicit permission/state differences.

Reviewed stateless technical-function, narrow-edit, unresolved-policy and runtime/change adaptations separately as bounded reasoning checks. These were not additional full generations or independent agent testing. This self-review does not establish correctness of an implemented approval system, default diagram styling, or reliability across every future module.

Artifacts: `/var/folders/32/j8l0yn2s2x92jjs31z7v4xl80000gn/T/scribe-module-validation-rcitao3l`. Read `request.md`, `rendered.md`, `adaptation-review.md`, four `rendered-*.svg` figures and `inspection-1.png` / `inspection-2.png` there.

## Repository checks

- All 150 existing tests passed using the temporary development environment with `requirements-dev.txt` installed in the overall-template update.
- Canonical Claude marketplace and plugin validation passed.
- All 24 generated skills passed skill validation.
- Rebuilt the generated package and passed source/package parity.
- New contract/template links and packaging, shell syntax and whitespace checks passed.
- The available Codex CLI has no dedicated plugin validator. Generated-skill validation and package/tests are the available checks; dedicated validation remains unavailable.
