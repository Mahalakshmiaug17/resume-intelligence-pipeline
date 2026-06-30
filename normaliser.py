import re
import math


class DataNormaliser:
    """
    Normalises candidate data into a standard format.
    Also converts missing values to None.
    """

    def __init__(self, data):
        self.data = data

    def normalise(self):

        normalised = self.data.copy()

        # ---------------------------------
        # Handle Missing Values
        # ---------------------------------
        for key, value in normalised.items():

            # Handle NaN values from pandas
            if isinstance(value, float):

                if math.isnan(value):
                    normalised[key] = None
                    continue

            # Handle string values
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
        # Normalise Full Name
        # ---------------------------------
        if normalised.get("full_name"):

            normalised["full_name"] = normalised["full_name"].title()

        # ---------------------------------
        # Normalise Email
        # ---------------------------------
        if normalised.get("email"):

            match = re.search(
                r'[\w\.-]+@[\w\.-]+\.\w+',
                normalised["email"]
            )

            if match:
                normalised["email"] = match.group().lower()

        # ---------------------------------
        # Normalise Phone
        # ---------------------------------
        if normalised.get("phone"):

            normalised["phone"] = normalised["phone"].strip()

        # ---------------------------------
        # Normalise Skills
        # ---------------------------------
        skills = normalised.get("skills")

        if isinstance(skills, str):

            normalised["skills"] = [
                skill.strip()
                for skill in skills.split(",")
                if skill.strip()
            ]

        elif isinstance(skills, list):

            normalised["skills"] = [
                skill.strip()
                for skill in skills
                if skill.strip()
            ]

        # ---------------------------------
        # Normalise Experience
        # ---------------------------------
        if normalised.get("experience"):

            normalised["experience"] = normalised["experience"].strip()

        # ---------------------------------
        # Normalise Gender
        # ---------------------------------
        if normalised.get("gender"):

            normalised["gender"] = normalised["gender"].title()

        return normalised
