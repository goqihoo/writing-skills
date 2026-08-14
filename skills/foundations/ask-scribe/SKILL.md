---
name: ask-scribe
description: Ask which Scribe skill or short document flow fits the situation. A user-invoked router over this plugin.
disable-model-invocation: true
---

# Ask Scribe

Route the task to the smallest skill that owns the intended artifact. Recommend and stop; do not produce the artifact.

## Route

1. Identify the artifact, its reader action, its lifetime (reusable knowledge or project commitment), and whether the user needs writing, review, or a visual.
2. Inspect the installed `SKILL.md` for plausible routes before making a claim about them.
3. Recommend one skill or the shortest useful flow. Name the closest alternative only when the boundary is easy to confuse.
4. Return **Use**, **Why**, and **Next**. Make **Next** one ready-to-type `$skill-name` invocation for Agent Skills clients or `/skill-name` for Claude Code, then stop.

## Skill map

| Intended result | Skill | Boundary |
|---|---|---|
| Reusable explanation, method, pattern, model, case, or reference | `write-knowledge` | General knowledge, not architecture ownership and controls. |
| Reusable architecture knowledge or reference architecture | `study-architecture` | Retain context-dependent options; do not choose for one project. |
| Product requirements | `write-prd` | Define product outcome and behavior, not solution structure. |
| Project-specific technical, system, solution, or delivery architecture | `design-architecture` | Commit to boundaries, ownership, contracts, failure behavior, and validation. |
| One material product or technical decision | `record-decision` | The decision, not the full solution, is the artifact. |
| Architecture diagram, flow, sequence, state, topology, or technical illustration | `draw-diagrams` | Own the visual form; the source skill owns the meaning. |
| Another human-readable document | `write-docs` | Apply the shared method without forcing a mismatched template. |

## Common flows

- Product change: `write-prd` → `design-architecture`; add `record-decision` only for a decision with its own lifecycle.
- Reusable architecture to delivery: `study-architecture` → `design-architecture`, explicitly adopting, adapting, deferring, or rejecting reusable options.
- Visual inside another artifact: let the document skill define meaning, then use `draw-diagrams` for visual form and quality.

## Foundations underneath

`write-docs` supplies shared writing discipline. `reason-architecture` supplies shared architecture reasoning. Other skills invoke them; do not recommend an internal foundation when a deliverable skill owns the artifact.

The route is complete when the user can invoke the next skill without reading this map.
