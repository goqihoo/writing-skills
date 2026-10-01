import importlib.util
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/generate-architecture-template-catalog.py'
spec = importlib.util.spec_from_file_location('architecture_catalog', SCRIPT)
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


class ArchitectureTemplateFamiliesTest(unittest.TestCase):
    def test_reference_document_families_are_covered_by_real_assets(self):
        entries = catalog.knowledge_templates()
        expected = {
            'knowledge-set', 'view-overview', 'topic-index', 'domain-architecture',
            'application-architecture', 'subsystem-architecture', 'component-architecture',
            'engineering-strategy', 'technical-mechanism', 'governance-architecture',
            'security-governance', 'compliance-governance', 'risk-governance',
            'control-command', 'audit-evidence', 'runtime-architecture',
            'deployment-architecture', 'network-architecture', 'runtime-state-messaging',
            'observability-architecture', 'resilience-architecture', 'capacity-performance',
        }
        self.assertEqual(expected, {e['id'] for e in entries})
        headings = set()
        for entry in entries:
            path = ROOT / 'skills/write-architecture-knowledge/references' / entry['template']
            body = path.read_text()
            self.assertTrue(body.startswith('# ['), entry['id'])
            outline = tuple(line for line in body.splitlines() if line.startswith('## '))
            self.assertGreaterEqual(len(outline), 4, entry['id'])
            self.assertNotIn(outline, headings, entry['id'])
            headings.add(outline)

    def test_manifest_rejects_unreachable_and_dormant_assets(self):
        for corruption in ('missing', 'dormant', 'duplicate', 'escape'):
            with self.subTest(corruption=corruption), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                skill = root / 'skills/write-architecture-knowledge'
                shutil.copytree(ROOT / 'skills/write-architecture-knowledge', skill)
                manifest = skill / 'references/architecture-templates.yaml'
                config = yaml.safe_load(manifest.read_text())
                if corruption == 'missing':
                    (skill / 'references' / config['templates'][0]['template']).unlink()
                elif corruption == 'dormant':
                    (skill / 'assets/unused.md').write_text('# Unused\n')
                elif corruption == 'duplicate':
                    config['templates'].append(config['templates'][0])
                else:
                    (skill / 'references/outside.md').write_text('# Outside\n')
                    config['templates'][0]['template'] = 'outside.md'
                manifest.write_text(yaml.safe_dump(config))
                with self.assertRaises(ValueError):
                    catalog.knowledge_templates(root)

    def test_catalog_is_current(self):
        subprocess.run(['python3', str(SCRIPT), '--check'], check=True, capture_output=True)

    def test_project_and_stable_design_have_distinct_template_owners(self):
        def registry(owner):
            path = ROOT / 'skills' / owner / 'references/internal-document-types.yaml'
            return {e['id']: e for e in yaml.safe_load(path.read_text())['types']}
        project = registry('write-technical-architecture')
        stable = registry('write-technical-doc')
        for artifact in ('delivery-index', 'delivery-architecture', 'delivery-subsystem', 'delivery-component', 'delivery-deployment', 'delivery-migration', 'delivery-validation'):
            self.assertIn(artifact, project)
            self.assertNotIn(artifact, stable)
            self.assertIn('Project', project[artifact]['authority'])
        for artifact in ('system-architecture', 'subsystem-architecture', 'component-architecture'):
            self.assertIn(artifact, stable)
            self.assertNotIn(artifact, project)


if __name__ == '__main__':
    unittest.main()
