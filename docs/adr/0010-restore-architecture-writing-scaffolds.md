# Restore adaptive architecture writing scaffolds

Superseded in its template-family and Project-scope decisions by [ADR-0011](0011-separate-knowledge-and-delivery-template-families.md).

## Decision

Assign adaptive templates to System Architecture and Subsystem Architecture through the existing Writer registry. Retain the company Technical Architecture adaptive template and rebuild the Architecture Knowledge template around mechanism, worked scenarios, alternatives, transfer, and validation. Keep shared model/scenario/reader verification in `methods/architecture-reasoning.md`; keep artifact-specific expression in the owning templates.

## Reason

The registry refactor explicitly removed the company architecture template and selected Freeform Structure for System and Subsystem Architecture. The Knowledge template was also compressed over successive revisions. Removing fixed domain/viewpoint headings was useful, but coverage profiles did not replace the writing scaffolds that connected structure, behavior, rationale, and evidence. The user reports poor architecture deliverables. This is evidence to restore practical guidance, not evidence that every removed document type should return.

## Compatibility and cost

Revise the Freeform selections in the historical technical-architecture-and-internal-type-registry specification for System and Subsystem Architecture. Preserve ADR-0007's small registries and ADR-0008's optional template mechanism. Do not restore obsolete skill names, fixed domain headings, speculative types, or project Technical Design ownership. The original delivery template mixed stable System architecture and bounded project changes; recover its useful writing responsibilities within current authority scopes.

Maintain two additional registered assets and their reachability checks. Honor explicit user structures and narrow edits. Validate generated-package parity and real sample outputs; static contract tests establish packaging and routing, not professional writing quality. Reassess using real poor-quality deliverables when available.

## Structural refinement

Place concise document status at entry, design priorities before detail, rationale beside the relevant design, and validation separately from evolution. Let logical structure, contracts and scenarios, and deployment/operation answer distinct reader questions, merging short sections as appropriate. Let Architecture Knowledge choose an explanatory, comparative, or pattern-oriented reading path within the same skill and adaptive template. Validate transfer beyond transaction-processing examples.
