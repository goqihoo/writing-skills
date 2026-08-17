# 公司 Product 与 Technical 文档体系

Status: ready-for-agent

## Problem Statement

Scribe 当前把 `Product Knowledge` 同时用于通用产品知识和某个具体产品的文档，把 `Technical Knowledge` 同时用于通用技术知识、项目交付架构和具体系统事实。这使知识的适用范围、公司承诺、项目记录和机器权威彼此混淆，也让 Product 与 Technical 技能采用了不同的抽象层级。

现有 Product 体系主要围绕单个产品和七个默认目录构建，不能表达一家公司的产品组合、多个产品和产品治理。现有 Technical 体系则以项目或代码仓库的交付架构为中心，不能为一家公司建立技术战略、技术架构、系统版图和技术治理目录。部分事件型目录被预先创建，容易产生空目录和陈旧占位文档。

技能目录还倾向于为每一种标准文档创建一个公共技能。随着 Product 和 Technical 文档类型增加，公共调用面会持续膨胀。技能之间的依赖也必须保持完全显式，不能因为建立协调技能或公共写作技能而引入自动调用。

用户需要 Scribe 建立一套统一的公司文档模型：把非特定公司的通用 Knowledge 与特定公司的 Product Documentation、Technical Documentation 分开；让 Product 和 Technical 都能为一家公司生成默认目录和标准文档；默认创建高频稳定职责，按需创建类型扩展和事件集合；用少量公共技能覆盖高频任务，并通过内部文档类型覆盖其他标准文档。

## Solution

Scribe 将采用以权威范围、主题和技能角色相互正交的模型：

- `Knowledge` 保存不绑定具体公司的通用知识，其主题可以是 Domain、Product、Technical、Architecture 或其他领域。
- `Company Documentation` 保存由一家特定公司拥有并维护的事实、标准和治理记录，其中包含 `Product Documentation` 与 `Technical Documentation`。
- `Project Documentation` 保存客户、合同、项目、计划、交付状态和验收记录，但本期不建设相应目录或技能。
- 协调由 `reason-*`、`assess-*`、`structure-*` 等动词表达，不建立 `delivery/` 或 `coordination/` 内容分类。

公司文档的默认结构为：

```text
{Company}/
├── README.md
├── Product/
│   ├── README.md
│   ├── Portfolio/
│   ├── Governance/
│   └── Products/
│       └── {Product}/
│           ├── README.md
│           ├── Definition/
│           ├── Capabilities/
│           ├── Planning/
│           └── Measurement/
└── Technical/
    ├── README.md
    ├── Strategy/
    ├── Architecture/
    ├── Systems/
    └── Governance/
```

`Product/` 与 `Technical/` 可以独立生成并共享公司根目录和导航约定。独立公司文档目录使用首字母大写；代码仓库的目录约定不属于本期生成范围。

目录采用三种物化规则：

- `Stable Responsibility`：在已接受的公司、产品或技术范围内持续存在，默认获得目录和责任 README。
- `Type Extension`：只有在独立所有权、治理或导航需求得到证明时创建。
- `Event Collection`：只有在第一份真实事件文档产生时创建。

Product 的类型扩展包括 `Solutions/` 与 `Experience/`；事件集合包括 `Initiatives/`、`Evidence/`、`Releases/` 与 `Decisions/`。Technical 的类型扩展包括 `Platforms/`、`Engineering/`、`Data/`、`Security/`、`Quality/` 与 `Operations/`；事件集合放在相应稳定职责下，例如 Architecture Decisions、Governance Exceptions 和 Operations Incidents。

公共技能只在任务跨公司或跨产品反复发生、具有独立推理或工作流，并且具有可检查完成条件时创建。低频标准文档作为 `write-product-doc` 或 `write-technical-doc` 的内部文档类型。所有公共技能保持用户显式调用；任何技能发现缺少依赖时必须停止并返回完整的显式调用，不能自动执行另一个技能。`draw-diagram` 继续作为跨 Knowledge、Product 和 Technical 的 Visual 技能，并且只有用户显式调用时才生成图表。

## User Stories

1. 作为 Scribe 使用者，我希望区分通用 Knowledge 与公司文档，从而不会把一般方法误认为公司的正式承诺。
2. 作为知识作者，我希望 Product Knowledge 保持跨公司适用，从而可以在不同产品组织中复用同一套概念和方法。
3. 作为技术知识作者，我希望 Technical Knowledge 保持跨公司和跨系统适用，从而不会把某家公司的技术选择写成普遍事实。
4. 作为公司文档负责人，我希望 Product Documentation 的权威明确属于一家特定公司，从而可以判断谁负责更新和批准内容。
5. 作为公司文档负责人，我希望 Technical Documentation 的权威明确属于一家特定公司，从而可以治理技术战略、架构、系统和标准。
6. 作为项目负责人，我希望 Project Documentation 与公司 Product、Technical 文档分开，从而不会让客户或合同记录污染公司的长期事实。
7. 作为 Scribe 使用者，我希望协调能力由动词技能表达，从而不必理解含义模糊的 Delivery 或 Coordination 内容目录。
8. 作为 Scribe 维护者，我希望技能分类与内容权威范围分开，从而可以同时表达技能角色、知识主题和文档寿命。
9. 作为公司文档负责人，我希望用一个公司根目录导航 Product 与 Technical，从而获得统一入口。
10. 作为只需要产品体系的公司，我希望可以独立生成 Product 目录，从而不必创建没有内容的 Technical 目录。
11. 作为只需要技术体系的公司，我希望可以独立生成 Technical 目录，从而不必创建没有内容的 Product 目录。
12. 作为文档读者，我希望公司根 README 只承担导航和责任说明，从而不会重复下级文档正文。
13. 作为产品负责人，我希望 Product 根目录表达一家公司的产品组合，而不是把公司误当成一个产品。
14. 作为产品组合负责人，我希望 Portfolio 有稳定目录，从而可以治理产品、产品线、投资关系和生命周期。
15. 作为产品治理负责人，我希望 Governance 有稳定目录，从而可以维护产品决策权、运行方式和共同规则。
16. 作为公司产品读者，我希望 Products 是已接受产品的登记入口，从而可以发现每个正式产品的文档。
17. 作为多产品公司，我希望每个产品拥有自己的子目录，从而避免不同产品的事实和生命周期混在一起。
18. 作为产品经理，我希望每个产品默认拥有 Definition 目录，从而可以找到产品边界、用户、术语和当前定义。
19. 作为产品架构负责人，我希望每个产品默认拥有 Capabilities 目录，从而可以找到稳定能力模型和能力细节。
20. 作为产品规划负责人，我希望每个产品默认拥有 Planning 目录，从而可以组织战略、路线图和已接受变更的计划。
21. 作为产品分析负责人，我希望每个产品默认拥有 Measurement 目录，从而可以维护指标语义和产品测量模型。
22. 作为产品负责人，我希望产品线是 Portfolio 的分类视图而不是强制物理父目录，从而允许一个产品出现在多个产品线中。
23. 作为产品经理，我希望 Solutions 只在产品确实存在可重复方案组合时创建，从而避免所有产品都背负空目录。
24. 作为体验负责人，我希望 Experience 只在体验职责具有独立治理和导航需要时创建，从而让目录反映真实组织责任。
25. 作为产品经理，我希望 Initiatives 在第一项真实产品变更出现时创建，从而不预建事件集合。
26. 作为研究负责人，我希望 Evidence 在第一份真实证据记录出现时创建，从而不生成空的研究目录。
27. 作为发布负责人，我希望 Releases 在第一次真实发布活动出现时创建，从而让发布集合与实际事件一致。
28. 作为产品决策者，我希望 Decisions 在第一项需要持久解释的产品决策出现时创建，从而避免把普通事实都记录成决策。
29. 作为产品治理负责人，我希望 Product Lifecycle 是跨现有文档的治理视图，从而不会形成第二套生命周期目录树。
30. 作为产品决策者，我希望继续使用 Product Lifecycle Assessment，从而可以评估当前决策、证据和文档覆盖。
31. 作为公司产品负责人，我希望建立公司 Product 目录时不强制先做单个产品生命周期评估，从而可以先建立组合级结构。
32. 作为产品文档负责人，我希望仅对已接受的产品创建产品子目录，从而不把候选概念伪装成正式产品。
33. 作为技术负责人，我希望 Technical 根目录表达整家公司的技术能力和系统版图，从而不是某个项目或代码仓库的目录。
34. 作为技术战略负责人，我希望 Strategy 有稳定目录，从而可以维护公司的技术方向、原则和路线图。
35. 作为企业架构负责人，我希望 Architecture 有稳定目录，从而可以维护公司的技术架构、边界、关系和演进约束。
36. 作为系统治理负责人，我希望 Systems 有稳定目录，从而可以发现系统版图、系统档案、所有权和生命周期。
37. 作为技术治理负责人，我希望 Governance 有稳定目录，从而可以维护技术运行模式、标准、例外和决策权。
38. 作为平台负责人，我希望 Platforms 只在平台形成独立技术职责时创建，从而不把每个共享组件都提升为平台目录。
39. 作为工程负责人，我希望 Engineering 只在工程实践具有独立治理时创建，从而让目录与实际责任匹配。
40. 作为数据负责人，我希望 Data 只在数据治理形成独立所有权时创建，从而避免复制数据库和模式信息。
41. 作为安全负责人，我希望 Security 只在安全治理需要独立导航时创建，从而同时保留小型公司的简洁结构。
42. 作为质量负责人，我希望 Quality 只在质量模型和持续治理独立存在时创建，从而不复制普通测试结果。
43. 作为运维负责人，我希望 Operations 只在运行和恢复责任独立存在时创建，从而不为不可部署的技术对象制造目录。
44. 作为架构师，我希望 Architecture Decisions 在第一项符合条件的架构决策出现时创建，从而不预建事件目录。
45. 作为治理负责人，我希望 Governance Exceptions 在第一项真实例外出现时创建，从而让例外集合反映实际治理事件。
46. 作为运维负责人，我希望 Operations Incidents 在第一项真实事故出现时创建，从而不把事故目录当成稳定职责。
47. 作为系统所有者，我希望 System Profile 只保留目的、所有权、生命周期、关键关系和权威链接，从而不复制代码仓库中的实现细节。
48. 作为开发人员，我希望字段、行为、配置和模式等机器权威继续由代码或可执行定义持有，从而避免公司文档形成影子事实。
49. 作为文档读者，我希望每个稳定目录都有责任 README，从而知道什么内容属于这里、什么权威在别处。
50. 作为文档维护者，我希望责任 README 只链接真实存在的文档，从而不会展示虚假的计划内容。
51. 作为公司文档负责人，我希望缺乏事实时不生成虚假的战略、路线图、标准或系统档案，从而保持文档可信。
52. 作为结构规划者，我希望简单脚手架可以在执行中完成边界判断，从而不必总是创建永久 Assessment 文件。
53. 作为审计者，我希望边界争议、类型扩展或迁移决定可以保存 Product Assessment 或 Technical Assessment，从而保留决策依据。
54. 作为 Scribe 使用者，我希望 Assessment 与 Readiness 和生命周期事件明确区分，从而不会产生新的状态文档体系。
55. 作为 Scribe 使用者，我希望公共技能数量保持可记忆，从而可以通过少量明确接口完成公司文档任务。
56. 作为 Scribe 维护者，我希望只有高频且具有独立工作流和完成条件的任务成为公共技能，从而防止技能目录随模板数量膨胀。
57. 作为 Scribe 维护者，我希望文档标题或目录本身不足以证明需要新技能，从而让技能边界保持稳定。
58. 作为产品文档作者，我希望常见但低频的产品文档由 write-product-doc 路由，从而不必记住每一种文档的技能名。
59. 作为技术文档作者，我希望常见但低频的技术文档由 write-technical-doc 路由，从而不必记住每一种文档的技能名。
60. 作为产品负责人，我希望产品战略继续有独立技能，从而保留其独立选择逻辑和完成标准。
61. 作为产品架构负责人，我希望产品能力图继续有独立技能，从而保留能力边界、关系和权威推理。
62. 作为产品规划负责人，我希望产品路线图继续有独立技能，从而保留结果、赌注、依赖和决策门的推理。
63. 作为产品经理，我希望 PRD 继续有独立技能，从而可以明确一个产品变更的行为和验收。
64. 作为产品分析负责人，我希望产品指标设计继续有独立技能，从而可以维护准确的语义、护栏和治理。
65. 作为产品文档作者，我希望 Product Portfolio、Products Registry、Product Operating Model 和 Product Governance 是公共写作技能的内部类型，从而避免新增低频技能。
66. 作为产品文档作者，我希望 Product Solution、Product Release Plan 和 Product Review 成为内部类型，从而减少公共技能数量但保留标准模板。
67. 作为技术负责人，我希望 reason-technical 可以判断公司技术范围、所有权和类型扩展，从而为结构和写作提供一致边界。
68. 作为技术文档负责人，我希望 structure-technical-docs 可以规划、脚手架、审计和迁移公司技术文档，从而不使用代码仓库结构。
69. 作为技术文档作者，我希望 write-technical-doc 可以路由技术战略、路线图、系统版图、系统档案、治理和标准，从而通过一个公共入口覆盖常见类型。
70. 作为企业架构负责人，我希望 write-technical-architecture 保持独立技能，从而应用专门的架构推理和完成检查。
71. 作为技术文档作者，我希望平台、工程、数据、安全、质量和运营文档作为内部类型，从而按公司需要扩展而不增加公共技能。
72. 作为治理记录作者，我希望架构决策、治理例外和事故记录作为内部事件类型，从而在首次真实事件时创建相应集合。
73. 作为知识作者，我希望通用 Product Knowledge 与 Technical Knowledge 继续由 write-knowledge 负责，从而不为分类对称创建重复技能。
74. 作为架构知识作者，我希望 write-architecture-knowledge 保留独立技能，从而可以使用专门架构方法产生可复用知识。
75. 作为公司技术架构作者，我希望 write-technical-architecture 与 Architecture Knowledge 明确分开，从而不会把一般选项变成公司承诺。
76. 作为 Scribe 使用者，我希望项目型 Delivery Architecture 暂时退出 Technical 技能，从而让 Technical 只服务公司文档范围。
77. 作为 Scribe 使用者，我希望所有技能只能由我显式调用，从而始终知道哪些流程会运行。
78. 作为 Scribe 使用者，我希望组合工作流中每个依赖技能都由我明确写出，从而不会发生隐式技能链。
79. 作为 Scribe 使用者，我希望技能发现缺少依赖时停止并返回完整调用，从而可以自行决定是否继续。
80. 作为 Scribe 维护者，我希望所有技能的 frontmatter 和客户端策略都禁止隐式调用，从而让不同运行环境保持一致。
81. 作为 Scribe 使用者，我希望 ask-scribe 只解释和推荐技能，从而不会在咨询时修改文件或生成其他技能的制品。
82. 作为产品或技术文档作者，我希望内部文档类型选择不被误认为技能调用，从而允许公共写作技能完成自身的路由职责。
83. 作为图表作者，我希望 draw-diagram 继续跨 Product、Technical 和 Knowledge 使用，从而不重复建设画图技能。
84. 作为 Scribe 使用者，我希望只有显式包含 draw-diagram 时才生成图表，从而保留对视觉产出的控制。
85. 作为文档作者，我希望在需要专门处理读者流、语言和格式质量时可以显式组合 write-doc，而制品技能本身仍能独立完成正文。
86. 作为架构作者，我希望技术架构显式组合 reason-technical 与 reason-architecture，并可按需组合 write-doc 或 draw-diagram，从而让必需职责和可选处理清晰可见。
87. 作为 Scribe 维护者，我希望技能库有一份总架构文档，从而统一说明分类、准入、组合和显式调用原则。
88. 作为 Product 技能维护者，我希望产品架构文档使用 Product Documentation 命名，从而不再把公司产品文档叫作 Product Knowledge。
89. 作为 Technical 技能维护者，我希望有公司技术文档架构说明，从而固定 Technical 目录、技能和内部类型的边界。
90. 作为 Domain Knowledge 使用者，我希望现有 Domain Knowledge 架构保持独立，从而不受公司 Product/Technical 重构影响。
91. 作为 Scribe 维护者，我希望旧技能名称和兼容包装原子移除，从而避免两个名称指向同一责任。
92. 作为 Scribe 维护者，我希望插件、README、Ask Scribe 和市场元数据同时更新，从而让所有公开入口展示同一技能体系。
93. 作为 Scribe 使用者，我希望版本号反映破坏性技能迁移，从而知道需要更新调用方式。
94. 作为 Scribe 维护者，我希望测试验证用户可见契约而不是内部步骤措辞，从而允许后续优化技能实现。
95. 作为 Scribe 维护者，我希望 Product 与 Technical 使用同一套稳定职责、类型扩展和事件集合规则，从而减少体系偏差。
96. 作为知识库使用者，我希望能阅读一份面向人的划分依据说明，从而理解为什么公司文档与通用知识采用不同体系。

## Implementation Decisions

- 将 Knowledge、Company Documentation 与 Project Documentation 定义为三个不同权威范围。Domain、Product 与 Technical 是 Knowledge 的主题，也可以是 Company Documentation 的主题，但不能用相同名称混淆适用范围。
- 将 Product Documentation 定义为一家公司如何定义、组织、治理、演进、度量和运营其商业产品的公司文档。
- 将 Technical Documentation 定义为一家公司如何组织、治理、演进、保护和运营其技术能力与系统的公司文档。
- 本期生成目标是公司的 Product/Technical 文档目录和标准文档，不是代码仓库、软件项目或单个交付项目的文档结构。
- 公司根可以同时包含 Product 与 Technical，也允许二者独立物化。公司根 README 负责整体责任和导航。
- 独立公司文档目录使用首字母大写。此规则不扩展到代码仓库目录。
- Product 公司级稳定核心由 Portfolio、Governance 与 Products 组成。
- Products 下面按已接受产品创建子目录；产品线保持 Portfolio 分类视图，不作为默认物理父目录。
- 单个产品的稳定核心由 Definition、Capabilities、Planning 与 Measurement 组成。
- Product 的 Solutions 与 Experience 是 Type Extension；Initiatives、Evidence、Releases 与 Decisions 是 Event Collection。
- Technical 稳定核心由 Strategy、Architecture、Systems 与 Governance 组成。
- Technical 的 Platforms、Engineering、Data、Security、Quality 与 Operations 是 Type Extension。
- Technical 事件集合嵌入相应责任：Architecture Decisions、Governance Exceptions 与 Operations Incidents。只有拥有对应父责任且出现首个事件时才创建。
- 每个 Stable Responsibility 默认获得目录和 Responsibility README。README 只记录责任、所有权、边界、当前导航与外部权威链接。
- 脚手架不根据模板制造业务事实。缺少输入时不创建战略、路线图、标准、系统档案或其他看似权威的正文。
- 结构技能支持 proposal、scaffold、audit 与 approved migration。移动、重命名、合并、删除或覆盖现有材料前继续要求明确批准。
- reason-product 扩展为可以判断公司产品组合、产品线、产品和产品下级边界，同时继续为单个产品提供 Product Assessment。
- assess-product-lifecycle 保留现有名称和职责；Readiness 不替代 Lifecycle，也不创建 Readiness 文档或技能。
- 新增 reason-technical，负责公司技术范围、技术版图、所有权、权威边界、稳定职责和 Type Extension 判断，不负责代码仓库设计或项目 readiness。
- Product Assessment 与 Technical Assessment 只在边界争议、类型扩展、审计或迁移需要长期可追踪时持久化；简单脚手架可以只在执行中完成判断。
- Public Skill 只有在任务跨公司或产品反复发生、具有独立推理或工作流、并具有可检查完成条件时创建。目录、文档标题、重要性或模板不足以单独证明公共技能成立。
- Product 公共技能包括 reason-product、assess-product-lifecycle、structure-product-docs、write-product-doc、write-product-strategy、map-product-capabilities、write-product-roadmap、write-prd 与 design-product-metrics。
- write-product-doc 是 Product Common Writer。其公司级内部类型包括 Product 导航、Product Portfolio、Products Registry、Product Operating Model 与 Product Governance。
- write-product-doc 的单产品内部类型包括 Product Overview/Definition、Users and Roles、Product Terminology、Lifecycle Map、Capability Detail、Journey/Product Behavior、Product Solution、Initiative Record、Evidence Record、Product Decision、Product Release Plan、Release Notes 与 Product Review。
- write-product-doc 将 Product Strategy、Capability Map、Product Roadmap、PRD 与 Product Metric System 路由到各自公共技能，并返回完整显式调用而不是执行它们。
- Technical 首期公共技能只包括 reason-technical、structure-technical-docs、write-technical-doc 与 write-technical-architecture。
- write-technical-doc 是 Technical Common Writer。稳定核心内部类型包括 Technical 导航、Technical Strategy、Technical Roadmap、System Landscape、System Profile、Technical Operating Model、Technical Governance 与 Technical Standard。
- write-technical-doc 的 Type Extension 内部类型包括 Platform Definition、Engineering Practice、Data Governance、Security Governance、Quality Model 与 Operations Model。
- write-technical-doc 的事件内部类型包括 Architecture Decision、Governance Exception 与 Incident Record/Review。
- write-technical-architecture 独立拥有公司级技术架构，覆盖技术版图的原则、结构、边界、关系、约束和演进；它不生成项目交付架构或一个代码仓库的详细设计。
- System Profile 保留公司所需的目的、所有权、生命周期、关键依赖、治理状态和权威链接。详细 System Architecture、接口定义、部署、配置和实现留在下游权威位置。
- Machine Authority 继续拥有字段、协议、行为、模式、迁移、配置和测试级事实；公司文档通过链接和人类语义导航引用它们。
- write-knowledge 继续覆盖通用 Product Knowledge 与 Technical Knowledge；不添加仅为分类对称存在的 Product/Technical Knowledge 写作或结构技能。
- 将通用架构知识技能重命名为 write-architecture-knowledge，并继续组合 reason-architecture。
- 将现有项目型交付架构技能替换为公司级 write-technical-architecture。项目型架构能力留待未来 Project Documentation 体系重新设计。
- 将 Product Solution、Product Release Plan 与 Product Review 的现有独立技能合并为 write-product-doc 的内部类型。
- 删除没有正式实现或不再属于当前范围的 Product Requirements、Delivery Architecture Design、Decision Record 与 Technical Design 技能占位目录。
- 所有重命名和删除原子完成，不提供旧名称的兼容包装。
- 每个 SKILL 都设置 `disable-model-invocation: true`，每个 OpenAI skill metadata 都设置 `allow_implicit_invocation: false`。
- 用户必须显式命名组合工作流中的每个 Public Skill。技能不得调用其他技能；发现缺失依赖时停止并返回完整的 ready-to-type invocation。
- Common Writer 在自身内部选择 Internal Document Type 不构成技能调用，也不需要把每个内部类型暴露为用户调用名。
- ask-scribe 继续只解释 Scribe 的技能、边界、组合和完整调用，不执行工作流、不修改文件、不生成其他技能的制品。
- write-doc 是可选的通用写作流程；制品技能不得把它作为创建、修订、审阅或呈现正文的强制依赖。
- draw-diagram 保留在 Visual 技能类别，跨 Knowledge、Product 和 Technical 使用。只有显式调用 draw-diagram 时才能创建图表；否则保留最小可用的文字或表格表达。
- 技能库内部建立总架构、Product Documentation 架构和 Technical Documentation 架构说明；Domain Knowledge 架构继续保留。旧的 Product Knowledge 架构名称被 Product Documentation 架构替代。
- 在用户的产品知识库中生成一份面向人的划分依据文档，解释通用 Knowledge、公司 Product/Technical 文档、Project 文档、稳定职责、类型扩展、事件集合和技能准入原则。该文档与技能库自身的架构说明分开。
- 更新所有公开说明、技能桶说明、Ask Scribe、插件清单、默认提示、marketplace metadata 与版本，使术语和技能清单一致。
- 发布版本为 0.6.0；Codex 构建版本在 0.6.0 基础上使用仓库既有的构建后缀约定。

## Testing Decisions

- 好的测试验证用户可以观察到的稳定契约：技能是否存在、名称是否一致、显式调用是否被强制、目录责任是否正确、路由边界是否明确、公开入口是否同步。测试不锁定技能内部步骤顺序或可自由改写的措辞。
- 使用一个最高层的 Company Documentation contract 作为主要新接缝，联合验证 Company、Product 与 Technical 的结构模型、Public Skill 清单、Internal Document Type 路由和架构说明。
- 将现有 Product Knowledge contract 重构为 Product Documentation contract，或者把其稳定检查并入 Company Documentation contract；移除对旧七目录核心和已合并公共技能的断言。
- Product 结构测试验证公司级 Portfolio/Governance/Products、单产品 Definition/Capabilities/Planning/Measurement、两个 Type Extension 和四个 Event Collection 的物化分类。
- Technical 结构测试验证 Strategy/Architecture/Systems/Governance、六个 Type Extension，以及事件集合只在对应责任下按需创建。
- Common Writer 测试验证全部已确认 Internal Document Type 有唯一模板或完成 profile，并验证独立公共制品被路由而不是吸收。
- 技能接口测试验证每个 Public Skill 都有 SKILL 与 OpenAI metadata、技能目录名与 frontmatter 名一致、默认提示显式包含自身技能名。
- 复用并加强显式调用 contract：自动发现全部技能，验证 SKILL 禁止 model invocation、metadata 禁止 implicit invocation，并验证公开组合提示显式列出依赖。
- 显式组合测试验证 ask-scribe 与各技能只返回调用，不使用表示自动执行其他技能的指令。Internal Document Type 路由被视为同一技能内部行为。
- 可选写作 contract 测试验证 write-doc 保留独立职责，同时其他制品技能不把它声明为强制依赖。
- 更新 architecture skill name contract，验证 write-architecture-knowledge 与 write-technical-architecture 的目录、frontmatter、显示名、默认提示和插件入口一致。
- 迁移测试验证旧架构技能名、三个被合并的 Product 公共技能、已删除占位技能及旧 Product Knowledge 架构名称不再出现在公开入口。
- 插件和导航测试验证根 README、技能桶 README、Ask Scribe、Claude manifest、Codex manifest 与 marketplace metadata 展示同一组公共技能和公司文档术语。
- 版本测试验证正式插件版本为 0.6.0，并允许 Codex manifest 使用约定的 0.6.0 构建后缀。
- Responsibility README 和模板 contract 只验证稳定责任、必需决策字段、权威链接与完成条件，不锁定具体自然语言。
- 结构 contract 验证默认 scaffold 不物化任何 Type Extension 或 Event Collection，不链接不存在的计划文档，也不创建无事实正文。
- 权威边界测试验证 Product/Technical 技能明确引用而不复制 Machine Authority、项目交付事实或通用 Knowledge。
- draw-diagram contract 继续验证 Visual 技能独立存在；Product 与 Technical 的推荐调用只有在需要图表时显式加入它，并且其他技能不隐式执行它。
- 使用仓库现有的技能快速验证、完整单元测试、脚本语法检查和差异检查作为最终验证层。

## Out of Scope

- 不设计或生成 Project Documentation 的默认目录、标准文档或公共技能。
- 不为客户项目、合同、交付计划、任务、状态或验收建立新技能。
- 不生成代码仓库内的技术文档目录，也不规定代码仓库目录大小写。
- 不把本仓库开发使用的 CONTEXT、ADR 或本地 issue tracker 路径当成 Scribe 为公司生成的 Technical 目录。
- 不从代码、配置、OpenAPI、数据库模式或部署定义自动生成公司技术文档结构。
- 不重新建设项目型 Delivery Architecture、Technical Design、Runbook 或 Interface Contract 公共技能。
- 不创建 Technical Readiness、Product Readiness、reason-readiness 或 assess-technical-readiness 技能和文档。
- 不用 Readiness 取代 Product Lifecycle Assessment。
- 不创建 Delivery 或 Coordination 顶层技能桶。
- 不为每个公司标准文档创建独立公共技能。
- 不创建仅为 Product/Technical 分类对称存在的通用知识技能。
- 不默认创建 Product 或 Technical 的 Type Extension 与 Event Collection。
- 不创建 Changes 顶层目录，也不把变更历史从版本控制或 issue tracker 复制到公司文档。
- 不复制代码、配置、schema、测试、运行参数或其他 Machine Authority 的详细事实。
- 不提供旧技能名称的弃用期、别名或兼容包装。
- 不允许技能自动调用、隐式调用或由其他技能代为执行。
- 不在未显式调用 draw-diagram 时生成图表。
- 不修改 Domain Knowledge 的现有 admission、structure 和 document contracts，除非统一术语需要最小同步。

## Further Notes

- 本规格取代此前把 Technical Documentation 解释为代码仓库或项目交付文档的方案。公司 Technical Documentation 是本期唯一技术生成目标。
- Product 与 Technical 都是 Company Documentation；Product Knowledge 与 Technical Knowledge 都是非特定公司的 Knowledge。名称中的 Knowledge 与 Documentation 必须作为受控词汇使用。
- 结构模型追求“有用的默认核心”，而不是最小到只剩单个文件，也不是一次创建所有未来可能目录。
- Product Initiative 表示改变共享产品行为的公司产品活动；Delivery Project 表示客户、合同、计划、任务和验收。两者保持不同权威范围。
- `ready-for-agent` 表示需求和测试接缝已经确认，可以进入测试先行的实现阶段。
