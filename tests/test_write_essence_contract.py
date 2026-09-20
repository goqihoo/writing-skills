import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOMAIN_SKILL_ROOT = REPO_ROOT / "skills/write-domain-doc"
MODULE_PATH = DOMAIN_SKILL_ROOT / "references/essence-document-module.md"
TEMPLATE_PATH = DOMAIN_SKILL_ROOT / "assets/essence-article-template.md"


class EssenceModuleContractTest(unittest.TestCase):
    def test_essence_is_internal_to_write_domain_doc(self) -> None:
        self.assertFalse((REPO_ROOT / "skills/write-essence").exists())
        self.assertTrue(MODULE_PATH.is_file())
        self.assertTrue(TEMPLATE_PATH.is_file())

        module = MODULE_PATH.read_text(encoding="utf-8")
        domain_skill = (DOMAIN_SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("internal module", module)
        self.assertIn("not a standalone skill", module)
        self.assertFalse(module.startswith("---"))
        self.assertIn("references/essence-document-module.md", domain_skill)
        self.assertIn("assets/essence-article-template.md", domain_skill)

    def test_template_locks_the_stable_section_sequence(self) -> None:
        template = TEMPLATE_PATH.read_text(encoding="utf-8")
        required_sections = [
            "## 一、适用范围与锚点案例",
            "## 二、领域类型与最小目标",
            "## 三、必须面对的现实",
            "## 四、核心对象",
            "## 五、参与者与利益",
            "## 六、核心本质",
            "## 七、必然约束",
            "## 八、解法空间或能力空间",
            "## 九、核心矛盾",
            "## 十、稳定分析框架",
            "## 十一、适用边界与相邻领域",
            "## 十二、基础参考与修订条件",
        ]

        positions = [template.index(section) for section in required_sections]
        self.assertEqual(positions, sorted(positions))

    def test_module_follows_the_domain_cognition_derivation_order(self) -> None:
        module = MODULE_PATH.read_text(encoding="utf-8")
        workflow_steps = [
            "Choose the anchor example before drafting",
            "Classify the domain and define its minimum purpose",
            "Record unavoidable realities",
            "Identify the core objects",
            "Map participants and interests",
            "Compress the essence",
            "Derive necessary constraints",
            "Map the solution or capability space",
            "Expose the core tensions",
            "Turn the reasoning into a reusable analysis framework",
        ]

        positions = [module.index(step) for step in workflow_steps]
        self.assertEqual(positions, sorted(positions))

    def test_module_keeps_fixed_structure_and_stress_tests(self) -> None:
        module = MODULE_PATH.read_text(encoding="utf-8")

        self.assertIn("fixed public schema", module)
        self.assertIn("failure case", module)
        self.assertIn("real-system coordinates", module)
        self.assertIn("at least three materially different situations", module)
        self.assertIn("Domain-uniqueness test", module)
        self.assertIn("Adjacent-domain subtraction test", module)
        self.assertNotIn("four to seven subject-specific headings", module)

    def test_template_traces_realities_to_constraints_and_failures(self) -> None:
        template = TEMPLATE_PATH.read_text(encoding="utf-8")

        self.assertIn("### R1", template)
        self.assertIn("约束编号", template)
        self.assertIn("对应现实或对象", template)
        self.assertIn("不满足时的失败", template)
        self.assertIn("真实系统坐标", template)
        self.assertIn("输出型领域", template)
        self.assertIn("控制或治理型领域", template)
        self.assertIn("知识或实践型领域", template)

    def test_core_essence_is_a_recallable_cognitive_handle(self) -> None:
        template = TEMPLATE_PATH.read_text(encoding="utf-8")
        core = template.split("## 六、核心本质", 1)[1].split(
            "## 七、必然约束", 1
        )[0]

        for responsibility in [
            "认知抓手",
            "不承担完整论证",
            "尽可能简洁好理解",
            "需要时在后面紧接",
            "通俗的解释",
        ]:
            self.assertIn(responsibility, core)

        for overconstraint in [
            "领域独有的核心关系",
            "必须维持的结果",
            "关键失配",
            "前提、参与者、证据、授权、边界及失败后果",
            "由哪些参与者，把什么状态变成什么可接受状态",
        ]:
            self.assertNotIn(overconstraint, core)

    def test_core_objects_stay_conceptual_and_route_detail_outward(self) -> None:
        template = TEMPLATE_PATH.read_text(encoding="utf-8")
        core_objects = template.split("## 四、核心对象", 1)[1].split(
            "## 五、参与者与利益", 1
        )[0]

        for responsibility in [
            "必须分清的核心对象",
            "共同构成什么关系",
            "自然的认知顺序",
            "它回答的核心问题",
            "一至两句话",
            "怎样连接",
            "不能互相替代",
            "默认按认知顺序使用短段落",
            "只有确实需要横向比较时才使用表格",
            "核心对象与生命周期",
            "参与者、职责与规则",
            "理解领域本质不可缺少的内容",
        ]:
            self.assertIn(responsibility, core_objects)

        for displaced_detail in [
            "**关键状态：**",
            "**谁拥有或有权改变：**",
            "**重要变化：**",
        ]:
            self.assertNotIn(displaced_detail, core_objects)

    def test_public_skill_surfaces_do_not_expose_write_essence(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
        )
        surfaces = [
            (REPO_ROOT / "README.md").read_text(encoding="utf-8"),
            (REPO_ROOT / "skills/ask-scribe/SKILL.md").read_text(
                encoding="utf-8"
            ),
        ]

        self.assertEqual("./skills/", manifest["skills"])
        self.assertFalse((REPO_ROOT / "skills/write-essence").exists())
        self.assertTrue(all("write-essence" not in surface for surface in surfaces))

        metadata = "\n".join(
            path.read_text(encoding="utf-8")
            for path in (REPO_ROOT / "skills").rglob("agents/openai.yaml")
        )
        self.assertNotIn('display_name: "Write Essence"', metadata)
        self.assertNotIn("$write-essence", metadata)


if __name__ == "__main__":
    unittest.main()
