import json


def parse_json_credentials(file_path):
    with open(file_path, "r") as file:
        return json.load(file)
