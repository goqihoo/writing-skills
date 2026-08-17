import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills/foundations/reason-domain"
STRUCTURE_ROOT = REPO_ROOT / "skills/knowledge/structure-domain-docs"
WRITE_ROOT = REPO_ROOT / "skills/knowledge/write-domain-doc"
ARCHITECTURE_DOC = REPO_ROOT / "docs/domain-knowledge-skill-architecture.md"


class ReasonDomainContractTest(unittest.TestCase):
    def test_skill_owns_domain_assessment(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        metadata = (SKILL_ROOT / "agents/openai.yaml").read_text(encoding="utf-8")

        self.assertIn("name: reason-domain", skill)
        self.assertIn("disable-model-invocation: true", skill)
        self.assertNotIn("Apply `$Write Doc`", skill)
        self.assertIn("references/domain-reasoning-method.md", skill)
        self.assertIn("assets/domain-assessment-template.md", skill)
        self.assertIn('display_name: "Reason Domain"', metadata)
        self.assertIn("$Reason Domain", metadata)
        self.assertIn("allow_implicit_invocation: false", metadata)

    def test_reasoning_method_defines_the_domain_decision_contract(self) -> None:
        method = (SKILL_ROOT / "references/domain-reasoning-method.md").read_text(
            encoding="utf-8"
        )

        for criterion in [
            "Minimum purpose",
            "Core objects or activities",
            "Shared language and constraints",
            "Change authority",
            "Boundary and handoffs",
            "Reusability",
        ]:
            self.assertIn(criterion, method)

        for relation in ["Parent or child", "Related", "Handoff"]:
            self.assertIn(relation, method)

        for maturity in ["Emerging", "Building", "Stable", "Review required"]:
            self.assertIn(maturity, method)

    def test_domain_assessment_is_the_handoff(self) -> None:
        template = (SKILL_ROOT / "assets/domain-assessment-template.md").read_text(
            encoding="utf-8"
        )

        required_sections = [
            "## Decision",
            "## Domain boundary",
            "## Admission evidence",
            "## Relationships and handoffs",
            "## Subdomain decisions",
            "## Knowledge ownership",
            "## Maturity and review triggers",
            "## Unresolved questions",
        ]
        positions = [template.index(section) for section in required_sections]
        self.assertEqual(positions, sorted(positions))

    def test_domain_structure_and_writing_require_explicit_domain_reasoning(self) -> None:
        structure_skill = (STRUCTURE_ROOT / "SKILL.md").read_text(encoding="utf-8")
        structure_metadata = (
            STRUCTURE_ROOT / "agents/openai.yaml"
        ).read_text(encoding="utf-8")
        write_skill = (WRITE_ROOT / "SKILL.md").read_text(encoding="utf-8")
        write_metadata = (WRITE_ROOT / "agents/openai.yaml").read_text(
            encoding="utf-8"
        )

        self.assertIn("`$Reason Domain`", structure_skill)
        self.assertIn("$Reason Domain", structure_metadata)
        self.assertIn("`$Reason Domain`", write_skill)
        self.assertIn("$Reason Domain", write_metadata)
        self.assertIn("ready-to-type explicit invocation", structure_skill)
        self.assertIn("ready-to-type explicit invocation", write_skill)
        self.assertNotIn("invoke `$Write Domain Doc`", structure_skill)

    def test_plugin_guides_and_architecture_expose_the_design(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
        )
        surfaces = "\n".join(
            path.read_text(encoding="utf-8")
            for path in [
                REPO_ROOT / "README.md",
                REPO_ROOT / "skills/foundations/README.md",
                REPO_ROOT / "skills/foundations/ask-scribe/SKILL.md",
            ]
        )
        architecture = ARCHITECTURE_DOC.read_text(encoding="utf-8")

        self.assertIn("./skills/foundations/reason-domain", manifest["skills"])
        self.assertIn("reason-domain", surfaces)
        self.assertIn("Domain Assessment", architecture)
        self.assertIn("structure-domain-docs", architecture)
        self.assertIn("write-domain-doc", architecture)
        self.assertIn("Do not split the ten document types", architecture)


if __name__ == "__main__":
    unittest.main()
