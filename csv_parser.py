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

            candidate = df.iloc[0].to_dict()

            # Clean email if stored as markdown/mailto
            if "email" in candidate:
                email = str(candidate["email"])

                if "mailto:" in email:
                    import re

                    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', email)

                    if match:
                        candidate["email"] = match.group()

            return candidate

        except Exception as e:
            print(f"Error reading CSV: {e}")
            return {}