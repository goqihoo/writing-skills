---
name: reason-domain
description: Assess whether a subject forms a reusable professional domain and record its boundary, relationships, knowledge ownership, subdomain decisions, maturity, and review triggers.
disable-model-invocation: true
---

# Reason About Domains

Decide whether a proposed knowledge boundary is real before a directory or document makes it look real.

## Workflow

1. Apply `$write-doc` to the assessment.
2. Read repository instructions, the domain-root README, the candidate domain README when present, and one or two healthy sibling domains. Record the local terms and decisions that must survive.
3. Read `references/domain-reasoning-method.md` completely.
4. **Establish the evidence.** Identify the candidate subject, available material, intended reuse, current owner, and the request being decided. Separate observed facts from interpretations and missing evidence.
5. **Run admission.** Test minimum purpose, core objects or activities, shared language and constraints, change authority, boundary and handoffs, and reusability. Return `Accept`, `Do not accept`, or `Needs evidence`; do not repair a failed candidate by inventing a directory.
6. **Resolve relationships.** Classify each supported relationship as parent or child, related, or handoff. Test every proposed subdomain independently and keep related subjects linked rather than nested.
7. **Assign knowledge ownership.** Give each material one primary content class and explain what can change its truth. Record a classification gap when no current home is honest.
8. **Record maturity and change.** Assign maturity only after admission succeeds. Name the evidence, authority, ownership conflict, or boundary change that would trigger review.
9. **Deliver the handoff.** Use `assets/domain-assessment-template.md`. Preserve unresolved material choices instead of hiding them in a confident domain label.
10. **Verify the decision.** Confirm every conclusion traces to evidence, every exclusion has a destination, only parent-or-child relationships imply nesting, and a downstream skill can use the assessment without redoing domain admission.

## Boundaries

- Own domain admission, boundary, relationships, subdomain validity, high-level knowledge ownership, maturity, and review triggers.
- Let `$structure-domain-docs` own inventory, directory scale, materialization, navigation, scaffolding, and structure migrations.
- Let `$write-domain-doc` own the structure and content of one common domain document.
- Let `$structure-docs` own repository-wide placement across business, domain, product, company, project, technical, and reference content.
- Let product, architecture, company, and project skills own commitments whose truth changes with their corresponding product, system, organization, or delivery.

## Completion test

The work is complete only when the assessment gives a supported admission decision, a usable boundary, explicit exclusions and destinations, evidenced relationships, tested subdomains, one primary content class per assessed material, maturity or a reason it cannot be assigned, review triggers, and visible unresolved questions.
