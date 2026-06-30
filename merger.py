class CandidateMerger:
    """
    Merges candidate data from CSV and Resume
    using conflict resolution.
    """

    def __init__(self, csv_data, pdf_data):
        self.csv_data = csv_data
        self.pdf_data = pdf_data

    def merge(self):

        merged = {}

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

            # Case 1 : Same value
            if csv_value == pdf_value:
                merged[field] = csv_value

            # Case 2 : Resume has value, CSV doesn't
            elif pdf_value and not csv_value:
                merged[field] = pdf_value

            # Case 3 : CSV has value, Resume doesn't
            elif csv_value and not pdf_value:
                merged[field] = csv_value

            # Case 4 : Both different → Resume wins
            elif pdf_value and csv_value:
                merged[field] = pdf_value

            # Case 5 : Missing everywhere
            else:
                merged[field] = None

        return merged