#!/usr/bin/python3
"""
Contains the "save_to_json_file" function
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Save an object as a JSON file.

    Args:
        my_obj (object): The object to be saved as a JSON file.
        filename (str): The name of the file to save the JSON data to.

    Returns:
        None

    Example Usage:
        my_obj = {"name": "John", "age": 30}
        filename = "data.json"
        save_to_json_file(my_obj, filename)

    Code Analysis:
        This function opens the file specified by `filename`
        in write mode with UTF-8 encoding.
        It then uses the `json.dump` function to
        write the JSON representation of `my_obj` to the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
