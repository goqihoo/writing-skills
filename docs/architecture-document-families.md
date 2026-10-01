# Architecture document families

Scribe distinguishes reusable Architecture Knowledge systems, stable company design, and Project architecture delivery. Each has actual Markdown scaffolds with headings, fillable fields, tables and figure slots; references and Shared Methods own execution instructions. [The generated template catalog](architecture-template-catalog.md) links the files.

| Result | Owner | Template authority |
| --- | --- | --- |
| Knowledge system or detailed reference document | Write Arch Knowledge (`write-architecture-knowledge`) | `references/architecture-templates.yaml` |
| Company landscape and Product-System mapping | Write Tech Arch (`write-technical-architecture`) | Writer Internal Document Type registry |
| Stable System, Subsystem or Component design | Write Tech Doc (`write-technical-doc`) | Writer Internal Document Type registry |
| Project architecture and directly required delivery details | Write Tech Arch (`write-technical-architecture`) | Delivery entries in its Writer registry |

## Knowledge system

Support the reference profile of Domain, Application, Governance and Runtime when appropriate to the subject. Separate a knowledge-set entry, view overview and collection index from substantive architecture. Organize application knowledge into an overall model, subsystems, components, engineering strategies and shared mechanisms. Governance and Runtime topics have distinct templates because their questions and structures differ. Reuse one template for multiple subjects rather than creating a new skill for every document.

Preserve established topology, explicit user structure and local language. A request to organize a system includes inventories, gap/overlap assessment, appropriate writing and navigation within authorized scope. It does not require separate skill invocations. Link a shared explanation from its dependents; do not duplicate it or create placeholder documents for every possible topic.

## Delivery adaptation

| Reference Knowledge | Concrete delivery |
| --- | --- |
| Model, variants and applicability | Named object, actual constraints and selected/proposed design |
| Illustrative assumptions | Verified baseline or explicit design assumptions |
| Reusable tradeoffs and review triggers | Decision authority, accepted cost and unresolved choices |
| Validation expectations | Requirement-to-design-to-evidence traceability |
| Project extraction | Adopt/Adapt/Reject decisions and compatibility/migration constraints |

Use the delivery main document to integrate the relevant architecture concerns. Split subsystem, component, deployment, migration or validation documents only for independently useful detail. Keep stable System authorities linked; promotion of Project decisions requires evidence and authorization. Project architecture support does not expand into general task planning or executing deployment.

## Maintenance and validation

Keep Knowledge template selection in its manifest and Company/Project type configuration in their existing registries. Generate the catalogs, check all bundled assets are selected and reachable, rebuild the plugin, and verify both system-writing and delivery-writing behavior with isolated samples. Keep Public Skill IDs, exact Display Names, explicit invocation, and flat skill layout unchanged.

The CEX knowledge base is a structural reference, not a bundled dependency or source of universal trading requirements. Its README references template directories absent from the inspected local copy; the new files are reconstructed from document responsibilities and representative content, not claimed verbatim recoveries.
