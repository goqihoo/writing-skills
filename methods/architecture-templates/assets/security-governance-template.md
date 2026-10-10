# [Security Governance]

**Status:** [Draft / Reviewed / Superseded]

**Evidence baseline:** [Date, sources and verification limits]

## Security scope

[Protected outcomes, boundaries and security assumptions. Include architecture-significant protection mechanisms while linking executable configuration to its implementation owner.]

## Assets and trust boundaries

[Explain what must be protected, the threats that change architecture decisions and the trust crossings they exploit. Connect each material threat to the required protection and the limits of the assumed model.]

[Figure: protected assets and trust crossings]

## Identity and authority

[Explain how identities acquire privileges, how scope and approval constrain actions, and why duties are separated. Show how authority reaches the enforcement point; use a role/action matrix only for repeated access decisions.]

## Protection mechanisms and realization

[Derive relevant technical protections from the threats and trust crossings. Explain isolation, data protection, key and secret lifecycles or other applicable mechanisms, their enforcing application and infrastructure owners, and their failure limits. Trace a representative threat through prevention, detection and response; link detailed network, data or component mechanisms. Keep these choices distinct from the governance of policy changes.]

## Security state and commands

[Explain how security policy or command versions reach their owning executors, how freshness and scope are established and what happens when validity cannot be confirmed.]

## Security flows

[Walk a protected action or policy change through authentication, authorization, enforcement and evidence. Include a relevant denied or compromised-authority case and explain the emergency-control limits.]

## Evidence and failure

[Attributable evidence, stale or conflicting policy, bypass, compromised authority and recovery]

## Patterns and tradeoffs

[Explain the relevant alternatives under the same scenario and assumptions: how each mechanism works, what it gains, what it costs and where it fails. Use a compact comparison table only when several choices share meaningful criteria; state the conditional selection and review trigger in prose.]

## Validation

[Explain how the principal claims could be established or challenged. Connect a concrete example, experiment, review or operational observation to the claim it tests, the expected signal and the limits of the evidence. Distinguish illustrative reasoning, sourced observations and proposed checks.]

## Application and adaptation

[Explain the assumptions that make the design valid, the changes that require adaptation and the consequences for dependent owners. Identify prerequisites, compatibility or transition limits, and evidence needed before relying on the changed model. Bound reusable claims with an unsuitable context where relevant.]

## Related documents

[Link parent, child, cross-view and source documents with a short explanation of what each contributes. Keep a shared mechanism in its owning document and point to it from dependents.]
