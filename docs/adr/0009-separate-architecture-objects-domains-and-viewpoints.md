# Separate architecture objects, domains, and viewpoints

Status: superseded by [ADR-0013](0013-use-four-architecture-viewpoints.md) for the classification scheme; object, scope and authority remain distinct.

Scribe distinguishes the Architecture Object and Scope from foundational Architecture Domains and cross-cutting Architecture Viewpoints. Business, Data, Application, and Technology are domains; Security, Governance, and Runtime are viewpoints; Domain, Application, Governance, and Runtime remain four correctness checks rather than a peer taxonomy or mandatory output. Company, System, and Subsystem remain Authority Levels for Technical Documentation routing, while every architecture artifact names its object and scope explicitly. This supersedes ADR-0005 because the older four-view model preserved output flexibility but still conflated a business problem scope, one architecture domain, and two cross-cutting concerns.
