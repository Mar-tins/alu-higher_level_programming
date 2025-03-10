#!/usr/bin/python3
"""Module to create an object from a JSON file"""

import json


def load_from_json_file(filename):
    """Reads a JSON file and returns the corresponding Python object.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object representing the JSON content.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
