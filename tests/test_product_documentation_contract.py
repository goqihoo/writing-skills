import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
PRODUCT_ROOT = REPO_ROOT / "skills"
FOUNDATIONS_ROOT = REPO_ROOT / "skills"


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
        method = read(REPO_ROOT / "methods/product-reasoning.md")

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

    def test_common_writer_uses_the_registry_and_freeform_fallback(self) -> None:
        root = PRODUCT_ROOT / "write-product-doc"
        skill = read(root / "SKILL.md")
        registry = yaml.safe_load(
            read(root / "references/internal-document-types.yaml")
        )

        self.assertEqual(10, len(registry["types"]))
        self.assertIn("methods/internal-document-types.md", skill)
        self.assertIn("references/internal-document-types.yaml", skill)
        self.assertIn("Freeform Artifact", skill)

        for route in [
            "$Write Product Strategy",
            "$Map Product Capabilities",
            "$Write Product Roadmap",
            "$Write PRD",
            "$Design Product Metrics",
        ]:
            self.assertIn(route, skill)

        removed = {
            "Product Navigation",
            "Product Operating Model",
            "Users and Roles",
            "Product Terminology",
            "Lifecycle Map",
            "Journey/Product Behavior",
            "Product Solution",
            "Initiative Record",
        }
        self.assertTrue(removed.isdisjoint({entry["name"] for entry in registry["types"]}))

    def test_structure_product_docs_owns_navigation_readmes(self) -> None:
        structure_skill = read(PRODUCT_ROOT / "structure-product-docs/SKILL.md")
        writer_skill = read(PRODUCT_ROOT / "write-product-doc/SKILL.md")

        self.assertIn("Responsibility README", structure_skill)
        self.assertIn("Product navigation", structure_skill)
        self.assertIn("$Structure Product Docs", writer_skill)


if __name__ == "__main__":
    unittest.main()
