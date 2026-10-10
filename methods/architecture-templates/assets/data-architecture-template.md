# [Data Architecture]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## Purpose and data requirements

[Establish the reader decision, business outcomes, information scope, quality requirements and applicable privacy or retention constraints. Identify assumptions and exclusions.]

## Information model

[Explain entity identities, relationships, versions and business meaning with a concrete example. Distinguish logical information from a physical schema and show the essential relationships.]

## Authority and lifecycle

[Identify who establishes and changes facts, derived copies and lineage. Follow creation, correction, use, retention and deletion; explain how quality is established and how invalid data is handled.]

## Persistence and consistency

[Explain storage responsibilities, local atomic changes, cross-owner consistency and reconstruction sources. Show how the chosen mechanisms preserve the information invariants and where lag or conflict is allowed.]

## Exchange and protection

[Explain which information crosses boundaries, its meaning, freshness and allowed use. Connect classification to access, protection and disposal mechanisms; link integration protocols and security controls to their owners.]

## Worked lifecycle and failure

[Trace the same entity and versions through a representative lifecycle and a partial, stale or conflicting outcome. Explain repair, reconciliation or irrecoverable loss and its business consequence.]

## Variants and evolution

[Compare relevant models under the same requirements. Explain schema or meaning changes, compatibility, migration and downstream effects; identify which changes require a different model.]

## Validation and adaptation

[Connect integrity, quality, protection and recovery claims to checks and evidence limits. State adoption prerequisites and a context in which the model fails.]

## Related documents

[Link the domain meaning, overall commitments, application owners, integration contracts and runtime storage mechanisms. Keep their detailed explanations with their owners.]
