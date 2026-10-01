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
        entries = catalog.architecture_templates()
        expected = {
            'knowledge-set', 'view-overview', 'topic-index', 'domain-architecture',
            'overall-architecture', 'data-architecture', 'integration-architecture',
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
            path = ROOT / catalog.SHARED / entry['template']
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
                skill = root / catalog.SHARED
                shutil.copytree(ROOT / catalog.SHARED, skill)
                manifest = skill / 'templates.yaml'
                config = yaml.safe_load(manifest.read_text())
                if corruption == 'missing':
                    (skill / config['templates'][0]['template']).unlink()
                elif corruption == 'dormant':
                    (skill / 'assets/unused.md').write_text('# Unused\n')
                elif corruption == 'duplicate':
                    config['templates'].append(config['templates'][0])
                else:
                    (skill / 'outside.md').write_text('# Outside\n')
                    config['templates'][0]['template'] = 'outside.md'
                manifest.write_text(yaml.safe_dump(config))
                with self.assertRaises(ValueError):
                    catalog.architecture_templates(root)

    def test_shared_assignments_resolve_in_source_and_packaged_layouts(self):
        for root in (ROOT, ROOT / 'plugins/scribe'):
            entries = {e['id']: (root / catalog.SHARED / e['template']).resolve()
                       for e in catalog.architecture_templates(root)}
            mappings = {
                'write-technical-architecture': {
                    'technical-architecture': 'overall-architecture',
                    'delivery-architecture': 'overall-architecture',
                    'delivery-subsystem': 'subsystem-architecture',
                    'delivery-component': 'component-architecture',
                    'delivery-deployment': 'deployment-architecture',
                },
                'write-technical-doc': {
                    'system-architecture': 'overall-architecture',
                    'subsystem-architecture': 'subsystem-architecture',
                    'component-architecture': 'component-architecture',
                },
            }
            for owner, assignments in mappings.items():
                registry = root / 'skills' / owner / 'references/internal-document-types.yaml'
                types = {e['id']: e for e in yaml.safe_load(registry.read_text())['types']}
                for type_id, shared_id in assignments.items():
                    assigned = (registry.parent / types[type_id]['template']['path']).resolve()
                    self.assertEqual(entries[shared_id], assigned)
                    self.assertTrue(assigned.is_file())
                    self.assertFalse((registry.parent.parent / 'assets' / (type_id + '-template.md')).exists())
            self.assertFalse((root / 'skills/write-architecture-knowledge/references/architecture-templates.yaml').exists())
            self.assertFalse(list((root / 'skills/write-architecture-knowledge/assets').glob('*.md')))

    def test_catalog_is_current(self):
        subprocess.run(['python3', str(SCRIPT), '--check'], check=True, capture_output=True)

    def test_project_and_stable_design_keep_distinct_artifact_authorities(self):
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
