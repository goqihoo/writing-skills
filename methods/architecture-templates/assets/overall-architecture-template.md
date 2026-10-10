# [总体架构]

**Purpose:** [Architecture Knowledge / Concrete Design]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## 背景与范围

### 问题与目标

[Explain the motivating problem, intended outcomes and decisions this design supports. Ground the need in evidence or explicit assumptions; distinguish a technology choice from the outcome it serves.]

### 设计范围

[Name the object and authority, included responsibilities and lifecycle, meaningful exclusions, and relationships to governing, adjacent and detailed documents. Define scope through responsibility rather than repository or deployment counts.]

### 外部上下文

[Explain actors, callers and external dependencies, the requests, information and results crossing the boundary, and dependency assumptions. Treat the object as a black box in this view.]

[Figure: external context]

### 现状与设计起点

[Explain the existing structure, assets and accepted decisions that constrain this design, separating observed baseline from target and proposals. For greenfield work describe the starting environment; for Knowledge describe applicability and assumptions. Keep evidence dates and limits identifiable.]

## 架构驱动

### 关键功能场景

[Select scenarios whose actors, conditions and required outcomes affect boundaries, cooperation or guarantees. Establish what must be achieved before describing internal execution. Use a requirements-level activity figure only when useful.]

### 架构特性与优先级

[Explain relevant characteristics through context, stimulus, response and observable satisfaction criteria, with priorities and conflicts. Distinguish sourced targets, design assumptions and unresolved budgets; use bounded qualitative criteria where numerical targets lack evidence.]

### 约束与不变量

[Identify binding constraints and invariants, their sources, scope and design consequences. Include quality targets that are genuinely binding. Separate established restrictions from proposed technologies and link inherited governing principles.]

## 总体方案

### 方案概览

[Explain the core arrangement and how its parts jointly produce the intended outcome. Establish the defining relationships and, for an operating system, who initiates work, what controls its next action and how completion is recognized. Walk a short representative working path before detailed state and contracts. Distinguish material baseline-to-target changes and unresolved choices. Select a subject-specific subsection when this core model needs independent explanation; keep it visible here even when later flows or shared mechanisms expand it.]

[Figure: overall architecture]

### 设计原则

[Explain applicable decision-guiding principles, their rationale, scope and local consequences. Distinguish inherited rules from locally chosen principles and identify established exception authority where relevant.]

### 架构风格与组织方式

[Name or precisely describe the actual organization and its scope. Explain its structural evidence, dependency rules, interaction modes and mixed-style boundaries. Show how this object applies that organization rather than reproducing a generic style specimen.]

[Figure: architecture style and organizing rules; reference the overall figure when it explicitly covers this question]

### 关键策略与取舍

[Connect major strategies to their drivers, realizing mechanisms, reasons for fit, accepted costs, meaningful alternatives and review triggers. Distinguish accepted decisions, proposals and inferred rationale. Link detailed decision records where they exist.]

## 结构与职责

### 组成与责任边界

[Explain each principal part's responsibilities, provided guarantees, exclusions and boundary rationale, including the applications, packages, components, stores or adapters that realize it where known. Distinguish peer functions, shared mechanisms and containment/use relationships; allocate overall guarantees without requiring extra design levels. Separate actual implementation from target design. Link owned detail. Develop a separate, specifically named mapping explanation only when the realization is complex enough to answer an independent reader question; leave process placement to 部署与运行.]

### 数据与状态

[Explain core identities, relationships, versions, authoritative and derived state, and decision/change ownership. Define architecturally important state meanings, legal transitions, guards and invariants; distinguish storage from decision authority. Locate local transactions and cross-boundary consistency, access, retention, lineage and reconstruction responsibilities where material. Link detailed models and executable schemas.]

[Conditional figure: important state transitions]

### 契约与依赖

[Explain significant operations, commands, events or queries; their callers, owners, information meaning, preconditions, and accepted/completed/rejected/failed/unknown semantics. Specify dependency direction, local/remote and synchronous/asynchronous relationships, compatibility and assumptions. Locate authorization responsibility while leaving common enforcement design to its owning topic.]

## 关键流程与协作

[When multiple entry points, optional stages or independent/composed execution apply, introduce request selection and reusable operations through Show independent and composed execution in `../../references/overall-architecture-writing.md`. Keep this overview before the selected detailed flows; omit it for a simple single-path design.]

[Conditional figure: flow selection, prerequisites, reuse and completion across independent requests and the composed run; choose the type through Visual-type routing in the shared Visual Production Method]

### [关键流程名称]

[Explain the trigger, preconditions, inputs or versions and observable result. Follow the named responsibility owners from 结构与职责 and participants from 外部上下文 through actions, data/state changes, contracts, transaction boundaries and handoffs, applying Structure-to-flow traceability in the shared Architecture Reasoning Method. Explain consequential branches, competition, duplicates, partial or unknown outcomes where relevant; locate detection, recovery responsibility, retry/compensation permissions and evidence for continuation. State any temporarily weakened guarantee. Reference common mechanisms instead of repeating them.]

[Figure: collaboration among the whole object's principal responsibility owners, including important branches or supplemental failure/recovery views]

[Repeat this subsection for each selected key flow; name subsections after actual flows. Apply Select flows and shared technical topics in `../../references/overall-architecture-writing.md` when deciding which scenarios need their own subsections. Apply the Overall / System expansion boundary in Structure-to-flow traceability; reference an existing local processing explanation at the operation it realizes. For a static model, trace a concrete change impact.]

## 共性技术设计

### [共性技术主题名称]

[Explain a technical concern shared by multiple parts or flows: motivating requirement, scope, common rules and guarantees, realizing mechanism, provider/consumer responsibilities, boundaries and exceptions. Link the architecture characteristics served. Keep business rules with their owning function; reference existing governing standards and explain local application or deviation.]

[Add a mechanism figure when it clarifies the design; give any independently explained key flow its own corresponding figure. Apply Select flows and shared technical topics in `../../references/overall-architecture-writing.md` to retain qualifying topics or omit this chapter.]

## 部署与运行

### 部署结构与环境

[Map logical responsibilities to runtime and deployment units, infrastructure, networks, external dependencies and significant isolation/failure boundaries. Explain architecture-significant environment differences. Distinguish current deployment from proposed topology or illustrative reference realization; link complete configuration and runbooks.]

[Figure: deployment structure]

### 运行方式与资源管理

[Explain significant startup/readiness/shutdown dependencies, workload and resource assumptions, concurrency and capacity controls, bottlenecks, scaling limits and overload behavior. Distinguish measured capacity from estimates and unverified budgets.]

### 故障应对与运行保障

[Explain failure propagation, detection and action conditions, operating ownership, isolation, degradation, recovery/failover and checks for restored availability and data correctness. Reference shared security, audit and observability mechanisms and the local failure semantics of key flows. Include a corresponding figure for each independently explained operating recovery flow.]

### 发布与变更

[Explain routine release order, prerequisites, mixed-version compatibility, configuration/interface/data-change coordination, post-release checks and stopping conditions. State rollback limits and forward-repair paths for irreversible changes. Include a corresponding figure for each independently explained release flow; leave structural migration stages to 演进与迁移.]

## 架构验证与风险

### 验证目标与方法

[Trace important characteristics, constraints, invariants and uncertain design assumptions to validation objects, methods, conditions and pass criteria. Verify how the chosen principles, organization and strategies are realized and whether their mechanisms jointly produce the claimed result. Prioritize consequential uncertainty.]

### 验证结果与证据

[Separate planned, partial and completed checks. Summarize evidence and the conditions under which each conclusion holds; link existing reports or observations and state remaining coverage gaps.]

### 剩余风险与待决事项

[Explain risk triggers, affected guarantees, contradictory assumptions, unallocated responsibilities and pending choices. State the response or reason for accepting exposure and the evidence or decision needed for closure. Name owners and timing only where established.]

## 演进与迁移

### 演进方向与触发条件

[Separate established evolution commitments from conditional directions. Explain applicability limits and what evidence would require reconsidering boundaries, styles or strategies. For Knowledge, explain variants and adoption conditions; distinguish local changes from those requiring governing authority.]

### 实施阶段与过渡状态

[For staged change, explain each stage's usable outcome, prerequisites, viable intermediate structure and completion conditions. Locate responsibility, request routing and authoritative data during coexistence; keep task schedules in their owning plan.]

[Conditional figure: important transition architectures during coexistence, authority transfer or phased replacement]

### 迁移、切换与退出

[Explain actual migration scope, integrity/correctness checks, coexistence read/write rules, cutover conditions and decision authority, post-cutover verification, rollback limits or forward repair, and retirement conditions. Include a corresponding figure for every independently explained migration, cutover or recovery flow. Link an existing migration design where it owns detail.]
