---
name: write-product-review
description: Create, revise, or review an evidence-based product, release, period, or experiment review that compares expectations with observed outcomes, separates facts from causal interpretation, records implications, and commits next decisions and owners.
disable-model-invocation: true
---

# Write Product Review

Turn product evidence into an accountable decision without reducing the review to a status report or retrospective transcript.

## Workflow

1. Apply `$reason-product` and `$write-doc`.
2. Read the Product Assessment, decision or release being reviewed, expected outcomes and assumptions, metric definitions, evidence records, current product state, prior decisions, and known external changes.
3. Require an accepted product boundary. For a missing, routed, or disputed Product Assessment, return `$reason-product $write-doc` and stop.
4. Establish the review scope, time window, decision-maker, information available at the original decision, and decision now required.
5. Separate observed facts, metric movement, qualitative evidence, data limitations, causal interpretation, counterfactuals, and hindsight.
6. Compare expected and observed outcomes on the same definitions. Investigate meaningful segments, guardrails, contradictions, and unintended effects.
7. Derive implications for strategy, capability, solution, roadmap, initiative, metrics, release, or product boundary without rewriting those authoritative artifacts inside the review.
8. Record accepted decisions, stopped or continued bets, owners, follow-up evidence, and review triggers.
9. Use `assets/product-review-template.md` as the structure owner. Preserve its H2 headings, order, and responsibilities.
10. Update or link the authoritative downstream artifacts when their owners are explicitly invoked; otherwise return complete ready-to-type invocations.
11. Verify that every conclusion traces to evidence and every action traces to an accepted decision.

## Boundaries

- Own evidence-based product evaluation and resulting product decisions.
- Keep team-process retrospectives, technical incidents, and operational postmortems in their owning locations.
- Let evidence records preserve source observations and the affected product artifacts preserve updated current truth.

## Completion

The work is complete when expectations and decision-time assumptions are reconstructable, observations are distinguishable from interpretation, metrics retain their canonical definitions, alternative explanations and limitations are visible, implications route to the correct product owners, and each accepted next action has an owner and review trigger.
