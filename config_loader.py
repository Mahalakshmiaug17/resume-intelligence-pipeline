import json


class ConfigLoader:
    """
    Loads runtime configuration.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):

        with open(self.file_path, "r") as file:
            config = json.load(file)

        return config["fields"]