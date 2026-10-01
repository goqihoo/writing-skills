import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]

EXPECTED_TYPE_IDS = {
    "write-product-doc": {
        "product-portfolio",
        "products-registry",
        "product-governance",
        "product-definition",
        "capability-detail",
        "evidence-record",
        "product-decision",
        "product-release-plan",
        "release-notes",
        "product-review",
    },
    "write-technical-architecture": {
        "technical-architecture",
        "product-system-map",
        "delivery-index",
        "delivery-architecture",
        "delivery-subsystem",
        "delivery-component",
        "delivery-deployment",
        "delivery-migration",
        "delivery-validation",
    },
    "write-technical-doc": {
        "technical-strategy",
        "technical-roadmap",
        "system-landscape",
        "system-profile",
        "system-architecture",
        "subsystem-architecture",
        "component-architecture",
        "technical-governance",
        "technical-standard",
        "architecture-decision",
        "governance-exception",
        "incident-record-review",
    },
}


def registry_path(owner_skill: str) -> Path:
    return (
        REPO_ROOT
        / "skills"
        / owner_skill
        / "references"
        / "internal-document-types.yaml"
    )


def load_registry(owner_skill: str) -> dict:
    return yaml.safe_load(registry_path(owner_skill).read_text(encoding="utf-8"))


class InternalDocumentTypeRegistryTest(unittest.TestCase):
    def test_registries_define_exact_type_sets_and_active_templates(self) -> None:
        for owner_skill, expected_ids in EXPECTED_TYPE_IDS.items():
            with self.subTest(owner_skill=owner_skill):
                registry = load_registry(owner_skill)
                self.assertEqual(1, registry["schema_version"])
                self.assertEqual(owner_skill, registry["owner_skill"])
                self.assertTrue(registry["model"].strip())

                entries = registry["types"]
                actual_ids = {entry["id"] for entry in entries}
                self.assertEqual(expected_ids, actual_ids)
                self.assertEqual(len(entries), len(actual_ids))
                self.assertEqual(len(entries), len({entry["name"] for entry in entries}))

                referenced_templates = set()
                for entry in entries:
                    self.assertRegex(entry["id"], r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
                    for field in [
                        "name",
                        "description",
                        "reader_question",
                        "authority",
                        "completion",
                    ]:
                        self.assertTrue(entry[field].strip(), (owner_skill, entry["id"], field))

                    template = entry.get("template")
                    if template is None:
                        continue
                    self.assertIn(template["policy"], {"fixed", "sequence", "adaptive"})
                    template_path = registry_path(owner_skill).parent / template["path"]
                    self.assertTrue(template_path.is_file(), template_path)
                    referenced_templates.add(template_path.resolve())

                bundled_templates = {
                    path.resolve()
                    for path in (REPO_ROOT / "skills" / owner_skill / "assets").glob("*.md")
                }
                local_assets = (REPO_ROOT / "skills" / owner_skill / "assets").resolve()
                shared_assets = (REPO_ROOT / "methods/architecture-templates/assets").resolve()
                self.assertTrue(all(p.parent in (local_assets, shared_assets) for p in referenced_templates))
                self.assertEqual({p for p in referenced_templates if p.parent == local_assets}, bundled_templates)

    def test_generator_rejects_invalid_shared_assignments(self) -> None:
        for corruption in ("unregistered", "outside", "missing"):
            with self.subTest(corruption=corruption), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                shutil.copytree(REPO_ROOT / "scripts", root / "scripts")
                for owner in EXPECTED_TYPE_IDS:
                    shutil.copytree(REPO_ROOT / "skills" / owner, root / "skills" / owner)
                shared = root / "methods/architecture-templates"
                shutil.copytree(REPO_ROOT / "methods/architecture-templates", shared)
                registry = root / "skills/write-technical-architecture/references/internal-document-types.yaml"
                config = yaml.safe_load(registry.read_text())
                if corruption == "unregistered":
                    target = shared / "assets/unregistered.md"
                    target.write_text("# Unregistered\n")
                elif corruption == "outside":
                    target = shared / "outside.md"
                    target.write_text("# Outside\n")
                else:
                    target = shared / "assets/missing.md"
                config["types"][0]["template"]["path"] = str(target)
                registry.write_text(yaml.safe_dump(config))
                result = subprocess.run(
                    ["python3", str(root / "scripts/generate-internal-document-types.py"), "--check"],
                    capture_output=True, text=True,
                )
                self.assertEqual(1, result.returncode)
                self.assertIn("error:", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_catalog_is_generated_from_the_registries(self) -> None:
        subprocess.run(
            [
                "python3",
                str(REPO_ROOT / "scripts/generate-internal-document-types.py"),
                "--check",
            ],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

    def test_generator_reports_malformed_registry_without_traceback(self) -> None:
        malformed_registries = {
            "top-level scalar": "not-a-mapping\n",
            "non-mapping type": (
                "schema_version: 1\n"
                "owner_skill: write-product-doc\n"
                "model: Product Documentation\n"
                "types:\n"
                "  - not-a-mapping\n"
            ),
        }

        for label, registry_text in malformed_registries.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                script = root / "scripts/generate-internal-document-types.py"
                script.parent.mkdir(parents=True)
                shutil.copy2(
                    REPO_ROOT / "scripts/generate-internal-document-types.py",
                    script,
                )
                registry = (
                    root
                    / "skills/write-product-doc/references/internal-document-types.yaml"
                )
                registry.parent.mkdir(parents=True)
                registry.write_text(registry_text, encoding="utf-8")

                result = subprocess.run(
                    ["python3", str(script), "--check"],
                    cwd=root,
                    capture_output=True,
                    text=True,
                )

                self.assertEqual(1, result.returncode)
                self.assertIn("error:", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_domain_and_knowledge_models_remain_outside_yaml_registry(self) -> None:
        self.assertFalse(registry_path("write-domain-doc").exists())
        self.assertFalse(registry_path("write-knowledge").exists())
        self.assertTrue(
            (REPO_ROOT / "skills/write-domain-doc/references/domain-document-types.md").is_file()
        )
        self.assertTrue(
            (REPO_ROOT / "skills/write-knowledge/references/knowledge-types.md").is_file()
        )


if __name__ == "__main__":
    unittest.main()
