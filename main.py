import json

from parsers.csv_parser import CSVParser
from parsers.pdf_parser import PDFParser

from services.normaliser import DataNormaliser
from services.merger import CandidateMerger
from services.confidence import ConfidenceScorer
from services.provenance import ProvenanceTracker
from services.json_generator import JSONGenerator
from services.validator import DataValidator

print("\n========== Candidate Data Transformer ==========\n")

csv_parser = CSVParser("input/Recruiter.csv")
csv_candidates = csv_parser.parse()

all_profiles = []

for candidate in csv_candidates:

    print("\n======================================")
    print(f"Processing Candidate ID : {candidate['id']}")
    print("======================================")

    resume_path = f"input/Resume_{candidate['id']}.pdf"

    pdf_parser = PDFParser(resume_path)

    pdf_data = pdf_parser.parse()

    csv_data = DataNormaliser(candidate).normalise()
    pdf_data = DataNormaliser(pdf_data).normalise()

    print("\nCSV Data")
    print(csv_data)

    print("\nResume Data")
    print(pdf_data)

    merged = CandidateMerger(csv_data, pdf_data).merge()

    print("\nMerged Profile")
    print(merged)

    confidence = ConfidenceScorer(csv_data, pdf_data).calculate()

    print("\nConfidence")
    print(confidence)

    provenance = ProvenanceTracker(csv_data, pdf_data).track()

    print("\nProvenance")
    print(provenance)

    validator = DataValidator(merged)
    validation = validator.validate()

    print("\nValidation")
    print(validation)

    final_json = JSONGenerator(
        merged,
        confidence,
        provenance
    ).generate()

    all_profiles.append(final_json)

with open("output/final_profiles.json", "w") as file:

    json.dump(all_profiles, file, indent=4)

print("\n====================================")
print("All Candidate Profiles Generated")
print("Saved to output/final_profiles.json")
print("====================================")
