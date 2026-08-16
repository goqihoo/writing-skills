# Domain reasoning method

Use this method to decide whether a proposed domain, subdomain, relationship, or knowledge home is supportable. Produce a `Domain Assessment`; leave directories and document bodies to their owning skills.

## Contents

- Domain definition
- Admission decision
- Warning signals
- Relationships and subdomains
- Knowledge ownership
- Maturity

## Domain definition

A domain is a reusable knowledge boundary around a stable real-world problem. It has an independent minimum purpose, core objects or activities, shared language, unavoidable constraints, and external authorities that can change what is known.

A domain directory records primary knowledge ownership and navigation. It does not claim that the real world is isolated. Express related work and cross-domain handoffs through links unless a supported parent-or-child relationship justifies nesting.

Keep these concepts distinct:

- A **domain** is a stable problem space and knowledge boundary.
- A **subdomain** is a smaller problem space inside a parent with its own purpose, objects or activities, language, constraints, and handoffs.
- A **bounded context** is the applicability boundary of one model and language. It may align with a team or system, but it does not automatically define a knowledge directory.
- A software module, organization, product feature, vendor, technology, and project may use domain knowledge without becoming a domain.

## Admission decision

Assess all six criteria. The first five must be supported before accepting a first-level domain. Failed reusability routes the material to the content class whose changing context actually owns it.

| Criterion | Required evidence | Failure meaning |
| --- | --- | --- |
| **Minimum purpose** | A result, control, or professional judgment that cannot be performed reliably without this knowledge boundary | The candidate is a topic or collection without an independent reason to exist |
| **Core objects or activities** | Things with identity, state, lifecycle, or recurring professional action and judgment | The candidate is probably a label, tool, or document category |
| **Shared language and constraints** | Terms, rules, invariants, and tradeoffs with stable meaning inside the problem space | The candidate lacks a coherent model |
| **Change authority** | Laws, standards, market facts, research, incidents, or professional practice that can invalidate the knowledge | The source of truth cannot be identified |
| **Boundary and handoffs** | Explicit exclusions, destinations, and objects, events, facts, or decisions exchanged with adjacent domains | Ownership will remain ambiguous |
| **Reusability** | Core claims survive a change of company, product, implementation, customer, and project | The material belongs to business, product, technical, company, customer, or project knowledge |

Use one of three decisions:

- **Accept** — every required criterion is supported and reusability holds.
- **Do not accept** — evidence shows that the candidate belongs to another content class or lacks an independent problem space.
- **Needs evidence** — the decision depends on missing evidence; name exactly what would resolve it.

Content volume measures maturity, not admission. A valid domain may begin with one map or cognition anchor. A large product or technology collection may still fail admission.

## Warning signals

Recheck the candidate when:

- its name is a product, service, database, vendor, team, department, framework, or implementation;
- its claims hold only for one version, jurisdiction, customer, product, or project;
- its proposed children are document types such as principles, cases, or architecture rather than smaller problem spaces;
- it offers a feature list but no domain objects, constraints, or change authority;
- it shares objects and rules with an adjacent directory but cannot say who owns their definitions;
- it is a source collection without reusable explanation, method, or judgment.

Keep unresolved material in a classification gap. A new empty domain is not a substitute for evidence.

## Relationships and subdomains

Record only relationships supported by objects, facts, events, constraints, or decisions that actually cross between domains.

| Relationship | Meaning | Structural consequence |
| --- | --- | --- |
| **Parent or child** | One problem space fully contains a smaller problem space that has an independent purpose, objects or activities, constraints, and handoffs | May justify nesting when navigation also needs it |
| **Related** | Two domains exchange knowledge or constraints but neither contains the other | Preserve separate homes and link them |
| **Handoff** | One domain produces an object, fact, event, or decision consumed by another | Record definition authority, result responsibility, and handoff conditions; do not infer nesting |

A proposed subdomain must have:

- an independent minimum purpose inside the parent;
- dedicated objects, states, activities, or recurring professional judgments;
- language, rules, or invariants distinct from sibling subdomains;
- clear inputs, outputs, events, or decisions at each handoff;
- enough current knowledge to support an independent reading path.

Keep a cross-cutting control, implementation module, or knowledge form at the parent or in its true owning domain. File count, naming symmetry, and topic popularity do not establish a subdomain.

When several candidates qualify independently but the proposed parent owns no shared purpose, language, objects, constraints, or continuous state chain, treat them as peer domains and link their relationships.

## Knowledge ownership

Give each material one primary content class by asking what can change its truth and how long it must survive:

| Content class | Truth changes with |
| --- | --- |
| Domain knowledge | External evidence, standards, research, incidents, or professional practice |
| Business knowledge | Market strategy, operating model, commercial rules, or business decisions |
| Product knowledge | Product scope, behavior, users, metrics, and product decisions |
| Technical knowledge | System constraints, implementation, runtime behavior, and engineering decisions |
| Company knowledge | Internal policy, organization, roles, and company authority |
| Project knowledge | Customer scope, delivery plan, acceptance, and project decisions |
| Reference material | The version and authority of a stable fact, classification, field, or source |

Use links for secondary relevance. Split material only when the parts have independent reader questions, change authorities, lifetimes, or citation needs. Record a classification gap when no current home can own the material honestly.

## Maturity

Assign maturity only after the domain passes admission:

| Maturity | Meaning |
| --- | --- |
| **Emerging** | The boundary is valid, but only a README or cognition anchor exists |
| **Building** | Several knowledge responsibilities exist, but semantics, objects, evidence, or handoffs remain incomplete |
| **Stable** | Major objects, mechanisms, methods, boundaries, and authoritative entry points exist; new knowledge usually has a predictable home |
| **Review required** | Material conflict exists in naming, object ownership, change authority, or an adjacent boundary |

Low maturity does not invalidate a domain. Failed admission does. Record observable review triggers such as a new standard, changed authority, contradictory evidence, a recurring classification gap, or a handoff that moves ownership.
