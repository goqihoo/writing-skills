---
name: ask-scribe
description: Explain Scribe's skills, boundaries, composition rules, and invocation choices. A user-invoked guide to understanding and planning how to use this plugin.
disable-model-invocation: true
---

# Ask Scribe

Help the user understand Scribe and plan how to use it. Explain and recommend; leave every skill invocation and execution to the user.

## Guidance

1. Answer the user's actual question about the plugin, its skills, their boundaries, or how they can be combined.
2. Inspect the installed `SKILL.md` files for plausible skills before describing their current behavior.
3. Start from the user's intended result, future reader action, artifact lifetime, and requested output. Treat a draft's filename, location, and contents as evidence that may reveal a mismatch, not as stronger authority than explicit intent.
4. Explain the smallest suitable skill or useful sequence. Name the closest alternative when its boundary is easy to confuse, and state why it differs.
5. Provide ready-to-type `$skill-name` invocations for Agent Skills clients or `/skill-name` invocations for Claude Code when that helps the user proceed.
6. Keep control with the user. Do not invoke another skill, perform its workflow, modify files, or produce an artifact owned by another skill.

## Skill guide

| Intended result | Skill | Boundary |
|---|---|---|
| Understand Scribe, compare skills, or plan how to combine them | `ask-scribe` | Explain skills and rules without executing them. |
| Plan or review documentation directories, file placement, content boundaries, or a structure migration | `structure-docs` | Own the documentation-set structure, not the reasoning inside each artifact. |
| Create a reusable explanation of a concept, mechanism, method, pattern, mental model, case, or reference | `write-knowledge` | The reader primarily needs durable understanding. |
| Create reusable architecture knowledge or a reference architecture | `study-architecture` | Preserve reusable boundaries, ownership, contracts, controls, failure, validation, options, and evolution without choosing for one project. |
| Create product requirements | `write-prd` | Define product outcome and observable behavior, not solution structure. |
| Create project-specific technical, system, solution, or delivery architecture | `design-architecture` | Commit to boundaries, ownership, contracts, failure behavior, rollout, and validation. |
| Record one material product or technical decision | `record-decision` | Give one decision its own rationale, consequences, validation, and review lifecycle. |
| Create an architecture diagram, flow, sequence, state, topology, or technical illustration | `draw-diagrams` | Own the visual form; the source skill owns the meaning. |
| Create another human-readable document | `write-docs` | Apply the shared writing method without forcing a mismatched artifact template. |

Explicit intent is the strongest evidence. “Where should these documents live?”, “how should this knowledge base be divided?”, and “is this business, domain, product, or technical content?” indicate `structure-docs`. “What is its essence?”, “how should I understand it?”, and “build a mental model” indicate `write-knowledge`. “Who owns what?”, “how do controls execute?”, and “how does failure recover?” indicate an architecture skill; use `study-architecture` for reusable knowledge and `design-architecture` for one project's commitments.

## Common combinations

- Documentation set: `structure-docs` to establish homes and boundaries, then the matching artifact skills to create or revise the documents.
- Product change: `write-prd` followed by `design-architecture`; add `record-decision` only when one accepted choice needs its own lifecycle.
- Reusable architecture to delivery: `study-architecture` followed by `design-architecture`, explicitly adopting, adapting, deferring, or rejecting reusable options.
- Visual inside another artifact: let the document skill define the meaning, then use `draw-diagrams` for visual form and quality.

`write-docs` supplies shared writing discipline. `reason-architecture` supplies shared architecture reasoning. Explain these foundations when the user asks how Scribe works; recommend the artifact-owning skill when the user wants a deliverable.

The guidance is complete when the user understands the relevant choices, their boundaries, and the invocation or sequence they can choose next, without Ask Scribe having executed that choice.
