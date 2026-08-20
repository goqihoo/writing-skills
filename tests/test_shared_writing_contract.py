import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
WRITE_DOC = SKILLS_ROOT / "write-doc/SKILL.md"
PROSE_METHOD = REPO_ROOT / "methods/prose-quality.md"

class SharedWritingContractTest(unittest.TestCase):
    def test_shared_method_owns_the_reader_flow_contract(self) -> None:
        skill = WRITE_DOC.read_text(encoding="utf-8")
        method = PROSE_METHOD.read_text(encoding="utf-8")

        self.assertIn("methods/prose-quality.md", skill)
        self.assertIn("## Prose contract", method)
        self.assertIn("**Point first.**", method)
        self.assertIn("**Concrete before abstract.**", method)
        self.assertIn("**Causal movement.**", method)
        self.assertIn("**Human syntax.**", method)
        self.assertIn("**Selective structure.**", method)
        self.assertIn("reader-flow failures", method)

    def test_tables_require_compact_comparison_across_peer_items(self) -> None:
        method = PROSE_METHOD.read_text(encoding="utf-8")

        self.assertIn(
            "Use a table only when readers need to compare multiple peer items "
            "across the same compact repeated fields; otherwise use prose, lists, "
            "or a suitable visual.",
            method,
        )

    def test_write_doc_is_optional_for_other_skills(self) -> None:
        required = []

        for path in sorted(SKILLS_ROOT.glob("*/SKILL.md")):
            if path == WRITE_DOC:
                continue
            skill = path.read_text(encoding="utf-8")
            if "Apply `$Write Doc`" in skill or "require `$Write Doc`" in skill:
                required.append(str(path.relative_to(REPO_ROOT)))

        self.assertEqual([], required)

    def test_other_skill_prompts_do_not_require_write_doc(self) -> None:
        required = []

        for path in sorted(SKILLS_ROOT.glob("*/agents/openai.yaml")):
            if path.parent.parent == WRITE_DOC.parent:
                continue
            if "$Write Doc" in path.read_text(encoding="utf-8"):
                required.append(str(path.relative_to(REPO_ROOT)))

        self.assertEqual([], required)

    def test_repository_policy_describes_write_doc_as_optional(self) -> None:
        instructions = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")

        self.assertIn("optional general-purpose prose workflow", instructions)
        self.assertNotIn(
            "Every explicit invocation that creates, revises, reviews, or presents",
            instructions,
        )

    def test_no_public_skill_declares_a_competing_prose_contract(self) -> None:
        competing = []

        for path in sorted(SKILLS_ROOT.glob("*/SKILL.md")):
            skill = path.read_text(encoding="utf-8")
            if "## Prose contract" in skill or "## Shared prose contract" in skill:
                competing.append(str(path.relative_to(REPO_ROOT)))

        self.assertEqual([], competing)


if __name__ == "__main__":
    unittest.main()
