# Product reasoning method

Use this method to distinguish the company product portfolio, product lines, accepted products, and responsibilities within a product.

## Product decision

Return one decision:

- **Accept** — evidence supports the portfolio or independently governed product boundary.
- **Route as product line, product area, or capability** — the subject is a classification or responsibility inside an accepted product model.
- **Route to another authority scope** — the subject belongs to general Knowledge, Project Documentation, Technical Documentation, or another company responsibility.
- **Needs evidence** — a material decision depends on missing users, outcomes, authority, lifecycle, ownership, or navigation evidence.

Do not use a folder, brand, team, backlog, component, or customer request as proof that a product exists.

## Company product portfolio

Identify the named company that owns the Product Documentation Set. Establish who governs product admission, investment, lifecycle, shared constraints, and cross-product decisions. A product line is a classification view over accepted products in the Portfolio; it is not a default parent directory and one product may appear in more than one view.

## Product boundary tests

- **Minimum user outcome:** name the smallest continuing outcome the product promises.
- **Users and context:** identify users, buyers, operators, partners, and applicable contexts.
- **Offered value and capability:** distinguish stable capabilities from features or initiatives.
- **Product boundary:** state included responsibilities, exclusions, and handoffs.
- **Change authority:** name who may change scope and offered behavior.
- **Release boundary:** identify meaningful availability, measurement, versioning, and retirement decisions.
- **Sustained lifecycle:** show how the product is changed, measured, reviewed, and retired.

## Relationship tests

- **Portfolio and product:** the Portfolio governs investment and relationships; each product retains its outcome and lifecycle.
- **Product line and product:** the line is a Portfolio classification view, not a mandatory physical hierarchy.
- **Product and subproduct:** the child independently passes every product boundary test.
- **Product area:** a navigational or planning partition without independent product authority.
- **Capability:** a durable product ability, not a feature, system, or roadmap item.
- **Solution:** a reusable composition of capabilities for a class of situations.
- **Peer, dependency, or handoff:** another owner supplies an input, receives an output, or controls a decision.

## Materialization classification

- **Stable Responsibility:** persists for the accepted company or product scope and receives a default directory and Responsibility README.
- **Type Extension:** appears only when independent ownership, governance, or navigation is proven.
- **Event Collection:** appears with the first real initiative, evidence record, release, or decision, never as an empty default.

For Product Documentation, the company-level Stable Responsibilities are `Portfolio/`, `Governance/`, and `Products/`. Each accepted product receives `Definition/`, `Capabilities/`, `Planning/`, and `Measurement/`. `Solutions/` and `Experience/` are Type Extensions. `Initiatives/`, `Evidence/`, `Releases/`, and `Decisions/` are Event Collections.

## Authority ownership

| Material | Primary owner |
| --- | --- |
| Reusable product concepts, methods, and cases | Product Knowledge |
| One company's portfolio, governance, accepted products, and product truth | Product Documentation |
| Customer, contract, delivery plan, tasks, status, and acceptance | Project Documentation |
| Systems, technical standards, implementation, and operations | Technical Documentation or downstream Machine Authority |

Link across boundaries and keep one canonical explanation.

## Assessment persistence

Persist a Product Assessment only for a disputed boundary, Type Extension, audit finding, or approved migration that needs durable traceability. For a straightforward accepted scaffold, retain the reasoning in the execution and create only real navigation and Responsibility READMEs.

## Completion checks

- The company portfolio and each accepted product have named authority.
- Product lines remain classification views unless a separately justified structure is approved.
- Minimum user outcome, product boundary, change authority, and release boundary agree.
- Every proposed directory has exactly one materialization class.
- Every material has one primary authority scope and honest destination.
