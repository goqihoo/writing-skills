# Architecture document families

Scribe distinguishes reusable Architecture Knowledge systems, stable company design, and Project architecture delivery. They share actual Markdown scaffolds with distinct structures by architectural responsibility. Knowledge and concrete-design profiles adapt purpose, evidence and commitments; delivery supplements cover entry, migration and acceptance. [The generated template catalog](architecture-template-catalog.md) links the files.

| Result | Owner | Template authority |
| --- | --- | --- |
| Knowledge system or detailed reference document | Write Arch Knowledge (`write-architecture-knowledge`) | `methods/architecture-templates/templates.yaml` |
| Company landscape and Product-System mapping | Write Tech Arch (`write-technical-architecture`) | Writer Internal Document Type registry |
| Stable System, Subsystem or Component design | Write Tech Doc (`write-technical-doc`) | Writer Internal Document Type registry |
| Project architecture and directly required delivery details | Write Tech Arch (`write-technical-architecture`) | Delivery entries in its Writer registry |

## Knowledge system

Use Domain, Application, Governance and Runtime as the organizing and review framework. Separate a knowledge-set entry, view overview and collection index from substantive architecture. Use Overall Architecture to integrate the relevant views through shared outcomes and scenarios. Use Application Architecture for application decomposition, subsystems, components, engineering strategies and shared mechanisms. Do not add Data, Integration, Deployment or Security as separate categories or recommended splits while their organization is deferred. Retain their templates for explicitly requested specialist artifacts; a catalog resource is not an approved documentation topology. Reuse one template for multiple subjects rather than creating a new skill for every document.

Preserve established topology, explicit user structure and local language. A request to organize a system includes inventories, gap/overlap assessment, appropriate writing and navigation within authorized scope. It does not require separate skill invocations. Link a shared explanation from its dependents; do not duplicate it or create placeholder documents for every possible topic. Keep navigation separate from substantive design judgments. Apply the shared cross-document scenario check to verify that the models jointly preserve the claimed outcome, including failure and recovery. Derive technical security mechanisms from threats as well as describing policy authority.

## Delivery adaptation

| Reference Knowledge | Concrete delivery |
| --- | --- |
| Model, variants and applicability | Named object, actual constraints and selected/proposed design |
| Illustrative assumptions | Verified baseline or explicit design assumptions |
| Reusable tradeoffs and review triggers | Decision authority, accepted cost and unresolved choices |
| Validation expectations | Requirement-to-design-to-evidence traceability |
| Project extraction | Adopt/Adapt/Reject decisions and compatibility/migration constraints |

Apply `methods/architecture-templates/concrete-design.md` to the same overall, subsystem, component, deployment and topic assets used for Knowledge. Keep delivery entry, migration and validation assets with their owning Writer. Use the delivery main document to integrate the relevant architecture concerns. Split subsystem, component, deployment, migration or validation documents only for independently useful detail. Keep stable System authorities linked; promotion of Project decisions requires evidence and authorization. Project architecture support does not expand into general task planning or executing deployment.

## Reasoning and reader flow

Follow the shared chain in `methods/architecture-documents.md`: problem and scenarios, strategy, structure and mechanism, tradeoffs, then evidence. Adapt that chain to each document responsibility. Overall architecture allocates responsibilities and requirements; subsystem architecture explains how internal components realize external commitments; component architecture explains the contract, invariants and mechanism under allocated constraints. Deployment connects operating targets to topology, capacity and recovery. Migration protects invariants through transitions and irreversible boundaries. Validation connects claims to scenarios, evidence and actual acceptance decisions.

Apply `methods/prose-quality.md` to choose expression. Develop reasoning in prose and explain relationships or behavior with figures. Retain tables for useful comparisons, navigation, matrices and traceable records. A template's coverage does not require a table for each concern or a fixed number of tables. Keep a decision or evidence record in one owning document and link it from overviews and dependent designs.

For a complete document, review the aggregate reading path as well as individual blocks. A sequence of valid lookup tables can still duplicate boundary information and interrupt the design argument. Apply the whole-document expression review in the shared prose method, preserving source links and evidence limits when merging content. Use full-length output for this check; short samples establish only local expression.

## Design depth

Use the implementation-readiness checks in `methods/architecture-documents.md` to distinguish a useful design from a responsibility inventory. Overall designs connect logical structure to software realization and integration; subsystems realize parent guarantees through internal contracts and transactions; components explain their actual algorithm or protocol. Keep architecture-significant data relationships and contract semantics in the design while executable detail remains with implementation. A proposed, evidence-bounded design is valid output before approval; a collection of unallocated future decisions is not a completed design.

## Maintenance and validation

Keep the common template catalog and assets under `methods/architecture-templates/`. Keep Company/Project type identities and shared asset assignments in their existing Writer registries. Generate the catalogs, check all bundled assets are selected and reachable, rebuild the plugin, and verify both system-writing and delivery-writing behavior with isolated samples. Keep Public Skill IDs, exact Display Names, explicit invocation, and flat skill layout unchanged.

The CEX knowledge base is a structural reference, not a bundled dependency or source of universal trading requirements. Its README references template directories absent from the inspected local copy; the new files are reconstructed from document responsibilities and representative content, not claimed verbatim recoveries.
