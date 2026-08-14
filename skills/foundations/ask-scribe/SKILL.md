---
name: ask-scribe
description: Ask which Scribe skill or short document flow fits the situation. A user-invoked router over this plugin.
disable-model-invocation: true
---

# Ask Scribe

Route the task to the smallest skill that owns the intended artifact. Recommend and stop; do not produce the artifact.

## Route

1. Identify the intended artifact before using the draft as evidence. Start from the user's stated purpose, the core question, the future reader action, the lifetime (reusable knowledge or project commitment), and whether the user needs writing, review, a decision record, architecture design, or a visual.
2. Separate intended purpose from current contents. A draft under review may be off-topic, use the wrong structure, or contain material owned by another artifact. Never let its dominant current topic override a clear stated purpose.
3. Treat mismatched content as a review issue. Keep the route based on the intended artifact, note the possible responsibility drift in **Why**, and let the selected document skill decide what to remove, demote to supporting material, or move elsewhere.
4. Ask one short route-deciding question and stop only when stated intent, filename or location, and current contents conflict enough that the intended artifact remains unclear. Do not clarify when the user has already stated the purpose.
5. Inspect the installed `SKILL.md` for plausible routes before making a claim about them.
6. Recommend one skill or the shortest useful flow. Name the closest alternative only when the boundary is easy to confuse.
7. Return **Use**, **Why**, and **Next**. Make **Next** one ready-to-type `$skill-name` invocation for Agent Skills clients or `/skill-name` for Claude Code, then stop.

## Skill map

| Intended result | Skill | Boundary |
|---|---|---|
| Reusable explanation of a concept, essence, mechanism, method, general pattern, mental model, case, or reference | `write-knowledge` | The reader primarily needs understanding. Systems, actors, controls, or failures may support the explanation without making architecture the artifact. |
| Reusable architecture knowledge or reference architecture | `study-architecture` | The reader primarily needs to derive or compare boundaries, ownership, contracts, authority, controls, runtime failure and recovery, validation, or evolution without choosing for one project. |
| Product requirements | `write-prd` | Define product outcome and behavior, not solution structure. |
| Project-specific technical, system, solution, or delivery architecture | `design-architecture` | Commit to boundaries, ownership, contracts, failure behavior, and validation. |
| One material product or technical decision | `record-decision` | The decision, not the full solution, is the artifact. |
| Architecture diagram, flow, sequence, state, topology, or technical illustration | `draw-diagrams` | Own the visual form; the source skill owns the meaning. |
| Another human-readable document | `write-docs` | Apply the shared method without forcing a mismatched template. |

Treat explicit intent as the strongest routing evidence. Phrases such as “what is its essence,” “how should I understand it,” “concept explanation,” and “mental model” favor `write-knowledge`. Phrases such as “reference architecture,” “system boundaries,” “who owns what,” “how controls execute,” “how failure recovers,” and “how architecture evolves” favor `study-architecture`. Use `design-architecture` when those concerns are selected commitments for one project.

## Common flows

- Product change: `write-prd` → `design-architecture`; add `record-decision` only for a decision with its own lifecycle.
- Reusable architecture to delivery: `study-architecture` → `design-architecture`, explicitly adopting, adapting, deferring, or rejecting reusable options.
- Visual inside another artifact: let the document skill define meaning, then use `draw-diagrams` for visual form and quality.

## Foundations underneath

`write-docs` supplies shared writing discipline. `reason-architecture` supplies shared architecture reasoning. Other skills invoke them; do not recommend an internal foundation when a deliverable skill owns the artifact.

The route is complete when the user can invoke the next skill without reading this map.
