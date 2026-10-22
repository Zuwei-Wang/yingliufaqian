"""Check file invariants for the fictional full-run case; not visa eligibility.

Usage: python tests/check_simulation_artifacts.py FIXTURE_ROOT [--case CASE_DIR] [--stage final|initial-final|resume] [--layout separate|merged]
Requires pypdf. File-count expectations belong only to this synthetic scenario.
"""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path

from pypdf import PdfReader


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def page_digest(page):
    # Compare copied drawing/text content, independent of PDF container metadata.
    # Visual review is still needed for page resources and rendering.
    return hashlib.sha256(page.get_contents().get_data()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('fixture_root', type=Path)
    parser.add_argument('--case', type=Path)
    parser.add_argument('--stage', choices=['final', 'initial-final', 'resume'], default='final')
    parser.add_argument('--layout', choices=['separate', 'merged'], default='separate')
    parser.add_argument('--transport-source',
                        help='Fixture-relative replacement confirmation when the scenario supplies a corrected ticket')
    args = parser.parse_args()
    root = args.fixture_root.resolve()
    case = (args.case or root/'case').resolve()
    manifest_file = root/'all-input-hashes.json'
    if not manifest_file.exists():
        manifest_file = root/'source-hashes.json'
    original = json.loads(manifest_file.read_text())
    for name, expected in original.items():
        assert digest(root/name) == expected, f'Input changed: {name}'

    with (case/'文件索引.csv').open(newline='', encoding='utf-8-sig') as stream:
        rows = list(csv.DictReader(stream))
    seen = set()
    for row in rows:
        rel = row['相对路径']
        assert rel not in seen, f'Duplicate index path: {rel}'
        seen.add(rel)
        path = (case/rel).resolve()
        assert case in path.parents, f'Index escapes case: {rel}'
        assert path.is_file(), f'Indexed file missing: {rel}'
        assert digest(path) == row['SHA-256'], f'Index hash stale: {rel}'
        if path.suffix.lower() == '.pdf':
            assert len(PdfReader(path).pages) == int(row['页数']), f'Wrong page count: {rel}'

    selected = [
        'final-evidence/final-form.pdf', 'final-evidence/receipt.pdf',
        'final-evidence/appointment.pdf', 'final-evidence/insurance.pdf',
        'incoming/passport.pdf', 'incoming/status.pdf', 'incoming/student.pdf',
        'corrections/share-code.pdf', 'full-bank/bank-august.pdf',
        'full-bank/bank-september.pdf', 'full-bank/bank-october.pdf',
        'changed-dates/transport.pdf', 'changed-dates/hotel.pdf',
    ]
    if args.stage == 'initial-final':
        selected = [
            'portal/final-form.pdf', 'portal/receipt.pdf', 'portal/appointment.pdf',
            'corrections/insurance.pdf', 'incoming/passport.pdf', 'incoming/status.pdf',
            'incoming/student.pdf', 'corrections/share-code.pdf',
            'full-bank/bank-august.pdf', 'full-bank/bank-september.pdf',
            'full-bank/bank-october.pdf', 'incoming/transport.pdf', 'corrections/hotel.pdf',
        ]
    if args.stage == 'resume':
        selected = [
            'portal/final-form.pdf', 'portal/receipt.pdf',
            'incoming/passport.pdf', 'incoming/status.pdf', 'incoming/student.pdf',
            'corrections/share-code.pdf', 'incoming/bank-august.pdf',
            'corrections/bank-september.pdf', 'corrections/bank-october.pdf',
            'incoming/transport.pdf', 'corrections/hotel.pdf', 'corrections/insurance.pdf',
        ]
        assert all(row.get('清单项ID') for row in rows), 'A file lacks a checklist mapping'
        assert all(row.get('版本角色') for row in rows), 'A file lacks a version role'
    if args.transport_source:
        replacement = (root/args.transport_source).resolve()
        assert root in replacement.parents and replacement.is_file(), 'Replacement transport must be inside fixtures'
        positions = [i for i, name in enumerate(selected)
                     if name in ('incoming/transport.pdf', 'changed-dates/transport.pdf')]
        assert len(positions) == 1, 'Expected one transport source in this scenario'
        selected[positions[0]] = args.transport_source
    active = list((case/'04_打印材料').glob('*.pdf'))
    if args.layout == 'separate':
        counts = Counter(digest(p) for p in active)
        assert len(active) == len(selected)+1, f'Expected {len(selected)} selected documents and one itinerary; got {len(active)}'
        for name in selected:
            assert counts[digest(root/name)] == 1, f'Missing or repeated current print item: {name}'
    else:
        assert len(active) == 1, 'Merged delivery must not duplicate its component PDFs in the print folder'
        pages = list(PdfReader(active[0]).pages)
        expected = Counter(page_digest(page) for name in selected for page in PdfReader(root/name).pages)
        actual = Counter(page_digest(page) for page in pages)
        assert len(pages) == sum(expected.values()) + 1, 'Unexpected merged page count (one generated itinerary expected)'
        for fingerprint, count in expected.items():
            assert actual[fingerprint] == count, 'Missing, changed or repeated source page in merged pack'
        assert sum((actual - expected).values()) == 1, 'Unexpected pages beyond itinerary'
    for path in active:
        assert path.relative_to(case).as_posix() in seen, f'Print file not indexed: {path.name}'
    # Dates, physical signature, eligibility and website state still require semantic review.
    print(json.dumps({
        'input_files_unchanged': len(original), 'indexed_files_verified': len(rows),
        'current_print_files': len(active), 'current_print_pages': sum(len(PdfReader(p).pages) for p in active),
        'current_selected_sources_unique': len(selected),
        'stage': args.stage,
        'layout': args.layout,
        'scope': 'synthetic file integrity only; no official or hosted CI result',
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
