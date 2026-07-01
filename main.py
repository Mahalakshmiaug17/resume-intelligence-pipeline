import json

from csv_parser import CSVParser
from pdf_parser import PDFParser

from normaliser import DataNormaliser
from merger import CandidateMerger
from confidence import ConfidenceScorer
from provenance import ProvenanceTracker
from json_generator import JSONGenerator
from validator import DataValidator


print("\n========== Candidate Data Transformer ==========\n")

# Read all candidates from CSV
csv_parser = CSVParser("input/Recruiter.csv")
csv_candidates = csv_parser.parse()

all_profiles = []

# Process each candidate
for candidate in csv_candidates:

    print("\n======================================")
    print(f"Processing Candidate ID : {candidate['id']}")
    print("======================================")

    # Read corresponding resume
    resume_path = f"input/Resume_{candidate['id']}.pdf"

    pdf_parser = PDFParser(resume_path)
    pdf_data = pdf_parser.parse()

    # Normalize data
    csv_data = DataNormaliser(candidate).normalise()
    pdf_data = DataNormaliser(pdf_data).normalise()

    print("\n========== CSV Data ==========")
    print(json.dumps(csv_data, indent=4))

    print("\n========== Resume Data ==========")
    print(json.dumps(pdf_data, indent=4))

    # Merge
    merger = CandidateMerger(csv_data, pdf_data)
    merged = merger.merge()

    print("\n========== Merged Candidate Profile ==========")
    print(json.dumps(merged, indent=4))

    # Confidence
    confidence = ConfidenceScorer(csv_data, pdf_data).calculate()

    print("\n========== Confidence Scores ==========")
    print(json.dumps(confidence, indent=4))

    # Provenance
    provenance = ProvenanceTracker(csv_data, pdf_data).track()

    print("\n========== Provenance ==========")
    print(json.dumps(provenance, indent=4))

    # Generate Final JSON
    generator = JSONGenerator(
        merged,
        confidence,
        provenance
    )

    final_json = generator.generate()

    print("\n========== Final Standard JSON ==========")
    print(json.dumps(final_json, indent=4))

    # Print Overall Confidence
    print("\n========== Overall Confidence ==========")
    print(final_json["overall_confidence"])

    # Validation
    validator = DataValidator(merged)
    validation = validator.validate()

    print("\n========== Validation Results ==========")
    print(json.dumps(validation, indent=4))

    # Store profile
    all_profiles.append(final_json)

# Save all profiles
with open("output/final_profiles.json", "w") as file:
    json.dump(all_profiles, file, indent=4)

print("\n========================================")
print("All Candidate Profiles Generated")
print("Saved to output/final_profiles.json")
print("========================================")
