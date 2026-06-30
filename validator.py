import re


class DataValidator:
    """
    Validates the final merged candidate profile.
    """

    def __init__(self, data):
        self.data = data

    def validate(self):

        results = {}

        # Required fields
        required_fields = [
            "full_name",
            "email",
            "phone",
            "skills",
            "experience"
        ]

        for field in required_fields:

            value = self.data.get(field)

            if value:
                results[field] = "Valid"
            else:
                results[field] = "Missing"

        # Email validation
        email = self.data.get("email")

        if email:

            email = str(email)

            if re.search(r'[\w\.-]+@[\w\.-]+\.\w+', email):
                results["email"] = "Valid"
            else:
                results["email"] = "Invalid Email"

        # Phone validation
        phone = self.data.get("phone")

        if phone:

            digits = re.sub(r"\D", "", phone)

            if len(digits) >= 10:
                results["phone"] = "Valid"
            else:
                results["phone"] = "Invalid Phone"

        return results