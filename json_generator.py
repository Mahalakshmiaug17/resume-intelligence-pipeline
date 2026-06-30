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
            "full_name": 0.20,
            "email": 0.15,
            "phone": 0.15,
            "skills": 0.20,
            "experience": 0.15,
            "gender": 0.10,
            "age": 0.05
        }

        total_weight = 0
        weighted_score = 0

        for field in self.merged_data:

            # Ignore ID field
            if field == "id":
                continue

            score = self.confidence.get(field, 0.0)

            final_json[field] = {
                "value": self.merged_data[field],
                "confidence": score,
                "source": self.provenance.get(field, "Unknown")
            }

            # Calculate weighted confidence
            weight = weights.get(field, 0)

            weighted_score += score * weight
            total_weight += weight

        # Overall Confidence
        if total_weight > 0:
            overall = round(weighted_score / total_weight, 2)
        else:
            overall = 0.0

        final_json["overall_confidence"] = overall

        return final_json

    def save(self, output_path):

        data = self.generate()

        with open(output_path, "w") as file:
            json.dump(data, file, indent=4)

        print(f"\nFinal JSON saved to {output_path}")
