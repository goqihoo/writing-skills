# Product document types

This is the single source of truth for common product documents handled by `$write-product-doc`. Select from the user's explicit request first, then confirm with the primary reader question, path, filename, current content, and sibling conventions.

## Structure strength

### Stable map schema

Preserve navigation, current-versus-planned coverage, and maintenance responsibilities:

- **Product map and README:** `../assets/product-readme-template.md`
- **Lifecycle map:** `../assets/product-lifecycle-map-template.md`
- **Collection README:** `../assets/collection-readme-template.md`

### Stable lookup schema

Preserve required fields and artifact responsibilities while adapting subject-specific subsections:

- **Users and roles:** `../assets/users-and-roles-template.md`
- **Concepts and language:** `../assets/concepts-and-language-template.md`
- **Capability detail:** `../assets/capability-detail-template.md`
- **Release notes:** `../assets/release-notes-template.md`

### Stable reasoning sequence

Preserve the evidence or decision order while allowing subject-specific headings:

- **Journey and behavior:** `../assets/journey-and-behavior-template.md`
- **Evidence record:** `../assets/evidence-record-template.md`
- **Product decision record:** `../assets/product-decision-template.md`

## Routing table

| Artifact | Primary reader question | Required distinction |
| --- | --- | --- |
| Product map and README | What is this product, what is current, and where should I go? | Current linked content versus planned unlinked coverage |
| Lifecycle map | What product decision is next, which authoritative artifacts support it, and what blocks it? | Structure, acceptance, currency, and gate states remain independent |
| Collection README | What does this directory own, exclude, and contain? | Boundary contract versus document-body summaries |
| Users and roles | Who uses, buys, operates, decides, or participates in this product, and for what outcome? | Product participant versus company job title |
| Concepts and language | What do product-specific concepts and labels mean? | Product term versus reusable domain definition |
| Capability detail | What durable ability does the product provide and where does its responsibility stop? | Capability versus feature, module, or roadmap item |
| Journey and behavior | From a trigger, what can users observe across the main and edge paths? | Current behavior versus proposed PRD behavior |
| Evidence record | What was observed, how, and with what limitation? | Observation versus interpretation and decision |
| Product decision record | What was decided, why, at what cost, and when should it be reviewed? | Accepted choice versus proposal or meeting note |
| Release notes | What became available, changed, stayed limited, or was retired? | Released current state versus release plan |

## Standard artifact routes

Return a ready-to-type explicit invocation and stop before drafting:

- product strategy → `$write-product-strategy $reason-product $write-doc`;
- product capability map → `$map-product-capabilities $reason-product $write-doc`;
- reusable solution definition → `$write-solution-definition $reason-product $write-doc`;
- product roadmap → `$write-product-roadmap $reason-product $write-doc`;
- product requirements document → `$write-prd $write-doc`;
- product metric system → `$design-product-metrics $reason-product $write-doc`;
- product release plan → `$write-release-plan $reason-product $write-doc`;
- product, release, period, or experiment review → `$write-product-review $reason-product $write-doc`.

Return `$structure-product-docs $reason-product $assess-product-lifecycle $structure-docs $write-doc` for whole-set directory design, coverage, scaffolding, or migration. Add `$write-product-doc` when the same authorized request must write product map, lifecycle map, or collection README bodies.

Keep company portfolio choices, reusable method knowledge, customer-specific delivery, and technical material in their owning content classes.
