import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
TECHNICAL_ROOT = REPO_ROOT / "skills"
FOUNDATIONS_ROOT = REPO_ROOT / "skills"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class TechnicalDocumentationContractTest(unittest.TestCase):
    def test_technical_structure_models_registered_systems_and_localized_responsibilities(self) -> None:
        model = read(
            TECHNICAL_ROOT
            / "structure-technical-docs/references/technical-structure-model.md"
        )

        for concept in [
            "Strategy",
            "Architecture",
            "Systems",
            "Governance",
            "logical Stable Responsibilities",
            "documentation set's language",
            "Registered System",
            "System Responsibility README",
            "System Architecture",
            "Architecture Topics",
            "narrowest Authority Level",
        ]:
            self.assertIn(concept, model)
        self.assertIn("concrete platform", model)
        self.assertIn("supporting evidence", model)
        self.assertIn("no one of them is an additional mandatory condition", model)
        self.assertNotIn("Use initial capitals", model)

    def test_reason_technical_owns_company_scope_and_assessment(self) -> None:
        skill = read(FOUNDATIONS_ROOT / "reason-technical/SKILL.md")
        method = read(
            REPO_ROOT / "methods/technical-reasoning.md"
        )
        combined = skill + method

        for concept in [
            "Technical Landscape",
            "company technical scope",
            "ownership",
            "Machine Authority",
            "Stable Responsibility",
            "Type Extension",
            "Technical Assessment",
        ]:
            self.assertIn(concept, combined)
        self.assertNotIn("readiness", combined.lower())

    def test_technical_writers_own_company_system_and_subsystem_architecture(self) -> None:
        root = TECHNICAL_ROOT / "write-technical-doc"
        skill = read(root / "SKILL.md")
        registry = yaml.safe_load(
            read(root / "references/internal-document-types.yaml")
        )
        architecture_skill = read(
            TECHNICAL_ROOT / "write-technical-architecture/SKILL.md"
        )
        architecture_registry = yaml.safe_load(
            read(
                TECHNICAL_ROOT
                / "write-technical-architecture/references/internal-document-types.yaml"
            )
        )

        self.assertIn("methods/internal-document-types.md", skill)
        self.assertIn("methods/architecture-reasoning.md", skill)
        self.assertIn("Freeform Artifact", skill)
        self.assertIn("System Architecture", {entry["name"] for entry in registry["types"]})
        self.assertIn("Subsystem Architecture", {entry["name"] for entry in registry["types"]})
        self.assertIn("Technical Architecture", {entry["name"] for entry in architecture_registry["types"]})
        self.assertIn("Product-System Map", {entry["name"] for entry in architecture_registry["types"]})
        self.assertIn("Architecture Topic", architecture_skill)
        self.assertIn("Freeform Artifact", architecture_skill)
        self.assertEqual("adaptive", next(e for e in architecture_registry["types"] if e["id"] == "technical-architecture")["template"]["policy"])
        self.assertNotIn(
            "Draft Technical Architecture or an Architecture Topic as a Freeform Artifact",
            architecture_skill,
        )

    def test_system_profile_is_the_registered_system_readme(self) -> None:
        template = read(
            TECHNICAL_ROOT
            / "write-technical-doc/assets/system-profile-template.md"
        )
        for field in [
            "Purpose",
            "Owner",
            "Lifecycle",
            "Critical relationships",
            "Governance status",
            "Authoritative links",
        ]:
            self.assertIn(field, template)
        self.assertIn("System Responsibility README", template)
        self.assertIn("System Architecture", template)
        self.assertIn("Machine Authority", template)
        self.assertIn("Do not copy", template)

    def test_system_architecture_has_adaptive_template_with_explicit_completion_coverage(self) -> None:
        registry = yaml.safe_load(
            read(
                TECHNICAL_ROOT
                / "write-technical-doc/references/internal-document-types.yaml"
            )
        )
        system_architecture = next(
            entry for entry in registry["types"] if entry["id"] == "system-architecture"
        )
        method = read(
            TECHNICAL_ROOT
            / "write-technical-doc/references/system-architecture-method.md"
        )
        for type_id in ("system-architecture", "subsystem-architecture"):
            entry = next(item for item in registry["types"] if item["id"] == type_id)
            self.assertEqual("adaptive", entry["template"]["policy"])
            asset = (TECHNICAL_ROOT / "write-technical-doc/references" / entry["template"]["path"]).resolve()
            self.assertEqual(TECHNICAL_ROOT.parent / "methods/architecture-templates/assets", asset.parent)
            self.assertTrue(asset.is_file())
        for concept in [
            "non-goals",
            "external actors",
            "Applications",
            "Subsystems",
            "state",
            "consistency",
            "contracts",
            "commands",
            "events",
            "queries",
            "duplicate",
            "timeout",
            "ordering",
            "partial",
            "unknown",
            "permissions",
            "controls",
            "durable evidence",
            "deployment",
            "dependencies",
            "failure domains",
            "degradation",
            "recovery",
            "observability",
            "alternatives",
            "accepted costs",
            "validation",
            "operating evidence",
            "fitness",
            "review triggers",
            "compatibility",
            "migration",
            "evolution",
            "Machine Authority",
        ]:
            self.assertIn(concept, system_architecture["completion"] + method)

    def test_architecture_axes_are_separate_and_not_output_structure(self) -> None:
        method = read(REPO_ROOT / "methods/architecture-reasoning.md")
        technical_method = read(
            TECHNICAL_ROOT
            / "write-technical-architecture/references/technical-architecture-method.md"
        )
        combined = method + technical_method

        self.assertIn("Architecture Object", combined)
        self.assertIn("Architecture Scope", combined)
        self.assertIn("Architecture Viewpoint", combined)
        self.assertIn("Architecture View", combined)
        self.assertIn("Authority Level", combined)
        self.assertIn("correctness", combined)
        self.assertIn("coverage", combined)
        self.assertIn("not", combined)
        registry_path = TECHNICAL_ROOT / "write-technical-architecture/references/internal-document-types.yaml"
        registry = yaml.safe_load(read(registry_path))
        architecture = next(t for t in registry["types"] if t["id"] == "technical-architecture")
        self.assertEqual(architecture["template"]["policy"], "adaptive")
        assigned_template = registry_path.parent / architecture["template"]["path"]
        self.assertTrue(assigned_template.is_file())
        self.assertEqual(assigned_template.resolve().parent.name, "assets")

    def test_architecture_decisions_record_object_scope_and_authority(self) -> None:
        template = read(
            TECHNICAL_ROOT
            / "write-technical-doc/assets/architecture-decision-template.md"
        )
        self.assertIn("Architecture Object", template)
        self.assertIn("Governing Scope", template)
        self.assertIn("Authority Level", template)
        self.assertIn("Architecture Viewpoints", template)
        self.assertIn("narrowest", template)

    def test_ask_scribe_routes_architecture_levels_and_structure_requests(self) -> None:
        skill = read(TECHNICAL_ROOT / "ask-scribe/SKILL.md")

        for phrase in [
            "company overall architecture",
            "Product-System Map",
            "$Write Tech Arch",
            "System or Subsystem Architecture",
            "$Write Tech Doc",
            "Freeform Artifact",
            "Technical directory, navigation, scaffold, audit, or migration",
            "$Structure Tech Docs",
        ]:
            self.assertIn(phrase, skill)

    def test_system_architecture_remains_technical_documentation(self) -> None:
        method = read(REPO_ROOT / "methods/technical-reasoning.md")
        assessment = read(
            TECHNICAL_ROOT / "reason-technical/assets/technical-assessment-template.md"
        )
        inventory = read(
            TECHNICAL_ROOT
            / "structure-technical-docs/assets/technical-inventory-template.md"
        )

        self.assertIn("System Architecture", method)
        self.assertIn("Technical Documentation", method)
        self.assertIn("Registered System, Type Extension", method)
        self.assertNotIn(
            "Technical Documentation / Technical Knowledge / Project Documentation / System Architecture / Machine Authority",
            assessment + inventory,
        )


if __name__ == "__main__":
    unittest.main()
