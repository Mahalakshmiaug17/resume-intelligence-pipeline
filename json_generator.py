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

        for field in self.merged_data:

            final_json[field] = {
                "value": self.merged_data[field],
                "confidence": self.confidence.get(field, 0.0),
                "source": self.provenance.get(field, "Unknown")
            }

        return final_json

    def save(self, output_path):

        data = self.generate()

        with open(output_path, "w") as file:
            json.dump(data, file, indent=4)

        print(f"\nFinal JSON saved to {output_path}")