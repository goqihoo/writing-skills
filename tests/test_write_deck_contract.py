import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills/write-deck"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class WriteDeckContractTest(unittest.TestCase):
    def test_write_deck_is_an_explicit_general_markdown_artifact(self) -> None:
        skill = read(SKILL_ROOT / "SKILL.md")
        metadata = read(SKILL_ROOT / "agents/openai.yaml")

        self.assertIn("name: write-deck", skill)
        self.assertIn("disable-model-invocation: true", skill)
        self.assertIn('display_name: "Write Deck"', metadata)
        self.assertIn("allow_implicit_invocation: false", metadata)
        self.assertIn("presentation manuscript in Markdown", skill)
        self.assertIn("business", skill)
        self.assertIn("product", skill)
        self.assertIn("technical", skill)
        self.assertIn("learning", skill)
        self.assertIn("PowerPoint", skill)
        self.assertIn("Keynote", skill)

    def test_deck_method_and_template_separate_logic_from_production_fields(self) -> None:
        skill = read(SKILL_ROOT / "SKILL.md")
        method = read(SKILL_ROOT / "references/deck-writing-method.md")
        template = read(SKILL_ROOT / "assets/deck-manuscript-template.md")

        self.assertIn("references/deck-writing-method.md", skill)
        self.assertIn("assets/deck-manuscript-template.md", skill)
        for concept in [
            "communication job",
            "delivery mode",
            "narrative path",
            "title sequence",
            "adjacent",
            "screen copy",
            "speaker support",
            "transition",
            "source",
        ]:
            self.assertIn(concept, method)

        for field in [
            "Audience",
            "Delivery mode",
            "Audience outcome",
            "Central point",
            "Narrative path",
            "Slide job",
            "Screen copy",
            "Speaker support",
            "Transition",
            "Source notes",
        ]:
            self.assertIn(field, template)

        self.assertNotIn("Avalanche", method + template)
        self.assertNotIn("Team1", method + template)

    def test_catalog_routes_presentation_manuscripts_to_write_deck(self) -> None:
        readme = read(REPO_ROOT / "README.md")
        ask_scribe = read(REPO_ROOT / "skills/ask-scribe/SKILL.md")
        instructions = read(REPO_ROOT / "AGENTS.md")
        architecture = read(REPO_ROOT / "docs/scribe-skill-architecture.md")

        self.assertIn("24 Public Skills", readme)
        self.assertIn("[Write Deck](skills/write-deck/SKILL.md)", readme)
        self.assertIn("Write Deck", ask_scribe)
        self.assertIn("$Write Deck", ask_scribe)
        self.assertIn("presentation manuscript", ask_scribe)
        self.assertIn("write-deck", instructions)
        self.assertIn("presentation manuscript", instructions)
        self.assertIn("presentation manuscript", architecture)
        self.assertIn("derived expression", architecture)


if __name__ == "__main__":
    unittest.main()
