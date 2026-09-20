# Technical Architecture method

Treat Technical Architecture as the company-level structure of its Technical Landscape, even when the document title does not contain the word “company.” The Architecture Object is the named company's Technical Landscape, the Authority Level is Company, and the artifact describes a system of Systems rather than one repository or delivery project.

## Outputs

- **Technical Architecture:** the Technical Landscape as a system of Systems, including stable responsibilities, boundaries, relationships, constraints, controls, failure domains, and evolution.
- **Product-System Map:** the many-to-many relationships among Products, Systems, and capabilities. Never assume one Product maps to one System.
- **Architecture Topic:** one accepted cross-System concern whose information or state ownership, contracts, controls, failure recovery, joint release, or evolution cannot be governed by one System Architecture.

## Domains and viewpoints

Select only the Business, Data, Application, and Technology domains and the Security, Governance, and Runtime viewpoints that materially affect the company-level reader decision. Business and Product facts remain linked to their owning authorities; Technical Architecture records their structural consequences without redefining them.

Use domain, application, governance, and runtime correctness as final coverage checks. Do not require one section, file, or directory per domain or viewpoint. Distinguish Deployment Architecture topology from Runtime operating, failure, and recovery behavior.

## Decision tests

For every material choice, record the Architecture Object, governing scope, Authority Level, drivers, alternatives, decision authority, rationale, accepted costs, validation, and review triggers. Link governing System Architecture and Machine Authority instead of copying their detail.

## Evolution tests

Explain current and target states, transition constraints, compatibility, sequencing dependencies, retirement, and signals that require architecture review. Do not turn a roadmap or implementation plan into the architecture document.
