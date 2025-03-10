#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Valid test cases
files = ["my_list.json", "my_dict.json", "my_dict_with_list.json", "big_dict.json", "big_array_of_dicts.json", "simple_string.json"]

for filename in files:
    try:
        data = load_from_json_file(filename)
        print("✅ Successfully loaded:", filename)
        print("➡️", data)
        print("Type:", type(data), "\n")
    except Exception as e:
        print("❌ Error loading:", filename)
        print("[{}] {}".format(e.__class__.__name__, e))

# Invalid test cases (File not found & Permission error)
invalid_files = ["file_does_not_exist.json", "no_permission.json"]

for filename in invalid_files:
    try:
        data = load_from_json_file(filename)
    except Exception as e:
        print("❌ Expected error:", filename)
        print("[{}] {}".format(e.__class__.__name__, e), "\n")
