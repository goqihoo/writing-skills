import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"

DISPLAY_NAMES = {
    "ask-scribe": "Ask Scribe",
    "reason-architecture": "Reason Arch",
    "reason-domain": "Reason Domain",
    "reason-product": "Reason Product",
    "reason-technical": "Reason Tech Docs",
    "structure-docs": "Structure Docs",
    "write-deck": "Write Deck",
    "write-doc": "Write Doc",
    "structure-domain-docs": "Structure Domain Docs",
    "write-architecture-knowledge": "Write Arch Knowledge",
    "write-domain-doc": "Write Domain Doc",
    "write-knowledge": "Write Knowledge",
    "assess-product-lifecycle": "Assess Product Lifecycle",
    "design-product-metrics": "Design Product Metrics",
    "map-product-capabilities": "Map Product Capabilities",
    "structure-product-docs": "Structure Product Docs",
    "write-prd": "Write PRD",
    "write-product-doc": "Write Product Doc",
    "write-product-roadmap": "Write Product Roadmap",
    "write-product-strategy": "Write Product Strategy",
    "structure-technical-docs": "Structure Tech Docs",
    "write-technical-architecture": "Write Tech Arch",
    "write-technical-doc": "Write Tech Doc",
    "draw-diagram": "Draw Diagram",
}


def field(metadata: str, name: str) -> str:
    match = re.search(rf'^\s*{name}: "([^"]+)"$', metadata, re.MULTILINE)
    if match is None:
        raise AssertionError(f"Missing {name}")
    return match.group(1)


class DisplayNameInvocationContractTest(unittest.TestCase):
    def test_every_public_skill_has_the_exact_unique_display_name(self) -> None:
        actual = {}

        for skill_path in sorted(SKILLS_ROOT.glob("*/SKILL.md")):
            skill_id = skill_path.parent.name
            metadata = (skill_path.parent / "agents/openai.yaml").read_text(
                encoding="utf-8"
            )
            actual[skill_id] = field(metadata, "display_name")

        self.assertEqual(DISPLAY_NAMES, actual)
        self.assertEqual(len(actual), len(set(actual.values())))

    def test_default_prompts_prefer_exact_display_names(self) -> None:
        for skill_path in sorted(SKILLS_ROOT.glob("*/SKILL.md")):
            skill_id = skill_path.parent.name
            metadata = (skill_path.parent / "agents/openai.yaml").read_text(
                encoding="utf-8"
            )
            prompt = field(metadata, "default_prompt")

            with self.subTest(skill=skill_id):
                self.assertIn(f"${DISPLAY_NAMES[skill_id]}", prompt)
                self.assertNotIn(f"${skill_id}", prompt)

    def test_plugin_prompts_prefer_display_names(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / "plugins/scribe/.codex-plugin/plugin.json").read_text(
                encoding="utf-8"
            )
        )
        prompts = manifest["interface"]["defaultPrompt"]

        for prompt in prompts:
            with self.subTest(prompt=prompt):
                self.assertRegex(prompt, r"\$[A-Z]")
                self.assertIsNone(re.search(r"\$[a-z0-9]+(?:-[a-z0-9]+)+", prompt))

    def test_skill_ids_and_display_names_are_both_documented_invocations(self) -> None:
        instructions = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")

        self.assertIn("Skill ID", instructions)
        self.assertIn("Skill Display Name", instructions)
        self.assertIn("both valid invocation names", instructions)

    def test_draw_diagram_uses_only_the_singular_skill_id(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
        )
        old_id = "draw-diagram" + "s"

        self.assertTrue((SKILLS_ROOT / "draw-diagram").is_dir())
        self.assertFalse((SKILLS_ROOT / old_id).exists())
        self.assertEqual("./skills/", manifest["skills"])


if __name__ == "__main__":
    unittest.main()
