import json


class JSONGenerator:
    """
    Generates the final standardized JSON output.
    """

    def __init__(self, merged_data, confidence, provenance):
        self.merged_data = merged_data
        self.confidence = confidence
        self.provenance = provenance

    def generate(self):

        final_json = {}

        # -------------------------
        # Field Weights
        # -------------------------
        weights = {
            "full_name": 0.25,
            "email": 0.20,
            "phone": 0.20,
            "skills": 0.25,
            "experience": 0.10
        }

        overall_confidence = 0

        for field in self.merged_data:

            # Ignore CSV ID
            if field == "id":
                continue

            score = self.confidence.get(field, 0.0)

            final_json[field] = {
                "value": self.merged_data[field],
                "confidence": score,
                "source": self.provenance.get(field, "Unknown")
            }

            overall_confidence += score * weights.get(field, 0)

        final_json["overall_confidence"] = round(overall_confidence, 2)

        return final_json

    def save(self, output_path):

        data = self.generate()

        with open(output_path, "w") as file:
            json.dump(data, file, indent=4)

        print(f"\nFinal JSON saved to {output_path}")
