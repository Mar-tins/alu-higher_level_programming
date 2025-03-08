#!/usr/bin/python3
import json

"""
This module defines a function that creates a Python object from a JSON file.
It uses the `json` module to deserialize a JSON string into a Python object.

Function:
    load_from_json_file: Creates an object from a JSON file.
"""


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The Python object represented by the JSON string.
    """
    with open(filename, 'r') as f:
        return json.load(f)
