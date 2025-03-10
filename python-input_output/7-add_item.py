#!/usr/bin/python3
"""
This script adds command-line arguments to a list and saves the list to a JSON file.
If the file does not exist, it will be created. If the file already exists, the list
is loaded and new items are appended to it. The updated list is then saved back to the file.
"""
import sys
import os
from importlib import import_module

# Dynamically import the functions from the respective files
load_from_json_file = import_module(
    "6-load_from_json_file").load_from_json_file
save_to_json_file = import_module(
    "5-save_to_json_file").save_to_json_file

# File where the list will be saved
filename = "add_item.json"

# Check if the file exists
if os.path.exists(filename):
    # Load the existing list from the file
    items = load_from_json_file(filename)
else:
    # If the file doesn't exist, initialize an empty list
    items = []

# Add all command line arguments (excluding the script name itself)
for arg in sys.argv[1:]:
    items.append(arg)

# Save the updated list to the file
save_to_json_file(items, filename)
