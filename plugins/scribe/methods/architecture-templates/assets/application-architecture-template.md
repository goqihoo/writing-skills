# [Application Architecture]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## Purpose, scope and organizing idea

[Explain the application scope and inherited domain, information, protection and operating commitments. Derive the application organizing idea from these pressures. Link the overall architecture when present and keep combined cross-view judgments there.]

## Context

[Figure: system boundary, external actors and dependencies. Make the application being described the visual focus; show external participants as readable, visually subordinate context. Preserve clear relationship labels and direction without giving every external system equal emphasis.]

## Drivers and characteristics

[Explain the scenarios, competing quality needs and constraints that make the problem difficult. Show how their priorities lead to the organizing idea and structural choices below; identify the assumptions and evidence behind those priorities.]

## Functional decomposition

[Describe cohesive functional modules, or justified subsystems when independent internal design is needed. Explain their operations, rules, state ownership, collaboration and boundary tradeoffs. Use the actual level in the heading; an application need not contain subsystems. Keep shared mechanisms and runtime carriers in their respective explanations.]

[Figure: peer functional modules or justified subsystems and labeled relationships; group only where boundaries distinguish participants.]

## Software realization and integration model

[Explain how the logical model can be realized as modules, processes, persistence and transport boundaries. Distinguish necessary guarantees from replaceable technology choices, and show how a plausible realization supports the defined flows. Compare local and distributed variants only where they change the mechanism or its limits.]

## Shared components

[Explain which mechanisms are shared, why sharing is justified and which contracts their users rely on. Identify ownership and link the component explanation; distinguish a reusable component from shared business-state authority.]

## Information ownership

[Explain the important information model, authoritative owners and derived copies. Show how lifecycle and consistency boundaries influence subsystem collaboration and what must remain true when copies lag.]

## Internal collaboration contracts

[Explain the meaning of the principal exchanges, their producers and consumers, guarantees and failure consequences. Connect them to the information ownership model and the flow below.]

## Core flows

[Walk a representative scenario through the subsystems, exchanged information and state changes to its result. Trace a failure or exception and show how the owners preserve or restore the guarantee.]

[Figure: interaction among the named modules or subsystems]

## Architectural decisions and variants

[Explain why the model uses these boundaries and mechanisms. Compare plausible variants under the same scenario, showing their conditions, benefits, costs and failure limits. State which choice the model uses and why.]

## Governance and runtime relationships

[Explain how application control points and mechanisms realize the allocated protection and operating commitments in the shared scenario. Link governing explanations and surface assumptions that the application cannot satisfy locally.]

## Validation

[Explain how the principal claims could be established or challenged. Connect a concrete example, experiment, review or operational observation to the claim it tests, the expected signal and the limits of the evidence. Distinguish illustrative reasoning, sourced observations and proposed checks.]

## Evolution and adaptation

[Explain which changes preserve the model and which invalidate its boundaries or guarantees. Explain compatibility, transition constraints and the choices or evidence needed for the changed design. Bound reusable claims with an unsuitable context where relevant.]

## Related documents

[Link parent, child, cross-view and source documents with a short explanation of what each contributes. Keep a shared mechanism in its owning document and point to it from dependents.]
