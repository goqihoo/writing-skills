# Architecture document families

Let purpose determine content development, document responsibility determine the template, and four viewpoints guide design reasoning and completeness. Distinguish Architecture Knowledge from Concrete Design, retaining stable company design and Project delivery as separate authorities within Concrete Design. [The generated template catalog](architecture-template-catalog.md) links the files.

| Result | Owner | Template authority |
| --- | --- | --- |
| Knowledge system or detailed reference document | Write Arch Knowledge (`write-architecture-knowledge`) | `methods/architecture-templates/templates.yaml` |
| Company landscape and Product-System mapping | Write Tech Arch (`write-technical-architecture`) | Writer Internal Document Type registry |
| Stable System, Subsystem, Module or Component design | Write Tech Doc (`write-technical-doc`) | Writer Internal Document Type registry |
| Project architecture and directly required delivery details | Write Tech Arch (`write-technical-architecture`) | Delivery entries in its Writer registry |

Default Writer ownership determines recommendations. When a user explicitly invokes Write Tech Arch for stable System, Subsystem, Module or Component design, apply the explicit stable-design adaptation in `methods/architecture-documents.md`. Use the stable Writer registry and completion profile without invoking another skill, changing the document authority or inventing Project commitments.

Plan each applicable section's reader question, contribution and evidence before drafting. Keep writing-process checks in working notes, retain substantive controls and local uncertainty in the artifact, then edit the complete argument and recheck technical constraints through `methods/prose-quality.md`. Use its Chinese examples when reviewing Chinese technical explanations.

Preserve the design argument as well as technical constraints. Use Architecture judgment in [`methods/architecture-reasoning.md`](../methods/architecture-reasoning.md) to connect characteristics, principles, styles and strategies to mechanisms, tradeoffs and validation. The primary templates expose these explanations at the appropriate scope; child designs inherit the enclosing style and explain local consequences. Check old-to-new content coverage when merging template sections, and inspect complete generated artifacts rather than relying on structural tests.

## Primary architecture documents

Maintain one shared template for each primary document responsibility:

| Document | Responsibility |
| --- | --- |
| Overall Architecture | Explain the whole object's composition and how the parts jointly meet its requirements. |
| Subsystem Architecture | Explain how a justified responsibility group realizes guarantees allocated by its parent. |
| Module Design | Explain one cohesive function through operations, rules, state changes and processing coordination. |
| Component Architecture | Explain how encapsulated mechanisms realize a component's usage contract and required guarantees. |

Follow the reader progression of each current asset. Overall Architecture establishes the whole before decomposition and collaboration. Subsystem Architecture starts with allocated responsibility and external commitments, then explains their internal realization. Module Design starts with use and rules, then develops implementation and processing. Component Architecture starts with responsibility and contract, then selects and explains the mechanisms that realize its actual guarantees. Use short headings; chapter counts follow these responsibilities rather than a common outline. Keep migration and compatibility obligations beside contracts and implementation changes, adding independent migration detail when the actual scope warrants it.

For Overall Architecture, use the approved nine-chapter scaffold: 背景与范围 → 架构驱动 → 总体方案 → 结构与职责 → 关键流程与协作 → 共性技术设计 → 部署与运行 → 架构验证与风险 → 演进与迁移. Read the [overall writing contract](../methods/references/overall-architecture-writing.md) through the Architecture Documents Method for chapter boundaries, scope adaptation, mandatory figures and conditional state/transition views. Keep the template as the outline authority and that reference as the selection and completion authority.

For Subsystem Architecture, use the seven-chapter scaffold: 定位与设计要求 → 外部协作 → 内部方案 → 关键流程与协作 → 运行保障 → 架构验证与风险 → 演进与迁移. Read the [subsystem writing contract](../methods/references/subsystem-architecture-writing.md) for local realization of parent commitments, internal state before flows, runtime within the parent, required views and conditional migration. Inherit governing choices and explain local consequences rather than repeating the overall architecture.

For Module Design, use the five-chapter scaffold: 功能说明 → 规则与接口 → 实现设计 → 处理流程 → 设计验证. Read the [module writing contract](../methods/references/module-design-writing.md) for functional rules, interface semantics, implementation/state ownership, named processing flows, required views and local versus integration evidence. Keep runtime effects with affected processing and extension/compatibility with implementation rather than imposing additional platform or migration chapters.

For Component Architecture, use the four-chapter scaffold: 组件职责 → 接口设计 → 实现机制 → 设计验证. Read the [component writing contract](../methods/references/component-architecture-writing.md) for guarantee-driven mechanism selection, consumer duties, compatibility, required views and matching verification. Choose actual mechanism topics instead of a mandatory concurrency section; apply state/resources and algorithm/protocol detail only where relevant.

Use these as optional design granularities. A System may contain modules directly; a component may be private or shared by multiple modules. Independent documentation requires a reader question and sufficient design substance. Existing specialist and support resources remain outside this primary-template change and do not require extra documents.

Apply the four viewpoints through the shared Architecture Reasoning Method at three points: identify drivers and assumptions, derive mechanisms through success and failure scenarios, then verify combined guarantees and evidence. Put resulting decisions and gaps in their owning design sections. Viewpoints do not select templates or create four parallel document sets.

## Knowledge system

Organize around subjects, objects and reader questions. Use Domain, Application, Governance and Runtime to reason about the design and check coverage. Separate navigation from substantive architecture, and keep one coherent problem explanation together even when it spans all four viewpoints. Preserve useful established viewpoint organization or add it as optional retrieval navigation; link the owning explanations rather than copying them. Retain existing specialist resources for explicitly requested or established structures; a catalog resource is not an approved documentation topology. Reuse one template for multiple subjects rather than creating a new skill for every document.

Preserve established topology, explicit user structure and local language. A request to organize a system includes inventories, gap/overlap assessment, appropriate writing and navigation within authorized scope. It does not require separate skill invocations. Link a shared explanation from its dependents; do not duplicate it or create placeholder documents for every possible topic. Keep navigation separate from substantive design judgments. Apply the shared cross-document scenario check to verify that the models jointly preserve the claimed outcome, including failure and recovery. Derive technical security mechanisms from threats as well as describing policy authority.

## Delivery adaptation

| Reference Knowledge | Concrete delivery |
| --- | --- |
| Model, variants and applicability | Named object, actual constraints and selected/proposed design |
| Illustrative assumptions | Verified baseline or explicit design assumptions |
| Reusable tradeoffs and review triggers | Decision authority, accepted cost and unresolved choices |
| Validation expectations | Requirement-to-design-to-evidence traceability |
| Project extraction | Adopt/Adapt/Reject decisions and compatibility/migration constraints |

Apply `methods/architecture-templates/concrete-design.md` to the same overall, subsystem, module and component assets used for Knowledge. Keep delivery entry, migration and validation assets with their owning Writer. Use the delivery main document to integrate the relevant architecture concerns. Split subsystem, module, component, deployment, migration or validation documents only for independently useful detail. Keep stable System authorities linked; promotion of Project decisions requires evidence and authorization. Project architecture support does not expand into general task planning or executing deployment.

## Reasoning and reader flow

Follow the shared chain in `methods/architecture-documents.md`: problem and scenarios, strategy, structure and mechanism, tradeoffs, then evidence. Adapt that chain to each document responsibility. Overall architecture allocates responsibilities and requirements; subsystem architecture explains how its internal responsibilities realize external commitments; module design explains functional rules, state changes and dependency coordination; component architecture explains the contract, invariants and mechanism under allocated constraints. Deployment connects operating targets to topology, capacity and recovery. Migration protects invariants through transitions and irreversible boundaries. Validation connects claims to scenarios, evidence and actual acceptance decisions.

Apply `methods/prose-quality.md` to choose expression. Develop reasoning in prose and explain relationships or behavior with figures. Retain tables for useful comparisons, navigation, matrices and traceable records. A template's coverage does not require a table for each concern or a fixed number of tables. Keep a decision or evidence record in one owning document and link it from overviews and dependent designs.

For a complete document, review the aggregate reading path as well as individual blocks. A sequence of valid lookup tables can still duplicate boundary information and interrupt the design argument. Apply the whole-document expression review in the shared prose method, preserving source links and evidence limits when merging content. Use full-length output for this check; short samples establish only local expression.

## Design depth

Use the implementation-readiness checks in `methods/architecture-documents.md` to distinguish a useful design from a responsibility inventory. Overall designs connect logical structure to software realization and integration; subsystems realize parent guarantees through internal contracts and transactions; modules explain their functional rules and processing coordination; components explain the actual mechanisms behind each important guarantee, including relevant assumptions and failure boundaries. Keep architecture-significant data relationships and contract semantics in the design while executable detail remains with implementation. A proposed, evidence-bounded design is valid output before approval; a collection of unallocated future decisions is not a completed design.

## Maintenance and validation

Keep the common template catalog and assets under `methods/architecture-templates/`. Keep Company/Project type identities and shared asset assignments in their existing Writer registries. Generate the catalogs, check all bundled assets are selected and reachable, rebuild the plugin, and verify both system-writing and delivery-writing behavior with isolated samples. Keep Public Skill IDs, exact Display Names, explicit invocation, and flat skill layout unchanged.

The CEX knowledge base is a structural reference, not a bundled dependency or source of universal trading requirements. Its README references template directories absent from the inspected local copy; the new files are reconstructed from document responsibilities and representative content, not claimed verbatim recoveries.
