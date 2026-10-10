# [模块设计]

**Purpose:** [Architecture Knowledge / Concrete Design]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## 功能说明

### 场景与结果

[Explain a cohesive business or technical function through a representative actor, use condition, intended action and observable result. Establish the purpose before implementation; select scenarios that reveal the function rather than listing every screen or endpoint.]

### 功能范围

[Explain owned decisions, actions, facts and results, supported responsibilities and meaningful exclusions. Identify external capabilities the module uses and why its rules, state or coordination warrant independent design. Bound responsibility rather than copying repository folders.]

### 上层要求

[Identify the governing System or Subsystem and allocated guarantees, characteristics, data authority, interface/runtime constraints and principles. Explain their local consequences and which changes require coordination. Keep unallocated budgets explicit. Preserve direct System-to-module relationships without inventing a Subsystem or independent deployment.]

### 现状与设计起点

[Explain existing capabilities, interfaces/data/behavior to retain, and what this design adds or changes. Distinguish observed facts, accepted decisions, proposals and assumptions. For new work describe actual prerequisites and dependencies; for Knowledge describe applicability. Combine with 功能范围 when the baseline is brief.]

## 规则与接口

### 支持的操作

[Describe independently meaningful operations, their purposes, use conditions and responsibility boundaries. Group interfaces that expose the same operation; select actual capabilities without forcing CRUD. Link full interface catalogs.]

### 输入、输出与完成条件

[Explain object identity, input/output meaning, identity/version/context and preconditions. Specify observable completion and what the caller may do next; distinguish acceptance, completed processing and external effects where relevant. Retain implementation-significant semantics while linking complete field and protocol definitions.]

### 处理规则与限制

[Explain applicable business or technical rules for eligibility, permissions, judgment/calculation, allowed state-dependent actions, conflicts and priorities. Specify invalid, failed or uncertain outcomes. Link externally owned policy and explain local application; keep unresolved rules explicit with their implementation consequence. Leave the state model to 数据与状态 and execution order to 处理流程.]

### 调用关系与依赖

[Identify permitted callers, external dependencies and guarantees each party supplies. Specify local/remote and synchronous/asynchronous behavior, duplicate/order/timeout/cancellation handling and compatibility where material. Explain whether retries are safe and how an unknown result can be resolved. Add a relationship figure when needed for clarity.]

## 实现设计

### 内部结构与职责

[Explain which internal parts implement this module, what each owns and how they collaborate. Apply **Explain internal composition and collaboration** in `../../references/module-design-writing.md` to the figure and prose. Explain the responsibility split and map logical parts to actual or proposed code organization at the available evidence depth; link independently owned mechanisms without requiring extra component documents.]

[Figure: module internal composition, each part's responsibility and meaningful collaboration relationships; distinguish relevant external dependencies from internal parts]

### 数据与状态

[Explain core entities, identities, relationships and versions; distinguish maintained, referenced and derived data and their owners. Define important state meanings, legal transitions, guards and change permissions. Locate atomic changes and cross-boundary consistency, durable recovery/reconstruction evidence, access, retention and traceability needs. Link executable schemas rather than copying them.]

[Conditional figure: important state transitions]

### 实现选择与取舍

[Explain consequential choices in rule organization, coordination, algorithms, storage and existing components. Connect each choice to actual functional/quality requirements, inherited principles and style, realizing mechanisms, applicability and accepted costs. Discuss meaningful alternatives without manufacturing a separate style, deployment or option quota.]

### 扩展与兼容

[Explain the impact of actual rule, operation, state, interface, data or dependency changes on callers and parent commitments. Introduce extension points only for justified change needs. Locate compatible changes, data and unfinished-work transition requirements, rollback/recovery limits and changes requiring coordination. Add or link substantive migration detail where needed and give any independently explained migration/cutover/recovery flow a corresponding figure.]

## 处理流程

### [关键处理流程名称]

[Explain the triggering operation from 规则与接口, input/identity/version/state preconditions and observable result. Apply the Module Design expansion boundary in Structure-to-flow traceability in the shared Architecture Reasoning Method. Follow the internal responsibilities from 实现设计 through rule evaluation, decisions, dependency calls, intermediate state, atomic commits and responsibility handoffs. Explain significant branches, concurrency, repeats, ordering, waiting or cancellation where relevant. Locate authorization and durable control evidence at affected actions. Explain exceptions beside those steps: completed effects, result certainty, retry/recovery/compensation ownership, durable state and continuation evidence. Retain resource limits, overload, backpressure, degradation and completion signals where they affect the function, with parent runtime/isolation assumptions explicit.]

[Figure: internal realization of this module operation, with callers and dependency contracts at its boundary, including consequential branches or supplemental failure/recovery views]

[Repeat for actual selected key flows. Group equivalent operation variants around shared behavior and meaningful differences; give independently useful recovery flows their own corresponding figure.]

## 设计验证

### 功能与规则验证

[Connect supported operations, decisions/calculations, permission/state rules, conflicts/priorities and completion effects to meaningful input conditions, expected outcomes and sourced pass criteria. Verify consequential implementation choices and allocated characteristics as well as successful behavior. Preserve unknown business standards rather than inventing numeric or policy answers. Link detailed test cases or test code.]

### 边界与故障验证

[Select relevant invalid/stale input or state, concurrent/repeated operations, dependency failures/timeouts, resource limits, partial processing/recovery and compatibility changes. Check these against actual mechanisms, contracts and parent guarantees. Distinguish local checks from required integration with real dependencies, shared transactions and external effects.]

### 验证结果与证据

[Separate planned, partial and completed checks with implementation version, conditions, scope, evidence and remaining gaps. Explain what existing results establish and what still requires integration or broader validation; keep illustrative reasoning distinct from observed evidence.]

### 风险与待决事项

[Identify unresolved rules, dependency conditions, assumptions and choices, the affected operation/result/guarantee, interim handling, limitations and closure evidence. Distinguish local implementation decisions from business-rule, contract or parent-guarantee changes requiring their actual decision owner. Name owners and timing only when established, and identify conditions that require redesign or limit reuse.]
