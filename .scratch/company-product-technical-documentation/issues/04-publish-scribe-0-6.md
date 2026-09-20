# 04 — 发布统一的 Scribe 0.6 技能目录

**What to build:** 把已经完成的 Product 与 Technical 体系发布为一个一致、可安装、可解释的 Scribe 0.6 技能目录，让用户从 Ask Scribe、README、架构说明或客户端入口看到同一套术语、技能、组合方式和显式调用规则。

**Blocked by:** 02 — 完成公司 Product Documentation 体系；03 — 完成公司 Technical Documentation 与架构体系

**Status:** wontfix

- [ ] Scribe 总架构说明统一记录 Knowledge、Company Documentation、Project Documentation、技能角色、物化规则和公共技能准入原则。
- [ ] Product Documentation、Technical Documentation 与 Domain Knowledge 分别拥有边界清晰的技能架构说明，旧 Product Knowledge 架构名称不再公开出现。
- [ ] Ask Scribe 能解释完整的 Knowledge、Product、Technical 与 Visual 技能体系，并只返回用户可显式执行的完整调用。
- [ ] 根说明、各技能桶说明、客户端插件清单、默认提示和 marketplace metadata 展示完全一致的公共技能集合。
- [ ] 所有旧技能名、旧路径、已合并技能和空占位技能从公开入口与契约中消失，不存在兼容包装。
- [ ] 每个技能都有匹配的用户界面元数据，唯一显示名映射到稳定的目录名与 Skill ID，默认提示优先使用显示名。
- [ ] 每个技能都禁止自动调用和隐式调用；所有推荐组合显式列出必需的 coordination、structure、artifact，以及按需加入的 write-doc 和 draw-diagram。
- [ ] draw-diagram 保持独立 Visual 技能，Product、Technical 和 Knowledge 不复制其视觉路由与质量规则。
- [ ] 正式插件版本升级为 0.6.0，Codex 构建版本遵守既有后缀约定。
- [ ] 在约定的个人 Product 知识库位置生成面向使用者的划分依据文档，并与 Scribe 仓库内部技能架构说明保持清晰区分。
- [ ] Company Documentation、Product、Technical、Architecture、显式调用和共享写作契约测试全部通过。
- [ ] 每个新增或变更技能通过技能结构验证，全部测试、脚本语法检查和差异检查通过。
- [ ] 最终公开内容不会把公司文档描述为代码仓库结构，不会把 Project Documentation 纳入本期技能，也不会引入 Readiness 文档或技能。

## Comments

This historical 0.6 release specification is superseded by issue 05 for Scribe 0.7.0. Its required-composition rules are not compatibility interfaces.
