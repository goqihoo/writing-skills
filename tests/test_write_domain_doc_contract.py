import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills/write-domain-doc"


class WriteDomainDocContractTest(unittest.TestCase):
    def test_skill_is_the_common_domain_document_router(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        metadata = (SKILL_ROOT / "agents/openai.yaml").read_text(encoding="utf-8")

        self.assertIn("name: write-domain-doc", skill)
        self.assertIn("methods/domain-reasoning.md", skill)
        self.assertNotIn("Apply `$Write Doc`", skill)
        self.assertIn("references/domain-document-types.md", skill)
        self.assertIn("user's explicit request", skill)
        self.assertIn("target filename and title", skill)
        self.assertIn("references/essence-document-module.md", skill)
        self.assertIn("assets/essence-article-template.md", skill)
        self.assertNotIn("`$write-essence`", skill)
        self.assertIn("`$Write Knowledge`", skill)
        self.assertIn('display_name: "Write Domain Doc"', metadata)
        self.assertIn("$Write Domain Doc", metadata)
        self.assertNotIn("$Reason Domain", metadata)

    def test_type_reference_defines_rigidity_and_template_routes(self) -> None:
        reference = (SKILL_ROOT / "references/domain-document-types.md").read_text(
            encoding="utf-8"
        )

        for strength in [
            "Strict schema",
            "Stable lookup schema",
            "Stable reasoning sequence",
        ]:
            self.assertIn(strength, reference)

        expected_templates = [
            "domain-readme-template.md",
            "essence-article-template.md",
            "terminology-and-concept-relationships-template.md",
            "core-objects-and-lifecycle-template.md",
            "participants-responsibilities-and-rules-template.md",
            "mechanism-template.md",
            "capability-and-solution-template.md",
            "method-and-practice-template.md",
            "case-and-failure-template.md",
            "reference-template.md",
        ]
        for template in expected_templates:
            self.assertIn(template, reference)
            self.assertTrue((SKILL_ROOT / "assets" / template).is_file())

        self.assertIn("essence-document-module.md", reference)

    def test_templates_preserve_each_artifacts_distinct_question(self) -> None:
        expected_markers = {
            "domain-readme-template.md": [
                "## 领域定位",
                "## 阅读路径",
                "## 知识地图",
                "## 内容边界",
            ],
            "terminology-and-concept-relationships-template.md": [
                "## 适用语境",
                "## 核心概念",
                "## 概念关系",
                "## 易混淆概念",
            ],
            "core-objects-and-lifecycle-template.md": [
                "## 代表性场景",
                "## 核心对象",
                "## 状态与转换",
                "## 不变量与失败",
            ],
            "participants-responsibilities-and-rules-template.md": [
                "## 参与者",
                "## 职责、权限与证据",
                "## 规则与冲突",
                "## 例外与升级",
            ],
            "mechanism-template.md": [
                "## 要解释的现象",
                "## 前提与参与对象",
                "## 因果过程",
                "## 失效、反馈与边界",
            ],
            "capability-and-solution-template.md": [
                "## 约束与目标",
                "## 必要能力族",
                "## 解法模式",
                "## 选择条件与取舍",
            ],
            "method-and-practice-template.md": [
                "## 适用条件",
                "## 输入与准备",
                "## 执行步骤",
                "## 输出与验证",
            ],
            "case-and-failure-template.md": [
                "## 背景与分析问题",
                "## 已观察事实与时间线",
                "## 机制分析",
                "## 结论、反事实与边界",
            ],
            "reference-template.md": [
                "## 适用范围",
                "## 查找内容",
                "## 解释与使用规则",
                "## 来源、版本与修订条件",
            ],
        }

        for filename, markers in expected_markers.items():
            template = (SKILL_ROOT / "assets" / filename).read_text(encoding="utf-8")
            positions = [template.index(marker) for marker in markers]
            self.assertEqual(positions, sorted(positions), filename)

    def test_plugin_and_guides_expose_the_skill(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
        )
        root_readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        guide = (
            REPO_ROOT / "skills/ask-scribe/SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertEqual("./skills/", manifest["skills"])
        self.assertTrue((REPO_ROOT / "skills/write-domain-doc/SKILL.md").is_file())
        self.assertIn("write-domain-doc", root_readme)
        self.assertIn("write-domain-doc", guide)

        general_knowledge = (
            REPO_ROOT / "skills/write-knowledge/SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "Route every common domain-directory artifact, including essence documents",
            general_knowledge,
        )
        self.assertIn("`$Write Domain Doc`", general_knowledge)


if __name__ == "__main__":
    unittest.main()
