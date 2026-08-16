import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"


class ExplicitInvocationContractTest(unittest.TestCase):
    def test_every_skill_requires_explicit_invocation(self) -> None:
        missing_frontmatter = []
        missing_policy = []

        for skill_path in sorted(SKILLS_ROOT.glob("*/*/SKILL.md")):
            skill_root = skill_path.parent
            skill = skill_path.read_text(encoding="utf-8")
            metadata_path = skill_root / "agents/openai.yaml"
            metadata = metadata_path.read_text(encoding="utf-8")

            if "disable-model-invocation: true" not in skill:
                missing_frontmatter.append(str(skill_path.relative_to(REPO_ROOT)))
            if "allow_implicit_invocation: false" not in metadata:
                missing_policy.append(str(metadata_path.relative_to(REPO_ROOT)))

        self.assertEqual([], missing_frontmatter)
        self.assertEqual([], missing_policy)

    def test_codex_starter_prompts_name_skills_explicitly(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8")
        )

        prompts = manifest["interface"]["defaultPrompt"]
        self.assertTrue(prompts)
        for prompt in prompts:
            with self.subTest(prompt=prompt):
                self.assertIn("$", prompt)


if __name__ == "__main__":
    unittest.main()
