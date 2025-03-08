#!/usr/bin/python3
"""
Module that contains a function to return the Python object
represented by a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object (data structure) represented
    by a JSON string.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python object (list, dict, etc.) represented by
                the JSON string.
    """
    return json.loads(my_str)
