import pdfplumber
import re


class PDFParser:
    """
    Extracts candidate information from a resume PDF.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):

        data = {}
        text = ""

        try:
            with pdfplumber.open(self.file_path) as pdf:

                for page in pdf.pages:

                    extracted = page.extract_text()

                    if extracted:
                        text += extracted + "\n"

            if not text.strip():
                print("No readable text found in the PDF.")
                return {}

            # -------------------------
            # Full Name
            # -------------------------
            lines = text.split("\n")

            for line in lines:
                if line.strip():
                    data["full_name"] = line.strip()
                    break

            # -------------------------
            # Email
            # -------------------------
            email = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

            if email:
                data["email"] = email.group().lower()

            # -------------------------
            # Phone
            # -------------------------
            phone = re.search(r'(\+?\d[\d\s-]{8,}\d)', text)

            if phone:
                data["phone"] = phone.group()

            # -------------------------
            # Skills
            # -------------------------
            skills = []

            skill_list = [
                "Python",
                "Java",
                "SQL",
                "C++",
                "JavaScript",
                "HTML",
                "CSS"
            ]

            for skill in skill_list:
                if skill.lower() in text.lower():
                    skills.append(skill)

            data["skills"] = skills

            # -------------------------
            # Experience
            # -------------------------
            exp = re.search(r'(\d+\s*Years?)', text, re.IGNORECASE)

            if exp:
                data["experience"] = exp.group()

            return data

        except Exception as e:
            print(f"Error reading PDF: {e}")
            return {}