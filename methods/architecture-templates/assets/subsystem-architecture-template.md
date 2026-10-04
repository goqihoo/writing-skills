# [子系统架构]

**Purpose:** [Architecture Knowledge / Concrete Design]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## 定位与设计要求

### 定位与责任边界

[Locate the Subsystem within its parent, identify the governing architecture and authority, and explain its contribution, included/excluded responsibilities and relationships to adjacent parts. Explain why meaningful internal design warrants an independent Subsystem document.]

### 承接的场景与架构特性

[Explain allocated functional scenarios and priority characteristics through caller conditions, required outcomes and observable local criteria. Link established parent requirements, justify local refinements and identify newly discovered parent-level needs. Keep unallocated budgets explicit rather than treating the parent's full target as a local allowance.]

### 约束与不变量

[Identify inherited contracts, information authority, technical/runtime restrictions and invariants this Subsystem must preserve. Explain local consequences of governing principles and distinguish locally changeable decisions from changes requiring parent coordination. Leave proposed solution choices to 内部方案.]

### 现状与设计起点

[Explain existing implementation, accepted decisions, capabilities to preserve and intended changes. Separate observed baseline, target, proposals and unknowns. For a new Subsystem describe actual prerequisites and dependencies; for Knowledge describe applicability without inventing project history.]

## 外部协作

### 调用方与依赖

[Explain callers, event/data sources, upstream/downstream dependencies, interaction direction, meaning and assumptions, with owners where known. Distinguish in-process collaboration from remote interaction without treating every logical boundary as a network boundary.]

[Figure: subsystem external context]

### 提供的能力

[Explain externally meaningful capabilities and guarantees, where the Subsystem accepts responsibility, how far that responsibility extends, and what callers or dependencies still own. Link complete operation/interface catalogs rather than reproducing them.]

### 调用条件与结果

[Specify significant inputs/outputs, identity, state/version preconditions, synchronous/asynchronous behavior, handoff points and accepted/completed/rejected/failed/unknown semantics. Explain retry, ordering, cancellation and compatibility where supported and material. State what each outcome permits the caller to infer or do next.]

## 内部方案

### 内部结构与工作方式

[Show the principal internal parts and relationships, explain a short representative working path, and map responsibilities to implementation units. Name or precisely describe the organizing style and actual dependency rules, including inheritance or refinement of the parent architecture. Distinguish logical organization from deployment.]

[Figure: internal architecture and organizing rules]

### 职责与内部契约

[Allocate responsibilities, decision authority, provided guarantees and retained consumer duties. Explain important internal preconditions, outputs, completion/failure meanings and dependency direction, including sync/async and local/remote choices. Show how internal commitments jointly realize the external promise; keep peer functions distinct from shared mechanisms. Link independently owned implementation detail.]

### 数据与状态

[Explain core identities, relationships, versions, authoritative/derived data and change ownership. Define important state meanings, legal transitions, guards and permissions; locate atomic changes and cross-boundary consistency mechanisms. Preserve durable recovery records and material reconstruction, access, retention, lineage and audit requirements. Distinguish business invariants from storage choices and link detailed models or executable schemas.]

[Conditional figure: important state transitions]

### 关键设计选择与取舍

[Connect applicable principles, key strategies and technology choices to local problems, allocated characteristics and realizing mechanisms. Explain meaningful alternatives, accepted costs, review triggers, replaceable internals and limits imposed by external contracts or parent guarantees. Keep local rationale beside its mechanism and use this section for consequential comparisons rather than repeating explanations.]

## 关键流程与协作

### [关键流程名称]

[Explain trigger, preconditions, input and observable completion of an external promise. Follow internal participants, actions, data/state changes, transactions and handoffs. Explain consequential branches, concurrency, ordering, waiting, duplicates or cancellation where relevant, including who may commit. Trace failures, partial/unknown outcomes, durable recovery state, retry/reconciliation ownership and evidence for continuation; identify temporarily weakened guarantees. Reference established state and shared mechanisms rather than defining them again.]

[Figure: this key flow, including important branches or supplemental failure/recovery views]

[Repeat this subsection for each selected key flow. Add internal detail to a parent scenario; use a concrete change-impact flow for a static reference model. Give an independently explained recovery flow its own corresponding figure.]

## 运行保障

### 运行位置与资源

[Map internal responsibilities to the parent's runtime and deployment units, storage, communication and external services. Explain shared/exclusive resources, workload, capacity/concurrency limits and significant startup/readiness/shutdown conditions. Distinguish measured data, estimates and unresolved targets. Preserve actual in-process placement rather than inventing independent services.]

[Figure: subsystem runtime and deployment within the parent; reference an existing parent view when it fully answers this question]

### 依赖故障与降级

[Explain dependency, shared-resource and process failures; isolation or propagation; overload admission and handling of accepted work. State which capabilities remain available, must wait or must be rejected, and how degradation changes external guarantees. Distinguish whole-capability effects here from one request's failure path in 关键流程与协作.]

### 监测与运行恢复

[Explain meaningful health/completion signals, automatic/manual action conditions, restart, recovery or replay ownership and the durable facts that permit continuation. Verify restored data correctness and external capability. Reference inherited logging, tracing, alerts, backup and security mechanisms while specifying local signals, runtime identities, trust/access boundaries and audit responsibilities. Include a corresponding figure for each independently explained operating recovery or failover flow.]

### 发布与兼容

[Explain joint or independent release, code/instance coexistence, interface/event/data compatibility, change order, post-release verification and rollback limits or forward repair. Preserve actual parent release constraints. Include a corresponding figure for each independently explained release flow; leave structural splits, authority transfer and substantive replacement to 演进与迁移. Link configuration and runbooks.]

## 架构验证与风险

### 验证目标与方法

[Trace allocated requirements and important assumptions to validation objects, methods, conditions and pass criteria. Cover external contracts/characteristics, internal ownership/state/transaction/recovery composition and actual runtime/dependency conditions. Distinguish proof of the local guarantee from parent end-to-end validation; identify evidence owners for caller or dependency assumptions.]

### 验证结果与证据

[Separate planned, partial and completed validation with version/environment/condition limits, observed results and coverage gaps. Link existing reports. Check that inherited evidence applies to this Subsystem's actual use rather than inferring business correctness from an infrastructure capability.]

### 剩余风险与待决事项

[Explain triggers, affected guarantees, response or accepted exposure, and closure evidence or decisions. Distinguish locally resolvable gaps, changes requiring parent coordination and conditions owned by dependencies. Record owners and timing only when established.]

## 演进与迁移

### 演进方向与调整条件

[When evolution is relevant, distinguish established arrangements from conditional directions and applicability limits. Explain workload, scenario, contract or parent-responsibility changes that would require reconsideration, and distinguish local decisions from changes requiring coordination.]

### 过渡方案与兼容

[For staged change, explain coexistence, routing, read/write and decision authority, interface/event/data compatibility and stage entry/exit conditions. Account for unfinished requests, tasks or sessions and who completes, takes over or terminates them. Reference parent staging while explaining local mechanisms.]

[Conditional figure: transition architectures for complex coexistence, authority transfer or phased replacement]

### 迁移、切换与退出

[Explain migration scope, integrity and behavior checks, cutover conditions, rollback limits or forward repair, and retirement conditions. Protect established outcomes and unfinished work through every transition. Include a corresponding figure for every independently explained migration, cutover or recovery flow. Link an existing migration design where it owns detail; omit this chapter when no substantive evolution or migration applies.]
