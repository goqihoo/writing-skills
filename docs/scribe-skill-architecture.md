# Scribe Skill Architecture

## Authority scopes

Scribe separates three authorities:

- **Knowledge** is reusable across companies and projects. Domain, Product, Technical, and Architecture describe subjects, not ownership.
- **Company Documentation** records the facts, policies, structures, and decisions maintained by one named company. This release covers Product Documentation and Technical Documentation.
- **Project Documentation** records one customer, contract, engagement, plan, delivery state, and acceptance boundary. Its artifact system is outside the current Scribe scope.

Moving an idea between authority scopes requires an explicit adoption or extraction decision. A reusable method does not become company policy automatically, and a company incident does not become general Knowledge merely because it taught a lesson.

## Orthogonal skill roles

- reasoning skills admit boundaries and authority;
- assessment skills evaluate decision coverage;
- structure skills own directory responsibilities, navigation, materialization, and approved migration;
- artifact skills own one high-frequency artifact or one coherent document family;
- `write-doc` offers an optional dedicated reader-flow and prose-quality pass;
- `draw-diagram` owns visual selection and production when explicitly invoked.

Coordination is expressed by verbs. Scribe does not create Delivery or Coordination content buckets.

## Materialization contract

- **Stable Responsibility** exists continuously for an accepted company, product, or technical scope and receives a default home and Responsibility README.
- **Type Extension** is created only when independent ownership, governance, or navigation is proven.
- **Event Collection** is created with the first real event document.

A Responsibility README exposes responsibility, owner, boundary, current real navigation, and external authority links. It is not a placeholder document or a duplicate body.

## Public interfaces

A Public Skill exists only when a task recurs across companies or products, has distinct reasoning or workflow, and ends with a checkable completion condition. Lower-frequency standard documents remain an **Internal Document Type** within `write-product-doc` or `write-technical-doc`.

Every Public Skill has one canonical Skill ID and one exact, unique Skill Display Name. Both invoke the same skill. Catalogs and ready-to-type examples prefer the display name; paths, manifests, frontmatter, and code retain the Skill ID.

## Explicit Skill Composition

Every skill disables model invocation and implicit invocation. The user explicitly names every required coordination, structure, and artifact skill. Add `$Write Doc` for a dedicated prose-quality pass or `$Draw Diagram` for one visual. A skill that detects a missing required dependency stops and returns the complete ready-to-type invocation; it never invokes that skill itself. Selecting an Internal Document Type inside a Common Writer is internal routing, not skill invocation.

## Company root

One company root may navigate both `Product/` and `Technical/`, and either may be materialized independently. Company Documentation directories use initial capitals. This convention does not govern code repositories.

## Authority preservation

Company documents link detailed System Architecture and **Machine Authority** such as schemas, configuration, code, migrations, and tests. They preserve company purpose, ownership, lifecycle, critical relationships, governance, and human navigation without copying executable truth.

## Completion contract

The architecture is satisfied when every artifact has one authority scope and owner, every directory has one materialization class, public skills and Internal Document Types remain distinct, every composition is explicit, and public catalog surfaces expose the same names and boundaries.
