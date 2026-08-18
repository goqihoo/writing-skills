import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_ROOT = REPO_ROOT / "skills/write-architecture-knowledge"
TECHNICAL_ROOT = REPO_ROOT / "skills/write-technical-architecture"


class ArchitectureSkillNamesTest(unittest.TestCase):
    def test_skill_directories_frontmatter_and_display_names_agree(self) -> None:
        expected = {
            KNOWLEDGE_ROOT: "Write Arch Knowledge",
            TECHNICAL_ROOT: "Write Tech Arch",
        }

        for skill_root, display_name in expected.items():
            skill = (skill_root / "SKILL.md").read_text(encoding="utf-8")
            metadata = (skill_root / "agents/openai.yaml").read_text(
                encoding="utf-8"
            )
            name = re.search(r"^name: ([a-z0-9-]+)$", skill, re.MULTILINE)

            self.assertIsNotNone(name)
            self.assertEqual(skill_root.name, name.group(1))
            self.assertIn(f'display_name: "{display_name}"', metadata)
            self.assertIn(f"${display_name}", metadata)

    def test_plugin_exposes_only_current_architecture_skill_names(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
        )

        self.assertEqual("./skills/", manifest["skills"])
        self.assertTrue((KNOWLEDGE_ROOT / "SKILL.md").is_file())
        self.assertTrue((TECHNICAL_ROOT / "SKILL.md").is_file())
        for old_name in [
            "write-study-architecture",
            "write-delivery-architecture",
            "design-architecture",
            "record-decision",
        ]:
            self.assertFalse((REPO_ROOT / "skills" / old_name).exists())

    def test_architecture_authority_boundaries_are_explicit(self) -> None:
        knowledge = (KNOWLEDGE_ROOT / "SKILL.md").read_text(encoding="utf-8")
        technical = (TECHNICAL_ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("reusable Architecture Knowledge", knowledge)
        self.assertIn("not tied to one company", knowledge)
        self.assertIn("company Technical Architecture", technical)
        self.assertIn("Technical Landscape", technical)
        self.assertIn("methods/technical-reasoning.md", technical)
        self.assertIn("methods/architecture-reasoning.md", technical)


if __name__ == "__main__":
    unittest.main()
