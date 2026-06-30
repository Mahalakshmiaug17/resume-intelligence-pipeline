import re
import math


class DataNormaliser:
    """
    Normalises candidate data into a standard format.
    Handles:
    - Missing values
    - Email case differences
    - Phone number formatting
    - Skills formatting
    - Name formatting
    """

    def __init__(self, data):
        self.data = data

    def normalise(self):

        normalised = self.data.copy()

        # ---------------------------------
        # Handle Missing Values
        # ---------------------------------
        for key, value in normalised.items():

            # Handle pandas NaN
            if isinstance(value, float):

                if math.isnan(value):
                    normalised[key] = None
                    continue

            # Handle Strings
            if isinstance(value, str):

                value = value.strip()

                if value.lower() in [
                    "",
                    "na",
                    "n/a",
                    "null",
                    "none",
                    "-"
                ]:
                    normalised[key] = None

                else:
                    normalised[key] = value

        # ---------------------------------
        # Full Name
        # ---------------------------------
        if normalised.get("full_name"):

            normalised["full_name"] = normalised["full_name"].title()

        # ---------------------------------
        # Email
        # CSV : MAHA@GMAIL.COM
        # Resume : maha@gmail.com
        # Output : maha@gmail.com
        # ---------------------------------
        if normalised.get("email"):

            match = re.search(
                r'[\w\.-]+@[\w\.-]+\.\w+',
                str(normalised["email"])
            )

            if match:

                normalised["email"] = match.group().lower()

        # ---------------------------------
        # Phone
        #
        # CSV    : +91 9876543210
        # Resume : 9876543210
        #
        # Output : +91 9876543210
        # ---------------------------------
        if normalised.get("phone"):

            phone = str(normalised["phone"])

            # Keep only digits
            digits = re.sub(r"\D", "", phone)

            # 9876543210
            if len(digits) == 10:

                normalised["phone"] = "+91 " + digits

            # 919876543210
            elif len(digits) == 12 and digits.startswith("91"):

                normalised["phone"] = "+91 " + digits[2:]

            else:

                normalised["phone"] = phone.strip()

        # ---------------------------------
        # Skills
        # ---------------------------------
        skills = normalised.get("skills")

        if isinstance(skills, str):

            normalised["skills"] = sorted([
                skill.strip().title()
                for skill in skills.split(",")
                if skill.strip()
            ])

        elif isinstance(skills, list):

            normalised["skills"] = sorted([
                skill.strip().title()
                for skill in skills
                if skill.strip()
            ])

        # ---------------------------------
        # Experience
        # ---------------------------------
        if normalised.get("experience"):

            normalised["experience"] = str(
                normalised["experience"]
            ).strip()

        # ---------------------------------
        # Gender
        # ---------------------------------
        if normalised.get("gender"):

            normalised["gender"] = normalised["gender"].title()

        return normalised
