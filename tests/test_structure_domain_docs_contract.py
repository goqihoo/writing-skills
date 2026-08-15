import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills/knowledge/structure-domain-docs"


class StructureDomainDocsContractTest(unittest.TestCase):
    def test_skill_owns_domain_specific_structure(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        metadata = (SKILL_ROOT / "agents/openai.yaml").read_text(encoding="utf-8")

        self.assertIn("name: structure-domain-docs", skill)
        self.assertIn("`$structure-docs`", skill)
        self.assertIn("references/domain-structure-model.md", skill)
        self.assertIn("../write-domain-doc/assets/domain-readme-template.md", skill)
        self.assertIn('display_name: "Structure Domain Docs"', metadata)
        self.assertIn("$structure-domain-docs", metadata)

    def test_structure_model_has_stable_domain_knowledge_forms(self) -> None:
        model = (SKILL_ROOT / "references/domain-structure-model.md").read_text(
            encoding="utf-8"
        )

        expected = [
            "README.md",
            "{领域名称}本质.md",
            "术语与概念关系.md",
            "核心对象与生命周期.md",
            "参与者、职责与规则.md",
            "机制/",
            "能力与解法/",
            "方法与实践/",
            "案例与失败/",
            "参考/",
        ]
        for item in expected:
            self.assertIn(item, model)

        self.assertIn("Small domain", model)
        self.assertIn("Complex domain", model)
        self.assertIn("one dimension per directory level", model)
        self.assertIn("Do not create empty directories by default", model)

    def test_domain_readme_template_is_a_map_and_reading_path(self) -> None:
        template = (
            REPO_ROOT
            / "skills/knowledge/write-domain-doc/assets/domain-readme-template.md"
        ).read_text(encoding="utf-8")

        required_sections = [
            "## 领域定位",
            "## 阅读路径",
            "## 知识地图",
            "## 内容边界",
            "## 维护规则",
            "## 相关导航",
        ]
        positions = [template.index(section) for section in required_sections]
        self.assertEqual(positions, sorted(positions))

    def test_plugin_and_guides_expose_the_skill(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
        )
        knowledge_readme = (
            REPO_ROOT / "skills/knowledge/README.md"
        ).read_text(encoding="utf-8")
        root_readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        guide = (
            REPO_ROOT / "skills/foundations/ask-scribe/SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn("./skills/knowledge/structure-domain-docs", manifest["skills"])
        self.assertIn("structure-domain-docs", knowledge_readme)
        self.assertIn("structure-domain-docs", root_readme)
        self.assertIn("structure-domain-docs", guide)


if __name__ == "__main__":
    unittest.main()
