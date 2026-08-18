import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
METHODS_ROOT = REPO_ROOT / "methods"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def public_skills() -> list[tuple[Path, str]]:
    result = []
    for skill_path in sorted(SKILLS_ROOT.glob("*/SKILL.md")):
        metadata = read(skill_path.parent / "agents/openai.yaml")
        display_name = re.search(r'display_name: "([^"]+)"', metadata)
        if display_name is None:
            raise AssertionError(f"Missing display name: {skill_path}")
        result.append((skill_path, display_name.group(1)))
    return result


class IndependentPublicSkillContractTest(unittest.TestCase):
    def test_public_skills_do_not_require_another_public_skill(self) -> None:
        forbidden = [
            "Apply `$",
            "required dependency",
            "missing dependency",
            "was not explicitly invoked",
        ]

        violations = []
        for skill_path, _ in public_skills():
            skill = read(skill_path)
            matched = [phrase for phrase in forbidden if phrase in skill]
            if matched:
                violations.append(
                    (str(skill_path.relative_to(REPO_ROOT)), matched)
                )

        self.assertEqual([], violations)

    def test_default_prompts_invoke_only_the_selected_skill(self) -> None:
        catalog = [display_name for _, display_name in public_skills()]
        violations = []

        for skill_path, own_display_name in public_skills():
            metadata_path = skill_path.parent / "agents/openai.yaml"
            metadata = read(metadata_path)
            prompt = re.search(r'default_prompt: "([^"]+)"', metadata)
            self.assertIsNotNone(prompt, str(metadata_path))
            invocations = [
                name for name in catalog if f"${name}" in prompt.group(1)
            ]
            if invocations != [own_display_name]:
                violations.append(
                    (str(metadata_path.relative_to(REPO_ROOT)), invocations)
                )

        self.assertEqual([], violations)

    def test_ask_scribe_examples_use_one_public_skill_each(self) -> None:
        ask_scribe = read(SKILLS_ROOT / "ask-scribe/SKILL.md")
        catalog = [display_name for _, display_name in public_skills()]
        violations = []

        for line_number, line in enumerate(ask_scribe.splitlines(), start=1):
            invocations = [name for name in catalog if f"${name}" in line]
            if len(invocations) > 1:
                violations.append((line_number, invocations))

        self.assertEqual([], violations)

    def test_every_public_skill_applies_the_shared_prose_method(self) -> None:
        missing = []
        for skill_path, _ in public_skills():
            if "methods/prose-quality.md" not in read(skill_path):
                missing.append(str(skill_path.relative_to(REPO_ROOT)))

        self.assertEqual([], missing)

    def test_every_public_skill_can_apply_the_shared_visual_method(self) -> None:
        missing = []
        for skill_path, _ in public_skills():
            if "methods/visual-production.md" not in read(skill_path):
                missing.append(str(skill_path.relative_to(REPO_ROOT)))

        self.assertEqual([], missing)

    def test_shared_methods_are_complete_and_not_invocable(self) -> None:
        expected = {
            "architecture-reasoning.md",
            "documentation-structure.md",
            "domain-reasoning.md",
            "internal-document-types.md",
            "product-reasoning.md",
            "prose-quality.md",
            "technical-reasoning.md",
            "visual-production.md",
        }
        actual = {
            path.name
            for path in METHODS_ROOT.glob("*.md")
            if path.name != "README.md"
        }

        self.assertEqual(expected, actual)
        self.assertFalse(list(METHODS_ROOT.rglob("SKILL.md")))
        self.assertFalse(list(METHODS_ROOT.rglob("openai.yaml")))
        self.assertEqual(
            {"mermaid-guide.md", "style-guide.md", "svg-guide.md"},
            {
                path.name
                for path in (METHODS_ROOT / "visual-production").glob("*.md")
            },
        )

    def test_linked_and_flat_skill_installs_can_resolve_shared_methods(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            client_root = Path(temporary_directory) / "client"
            linked_skills = client_root / "skills"
            subprocess.run(
                [
                    "bash",
                    str(REPO_ROOT / "scripts/link-skills.sh"),
                    str(linked_skills),
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            self.assertEqual(METHODS_ROOT, (client_root / "methods").resolve())

            copied_skills = client_root / "copied-skills"
            copied_skills.mkdir()
            for skill_path, _ in public_skills():
                installed_skill = copied_skills / skill_path.parent.name
                shutil.copytree(skill_path.parent, installed_skill)
                for method_reference in re.findall(
                    r"`(\.\./\.\./methods/[a-z-]+\.md)`",
                    read(installed_skill / "SKILL.md"),
                ):
                    self.assertTrue(
                        (installed_skill / method_reference).is_file(),
                        f"Unresolved Shared Method: {installed_skill} {method_reference}",
                    )


if __name__ == "__main__":
    unittest.main()
