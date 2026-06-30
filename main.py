import json

from parsers.csv_parser import CSVParser
from parsers.pdf_parser import PDFParser

from services.normaliser import DataNormaliser
from services.config_loader import ConfigLoader
from services.merger import CandidateMerger
from services.confidence import ConfidenceScorer
from services.provenance import ProvenanceTracker
from services.json_generator import JSONGenerator
from services.validator import DataValidator


def main():

    print("\n========== Candidate Data Transformer ==========\n")

    # -------------------------
    # Load Config
    # -------------------------
    fields = ConfigLoader("config/config.json").load()

    # -------------------------
    # CSV
    # -------------------------
    csv_parser = CSVParser("input/Recruiter.csv")
    csv_data = csv_parser.parse()
    csv_data = DataNormaliser(csv_data).normalise()

    csv_data = {
        key: value
        for key, value in csv_data.items()
        if key in fields
    }

    print("========== CSV Data ==========")
    print(json.dumps(csv_data, indent=4))

    # -------------------------
    # Resume
    # -------------------------
    pdf_parser = PDFParser("input/Resume.pdf")
    pdf_data = pdf_parser.parse()
    pdf_data = DataNormaliser(pdf_data).normalise()

    pdf_data = {
        key: value
        for key, value in pdf_data.items()
        if key in fields
    }

    print("\n========== Resume Data ==========")
    print(json.dumps(pdf_data, indent=4))

    # -------------------------
    # Merge
    # -------------------------
    merger = CandidateMerger(csv_data, pdf_data)
    merged_data = merger.merge()

    print("\n========== Merged Candidate Profile ==========")
    print(json.dumps(merged_data, indent=4))

    # -------------------------
    # Confidence
    # -------------------------
    confidence = ConfidenceScorer(csv_data, pdf_data)
    confidence_scores = confidence.calculate()

    print("\n========== Confidence Scores ==========")
    print(json.dumps(confidence_scores, indent=4))

    # -------------------------
    # Provenance
    # -------------------------
    provenance = ProvenanceTracker(csv_data, pdf_data)
    provenance_data = provenance.track()

    print("\n========== Provenance ==========")
    print(json.dumps(provenance_data, indent=4))

    # -------------------------
    # Final JSON
    # -------------------------
    generator = JSONGenerator(
        merged_data,
        confidence_scores,
        provenance_data
    )

    final_json = generator.generate()

    print("\n========== Final Standard JSON ==========")
    print(json.dumps(final_json, indent=4))

    generator.save("output/final_profile.json")

    # -------------------------
    # Validation
    # -------------------------
    validator = DataValidator(merged_data)
    validation = validator.validate()

    print("\n========== Validation Results ==========")
    print(json.dumps(validation, indent=4))

    print("\nProject completed successfully!")


if __name__ == "__main__":
    main()