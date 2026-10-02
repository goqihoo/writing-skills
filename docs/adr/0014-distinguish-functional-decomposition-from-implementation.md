---
status: accepted
---

# Distinguish functional decomposition from implementation

Application diagrams were mixing functional responsibilities with versioning, adapters, Agents and Workers. The application template also presumed a Subsystem layer, while the domain vocabulary collapsed Modules and Components into one implementation concept.

Use the shared Architecture Reasoning Method as the authority for responsibility decomposition. Distinguish Systems, justified Subsystems, functional modules and implementation components without requiring every level. Describe peer functions before mapping them to shared or private mechanisms and runtime carriers. A technical platform may still qualify as a System through its responsibility and lifecycle; deployment alone does not establish that boundary.

Application and Subsystem templates allow the actual decomposition level. Templates retain short artifact prompts; the shared method owns split criteria and reader checks. This refines the existing object/viewpoint distinction without adding an Authority Level, public skill or document type. Existing documents need changes only where their responsibility model or reader task warrants them.
