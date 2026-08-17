# Product Internal Document Types

Select exactly one Internal Document Type. The table is the source of truth for templates and completion profiles owned by `$write-product-doc`.

| Internal Document Type | Template | Completion profile |
| --- | --- | --- |
| Product navigation | product-readme-template.md | Responsibility, ownership, boundaries, real current links, and external authorities are visible. |
| Product Portfolio | product-portfolio-template.md | Accepted products, classification views, investment relationships, lifecycle, and authority are current. |
| Products Registry | products-registry-template.md | Every listed product is accepted, directly navigable, owned, and lifecycle-qualified. |
| Product Operating Model | product-operating-model-template.md | Decision forums, operating cadence, inputs, outputs, and escalation are explicit. |
| Product Governance | product-governance-template.md | Decision rights, policies, exceptions, evidence, and review triggers are enforceable. |
| Product Overview/Definition | product-definition-template.md | Boundary, users, value, current behavior, exclusions, and relationships agree. |
| Users and Roles | users-and-roles-template.md | Participants, outcomes, authority, evidence, and conflicts are distinguished. |
| Product Terminology | concepts-and-language-template.md | Product terms link reusable definitions and expose aliases and conflicts. |
| Lifecycle Map | product-lifecycle-map-template.md | Decision gates link current authoritative artifacts and keep state dimensions separate. |
| Capability Detail | capability-detail-template.md | Responsibility, observable behavior, rules, relationships, evidence, and evolution are clear. |
| Journey/Product Behavior | journey-and-behavior-template.md | Current main, edge, recovery, and handoff behavior is observable and sourced. |
| Product Solution | solution-definition-template.md | A reusable scenario composition is distinct from customer-specific delivery. |
| Initiative Record | initiative-record-template.md | Intended change, authority, evidence, scope, decisions, and lifecycle are traceable. |
| Evidence Record | evidence-record-template.md | Observations, method, limits, interpretation, and decision implications remain distinct. |
| Product Decision | product-decision-template.md | Accepted choice, alternatives, rationale, costs, authority, and review triggers are recorded. |
| Product Release Plan | release-plan-template.md | Availability, evidence gates, product criteria, dependencies, and stop conditions support a decision. |
| Release Notes | release-notes-template.md | Released current state is distinct from the plan and links updated authorities. |
| Product Review | product-review-template.md | Expectations, evidence, outcomes, interpretations, decisions, and follow-up are traceable. |

## Public artifact routes

Return the complete invocation and stop before drafting:

- Product Strategy → `$write-product-strategy $reason-product $write-doc`
- Capability Map → `$map-product-capabilities $reason-product $write-doc`
- Product Roadmap → `$write-product-roadmap $reason-product $write-doc`
- PRD → `$write-prd $write-doc`
- Product Metric System → `$design-product-metrics $reason-product $write-doc`

Return `$structure-product-docs $reason-product $structure-docs $write-doc` for proposal, scaffold, audit, or approved migration work. Add `$write-product-doc` when the same request also creates navigation or Responsibility README bodies. Selecting an Internal Document Type is routing within this skill and never invokes another skill.
