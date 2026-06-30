import pandas as pd

class CSVParser:
    """
    Parses candidate information from a recruiter CSV file.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):

        try:
            df = pd.read_csv(self.file_path)

            candidates = df.to_dict(orient="records")

            return candidates

        except Exception as e:
            print(f"Error reading CSV: {e}")
            return []
