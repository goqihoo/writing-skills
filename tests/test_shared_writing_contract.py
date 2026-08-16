import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
WRITE_DOC = SKILLS_ROOT / "foundations/write-doc/SKILL.md"

# These skills provide guidance or reasoning to another skill and do not own a
# human-readable artifact. Every other current or future Scribe skill must
# compose the shared prose foundation instead of carrying its own style rules.
NON_ARTIFACT_SKILLS = {"ask-scribe", "reason-architecture", "write-doc"}


class SharedWritingContractTest(unittest.TestCase):
    def test_write_doc_owns_the_reader_flow_contract(self) -> None:
        skill = WRITE_DOC.read_text(encoding="utf-8")

        self.assertIn("## Shared prose contract", skill)
        self.assertIn("**Point first.**", skill)
        self.assertIn("**Concrete before abstract.**", skill)
        self.assertIn("**Causal movement.**", skill)
        self.assertIn("**Human syntax.**", skill)
        self.assertIn("**Selective structure.**", skill)
        self.assertIn("reader-flow failures", skill)

    def test_every_artifact_skill_composes_write_doc(self) -> None:
        missing = []

        for path in sorted(SKILLS_ROOT.glob("*/*/SKILL.md")):
            skill_name = path.parent.name
            if skill_name in NON_ARTIFACT_SKILLS:
                continue
            skill = path.read_text(encoding="utf-8")
            if "$write-doc" not in skill:
                missing.append(str(path.relative_to(REPO_ROOT)))

        self.assertEqual([], missing)

    def test_no_other_skill_declares_a_competing_prose_contract(self) -> None:
        competing = []

        for path in sorted(SKILLS_ROOT.glob("*/*/SKILL.md")):
            if path == WRITE_DOC:
                continue
            skill = path.read_text(encoding="utf-8")
            if "## Shared prose contract" in skill:
                competing.append(str(path.relative_to(REPO_ROOT)))

        self.assertEqual([], competing)


if __name__ == "__main__":
    unittest.main()
