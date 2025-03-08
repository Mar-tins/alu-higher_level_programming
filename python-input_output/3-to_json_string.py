#!/usr/bin/python3
"""
Module that contains a function to return the JSON representation of an object.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj (object): The object to be converted to JSON.

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
