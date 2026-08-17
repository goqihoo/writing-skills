import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_ROOT = REPO_ROOT / "skills/knowledge/write-architecture-knowledge"
TECHNICAL_ROOT = REPO_ROOT / "skills/technical/write-technical-architecture"


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

        self.assertIn(
            "./skills/knowledge/write-architecture-knowledge", manifest["skills"]
        )
        self.assertIn(
            "./skills/technical/write-technical-architecture", manifest["skills"]
        )
        for old_path in [
            "./skills/knowledge/write-study-architecture",
            "./skills/technical/write-delivery-architecture",
            "./skills/technical/design-architecture",
            "./skills/technical/record-decision",
        ]:
            self.assertNotIn(old_path, manifest["skills"])

    def test_architecture_authority_boundaries_are_explicit(self) -> None:
        knowledge = (KNOWLEDGE_ROOT / "SKILL.md").read_text(encoding="utf-8")
        technical = (TECHNICAL_ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("reusable Architecture Knowledge", knowledge)
        self.assertIn("not tied to one company", knowledge)
        self.assertIn("company Technical Architecture", technical)
        self.assertIn("Technical Landscape", technical)
        self.assertIn("$Reason Tech Docs", technical)
        self.assertIn("$Reason Arch", technical)


if __name__ == "__main__":
    unittest.main()
