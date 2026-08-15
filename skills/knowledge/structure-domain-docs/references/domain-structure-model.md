# Domain structure model

Use this model after local repository rules. It defines stable knowledge responsibilities; it does not require every domain to materialize every path.

## Canonical knowledge forms

| Default path | Reader question | Owns | Excludes |
| --- | --- | --- | --- |
| `README.md` | What is this domain and how should I read it? | Boundary, map, reading path, coverage, navigation | Full explanations and reference data |
| `{领域名称}本质.md` | Why must this domain exist? | First-principles cognition anchor: realities, objects, participants, essence, constraints, capability space, tensions | Exhaustive terminology, procedures, catalogs, implementation commitments |
| `术语与概念关系.md` | What do the domain's words mean here? | Preferred terms, aliases, definitions, distinctions, broader, narrower, and related concepts | Object lifecycle detail and causal explanations |
| `核心对象与生命周期.md` | What has identity or state, and how does it change? | Domain objects, identity, ownership, states, transitions, invariants | Software modules and organization charts |
| `参与者、职责与规则.md` | Who may act, decide, benefit, or bear harm? | Participants, authority, duties, incentives, information, rules, evidence, escalation | Company-specific job descriptions and procedures |
| `机制/` | Why and how does an outcome occur? | Causal chains, feedback, propagation, controls, failure, recovery | Step-by-step practitioner instructions |
| `能力与解法/` | What response families are possible? | Necessary capability families, reusable patterns, selection conditions, tradeoffs, real-system coordinates | Product commitments and project-specific solution choices |
| `方法与实践/` | How should a practitioner perform a repeatable task? | Inputs, steps, decision branches, outputs, validation, pitfalls | Explanation that does not enable the task |
| `案例与失败/` | Does the model survive contact with reality? | Observed cases, incidents, counterexamples, timelines, causal analysis, lessons and limits | Unsupported anecdotes and generic advice |
| `参考/` | What stable fact or rule must readers look up? | Standards, classifications, metrics, data definitions, source indexes, version and authority | Long causal arguments or project decisions |

The default Chinese names apply only when they match local language rules. Translate the names while preserving the responsibilities in another-language knowledge base.

## Small domain

Use knowledge form directly at the domain root while each form needs only one document:

```text
{领域名称}/
├── README.md
├── {领域名称}本质.md
├── 术语与概念关系.md
├── 核心对象与生命周期.md
├── 参与者、职责与规则.md
├── 机制/
├── 能力与解法/
├── 方法与实践/
├── 案例与失败/
└── 参考/
```

Keep a knowledge form as a single root file until it has several independently useful children or needs its own navigation. For example, retain `术语与概念关系.md` as one file before creating a `术语与概念关系/` directory.

## Complex domain

Use shared root knowledge followed by stable subdomains:

```text
{领域名称}/
├── README.md
├── {领域名称}本质.md
├── 共享语义/
│   ├── 术语与概念关系.md
│   └── 跨子域对象.md
├── {子域一}/
│   ├── README.md
│   ├── 机制/
│   ├── 能力与解法/
│   ├── 方法与实践/
│   ├── 案例与失败/
│   └── 参考/
└── {子域二}/
    └── ...
```

At the domain root, siblings represent shared material or subdomains. Inside one subdomain, siblings represent knowledge forms. This preserves one dimension per directory level.

A subdomain earns its own `{子域名称}本质.md` only when it has an independent minimum purpose, domain realities, objects, and boundary. Directory size alone is not enough.

## Materialization rules

- Do not create empty directories by default. Record a missing or planned knowledge form in the root README until real content exists.
- Create the root `README.md` and `{领域名称}本质.md` first when starting a durable domain set, unless the user asks for structure only or the evidence needed for the essence is not ready.
- Create semantic documents when inconsistent language, object identity, state, authority, or rules already impede understanding.
- Create a directory when a knowledge form has several independent documents, needs navigation, or has a stable boundary of its own.
- Link to one canonical explanation from secondary contexts instead of maintaining equivalent prose in several files.
- Keep company policy, product behavior, software implementation, customer delivery, and business-specific lifecycle in their owning repository areas.

## Default reading path

1. `README.md` — establish scope and choose a route.
2. `{领域名称}本质.md` — understand why the domain exists and how to analyze it.
3. `术语与概念关系.md` and `核心对象与生命周期.md` — learn the language and state model.
4. `参与者、职责与规则.md` — understand authority, incentives, obligations, and conflict.
5. `机制/` — follow causal explanations.
6. `能力与解法/` and `方法与实践/` — compare responses and perform work.
7. `案例与失败/` — test the model against evidence and counterexamples.
8. `参考/` — look up stable facts, definitions, and authorities.

Readers may enter through a task, case, or reference link. The README should support those routes without forcing everyone through every document.
