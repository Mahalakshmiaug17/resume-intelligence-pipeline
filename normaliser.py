import re


class DataNormaliser:
    """
    Converts candidate data into a standard format.
    """

    def __init__(self, data):
        self.data = data

    def normalise(self):

        normalised = self.data.copy()

        # -------------------------
        # Normalize Full Name
        # -------------------------
        name = normalised.get("full_name")

        if name:
            normalised["full_name"] = str(name).strip().title()

        # -------------------------
        # Normalize Email
        # -------------------------
        email = normalised.get("email")

        if email:

            email = str(email)

            # Extract only the actual email address
            match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', email)

            if match:
                normalised["email"] = match.group().lower()
            else:
                normalised["email"] = email.strip().lower()

        # -------------------------
        # Normalize Phone
        # -------------------------
        phone = normalised.get("phone")

        if phone:
            normalised["phone"] = str(phone).strip()

        # -------------------------
        # Normalize Skills
        # -------------------------
        skills = normalised.get("skills")

        if isinstance(skills, str):

            normalised["skills"] = [
                skill.strip()
                for skill in skills.split(",")
                if skill.strip()
            ]

        elif isinstance(skills, list):

            normalised["skills"] = [
                str(skill).strip()
                for skill in skills
                if str(skill).strip()
            ]

        # -------------------------
        # Normalize Experience
        # -------------------------
        experience = normalised.get("experience")

        if experience:
            normalised["experience"] = str(experience).strip()

        return normalised