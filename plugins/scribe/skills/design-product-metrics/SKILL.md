---
name: design-product-metrics
description: Create, revise, or review a product metric system covering intended outcomes, metric hierarchy, exact definitions, segments, guardrails, decision use, evidence gaps, governance, and review triggers without designing instrumentation or dashboards.
---

# Design Product Metrics

Define product measures that support real decisions and retain stable meaning across initiatives and releases.

## Workflow

1. Read `../../methods/product-reasoning.md` and apply it inside this workflow.
2. Read the Product Assessment when persisted, product strategy, users and outcomes, capability map, current product behavior, available data, existing metrics, experiments, and material constraints.
3. Establish an accepted product boundary from the available evidence. If the subject routes elsewhere or remains materially disputed, stop because a metric system would formalize the wrong product; name the evidence or decision required.
4. Identify the product decisions the metric system must support. Separate desired outcomes, observable product behavior, business results, operational health, and data availability.
5. Build an outcome model before naming a north-star or dashboard metric. Record causal assumptions rather than presenting correlation as proof.
6. Define the metric hierarchy, exact numerator and denominator, population, event or state semantics, time window, segmentation, exclusions, latency, and source owner.
7. Add guardrails and diagnostic measures that expose harmful optimization or misleading aggregate movement.
8. Record baseline availability, instrumentation and evidence gaps, validation method, decision thresholds, ownership, and review triggers.
9. Read `../../methods/prose-quality.md`, then use `assets/product-metrics-template.md` as the structure owner. Preserve its H2 headings, order, and responsibilities. Read `../../methods/visual-production.md` when the request includes a visual or the outcome model is materially clearer as one.
10. Keep instrumentation schema, pipeline, storage, and dashboard implementation in technical or analytics delivery documentation.
11. Verify that another reader can calculate each metric consistently and name the decision it changes.

## Boundaries

- Own product outcome and metric semantics, hierarchy, guardrails, governance, and decision use.
- Let product strategy own target direction, PRDs own initiative acceptance, and evidence records own observations and interpretations.
- Keep tracking implementation, schemas, data pipelines, and dashboard construction externally owned.

## Completion

The work is complete when outcomes precede measures, every metric has one unambiguous calculation and population, guardrails constrain gaming and harm, segments expose meaningful variation, data gaps are visible, ownership and decision thresholds are explicit, and review triggers show when definitions or targets must change.
