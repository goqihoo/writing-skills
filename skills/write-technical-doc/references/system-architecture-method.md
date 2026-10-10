# System Architecture method

Use this method for System Architecture and proportionally for Subsystem Architecture, Module Design and Component Architecture. Lock the Architecture Object to the named System, Subsystem, functional module or component. Let a module or component inherit its governing System or Subsystem Authority Level without introducing another level, and keep the direct design document as the coherent entry point.

## Drafting and verification

Read the assigned shared adaptive template and `../../../methods/architecture-templates/concrete-design.md`. Use the Architecture Reasoning Method to develop the model at the selected object's scope. Apply **Plan section questions before drafting**, **Make the design usable** and **Review before completion** in [the Architecture Documents Method](../../../methods/architecture-documents.md) while developing the artifact. Let the selected branch contract own chapter responsibilities and required views; let that Shared Method own explanation testing and repair.

## Select relevant concerns

Derive explanatory depth from the object's commitments, source requirements and reader decisions. Use the Domain, Application, Governance and Runtime correctness checks in [the Architecture Reasoning Method](../../../methods/architecture-reasoning.md) to find an overlooked concern, then explain its consequence in the owning section. Preserve linked Business/Product authority and stable Company/System decisions. Map relevant logical responsibilities to their realization and operating conditions without assuming every function is a separately deployed unit or that every object owns persistent state.

Use source facts and concrete scenarios to distinguish missing explanation from unresolved design. Keep Machine Authority responsible for executable detail while retaining the semantics needed to understand and constrain that implementation. Coverage diagnoses an omission; apply the shared reader reconstruction to determine whether the delivered explanation actually resolves it.

## Supporting files

Split a supporting file only when it has an independent reader task, authority, change cycle, and navigation value. One invocation may update the main architecture document and directly affected supporting files; do not rewrite unrelated files.

## Completion

Complete the shared explanation review at the requested scope and apply the owning type's completion profile. Keep the direct architecture a coherent entry point with correct authority links. Distinguish completed writing from design readiness wherever a necessary judgment remains unresolved.
