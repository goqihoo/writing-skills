import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills/knowledge/write-knowledge"


class WriteKnowledgeContractTest(unittest.TestCase):
    def test_infers_type_from_artifact_signals_before_reader_action(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")

        signals = [
            "user's explicit description",
            "title, filename, and directory",
            "existing healthy structure",
            "project rules and established sibling-document conventions",
        ]

        positions = [skill.index(signal) for signal in signals]
        self.assertEqual(positions, sorted(positions))
        self.assertIn(
            "Use the future reader action to validate the inferred type",
            skill,
        )
        self.assertIn(
            "For every common domain-directory artifact, including essence documents, stop and return a ready-to-type explicit invocation",
            skill,
        )
        self.assertIn("`$write-domain-doc $reason-domain $write-doc`", skill)
        self.assertNotIn("`$write-essence`", skill)


if __name__ == "__main__":
    unittest.main()
