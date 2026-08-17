import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PRODUCT_ROOT = REPO_ROOT / "skills/product"
FOUNDATIONS_ROOT = REPO_ROOT / "skills/foundations"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class ProductDocumentationContractTest(unittest.TestCase):
    def test_product_structure_uses_company_and_product_stable_cores(self) -> None:
        model = read(
            PRODUCT_ROOT
            / "structure-product-docs/references/product-structure-model.md"
        )

        company_core = model.split("## Company Product stable core", 1)[1].split(
            "## Accepted-product stable core", 1
        )[0]
        product_core = model.split("## Accepted-product stable core", 1)[1].split(
            "## Type Extensions", 1
        )[0]
        extensions = model.split("## Type Extensions", 1)[1].split(
            "## Event Collections", 1
        )[0]
        events = model.split("## Event Collections", 1)[1].split(
            "## Materialization rules", 1
        )[0]

        for directory in ["Portfolio/", "Governance/", "Products/"]:
            self.assertIn(directory, company_core)
        for directory in [
            "Definition/",
            "Capabilities/",
            "Planning/",
            "Measurement/",
        ]:
            self.assertIn(directory, product_core)
        for directory in ["Solutions/", "Experience/"]:
            self.assertIn(directory, extensions)
        for directory in [
            "Initiatives/",
            "Evidence/",
            "Releases/",
            "Decisions/",
        ]:
            self.assertIn(directory, events)

        self.assertIn("product line", model.lower())
        self.assertIn("classification view", model.lower())
        self.assertIn("first real event", model.lower())
        self.assertNotIn("seven-directory core", model.lower())

    def test_default_scaffold_excludes_extensions_and_event_collections(self) -> None:
        skill = read(PRODUCT_ROOT / "structure-product-docs/SKILL.md")
        plan = read(
            PRODUCT_ROOT
            / "structure-product-docs/assets/product-structure-plan-template.md"
        )

        for text in [skill, plan]:
            self.assertIn("Stable Responsibility", text)
            self.assertIn("Type Extension", text)
            self.assertIn("Event Collection", text)
        self.assertIn("Do not create", skill)
        self.assertIn("proposal", skill)
        self.assertIn("scaffold", skill)
        self.assertIn("audit", skill)
        self.assertIn("approved migration", skill)

    def test_reason_product_covers_company_portfolio_and_product_boundaries(self) -> None:
        skill = read(FOUNDATIONS_ROOT / "reason-product/SKILL.md")
        method = read(REPO_ROOT / "skills/methods/product-reasoning.md")

        for concept in [
            "company product portfolio",
            "product line",
            "product boundary",
            "Stable Responsibility",
            "Type Extension",
            "Product Assessment",
        ]:
            self.assertIn(concept, skill + method)
        self.assertIn("persist", skill.lower())
        self.assertIn("disputed", skill.lower())

    def test_common_writer_covers_internal_types_and_routes_public_artifacts(self) -> None:
        reference = read(
            PRODUCT_ROOT / "write-product-doc/references/product-document-types.md"
        )

        internal_types = [
            "Product navigation",
            "Product Portfolio",
            "Products Registry",
            "Product Operating Model",
            "Product Governance",
            "Product Overview/Definition",
            "Users and Roles",
            "Product Terminology",
            "Lifecycle Map",
            "Capability Detail",
            "Journey/Product Behavior",
            "Product Solution",
            "Initiative Record",
            "Evidence Record",
            "Product Decision",
            "Product Release Plan",
            "Release Notes",
            "Product Review",
        ]
        for document_type in internal_types:
            self.assertRegex(
                reference,
                rf"(?m)^\| {re.escape(document_type)} \| .*\.md \|",
            )

        for route in [
            "$Write Product Strategy",
            "$Map Product Capabilities",
            "$Write Product Roadmap",
            "$Write PRD",
            "$Design Product Metrics",
        ]:
            self.assertIn(route, reference)

    def test_product_common_writer_has_every_routed_template(self) -> None:
        root = PRODUCT_ROOT / "write-product-doc"
        reference = read(root / "references/product-document-types.md")
        routed_templates = set()
        for line in reference.splitlines():
            if line.startswith("|") and ".md |" in line:
                routed_templates.add(line.split("|")[2].strip())

        self.assertTrue(routed_templates)
        self.assertEqual(
            routed_templates,
            {path.name for path in (root / "assets").glob("*.md")},
        )


if __name__ == "__main__":
    unittest.main()
