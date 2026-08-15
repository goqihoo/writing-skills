import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
STUDY_ROOT = REPO_ROOT / "skills/knowledge/write-study-architecture"
DELIVERY_ROOT = REPO_ROOT / "skills/technical/write-delivery-architecture"


class ArchitectureSkillNamesTest(unittest.TestCase):
    def test_skill_directories_frontmatter_and_display_names_agree(self) -> None:
        expected = {
            STUDY_ROOT: "Write Study Architecture",
            DELIVERY_ROOT: "Write Delivery Architecture",
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
            self.assertIn(f"${skill_root.name}", metadata)

    def test_plugin_exposes_only_the_new_architecture_skill_names(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
        )

        self.assertIn(
            "./skills/knowledge/write-study-architecture", manifest["skills"]
        )
        self.assertIn(
            "./skills/technical/write-delivery-architecture", manifest["skills"]
        )
        self.assertNotIn("./skills/knowledge/study-architecture", manifest["skills"])
        self.assertNotIn("./skills/technical/design-architecture", manifest["skills"])
        self.assertNotIn("./skills/technical/record-decision", manifest["skills"])

    def test_removed_skill_and_old_public_identifiers_are_absent(self) -> None:
        self.assertFalse((REPO_ROOT / "skills/technical/record-decision").exists())
        self.assertFalse((REPO_ROOT / "skills/knowledge/study-architecture").exists())
        self.assertFalse((REPO_ROOT / "skills/technical/design-architecture").exists())

        tracked_text = []
        for path in [
            REPO_ROOT / "README.md",
            REPO_ROOT / ".claude-plugin/plugin.json",
            REPO_ROOT / "skills/foundations/ask-scribe/SKILL.md",
            REPO_ROOT / "skills/knowledge/README.md",
            REPO_ROOT / "skills/technical/README.md",
        ]:
            tracked_text.append(path.read_text(encoding="utf-8"))
        combined = "\n".join(tracked_text)

        for old_identifier in [
            "skills/knowledge/study-architecture",
            "skills/technical/design-architecture",
            "record-decision",
            "`study-architecture`",
            "`design-architecture`",
        ]:
            self.assertNotIn(old_identifier, combined)


if __name__ == "__main__":
    unittest.main()
