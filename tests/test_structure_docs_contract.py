import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class StructureDocsContractTest(unittest.TestCase):
    def test_ask_scribe_explains_without_executing_skills(self) -> None:
        skill = (
            REPO_ROOT / "skills/foundations/ask-scribe/SKILL.md"
        ).read_text(encoding="utf-8")
        metadata = (
            REPO_ROOT / "skills/foundations/ask-scribe/agents/openai.yaml"
        ).read_text(encoding="utf-8")

        self.assertIn("disable-model-invocation: true", skill)
        self.assertIn(
            "Do not invoke another skill, perform its workflow, modify files, or "
            "produce an artifact owned by another skill.",
            skill,
        )
        self.assertIn("allow_implicit_invocation: false", metadata)

    def test_structure_docs_has_the_expected_name_and_plugin_entry(self) -> None:
        metadata = (
            REPO_ROOT / "skills/foundations/structure-docs/agents/openai.yaml"
        ).read_text(encoding="utf-8")
        claude_manifest = json.loads(
            (REPO_ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
        )

        self.assertIn('display_name: "Structure Docs"', metadata)
        self.assertIn(
            "./skills/foundations/structure-docs", claude_manifest["skills"]
        )

    def test_structure_docs_preserves_boundary_decisions(self) -> None:
        skill = (
            REPO_ROOT / "skills/foundations/structure-docs/SKILL.md"
        ).read_text(encoding="utf-8")
        patterns = (
            REPO_ROOT
            / "skills/foundations/structure-docs/references/structure-patterns.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Record a taxonomy gap", skill)
        self.assertIn("Obtain confirmation before moving", skill)
        self.assertIn("Use one dimension per level", patterns)


if __name__ == "__main__":
    unittest.main()
