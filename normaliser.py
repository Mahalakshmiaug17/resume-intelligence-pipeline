import re

class DataNormaliser:
    """
    Converts candidate data into a standard format.
    Also handles missing values.
    """

    def __init__(self, data):
        self.data = data

    def normalise(self):

        normalised = self.data.copy()

        # ---------------------------------
        # Convert Missing Values to None
        # ---------------------------------
        for key, value in normalised.items():

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
        # Normalize Full Name
        # ---------------------------------
        name = normalised.get("full_name")

        if name:
            normalised["full_name"] = name.title()

        # ---------------------------------
        # Normalize Email
        # ---------------------------------
        email = normalised.get("email")

        if email:

            match = re.search(
                r'[\w\.-]+@[\w\.-]+\.\w+',
                email
            )

            if match:
                normalised["email"] = match.group().lower()

        # ---------------------------------
        # Normalize Phone
        # ---------------------------------
        phone = normalised.get("phone")

        if phone:
            normalised["phone"] = phone.strip()

        # ---------------------------------
        # Normalize Skills
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
        # Normalize Experience
        # ---------------------------------
        experience = normalised.get("experience")

        if experience:
            normalised["experience"] = experience.strip()

        return normalised
