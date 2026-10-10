# Technical Architecture method

Treat Technical Architecture as the company-level structure of its Technical Landscape, even when the document title does not contain the word “company.” The Architecture Object is the named company's Technical Landscape, the Authority Level is Company, and the artifact describes a system of Systems rather than one repository or delivery project.

## Outputs

- **Technical Architecture:** the Technical Landscape as a system of Systems, including stable responsibilities, boundaries, relationships, constraints, controls, failure domains, and evolution.
- **Product-System Map:** the many-to-many relationships among Products, Systems, and capabilities. Never assume one Product maps to one System.
- **Architecture Topic:** one accepted cross-System concern whose information or state ownership, contracts, controls, failure recovery, joint release, or evolution cannot be governed by one System Architecture.

## Viewpoints

Apply the four viewpoints and deferred-category rule in `../../../methods/architecture-reasoning.md`. Business and Product facts remain linked to their owning authorities; Technical Architecture records their structural consequences without redefining them. Review domain, application, governance and runtime correctness without requiring a section, file or directory for each viewpoint.

## Decision tests

For every material choice, record the Architecture Object, governing scope, Authority Level, drivers, alternatives, decision authority, rationale, accepted costs, validation, and review triggers. Link governing System Architecture and Machine Authority instead of copying their detail.

## Evolution tests

Explain current and target states, transition constraints, compatibility, sequencing dependencies, retirement, and signals that require architecture review. Do not turn a roadmap or implementation plan into the architecture document.

## Overview and evolution presentation

Apply the shared overall architecture template assigned by the Writer registry with `../../../methods/architecture-templates/concrete-design.md`. Lead with the requested structural view; apply the reader verification in the shared Architecture Reasoning Method before treating coverage checks as completion. Keep delivery status and decision status independent, and distinguish a full product-driven target from a delivery slice. Do not impose this template on Product-System Maps, occasional Architecture Topics, or another Writer's System Architecture.
