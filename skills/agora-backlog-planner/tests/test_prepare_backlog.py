"""Synthetic workbook tests; never contacts GitHub."""
import csv
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('prepare_backlog', ROOT / 'scripts/prepare_backlog.py')
planner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(planner)


class PlannerTests(unittest.TestCase):
    def setUp(self):
        self.config = json.loads((ROOT / 'examples/project.example.json').read_text())
        self.run = json.loads((ROOT / 'examples/run.example.json').read_text())
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'synthetic.csv'
        self.path.write_text((ROOT / 'examples/synthetic-requirements.csv').read_text())
        self.run['workbook'] = str(self.path)

    def prepare(self):
        return planner.prepare(self.config, self.run)

    def rewrite(self, change):
        with self.path.open(newline='') as f:
            rows = list(csv.reader(f))
        change(rows)
        with self.path.open('w', newline='') as f:
            csv.writer(f).writerows(rows)

    def test_explicit_selection_and_layer_specialization(self):
        result = self.prepare()
        self.assertEqual([r['requirement_id'] for r in result['requirements']], ['SYN-HU-001', 'SYN-HU-002'])
        first, second = result['requirements']
        self.assertEqual([p['layer'] for p in first['packets']], ['CRUD', 'MID', 'FRONT'])
        self.assertEqual([p['layer'] for p in second['packets']], ['MID', 'FRONT'])
        self.assertEqual(len({p['responsibility_guide'] for p in first['packets']}), 3)
        self.assertTrue(all(len(p['siblings']) == 2 for p in first['packets']))
        self.assertNotIn('Developed', first['packets'][0]['proposed_fields'])
        self.assertIsNone(first['packets'][0]['proposed_fields']['Estimate'])

    def test_dry_run_default_and_apply_rejected_before_read(self):
        del self.run['mode']
        self.assertEqual(self.prepare()['mode'], 'dry-run')
        self.run.update(mode='apply', workbook='does-not-exist.xlsx', enable_writes=True)
        with self.assertRaisesRegex(ValueError, 'apply'):
            self.prepare()

    def test_ambiguous_empty_and_invalid_selection(self):
        invalid = [{}, {'requirement_ids': []}, {'requirement_ids': ['SYN-HU-001'], 'row_range': {'start': 2, 'end': 3}}, {'start_row': 2}, {'start_row': True, 'count': 1}, {'row_range': {'start': 3, 'end': 2}}, {'requirement_ids': ['SYN-HU-001'] , 'count': 1}]
        for selection in invalid:
            with self.subTest(selection=selection), self.assertRaises(ValueError):
                planner.validate_selection(selection)

    def test_row_range_and_count_are_physical_and_equivalent(self):
        self.run['selection'] = {'row_range': {'start': 2, 'end': 3}}
        ranged = self.prepare()['requirements']
        self.run['selection'] = {'start_row': 2, 'count': 2}
        self.assertEqual(ranged, self.prepare()['requirements'])
        self.run['selection'] = {'start_row': 1, 'count': 1}
        with self.assertRaises(ValueError):
            self.prepare()

    def test_duplicate_and_missing_ids(self):
        for ids in [['SYN-HU-001', 'SYN-HU-001'], ['UNKNOWN']]:
            self.run['selection'] = {'requirement_ids': ids}
            with self.assertRaises(ValueError):
                self.prepare()
        self.run['selection'] = {'requirement_ids': ['SYN-HU-001']}
        self.rewrite(lambda rows: rows.append(rows[1]))
        with self.assertRaisesRegex(ValueError, 'duplicado'):
            self.prepare()

    def test_invalid_repo_priority_and_formula(self):
        for col, value in [(3, 'https://github.com/udistrital/agora_crud'), (8, '5'), (1, '=HYPERLINK("bad")')]:
            original = self.path.read_text()
            self.rewrite(lambda rows: rows[1].__setitem__(col, value))
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.prepare()
            self.path.write_text(original)

    def test_missing_link_preserves_composite_trace_and_gap(self):
        hu = self.prepare()['requirements'][0]
        self.assertEqual(hu['hu_source']['type'], 'COMPOSITE_REFERENCE')
        self.assertEqual(hu['hu_source']['row'], 2)
        self.assertTrue(any('ACCESSIBILITY_UNVERIFIED' in gap for gap in hu['gaps']))

    def test_missing_context_never_fabricates_readiness(self):
        self.rewrite(lambda rows: rows[1].__setitem__(1, ''))
        hu = self.prepare()['requirements'][0]
        self.assertIn('DESCRIPTION_MISSING: NOT_READY', hu['gaps'])
        self.assertIn('EVIDENCE_BASED_DOR', hu['packets'][0]['required_analysis'])

    def test_estimates_and_decomposition(self):
        for value in planner.POINTS:
            self.assertEqual(planner.validate_estimate(value), 'VALID')
        self.assertEqual(planner.validate_estimate(21), 'DECOMPOSE')
        for value in [0, -1, 4, 12, True, 5.0, '5', None]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                planner.validate_estimate(value)

    def test_developed_guard_and_fixed_scale(self):
        self.config['project_fields']['developed_is_read_only'] = False
        with self.assertRaisesRegex(ValueError, 'Developed'):
            self.prepare()
        self.config['project_fields']['developed_is_read_only'] = True
        self.config['estimation']['allowed_points'].append(21)
        with self.assertRaises(ValueError):
            self.prepare()

    def test_header_mapping_is_configurable(self):
        self.rewrite(lambda rows: rows[0].__setitem__(0, 'Arbitrary ID'))
        self.config['mapping']['columns']['requirement_id'] = 'Arbitrary ID'
        self.assertEqual(len(self.prepare()['requirements']), 2)

    def test_malformed_config_fails_explicitly(self):
        self.config['mapping'] = []
        with self.assertRaisesRegex(ValueError, 'mapping'):
            self.prepare()

    def test_blank_selected_row_and_unheaded_data_rejected(self):
        self.rewrite(lambda rows: rows.append([]))
        self.run['selection'] = {'row_range': {'start': 5, 'end': 5}}
        with self.assertRaises(ValueError):
            self.prepare()
        self.run['selection'] = {'requirement_ids': ['SYN-HU-001']}
        self.rewrite(lambda rows: rows[1].append('unheaded context'))
        with self.assertRaisesRegex(ValueError, 'encabezado'):
            self.prepare()

    def test_cli_has_no_partial_stdout_on_error(self):
        self.run['mode'] = 'apply'
        run_path = Path(self.temp.name) / 'run.json'
        run_path.write_text(json.dumps(self.run))
        proc = subprocess.run([sys.executable, str(ROOT / 'scripts/prepare_backlog.py'), '--config', str(ROOT / 'examples/project.example.json'), '--run', str(run_path)], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 2)
        self.assertEqual(proc.stdout, '')
        self.assertIn('apply', proc.stderr)

    def test_xlsx_values_selection_merged_and_formula(self):
        try:
            from openpyxl import Workbook
        except ImportError:
            self.skipTest('openpyxl no instalado')
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = 'Synthetic'
        with self.path.open(newline='') as f:
            for row in csv.reader(f):
                sheet.append(row)
        xlsx = Path(self.temp.name) / 'synthetic.xlsx'
        workbook.save(xlsx)
        self.run['workbook'] = str(xlsx)
        self.assertEqual(len(self.prepare()['requirements']), 2)
        self.run['sheet'] = 'missing'
        with self.assertRaisesRegex(ValueError, 'Hoja'):
            self.prepare()
        self.run['sheet'] = 'Synthetic'
        sheet['A2'] = 34
        workbook.save(xlsx)
        with self.assertRaisesRegex(ValueError, 'ID debe ser texto'):
            self.prepare()
        sheet['A2'] = 'SYN-HU-001'
        sheet['B2'] = '=1+1'
        workbook.save(xlsx)
        with self.assertRaisesRegex(ValueError, 'Fórmula'):
            self.prepare()
        sheet['B2'] = 'SYNTHETIC context'
        sheet.merge_cells('B2:C2')
        workbook.save(xlsx)
        with self.assertRaisesRegex(ValueError, 'combinadas'):
            self.prepare()
        workbook.close()


if __name__ == '__main__':
    unittest.main()
