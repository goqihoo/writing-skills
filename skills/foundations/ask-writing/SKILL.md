---
name: ask-writing
description: Explain the writing skills in this repository and recommend the smallest skill or short flow that fits the user's document. Use when the user asks which writing skill to use, how two document skills differ, what a skill produces, or where to start with a knowledge, product, or technical document.
---

# Ask Writing

Route the user to the smallest writing skill that owns the document they need. Recommend and stop; do not draft or edit the document.

## Routing workflow

1. Identify the artifact the reader will use, the decision or action it must support, and whether the user is creating, revising, or reviewing it.
2. Shortlist candidates from the map below.
3. Inspect each shortlisted skill's installed `SKILL.md` before making a load-bearing claim about its behavior. Treat that file as authoritative.
4. Recommend one skill. Name the nearest alternative and state the concrete reason it does not fit.
5. Give the user one invocation they can type next. Use `$skill-name` in Agent Skills-compatible clients and `/skill-name` in Claude Code, then stop.

## Skill map

| User's intended artifact | Recommend | Boundary |
|---|---|---|
| A reusable explanation, methodology, decision pattern, mental model, case, or reference note | `write-knowledge-document` | The result must remain useful beyond one project or delivery cycle. |
| A product requirements document that aligns problem, scope, behavior, and acceptance | `write-product-requirements` | The document defines what outcome and behavior the product needs, not the implementation design. |
| A technical design that makes implementation and review possible | `write-technical-design` | The document explains how the system will meet agreed requirements across runtime, data, interfaces, failure, rollout, and validation. |
| A record of one material decision and why it was made | `write-decision-record` | The decision is the subject. A full solution design belongs in `write-technical-design`. |
| A human-readable document with no dedicated artifact skill | `writing-foundations` | Use the shared discipline without forcing the artifact into a structure that does not fit. |

## Close calls

- Choose `write-product-requirements` when product behavior and acceptance remain the main question. Choose `write-technical-design` when the product requirement is stable and implementation is now the main question.
- Choose `write-technical-design` when several related decisions must form one coherent solution. Choose `write-decision-record` when one decision needs a durable record and review trigger.
- Choose `write-knowledge-document` for reusable understanding. Choose a delivery skill for a document tied to a specific initiative, status, approval, or handoff.
- If no skill owns the artifact, say so. Recommend `writing-foundations` and name the missing deliverable skill that would be worth adding after repeated use.

## Response format

Return four short fields:

- **Use:** the recommended skill.
- **Why:** the artifact outcome that matches it.
- **Not:** the closest alternative and why it does not fit.
- **Next:** one ready-to-type invocation.

The route is complete when the user can invoke one skill without reading the repository map.
