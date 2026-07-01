class ConfidenceScorer:
    """
    Assigns confidence scores to each candidate field.
    """

    def __init__(self, csv_data, pdf_data):
        self.csv_data = csv_data
        self.pdf_data = pdf_data

    def calculate(self):

        confidence = {}

        fields = [
            "full_name",
            "email",
            "phone",
            "skills",
            "experience",
            "age",
            "gender"
        ]

        for field in fields:

            csv_value = self.csv_data.get(field)
            pdf_value = self.pdf_data.get(field)

            if csv_value and pdf_value:
                confidence[field] = 1.00

            elif pdf_value:
                confidence[field] = 0.90

            elif csv_value:
                confidence[field] = 0.80

            else:
                confidence[field] = 0.60

        return confidence