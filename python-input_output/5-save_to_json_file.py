#!/usr/bin/python3
"""
Module that contains a function to save an object to a file
using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using JSON representation.

    Args:
        my_obj: The Python object to be saved.
        filename (str): The name of the file where the object
                        will be saved.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
