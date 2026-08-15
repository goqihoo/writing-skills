import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills/foundations/write-doc"


class WriteDocContractTest(unittest.TestCase):
    def test_uses_singular_skill_and_display_names(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        metadata = (SKILL_ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
        old_name = "write-doc" + "s"

        self.assertIn("name: write-doc", skill)
        self.assertIn("# Write Doc", skill)
        self.assertIn('display_name: "Write Doc"', metadata)
        self.assertIn("$write-doc", metadata)
        self.assertFalse((REPO_ROOT / "skills/foundations" / old_name).exists())

    def test_plugin_manifest_uses_singular_skill_path(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
        )

        self.assertIn("./skills/foundations/write-doc", manifest["skills"])

    def test_old_skill_name_is_absent_from_tracked_text_contracts(self) -> None:
        old_name = "write-doc" + "s"
        suffixes = {".md", ".yaml", ".json", ".sh", ".py"}
        stale = []

        for path in REPO_ROOT.rglob("*"):
            if not path.is_file() or path.suffix not in suffixes or ".git" in path.parts:
                continue
            if old_name in path.read_text(encoding="utf-8"):
                stale.append(str(path.relative_to(REPO_ROOT)))

        self.assertEqual([], stale)


if __name__ == "__main__":
    unittest.main()
