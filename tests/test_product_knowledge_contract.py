import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
PRODUCT_ROOT = SKILLS_ROOT / "product"
FOUNDATIONS_ROOT = SKILLS_ROOT / "foundations"
ARCHITECTURE_DOC = REPO_ROOT / "docs/product-knowledge-skill-architecture.md"

PRODUCT_SKILLS = {
    "reason-product": FOUNDATIONS_ROOT / "reason-product",
    "assess-product-lifecycle": PRODUCT_ROOT / "assess-product-lifecycle",
    "structure-product-docs": PRODUCT_ROOT / "structure-product-docs",
    "write-product-doc": PRODUCT_ROOT / "write-product-doc",
    "write-product-strategy": PRODUCT_ROOT / "write-product-strategy",
    "map-product-capabilities": PRODUCT_ROOT / "map-product-capabilities",
    "write-solution-definition": PRODUCT_ROOT / "write-solution-definition",
    "write-product-roadmap": PRODUCT_ROOT / "write-product-roadmap",
    "write-prd": PRODUCT_ROOT / "write-prd",
    "design-product-metrics": PRODUCT_ROOT / "design-product-metrics",
    "write-release-plan": PRODUCT_ROOT / "write-release-plan",
    "write-product-review": PRODUCT_ROOT / "write-product-review",
}

STANDARD_ARTIFACTS = {
    "write-product-strategy": "product-strategy-template.md",
    "map-product-capabilities": "product-capability-map-template.md",
    "write-solution-definition": "solution-definition-template.md",
    "write-product-roadmap": "product-roadmap-template.md",
    "write-prd": "prd-template.md",
    "design-product-metrics": "product-metrics-template.md",
    "write-release-plan": "release-plan-template.md",
    "write-product-review": "product-review-template.md",
}

ASSESSMENT_GATED_ARTIFACTS = set(STANDARD_ARTIFACTS) - {"write-prd"}


class ProductKnowledgeContractTest(unittest.TestCase):
    def test_every_product_knowledge_skill_has_the_required_interface(self) -> None:
        for skill_name, skill_root in PRODUCT_SKILLS.items():
            with self.subTest(skill=skill_name):
                skill = (skill_root / "SKILL.md").read_text(encoding="utf-8")
                metadata = (skill_root / "agents/openai.yaml").read_text(
                    encoding="utf-8"
                )

                self.assertIn(f"name: {skill_name}", skill)
                self.assertIn("disable-model-invocation: true", skill)
                self.assertIn("$write-doc", skill)
                self.assertIn(f"${skill_name}", metadata)
                self.assertIn("allow_implicit_invocation: false", metadata)

    def test_product_assessment_is_the_boundary_handoff(self) -> None:
        skill_root = PRODUCT_SKILLS["reason-product"]
        skill = (skill_root / "SKILL.md").read_text(encoding="utf-8")
        method = (skill_root / "references/product-reasoning-method.md").read_text(
            encoding="utf-8"
        )
        template = (skill_root / "assets/product-assessment-template.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("Product Assessment", skill)
        for decision in ["Accept", "Route as product area or capability", "Needs evidence"]:
            self.assertIn(decision, method)
        for responsibility in [
            "Minimum user outcome",
            "Product boundary",
            "Change authority",
            "Release boundary",
            "Relationships",
            "Review triggers",
        ]:
            self.assertIn(responsibility, method)
        for section in [
            "## Decision",
            "## Product boundary",
            "## Users, outcomes, and evidence",
            "## Relationships",
            "## Knowledge ownership",
            "## Lifecycle and review triggers",
            "## Unresolved questions",
        ]:
            self.assertIn(section, template)

    def test_lifecycle_assessment_keeps_three_state_dimensions_separate(self) -> None:
        skill_root = PRODUCT_SKILLS["assess-product-lifecycle"]
        model = (skill_root / "references/product-lifecycle-model.md").read_text(
            encoding="utf-8"
        )
        template = (
            skill_root / "assets/product-lifecycle-assessment-template.md"
        ).read_text(encoding="utf-8")

        for state in ["Existing", "Create now", "Planned", "Unresolved"]:
            self.assertIn(state, model)
        for state in ["Draft", "Accepted", "Current", "Needs review", "Superseded"]:
            self.assertIn(state, model)
        for state in [
            "Not applicable",
            "Collecting evidence",
            "Ready for decision",
            "Go",
            "Hold",
            "Recycle",
            "Stop",
        ]:
            self.assertIn(state, model)
        self.assertIn("## Decision-gate matrix", template)
        self.assertIn("## Missing or stale artifacts", template)
        self.assertIn("Acceptance state", template)
        self.assertIn("Currency state", template)
        self.assertNotIn("| Artifact state |", template)

    def test_default_product_structure_has_seven_frequent_directories(self) -> None:
        skill_root = PRODUCT_SKILLS["structure-product-docs"]
        model = (skill_root / "references/product-structure-model.md").read_text(
            encoding="utf-8"
        )

        core_directories = [
            "definition/",
            "capabilities/",
            "planning/",
            "initiatives/",
            "evidence/",
            "measurement/",
            "releases/",
        ]
        extension_directories = ["solutions/", "experience/", "decisions/"]
        core_section = model.split("## Seven-directory core", 1)[1].split(
            "## Product-type extensions", 1
        )[0]
        extensions_section = model.split("## Product-type extensions", 1)[1].split(
            "## Materialization states", 1
        )[0]

        for directory in core_directories:
            self.assertIn(directory, core_section)
        for conditional_directory in extension_directories:
            self.assertNotIn(conditional_directory, core_section)
            self.assertIn(conditional_directory, extensions_section)
        self.assertIn("Seven-directory core", model)
        self.assertIn("Product-type extensions", model)
        self.assertIn("Upgrade a file or flat collection", model)
        self.assertIn("Technical material", model)

        for template_name in [
            "product-inventory-template.md",
            "product-structure-plan-template.md",
        ]:
            self.assertTrue((skill_root / "assets" / template_name).is_file())

    def test_general_product_writer_routes_only_common_product_documents(self) -> None:
        skill_root = PRODUCT_SKILLS["write-product-doc"]
        skill = (skill_root / "SKILL.md").read_text(encoding="utf-8")
        reference = (skill_root / "references/product-document-types.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("references/product-document-types.md", skill)
        for artifact in [
            "Product map and README",
            "Lifecycle map",
            "Collection README",
            "Users and roles",
            "Concepts and language",
            "Capability detail",
            "Journey and behavior",
            "Evidence record",
            "Product decision record",
            "Release notes",
        ]:
            self.assertIn(artifact, reference)
        for standard_skill in STANDARD_ARTIFACTS:
            self.assertIn(f"${standard_skill}", reference)
        self.assertIn("$write-prd", reference)

        expected_templates = {
            "product-readme-template.md",
            "product-lifecycle-map-template.md",
            "collection-readme-template.md",
            "users-and-roles-template.md",
            "concepts-and-language-template.md",
            "capability-detail-template.md",
            "journey-and-behavior-template.md",
            "evidence-record-template.md",
            "product-decision-template.md",
            "release-notes-template.md",
        }
        self.assertEqual(
            expected_templates,
            {path.name for path in (skill_root / "assets").glob("*.md")},
        )

        lifecycle_map = (
            skill_root / "assets/product-lifecycle-map-template.md"
        ).read_text(encoding="utf-8")
        for field in [
            "Decision gate",
            "Required artifact",
            "Authoritative link",
            "Structure state",
            "Acceptance state",
            "Currency state",
            "Gate state",
            "Owner",
            "Evidence gap",
            "Next review",
        ]:
            self.assertIn(field, lifecycle_map)

    def test_standard_artifact_skills_own_one_template_each(self) -> None:
        self.assertEqual(
            {
                "write-product-strategy",
                "map-product-capabilities",
                "write-solution-definition",
                "write-product-roadmap",
                "write-prd",
                "design-product-metrics",
                "write-release-plan",
                "write-product-review",
            },
            set(STANDARD_ARTIFACTS),
        )
        for skill_name, template_name in STANDARD_ARTIFACTS.items():
            with self.subTest(skill=skill_name):
                skill_root = PRODUCT_SKILLS[skill_name]
                skill = (skill_root / "SKILL.md").read_text(encoding="utf-8")
                template_path = skill_root / "assets" / template_name

                self.assertTrue(template_path.is_file())
                self.assertIn(f"assets/{template_name}", skill)
                self.assertIn("Completion", skill)
                self.assertEqual(
                    {template_name},
                    {path.name for path in (skill_root / "assets").glob("*.md")},
                )
                template = template_path.read_text(encoding="utf-8")
                self.assertIn("Acceptance state", template)
                self.assertIn("Currency state", template)

                if skill_name in ASSESSMENT_GATED_ARTIFACTS:
                    self.assertIn("Require an accepted product boundary", skill)
                else:
                    self.assertNotIn("Require an accepted product boundary", skill)

    def test_strategy_references_instead_of_redefining_product_boundary(self) -> None:
        template = (
            PRODUCT_SKILLS["write-product-strategy"]
            / "assets/product-strategy-template.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Product Assessment link", template)
        self.assertIn("Product scope and version", template)
        self.assertNotIn("Minimum user outcome:", template)
        self.assertNotIn("Included product responsibilities:", template)
        self.assertNotIn("Product and release authority:", template)

    def test_plugin_and_guides_expose_the_product_system(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
        )
        surfaces = "\n".join(
            path.read_text(encoding="utf-8")
            for path in [
                REPO_ROOT / "README.md",
                REPO_ROOT / "skills/product/README.md",
                REPO_ROOT / "skills/foundations/README.md",
                REPO_ROOT / "skills/foundations/ask-scribe/SKILL.md",
            ]
        )
        architecture = ARCHITECTURE_DOC.read_text(encoding="utf-8")

        for skill_name, skill_root in PRODUCT_SKILLS.items():
            plugin_path = f"./{skill_root.relative_to(REPO_ROOT)}"
            self.assertIn(plugin_path, manifest["skills"])
            self.assertIn(skill_name, surfaces)

        self.assertIn("Seven-directory core", architecture)
        self.assertIn("Product Assessment", architecture)
        self.assertIn("Product Lifecycle Assessment", architecture)
        self.assertIn("write-product-doc", architecture)
        self.assertIn("write-prd", architecture)


if __name__ == "__main__":
    unittest.main()
