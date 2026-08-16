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
4. Explain the smallest suitable skill or useful sequence. Include every foundation and artifact skill the workflow requires. Name the closest alternative when its boundary is easy to confuse, and state why it differs.
5. Provide ready-to-type explicit invocations for Agent Skills clients or Claude Code when that helps the user proceed. Never omit a required foundation from the invocation.
6. Keep control with the user. Do not invoke another skill, perform its workflow, modify files, or produce an artifact owned by another skill.

## Skill guide

| Intended result | Skill | Boundary |
|---|---|---|
| Understand Scribe, compare skills, or plan how to combine them | `ask-scribe` | Explain skills and rules without executing them. |
| Plan or review documentation directories, file placement, content boundaries, or a structure migration | `structure-docs` | Own the documentation-set structure, not the reasoning inside each artifact. |
| Plan, scaffold, or audit one reusable domain knowledge directory | `structure-domain-docs` | Own the domain map, subdomains, knowledge-form homes, coverage, and reading path. |
| Create or revise any common document inside a domain directory, including README and essence | `write-domain-doc` | Classify from the prompt, then apply the matching internal module and template. |
| Create a reusable explanation of a concept, mechanism, method, pattern, mental model, case, or reference | `write-knowledge` | The reader primarily needs durable understanding. |
| Create reusable architecture knowledge or a reference architecture | `write-study-architecture` | Preserve reusable boundaries, ownership, contracts, controls, failure, validation, options, and evolution without choosing for one project. |
| Create product requirements | `write-prd` | Define product outcome and observable behavior, not solution structure. |
| Create project-specific technical, system, solution, or delivery architecture | `write-delivery-architecture` | Commit to boundaries, ownership, contracts, failure behavior, rollout, and validation. |
| Create an architecture diagram, flow, sequence, state, topology, or technical illustration | `draw-diagrams` | Own the visual form; the source skill owns the meaning. |
| Create another human-readable document | `write-doc` | Apply the shared prose contract without forcing a mismatched artifact template. |

Explicit intent is the strongest evidence. “Where should these documents live?”, “how should this whole knowledge base be divided?”, and “is this business, domain, product, or technical content?” indicate `structure-docs`. “Create this domain knowledge directory”, “which documents should this domain have?”, and “design the domain reading path” indicate `structure-domain-docs`. Every request to write a domain README, essence, terminology, objects, participants, mechanism, capability, method, case, or reference document indicates `write-domain-doc`; it infers the type from the prompt and loads the corresponding internal module and template. “Explain this concept” and “build a mental model” outside the common domain-document set indicate `write-knowledge`. “Who owns what?”, “how do controls execute?”, and “how does failure recover?” indicate an architecture skill when system or application architecture is the primary subject; use `write-study-architecture` for reusable knowledge and `write-delivery-architecture` for one project's commitments.

## Common combinations

- Documentation set: `structure-docs` to establish repository-wide homes and boundaries, then the matching artifact skills to create or revise the documents.
- Domain knowledge set: `structure-domain-docs` to establish the domain map and reading path, then `write-domain-doc` to classify and create every domain artifact from the matching internal module and template.
- Product change: `write-prd` followed by `write-delivery-architecture`, with accepted architecture choices retained in the delivery document.
- Reusable architecture to delivery: `write-study-architecture` followed by `write-delivery-architecture`, explicitly adopting, adapting, deferring, or rejecting reusable options.
- Visual inside another artifact: let the document skill define the meaning, then use `draw-diagrams` for visual form and quality.

`write-doc` supplies the shared prose contract for natural reader flow across Scribe artifacts. `reason-architecture` supplies shared architecture reasoning. Every skill is user-invoked, so include these foundations in the ready-to-type invocation whenever the selected artifact skill requires them.

The guidance is complete when the user understands the relevant choices, their boundaries, and the invocation or sequence they can choose next, without Ask Scribe having executed that choice.
