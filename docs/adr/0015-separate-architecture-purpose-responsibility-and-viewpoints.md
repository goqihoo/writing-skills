---
status: accepted
---

# Separate architecture purpose, document responsibility and viewpoints

Use Architecture Knowledge or Concrete Design to determine applicability, choices, evidence and commitments. Preserve stable Company/System versus Project authority within Concrete Design. Maintain one shared primary template for each of Overall Architecture, Subsystem Architecture, Module Design and Component Architecture; select by the reader question rather than duplicating templates by purpose.

Use Domain, Application, Governance and Runtime during driver identification, mechanism design and completeness checks for all four document types. This refines ADR-0013: viewpoints guide reasoning rather than default document organization. Preserve useful established viewpoint navigation, but organize new knowledge around subjects, objects and reader questions.

The four primary types are optional design granularities, not a mandatory hierarchy. A module owns a cohesive function and coordination; a component owns an encapsulated implementation mechanism and may be shared. Modules and components inherit governing System or Subsystem authority. Existing specialist and support resources remain outside this primary-template change; their presence does not require additional documents.

Verify source and packaged template routing, purpose adaptation and an end-to-end success/failure explanation across the selected objects. A complete hierarchy or four viewpoint sections alone does not establish design completeness.
