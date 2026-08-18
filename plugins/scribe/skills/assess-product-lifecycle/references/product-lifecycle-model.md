# Product lifecycle model

Use lifecycle as a decision view over authoritative product files. A stage groups work that reduces uncertainty; it does not own every artifact used during that work.

## Decision views

| Decision view | Main question | Common evidence and artifacts | Owning Public Skill or skills |
| --- | --- | --- | --- |
| Discovery | Is the problem real and worth further investment? | Hypotheses, interviews, experiments, decision record | Write Product Doc |
| Product boundary and strategy | For whom will this product create what value, and what will it not do? | Product Assessment, product strategy | Reason Product for the assessment; Write Product Strategy for the strategy |
| Capability definition | What durable abilities and responsibilities must the product provide? | Capability map and capability details | Map Product Capabilities for the map; Write Product Doc for a detail |
| Solution definition | How will shared capabilities address a repeatable customer or partner situation? | Product Solution | Write Product Doc |
| Product planning | Which outcomes and capability gaps should be addressed next? | Product roadmap | Write Product Roadmap |
| Initiative definition | What changes now, with what behavior and acceptance? | PRD | Write PRD |
| Release decision | Can the product change be released, supported, observed, and stopped under explicit criteria? | Product Release Plan and linked evidence | Write Product Doc |
| Operate and learn | What happened, and which assumptions changed? | Metrics, evidence, release notes, Product Review | Design Product Metrics for metrics; Write Product Doc for the records |
| Iterate, merge, or retire | What should continue, change, combine, pause, or stop? | Product Review, Product Decision, revised strategy or roadmap | Write Product Doc |

Activities can run in parallel, revisit earlier decisions, or require different depth by risk. Select the current decision from its consequence and uncertainty, not from a claimed phase number.

## Evidence sufficiency

For each required conclusion, record:

- the claim being decided;
- the evidence or authoritative upstream decision;
- scope, version, market, customer class, and observation date;
- contradictory or missing evidence;
- the person authorized to accept the residual uncertainty.

An artifact is sufficient when it supports the current decision, exposes material uncertainty, and gives downstream readers the boundary they need. Completeness against a large template is not sufficient by itself.

## Structure states

Use these only for path and materialization decisions:

- **Existing** — a current path already owns the responsibility.
- **Create now** — the current decision and evidence justify materialization.
- **Planned** — the responsibility is real but content or evidence is not ready.
- **Unresolved** — ownership or boundary must be decided first.

## Artifact validity states

Represent artifact validity with two controlled fields so acceptance and currency cannot overwrite one another.

Acceptance state:

- **Draft** — content is being formed and is not an accepted commitment.
- **Accepted** — the authorized decision-maker accepted the artifact.

Currency state:

- **Current** — the artifact still applies to the named product scope and version.
- **Needs review** — a review trigger fired or material evidence changed.
- **Superseded** — a named artifact replaced it.

Accepted and Current answer different questions and can coexist.

## Decision-gate states

Use these for readiness and investment decisions:

- **Not applicable** — the gate does not apply to this change or risk.
- **Collecting evidence** — a material decision still lacks evidence.
- **Ready for decision** — required evidence and residual uncertainty are visible.
- **Go** — continue and commit the named resources or scope.
- **Hold** — delay without rejecting the opportunity.
- **Recycle** — gather or revise specific information before deciding again.
- **Stop** — stop the product, initiative, or investment in scope.

## Right-sizing

Require the smallest artifact that preserves the decision, authority, evidence, and downstream handoff. Increase depth when:

- a decision changes product boundary, commitments, economics, or external authority;
- several teams or partners need the same stable interpretation;
- failure is costly, irreversible, regulated, or hard to observe;
- competing options depend on different assumptions;
- the artifact will be reused across several initiatives or releases.

Do not require every artifact before every decision. Record `Not applicable` or `Planned` honestly.

## Lifecycle-map contract

For each decision gate, expose:

- decision and owner;
- required artifacts and authoritative links;
- acceptance state and currency state, which together express artifact validity;
- evidence gaps and contradictory signals;
- gate state;
- next action, owner, and review date or trigger;
- one complete single-skill invocation for each missing Scribe artifact.

Technical material remains linked from its owning location. The lifecycle map may record product-facing readiness and a link, but it does not copy technical content or define the technical directory.
