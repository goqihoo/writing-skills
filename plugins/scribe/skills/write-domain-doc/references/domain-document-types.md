# Domain document types

This is the single source of truth for the ten common domain document responsibilities. `$Structure Domain Docs` uses the types as a coverage model; `$Write Domain Doc` uses them to select one artifact contract. Select from the user prompt and explicit instructions first. Use filename and title, directory, primary reader question, content, and sibling conventions only as confirmation or as fallback when the prompt is underspecified. Read the matching template whenever one exists, and read no unrelated template.

## Structure strength

### Strict schema

Use an exact heading sequence when cross-domain comparability and reasoning traceability are part of the artifact's interface.

- **Domain essence:** Read `essence-document-module.md` and `../assets/essence-article-template.md`. The internal module is the single source of truth for the fixed derivation and completion contract.

### Stable lookup schema

Preserve the required fields and section responsibilities. Adapt layout, add subject-specific subsections, or omit a field only when it truly does not apply and the omission is visible.

- **Terminology and concept relationships:** `../assets/terminology-and-concept-relationships-template.md`
- **Core objects and lifecycle:** `../assets/core-objects-and-lifecycle-template.md`
- **Participants, responsibilities, and rules:** `../assets/participants-responsibilities-and-rules-template.md`
- **Domain map and README:** `../assets/domain-readme-template.md`
- **Reference:** `../assets/reference-template.md`

### Stable reasoning sequence

Preserve the reasoning or action order. Subject-specific headings may replace generic wording when every required reasoning job remains visible.

- **Mechanism:** `../assets/mechanism-template.md`
- **Capability and solution space:** `../assets/capability-and-solution-template.md`
- **Method and practice:** `../assets/method-and-practice-template.md`
- **Case and failure:** `../assets/case-and-failure-template.md`

## Routing table

| Artifact | Strong filename or path signals | Primary reader question | Required distinction |
| --- | --- | --- | --- |
| Domain map and README | `README.md` at a domain or subdomain root | What does this domain contain, and how should I navigate it? | Current linked content versus planned unlinked coverage |
| Domain essence | `{领域}本质.md`, `{子域}本质.md` | Why must this domain exist, and how can I analyze a new problem? | Essence versus implementation and adjacent-domain ownership |
| Terminology and concept relationships | `术语与概念关系.md`, `概念模型.md`, `术语表.md` | What does each term mean here, and how do the concepts relate? | Concept versus label; preferred term versus alias |
| Core objects and lifecycle | `核心对象与生命周期.md`, `对象与状态.md` | Which objects or matters vary independently, how do their states change, and when is a domain event complete? | Tracked item versus abstract concept; transition evidence versus participant authority |
| Participants, responsibilities, and rules | `参与者、职责与规则.md`, `角色与规则.md` | Who may act or decide, under what rule, and with what evidence? | Domain authority versus company job description |
| Mechanism | `机制/`, `*机制.md`, `*原理.md` | Why and through what causal chain does the result occur? | Causal explanation versus practitioner steps |
| Capability and solution space | `能力与解法/`, `能力空间.md`, `模式与决策.md` | What reusable response families exist, and when should each be chosen? | Necessary capability versus optional implementation or product promise |
| Method and practice | `方法与实践/`, `*方法.md`, `*指南.md` | How does a practitioner complete and verify a repeatable task? | Action sequence versus general explanation |
| Case and failure | `案例与失败/`, `*案例.md`, `*事故.md`, `*复盘.md` | What happened, why, and what conclusion transfers beyond this case? | Observed fact versus interpretation and hindsight |
| Reference | `参考/`, `*参考.md`, `*字典.md`, `*分类.md`, `*指标.md` | What stable fact, rule, field, or authority must I look up? | Authoritative source versus explanatory commentary |

## Boundary routes

- Route directory design, coverage planning, scaffolding, and domain navigation to `$Structure Domain Docs`.
- Route a reusable architecture document whose main question is ownership, contracts, controls, runtime failure, validation, or evolution to `$Write Arch Knowledge`.
- Return a ready-to-type explicit invocation using `$Write Knowledge` for a general concept, mental model, comparison, or explanation that does not match these common domain artifacts.
- Keep business lifecycle, product commitments, technical implementation, company policy, and project-specific decisions in their owning content classes even when they use domain knowledge.
