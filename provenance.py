class ProvenanceTracker:
    """
    Tracks the source of each field.
    """

    def __init__(self, csv_data, pdf_data):
        self.csv_data = csv_data
        self.pdf_data = pdf_data

    def track(self):

        provenance = {}

        fields = [
            "full_name",
            "email",
            "phone",
            "skills",
            "experience"
        ]

        for field in fields:

            csv_value = self.csv_data.get(field)
            pdf_value = self.pdf_data.get(field)

            if csv_value and pdf_value:
                provenance[field] = "Both"

            elif pdf_value:
                provenance[field] = "Resume"

            elif csv_value:
                provenance[field] = "CSV"

            else:
                provenance[field] = "Unknown"

        return provenance