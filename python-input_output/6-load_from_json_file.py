#!/usr/bin/python3
import json


"""
Module that contains a function to load an object from a JSON file.
"""


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the file containing the JSON string.

    Returns:
        object: The object created from the JSON string.

    Raises:
        ValueError: If the JSON is not formatted correctly.
        FileNotFoundError: If the file doesn't exist.
    """
    with open(filename, 'r') as file:
        return json.load(file)
