import json
import subprocess
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
METHODS_ROOT = REPO_ROOT / "methods"
CODEX_PLUGIN_ROOT = REPO_ROOT / "plugins/scribe"

PUBLIC_SKILLS = {
    "ask-scribe",
    "assess-product-lifecycle",
    "design-product-metrics",
    "draw-diagram",
    "map-product-capabilities",
    "reason-architecture",
    "reason-domain",
    "reason-product",
    "reason-technical",
    "structure-docs",
    "structure-domain-docs",
    "structure-product-docs",
    "structure-technical-docs",
    "write-architecture-knowledge",
    "write-doc",
    "write-domain-doc",
    "write-knowledge",
    "write-prd",
    "write-product-doc",
    "write-product-roadmap",
    "write-product-strategy",
    "write-technical-architecture",
    "write-technical-doc",
}


class FlatPluginLayoutTest(unittest.TestCase):
    def test_canonical_skills_are_flat_and_methods_are_not_skills(self) -> None:
        actual = {
            path.parent.name for path in SKILLS_ROOT.glob("*/SKILL.md")
        }

        self.assertEqual(PUBLIC_SKILLS, actual)
        self.assertFalse(list(SKILLS_ROOT.glob("*/*/SKILL.md")))
        self.assertTrue((METHODS_ROOT / "prose-quality.md").is_file())
        self.assertFalse(list(METHODS_ROOT.rglob("SKILL.md")))

    def test_claude_uses_the_default_flat_skill_root(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / ".claude-plugin/plugin.json").read_text(
                encoding="utf-8"
            )
        )

        self.assertEqual("./skills/", manifest["skills"])

    def test_codex_marketplace_points_to_a_flat_generated_plugin(self) -> None:
        marketplace = json.loads(
            (REPO_ROOT / ".agents/plugins/marketplace.json").read_text(
                encoding="utf-8"
            )
        )
        entry = next(
            plugin
            for plugin in marketplace["plugins"]
            if plugin["name"] == "scribe"
        )

        self.assertEqual("./plugins/scribe", entry["source"]["path"])
        self.assertTrue(
            (CODEX_PLUGIN_ROOT / ".codex-plugin/plugin.json").is_file()
        )

        packaged = {
            path.parent.name
            for path in (CODEX_PLUGIN_ROOT / "skills").glob("*/SKILL.md")
        }
        self.assertEqual(PUBLIC_SKILLS, packaged)
        self.assertTrue(
            (CODEX_PLUGIN_ROOT / "methods/prose-quality.md").is_file()
        )

        for skill_path in sorted(
            (CODEX_PLUGIN_ROOT / "skills").glob("*/SKILL.md")
        ):
            skill = skill_path.read_text(encoding="utf-8")
            metadata = (skill_path.parent / "agents/openai.yaml").read_text(
                encoding="utf-8"
            )
            self.assertNotIn("disable-model-invocation: true", skill)
            self.assertIn("allow_implicit_invocation: false", metadata)

    def test_codex_package_is_in_sync_with_canonical_skills(self) -> None:
        subprocess.run(
            ["bash", str(REPO_ROOT / "scripts/build-codex-plugin.sh"), "--check"],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )


if __name__ == "__main__":
    unittest.main()
