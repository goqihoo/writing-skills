# Architecture document quality assessment and repair

## Evidence and diagnosis

- `f7c990d` removed the old `skills/technical/write-delivery-architecture/assets/delivery-architecture-template.md` during the company-documentation scope change. The old template offered a complete progression from context and drivers to scenarios, responsibilities, contracts, failures, controls, operation, migration, decisions, and validation.
- `e93e20c` explicitly implemented `.scratch/technical-architecture-and-internal-type-registry/spec.md`: delete the company Technical Architecture template and configure System/Subsystem Architecture as Freeform. The intent was reader-driven structure and smaller registries, not an accidental missing-file operation.
- Architecture Knowledge still has a template. The pre-0.5 version contained explicit scenarios, validation signals, and project extraction. Later revisions compressed these responsibilities; `47eb15d` replaced named analysis sections with one generic analysis prompt and classification fields. Avoiding fixed taxonomy headings was valid, but concrete explanatory support was weakened.
- Current methods cover many correctness concerns. Coverage does not establish that a document explains its structure and mechanism. Existing tests mainly assert contract vocabulary and routing, so passing them cannot prove writing quality.
- No actual failing user deliverable was supplied in this chat. These are repository-grounded failure mechanisms and a repair hypothesis, not a measured attribution of every poor output to template deletion.

## Recovery decisions

| Resource | Action | Reason |
| --- | --- | --- |
| Company Technical Architecture | Retain the pre-existing working-tree adaptive restoration; connect shared reader verification | Preserve ongoing work and overview-first structure |
| Old delivery architecture template | Recover responsibilities into System and Subsystem adaptive templates | Its mixed project/System scope cannot be copied wholesale |
| Architecture Knowledge | Rewrite the existing adaptive template | Restore mechanism, example, counterexample, selection, and adoption validation |
| Other deleted Product/Technical templates | Leave unchanged | This request and evidence concern architecture quality; no basis for restoring the entire removed taxonomy |
| Public Skill IDs, display names, authority boundaries | Preserve | A template repair does not establish a new project-delivery Writer |

## Completion

Verify assigned templates resolve in canonical and generated packages, regenerate the type catalog, run repository checks, and evaluate architecture sample outputs for structural clarity, behavioral trace, rationale, and evidence discipline. Record the limits of sample validation. Preserve unrelated working-tree edits.

## Validation record

- A clean virtual environment installed `requirements-dev.txt`; all 136 repository tests passed.
- Generated catalog and Codex package are in sync; shell syntax and whitespace checks passed.
- Claude marketplace and plugin manifests passed validation. The three modified generated skills passed the generic skill validator.
- The installed Codex CLI exposes no plugin-validator command, and no dedicated validator was found among available tools. Package parity, manifest/layout contracts, and generated skill validation passed; dedicated Codex plugin validation remains unavailable.
- An unrelated Finder `.DS_Store` in the generated skill root caused the first parity check to fail. Removing that generated metadata file allowed the unchanged parity check and full suite to pass.
- Independent sample generation is being used as a behavioral smoke test, not a benchmark or proof of quality across all domains.

## Behavioral sample result

An independent agent read the updated skills and produced a Chinese fictional Order System architecture and reusable asynchronous-confirmation knowledge article in `/tmp/scribe-architecture-eval-vo3SZO/`. Parent review read both full outputs. The artifacts expose ownership, a concrete recovery path, conditional guarantees, alternative mechanisms, and current/proposed distinctions. The knowledge article transfers the mechanism to a borrowing case and names an inventory-expiry counterexample. These are useful sample results, not before/after benchmark scores or evidence about a production implementation.

The sample exposed an unrelated but user-visible completion defect: standalone documents inherited mandatory repository navigation and ended with integration warnings. Updated all three architecture Writers to scope navigation completion to work in an existing documentation set, and keep integration notes outside the document body. This final instruction correction received static/repository validation; the saved samples retain the original warning as test evidence.

## Second-pass structural review

The restored templates were reviewed for reading order, section ownership, repetition, and topic fit. This pass preserves the skill boundaries and improves the artifact structures:

| Finding | Structural change | Reader benefit |
| --- | --- | --- |
| Status and scope can arrive after the design | Put compact status/baseline/owner near the title and scope in the opening | Readers distinguish a proposal from current truth immediately |
| Logical responsibilities, information, contracts, and operating concerns can accumulate in one section | Separate logical/information design from contracts/behavior and deployment/operation; allow further splits only by reader question | Readers can locate structure, behavior, and realization independently |
| Drivers, rationale, alternatives, and tests do not form a visible chain | State priorities early, place rationale beside design, reserve comparison for material choices, and trace claims to validation | Decisions are assessable without repeated explanation |
| Evolution and validation mix two questions | Separate transition constraints from proof and residual risk | Migration plans cannot stand in for design evidence |
| Knowledge template assumes every topic is an adoptable pattern | Add explanatory, comparative, and pattern-oriented reading paths in the existing reference | Conceptual topics can teach distinctions without fabricated alternatives or implementation plans |
| Model, scenario, and application can repeat the same mechanism | Give each a distinct responsibility: general model, concrete consequences, transfer judgment | Each section advances understanding |

Check the revised paths using a non-transactional System architecture and conceptual Architecture Knowledge sample, in addition to registry, package, and repository checks. These are structural and behavioral smoke tests, not evidence of production correctness.

### Second-pass validation result

- All 136 repository tests passed; generated-package parity, shell syntax, whitespace checks, Claude plugin/marketplace validation, and the three modified generated-skill validators passed. Dedicated Codex plugin validation remains unavailable as noted above.
- Independent samples are in `/tmp/scribe-architecture-eval-rfsm9W/`: a document-search System architecture and a conceptual article distinguishing logical and deployment boundaries. Parent review read both outputs. The System article uses index publication, resource isolation, permissions, and reconstruction instead of transaction-processing scaffolding. The Knowledge article uses change propagation and a counterexample, with no forced adoption plan or alternatives table. Sections were combined naturally rather than copied mechanically.
- Remaining sample limitations: a System preamble sentence exposes internal scope reasoning; the short System article does not fully develop deletion and source-version consistency. Treat these as prose/coverage review findings under existing contracts, not reasons to add universal topic-specific template sections. The samples demonstrate structural flexibility, not full System design acceptance or measured performance.
