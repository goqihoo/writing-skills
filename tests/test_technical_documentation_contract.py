import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TECHNICAL_ROOT = REPO_ROOT / "skills"
FOUNDATIONS_ROOT = REPO_ROOT / "skills"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class TechnicalDocumentationContractTest(unittest.TestCase):
    def test_technical_structure_classifies_responsibilities_and_events(self) -> None:
        model = read(
            TECHNICAL_ROOT
            / "structure-technical-docs/references/technical-structure-model.md"
        )
        core = model.split("## Stable Responsibilities", 1)[1].split(
            "## Type Extensions", 1
        )[0]
        extensions = model.split("## Type Extensions", 1)[1].split(
            "## Event Collections", 1
        )[0]
        events = model.split("## Event Collections", 1)[1].split(
            "## Materialization rules", 1
        )[0]

        for directory in ["Strategy/", "Architecture/", "Systems/", "Governance/"]:
            self.assertIn(directory, core)
        for directory in [
            "Platforms/",
            "Engineering/",
            "Data/",
            "Security/",
            "Quality/",
            "Operations/",
        ]:
            self.assertIn(directory, extensions)
        for event in [
            "Architecture/Decisions/",
            "Governance/Exceptions/",
            "Operations/Incidents/",
        ]:
            self.assertIn(event, events)

        self.assertIn("first real event", events.lower())
        self.assertIn("parent responsibility", events.lower())

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

    def test_technical_writer_covers_every_internal_document_type(self) -> None:
        root = TECHNICAL_ROOT / "write-technical-doc"
        reference = read(root / "references/technical-document-types.md")
        internal_types = [
            "Technical navigation",
            "Technical Strategy",
            "Technical Roadmap",
            "System Landscape",
            "System Profile",
            "Technical Operating Model",
            "Technical Governance",
            "Technical Standard",
            "Platform Definition",
            "Engineering Practice",
            "Data Governance",
            "Security Governance",
            "Quality Model",
            "Operations Model",
            "Architecture Decision",
            "Governance Exception",
            "Incident Record/Review",
        ]
        for document_type in internal_types:
            self.assertRegex(
                reference,
                rf"(?m)^\| {re.escape(document_type)} \| .*\.md \|",
            )

        routed_templates = {
            line.split("|")[2].strip()
            for line in reference.splitlines()
            if line.startswith("|") and ".md |" in line
        }
        self.assertEqual(
            routed_templates,
            {path.name for path in (root / "assets").glob("*.md")},
        )

    def test_system_profile_links_downstream_authority_without_copying_it(self) -> None:
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
        self.assertIn("Machine Authority", template)
        self.assertIn("Do not copy", template)


if __name__ == "__main__":
    unittest.main()
