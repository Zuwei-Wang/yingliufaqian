"""Create visibly fictional PDF fixtures outside the source tree. Requires reportlab.

Usage: python tests/build_simulation_fixtures.py /tmp/yingliufaqian-forward-UNIQUE
These are test inputs, never official documents or visa requirements.
"""
import hashlib
import json
import argparse
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def pdf(path, title, lines):
    path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(path), pagesize=A4)
    c.setTitle("SIMULATION ONLY - " + title)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(36, 800, "SIMULATION ONLY - NOT VALID FOR ANY APPLICATION")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(36, 770, title)
    c.setFont("Helvetica", 10)
    for i, line in enumerate(lines):
        c.drawString(36, 740 - i * 19, line)
    c.setFont("Helvetica", 9)
    c.drawString(36, 32, "Fictional test evidence. No issuer, booking, signature or official authority.")
    c.save()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    parser.add_argument('--university', default='fictional Example Leeds University',
                        help='Scenario school name only; never an issuer of these test PDFs')
    parser.add_argument('--refundable-test-bookings', action='store_true',
                        help='Add fictional fare/refund facts for the letter-choice planning scenario')
    args = parser.parse_args()
    root = args.output.expanduser().resolve()
    repo = Path(__file__).resolve().parents[1]
    if root == repo or repo in root.parents:
        raise SystemExit("Fixture output must be outside the source tree")
    root.mkdir(parents=True, exist_ok=False)
    inputs = {
        "incoming/passport.pdf": ("Travel document facts", [
            "Name: ALEX CHEN; nationality: Chinese; ordinary passport; adult, age 21.",
            "Issued 2022-06-01; expires 2032-05-31; 4 blank pages.",
            "Identity and all marked pages: 1 simulated page. No real passport number."]),
        "incoming/student.pdf": ("Student status", [
            f"Fictional applicant ALEX CHEN; scenario university: {args.university}.",
            "Full-time enrolled. NOT a certificate issued by the named university.",
            "Course: BSc Computer Science; course ends 2027-06-30.",
            "Issued 2026-10-20. Test fact: school signature and contact details verified."]),
        "incoming/status.pdf": ("UK immigration status", [
            "Name: ALEX CHEN; UK Student permission expires 2027-10-31.",
            "Issued 2026-10-21. Test fact: identity photo visible in the real-world equivalent."]),
        "incoming/bank-august.pdf": ("August statement", [
            "Name: ALEX CHEN; address: 1 Example Road, Leeds, TEST ADDRESS.",
            "UK current account; period 2026-08-01 to 2026-08-31.",
            "Opening GBP 4200; closing GBP 4000. Statement has one page."]),
        "incoming/bank-september.pdf": ("September statement", []),
        "incoming/bank-october.pdf": ("Current balance screenshot", [
            "Balance GBP 3600 on 2026-10-21. No statement period or address supplied."]),
        "incoming/transport.pdf": ("Return transport", [
            "Passenger: ALEX CHEN. Simulated confirmed booking.",
            "Outbound London to Paris 2026-12-12; return Paris to London 2026-12-16."]),
        "incoming/hotel.pdf": ("Accommodation", [
            "Guest: ALEX CHEN. Simulated confirmed booking.",
            "Example Paris Hotel, 1 Fictional Street, Paris, TEST ADDRESS.",
            "Check-in 2026-12-12; check-out 2026-12-15. Three nights."]),
        "incoming/insurance.pdf": ("Travel insurance", [
            "Insured person: JAMIE LI.",
            "Valid 2026-12-12 to 2026-12-16. All Schengen states; medical cover EUR 100000.",
            "Includes emergency treatment, hospital care and medical repatriation."]),
        "corrections/bank-september.pdf": ("September statement", [
            "Name: ALEX CHEN; address: 1 Example Road, Leeds, TEST ADDRESS.",
            "UK current account; period 2026-09-01 to 2026-09-30.",
            "Opening GBP 4000; closing GBP 3800. Statement has one page."]),
        "corrections/bank-october.pdf": ("October interim statement", [
            "Name: ALEX CHEN; address: 1 Example Road, Leeds, TEST ADDRESS.",
            "UK current account; period 2026-10-01 to 2026-10-21.",
            "Opening GBP 3800; closing GBP 3600. Statement has one page."]),
        "corrections/hotel.pdf": ("Accommodation corrected", [
            "Guest: ALEX CHEN. Simulated confirmed booking.",
            "Example Paris Hotel, 1 Fictional Street, Paris, TEST ADDRESS.",
            "Check-in 2026-12-12; check-out 2026-12-16. Four nights."]),
        "corrections/insurance.pdf": ("Travel insurance corrected", [
            "Insured person: ALEX CHEN.",
            "Valid 2026-12-12 to 2026-12-16. All Schengen states; medical cover EUR 100000.",
            "Includes emergency treatment, hospital care and medical repatriation."]),
        "corrections/share-code.pdf": ("Share code evidence", [
            "Name: ALEX CHEN; purpose: other / immigration status.",
            "Created 2026-10-21; expires 2027-01-19; no usable share code in this fixture."]),
        "portal/individual-checklist.pdf": ("Scenario-specific checklist - NOT official guidance", [
            "Test application TEST-CASE-A; ALEX CHEN; tourism; France only; UK resident.",
            "For this scenario only, require these items in the following order:",
            "1. Final application form, printed, dated and signed by applicant.",
            "2. Registration receipt, one printed copy. 3. Appointment confirmation, one copy.",
            "4. Passport original and one copy of identity/all marked pages; two recent photos.",
            "5. UK eVisa status and current share code, one printed copy each.",
            "6. Signed university status letter, original plus one copy, issued within 30 days.",
            "7. UK bank statements: August, September and October-to-date accepted in this test.",
            "8. Confirmed return transport. 9. Accommodation for every night. 10. Trip programme.",
            "11. Insurance for applicant, all Schengen, whole trip, EUR 30000 medical minimum",
            "with emergency care and medical repatriation. Items 7-11: one full printed copy each.",
            "In this scenario, no sponsor papers: applicant self-funds, stated trip budget GBP 800.",
            "A4 single-sided; legible colour or monochrome accepted for this simulated checklist.",
            "These synthetic parameters must never be presented as real official requirements."]),
        "portal/final-form.pdf": ("Final application form - simulated", [
            "TEST-CASE-A; ALEX CHEN; Chinese adult; ordinary passport; UK Student resident.",
            "Tourism, France only, 2026-12-12 to 2026-12-16; first entry France.",
            "Hotel: Example Paris Hotel, 1 Fictional Street, Paris.",
            "Self-funded GBP 800; all personal fields verified by simulated applicant.",
            "Applicant signature: NOT SIGNED; date: NOT ENTERED."]),
        "portal/receipt.pdf": ("Registration receipt", [
            "TEST-CASE-A; ALEX CHEN; simulated final submission complete.",
            "Trip 2026-12-12 to 2026-12-16; no real application was submitted."]),
        "portal/appointment.pdf": ("Appointment confirmation", [
            "TEST-CASE-A; ALEX CHEN; simulated booking CONFIRMED; service fee PAID.",
            "Manchester; 2026-11-09 10:00 Europe/London; one applicant.",
            "Address: TEST VENUE ONLY, Manchester. Never use this as a real address.",
            "Optional services: none. This is not a real TLScontact confirmation."]),
        "changed-dates/transport.pdf": ("Return transport revised", [
            "Passenger: ALEX CHEN. Simulated confirmed revised booking.",
            "Outbound London to Paris 2026-12-13; return Paris to London 2026-12-17."]),
        "changed-dates/hotel.pdf": ("Accommodation revised", [
            "Guest: ALEX CHEN. Simulated confirmed revised booking.",
            "Example Paris Hotel, 1 Fictional Street, Paris, TEST ADDRESS.",
            "Check-in 2026-12-13; check-out 2026-12-17. Four nights."]),
    }
    for name, (title, lines) in inputs.items():
        pdf(root/name, title, lines)
    if args.refundable_test_bookings:
        title, lines = inputs['incoming/passport.pdf']
        pdf(root/'incoming/passport.pdf', title, lines + ['Scenario fact: holder signature present; no real signature in this fixture.'])
        title, lines = inputs['incoming/student.pdf']
        pdf(root/'incoming/student.pdf', title, [line.replace('2026-10-20', '2026-10-22') for line in lines])
        rail_lines = [
            'Passenger ALEX CHEN. All fares/times below are synthetic scenario facts, NOT live offers.',
            'Eurostar Premier return: London-Paris 2026-12-12; Paris-London 2026-12-16.',
            'Eurostar total GBP 280; full original-card refund within stated fare window; no add-ons.',
            'Outbound original departure 12 Dec 12:00 Europe/London; refund by 14 Dec 12:00 same zone.',
            'Return original departure 16 Dec 12:00 Europe/Paris; refund by 18 Dec 12:00 same zone.',
            'Leeds-London flexible return connection, same travel days, GBP 60 total; confirmed.',
            'Connection: full original-card refund before each original departure; no booking fee.',
            'Connection departure: 12 Dec 07:00 Leeds; return 16 Dec 17:00 London, Europe/London.',
            'This is NOT a real operator schedule, ticket, fare or refund promise.',
        ]
        pdf(root/'incoming/transport.pdf', 'Fictional confirmed rail bookings', rail_lines)
        pdf(root/'corrections/transport.pdf', 'Fictional complete paid rail confirmations', rail_lines + [
            'Paid in full: Eurostar GBP 280 plus connection GBP 60. Original-card refund terms above.',
            'Connection arrival: 12 Dec 09:30 London; 16 Dec 19:30 Leeds, Europe/London.',
            'Eurostar arrival: 12 Dec 15:30 Europe/Paris; 16 Dec 13:30 Europe/London.',
        ])
        title, lines = inputs['corrections/hotel.pdf']
        pdf(root/'corrections/hotel.pdf', title, lines + [
            'Synthetic rate: GBP 240 total for 4 nights, prepaid, no non-refundable extras.',
            'Full original-card refund if cancelled before 2026-12-08 18:00 Europe/Paris.',
            'These are fictional test terms, not an actual hotel offer.',
        ])
    # A second basename, same bytes: must not create two copies in a current print set.
    (root/'incoming/hotel (1).pdf').write_bytes((root/'incoming/hotel.pdf').read_bytes())
    for month, start, end, before, after in [
        ('august', '2026-08-01', '2026-08-31', 4200, 4000),
        ('september', '2026-09-01', '2026-09-30', 4000, 3800),
        ('october', '2026-10-01', '2026-10-21', 3800, 3600),
    ]:
        pdf(root/f'full-bank/bank-{month}.pdf', 'Complete statement - '+month, [
            'Name: ALEX CHEN; address: 1 Example Road, Leeds, TEST ADDRESS.',
            f'Example Bank UK current account; period {start} to {end}.',
            f'Opening balance GBP {before}.',
            f'{start}: accommodation payment; debit GBP 200; balance GBP {after}.',
            f'Closing balance GBP {after}. End of statement; page 1 of 1.',
            'Test fact: this is the entire transaction history for the stated period.',
        ])
    for name in ['final-form.pdf', 'receipt.pdf', 'individual-checklist.pdf']:
        title, lines = inputs['portal/'+name]
        lines = [line.replace('TEST-CASE-A', 'TEST-CASE-B')
                 .replace('2026-12-12', '2026-12-13').replace('2026-12-16', '2026-12-17')
                 for line in lines]
        pdf(root/'final-evidence'/name, title+' - revised', lines)
    pdf(root/'final-evidence/insurance.pdf', 'Reissued insurance', [
        'Insured person: ALEX CHEN.',
        'Valid 2026-12-13 to 2026-12-17; all Schengen states; medical cover EUR 100000.',
        'Includes emergency treatment, hospital care and medical repatriation.',
    ])
    pdf(root/'final-evidence/appointment.pdf', 'Appointment - application linkage updated', [
        'TEST-CASE-B; ALEX CHEN; simulated booking CONFIRMED; service fee GBP 60 PAID.',
        'Manchester; 2026-11-09 10:00 Europe/London; one applicant.',
        'Address: TEST VENUE ONLY, Manchester. Never use this as a real address.',
        'Optional services: none. TEST-CASE-B linkage confirmed by simulated portal.',
    ])
    manifest = {name: hashlib.sha256(p.read_bytes()).hexdigest()
                for p in root.rglob('*.pdf') for name in [p.relative_to(root).as_posix()]}
    (root/'source-hashes.json').write_text(json.dumps(manifest, indent=2))
    print(root)
    print(f'Created {len(manifest)} fictional files; source hash manifest saved.')


if __name__ == '__main__':
    main()
