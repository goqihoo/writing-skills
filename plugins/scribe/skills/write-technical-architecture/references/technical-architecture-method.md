# Technical Architecture method

Treat Technical Architecture as the company-level structure of its Technical Landscape, even when the document title does not contain the word “company.” It describes the company as a system of systems, not one repository or one delivery project.

## Outputs

- **Technical Architecture:** the Technical Landscape as a system of systems, including stable responsibilities, boundaries, relationships, constraints, failure domains, and evolution.
- **Product-System Map:** the many-to-many relationships among products, systems, and capabilities. Never assume one product maps to one system.
- **Architecture Topic:** one accepted cross-system concern whose state ownership, contracts, failure recovery, joint release, or evolution cannot be governed by one System Architecture.

## Levels and views

Lock the Architecture Level to Company. Apply the Domain, Application, Governance, and Runtime Architecture Views only as coverage checks; do not require one section or file per view.

## Decision tests

For every material choice, record drivers, alternatives, decision authority, rationale, accepted costs, validation, and review triggers. Link the governing System Architecture and Machine Authority instead of copying their detail.

## Evolution tests

Explain current and target states, transition constraints, compatibility, sequencing dependencies, retirement, and signals that require architecture review. Do not turn a roadmap or implementation plan into the architecture document.
