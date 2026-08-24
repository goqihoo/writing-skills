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
- `write-doc` exposes prose improvement as an independently requested result;
- `write-deck` owns one audience-facing presentation manuscript in Markdown across professional subjects and settings;
- `draw-diagram` owns one independently requested visual.

Cross-skill reasoning, documentation structure, prose quality, and visual production live in non-invocable Shared Methods under `methods/`. Public Skills apply them internally and still own their end-to-end outcomes.

Coordination is expressed by verbs. Scribe does not create Delivery or Coordination content buckets.

## Catalog classifications

- **Foundations** covers standalone catalog guidance, shared reasoning, general documentation structure, general prose work, and general presentation-manuscript work.
- **Knowledge** covers reusable understanding that is not owned by one company or project.
- **Product Documentation** covers one company's product responsibilities, decisions, structure, and governed artifacts.
- **Technical Documentation** covers one company's Technical Landscape, responsibilities, architecture, and governed artifacts.
- **Visual** covers independently requested technical visual production.

These classifications organize the catalog and explain authority boundaries. They do not create intermediate filesystem directories: every Public Skill remains directly under `skills/<skill-id>/`.

## Materialization contract

- **Stable Responsibility** exists continuously for an accepted company, product, or technical scope and receives a default home and Responsibility README.
- **Type Extension** is created only when independent ownership, governance, or navigation is proven.
- **Event Collection** is created with the first real event document.

A Responsibility README exposes responsibility, owner, boundary, current real navigation, and external authority links. It is not a placeholder document or a duplicate body.

## Public interfaces

A Public Skill exists only when a task recurs across companies or products, has distinct reasoning or workflow, and ends with a checkable completion condition. Repeated or audit-sensitive writer artifacts may be registered as an **Internal Document Type**; compatible occasional work remains a **Freeform Artifact** until evidence justifies registration. Product and Technical Writers keep one YAML configuration authority per Writer, while `docs/internal-document-types.md` is generated for readers.

Every Public Skill has one canonical Skill ID and one exact, unique Skill Display Name. Both invoke the same skill. Catalogs and ready-to-type examples prefer the display name; paths, manifests, frontmatter, and code retain the Skill ID.

`write-deck` treats a presentation manuscript as a derived expression: it may combine business, product, technical, learning, planning, and other supported material into one audience path, but the sources continue to own their facts, commitments, decisions, evidence, and technical truth. Its current artifact boundary is Markdown and supporting assets rather than PowerPoint, Keynote, PDF, or another rendered presentation file.

## Independent Public Skills

Every Public Skill disables model invocation and implicit invocation, owns one independently valuable result, and completes its core workflow itself. One requested result maps to one recommended skill. Multiple invocations represent multiple independently requested results, not implementation dependencies. Selecting an Internal Document Type inside a Common Writer and applying a Shared Method are internal routing, not skill invocation.

Missing evidence, approval, or ownership may stop a workflow when the result would otherwise be unsafe or false. A missing skill invocation never stops it. A skill may create a supporting assessment internally when traceability is needed.

## Company root

One company root may navigate both Product and Technical Documentation, and either may be materialized independently. Product conventions may use initial-capital English names. Technical structure treats Strategy, Architecture, Systems, and Governance as logical responsibilities and reuses the documentation set's language. Neither convention governs code repositories.

## Authority preservation

System Architecture and justified Subsystem Architecture are Technical Documentation. They link **Machine Authority** such as schemas, configuration, code, migrations, and tests, plus Project Technical Design, instead of copying executable truth. Company-level architecture links the governing System Architecture rather than replacing it.

## Completion contract

The architecture is satisfied when every artifact has one authority scope and owner, presentation manuscripts preserve their source authorities as derived expressions, every directory has one materialization class, Public Skills and Internal Document Types remain distinct, Shared Methods stay non-invocable, each Public Skill completes independently, and public catalog surfaces expose the same names and boundaries.
