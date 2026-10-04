# Diagram Design 配色皮肤边界修复

Status: verified

## 目标

以 Diagram Design 源码为基准，只将 Scribe 默认配色作为新增皮肤。保留原生皮肤，允许以后增加配色文件，换肤不改变节点标题、描述、字体、几何、线宽或视觉角色。

## 对比基准

上游：`/Users/andrew/Code/OpenSource/diagram-design`，提交 `ac490fd1ac4b4014100f93e729cb4ad198700bd4`。比较 `skills/diagram-design/SKILL.md` 的 full node / arrow markers、`references/style-guide.md` 和各 `assets/example-*.html`，而非按截图估计。

| 项目 | 上游代码 | 修复前 Scribe 适配 | 本次处理 |
|---|---|---|---|
| 架构配色角色 | backend、store、external、input 使用不同强度中性色；focal 用 accent | 根据源内容有多个分类就自动分配多色填充 | 恢复原始角色；分类配色仅在类型或用户明确要求时启用 |
| 节点文本 | name 12px / 600，sublabel 9px / 400 | SVG starter 的 name 和 detail 都是 12px | 恢复 12/9 层级，中文描述保留 sans 字体 |
| 完整节点 | paper 遮罩 + 样式框 + 可选矩形 tag + 名称 + 副标签 | starter 缺少遮罩与可复用完整组件示范 | 恢复遮罩并提供原版 tag 示例；内容不支持时不虚构 tag |
| 箭头 | marker 8×6，ref=(7,3)，polygon | SVG starter 使用另一套 10×10 viewBox / 7×7 marker | 恢复原版箭头组件 |
| 字号与网格冲突 | 总则要求 4px 网格，但实际组件使用 7、9、14px 和 rx=2 | SVG guide 只列 4 倍数字号，易把副标签推到 12px | 明确具体组件优先，保留上游例外 |
| 比例与画布 | 类型样例决定 viewBox；架构样例框为 128–160×64 | 额外统一大画布和较宽节点使相同描边相对更弱 | 从类型样例起步，整体缩放，不独立拉宽框 |
| 皮肤边界 | 颜色语义与原始组件分开 | 主题还可覆盖字体与测量参数，且只打包 Scribe 配色 | 字体移到独立共享配置，皮肤仅接受颜色/颜色透明度 |

## 实现

- 增加 `apply_theme.py`，按 `var(--dd-ROLE, COLOR)` 标记换色，不按相同 hex 猜测角色。保留可编辑标记，SVG 导出单独解析为字面颜色。
- 从固定提交重新导入 39 个样例和 1 个 HTML starter。保留所有非配色字节，并用 `UPSTREAM_VISUAL_CONTRACTS.json` 记录快照。来源内容是样例，不是用户系统的事实。
- 保留 `scribe-plotly` 默认；增加 `diagram-design`、`diagram-design-dark` 和 `diagram-design-terminal`。Terminal 仅切换原生颜色，不自动添加窗口外框。
- 新皮肤只需复制配色 Markdown 文件并传入路径；无需改组件或注册代码。未知非配色 token、无效颜色、缺失使用中的角色都会报错。
- 保留此前 Scribe 默认分组透明等配色选择。保留用户已有文档，本次不重写正文或 `_assets` 中已有图。

## 验证

- 40 个上游资产的非配色源码哈希一致。
- 全部皮肤和样例往返切换不改变非配色内容；新皮肤路径、错误 token、SVG 输出和原生语义角色均有行为测试。
- 干净虚拟环境中的完整 127 项测试、插件校验、构建同步及空白检查全部通过。已安装 `0.9.0+codex.20260831113236`，234 个安装文件与生成包逐字节一致；安装目录内的原生皮肤导出通过。
- [同源配色对比页](comparison.html) 保留同一份架构图的四种配色。静态 SVG 已渲染检查。浏览器安全策略阻止本地文件预览，因此没有通过浏览器验证在线字体；本机未安装 Geist，静态预览使用字体回退。HTML 保留上游字体链接，字体声明在所有皮肤间相同。

完成条件：上述验证通过，安装副本与生成插件一致；已有用户配图的重绘与纯换色明确分开。
