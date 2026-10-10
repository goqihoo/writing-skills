# Use four architecture viewpoints

Status: accepted by the user, 2026-10-01.

## Decision

Use Domain, Application, Governance and Runtime as Scribe's organizing and review framework. Keep Architecture Object, Scope, Viewpoint, View, Authority Level and document template selection distinct. The four viewpoints guide coverage without requiring four headings, files or directories.

Defer a separate classification and recommended splitting scheme for Data, Integration, Deployment and Security. Keep necessary design substance in the relevant explanation without prescribing fixed placement. Preserve existing specialist template files for explicitly requested artifacts. This decision does not migrate user knowledge bases or change registered template assignments.

## Rationale and consequences

Competing domain/viewpoint schemes encouraged treating object levels, topics and document boundaries as interchangeable. One framework makes reasoning and review consistent, while the selected template still owns the writing structure. Do not expand a normal architecture request into specialist documents simply because templates exist.

This supersedes ADR-0009's foundational-domain and cross-cutting-viewpoint classification. Its separation of design object, scope and authority remains valid. Review the deferred organization only when a concrete proposal is established with the user.
