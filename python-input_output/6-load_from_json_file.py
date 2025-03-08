import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the file containing the JSON string.

    Returns:
        object: The object created from the JSON string.
    """
    with open(filename, 'r') as file:
        return json.load(file)
