import json # Standard library


def read_JSON(jsonPath):
    with open(jsonPath) as f:
        JSON = json.load(f)
    return JSON