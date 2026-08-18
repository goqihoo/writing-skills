import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"

PUBLIC_SKILLS = {
    "foundations": {
        "ask-scribe",
        "structure-docs",
        "write-doc",
        "reason-architecture",
        "reason-domain",
        "reason-product",
        "reason-technical",
    },
    "knowledge": {
        "structure-domain-docs",
        "write-domain-doc",
        "write-knowledge",
        "write-architecture-knowledge",
    },
    "product": {
        "assess-product-lifecycle",
        "structure-product-docs",
        "write-product-doc",
        "write-product-strategy",
        "map-product-capabilities",
        "write-product-roadmap",
        "write-prd",
        "design-product-metrics",
    },
    "technical": {
        "structure-technical-docs",
        "write-technical-doc",
        "write-technical-architecture",
    },
    "visual": {"draw-diagram"},
}

REMOVED_SKILLS = {
    "write-study-architecture",
    "write-delivery-architecture",
    "write-solution-definition",
    "write-release-plan",
    "write-product-review",
    "write-product-requirements",
    "design-delivery-architecture",
    "record-decision",
    "write-technical-design",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class CompanyDocumentationContractTest(unittest.TestCase):
    def test_public_skill_catalog_has_one_matching_interface_per_skill(self) -> None:
        manifest = json.loads(read(REPO_ROOT / ".claude-plugin/plugin.json"))
        expected_names = {
            name for names in PUBLIC_SKILLS.values() for name in names
        }

        self.assertEqual("./skills/", manifest["skills"])
        self.assertEqual(
            expected_names,
            {path.parent.name for path in SKILLS_ROOT.glob("*/SKILL.md")},
        )

        for names in PUBLIC_SKILLS.values():
            for name in names:
                with self.subTest(skill=name):
                    root = SKILLS_ROOT / name
                    skill = read(root / "SKILL.md")
                    metadata = read(root / "agents/openai.yaml")
                    frontmatter_name = re.search(
                        r"^name: ([a-z0-9-]+)$", skill, re.MULTILINE
                    )

                    self.assertIsNotNone(frontmatter_name)
                    self.assertEqual(name, frontmatter_name.group(1))
                    self.assertIn("disable-model-invocation: true", skill)
                    self.assertIn("allow_implicit_invocation: false", metadata)
                    self.assertIn("display_name:", metadata)

    def test_removed_skills_and_old_architecture_names_are_absent(self) -> None:
        for removed in REMOVED_SKILLS:
            self.assertFalse((SKILLS_ROOT / removed).exists(), removed)

        public_files = [
            REPO_ROOT / "README.md",
            REPO_ROOT / ".claude-plugin/plugin.json",
            REPO_ROOT / ".claude-plugin/marketplace.json",
            REPO_ROOT / "plugins/scribe/.codex-plugin/plugin.json",
            REPO_ROOT / "skills/ask-scribe/SKILL.md",
        ]
        public_text = "\n".join(read(path) for path in public_files)

        for removed in REMOVED_SKILLS:
            self.assertNotIn(removed, public_text)
        self.assertNotIn("Product Knowledge Skill Architecture", public_text)
        self.assertNotIn("seven-directory", public_text.lower())

    def test_catalog_surfaces_use_the_same_controlled_language(self) -> None:
        surfaces = [
            REPO_ROOT / "README.md",
            REPO_ROOT / "skills/ask-scribe/SKILL.md",
            REPO_ROOT / "docs/scribe-skill-architecture.md",
            REPO_ROOT / "docs/product-documentation-skill-architecture.md",
            REPO_ROOT / "docs/technical-documentation-skill-architecture.md",
        ]
        combined = "\n".join(read(path) for path in surfaces)

        for term in [
            "Knowledge",
            "Company Documentation",
            "Product Documentation",
            "Technical Documentation",
            "Project Documentation",
            "Stable Responsibility",
            "Type Extension",
            "Event Collection",
            "Internal Document Type",
            "Explicit Skill Composition",
        ]:
            self.assertIn(term, combined)

    def test_release_versions_match_the_0_7_contract(self) -> None:
        claude = json.loads(read(REPO_ROOT / ".claude-plugin/plugin.json"))
        codex = json.loads(
            read(REPO_ROOT / "plugins/scribe/.codex-plugin/plugin.json")
        )

        self.assertEqual("0.7.1", claude["version"])
        self.assertRegex(codex["version"], r"^0\.7\.1\+codex\.\d{14}$")


if __name__ == "__main__":
    unittest.main()
