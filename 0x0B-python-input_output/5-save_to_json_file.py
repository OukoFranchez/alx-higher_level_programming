#!/usr/bin/python3
"""Module for task 5"""

from json import dump


def save_to_json_file(my_obj, filename):
    """
    Save an object as a JSON file.

    Args:
        my_obj (object): The object to be saved as a JSON file.
        filename (str): The name of the JSON file to be created.

    Returns:
        None

    Example:
        my_obj = {"name": "John", "age": 30}
        filename = "data.json"
        save_to_json_file(my_obj, filename)

    This function takes an object and a filename as inputs
    and saves the object as a JSON file with the given filename.
    """
    with open(filename, "w", encoding="utf-8") as file:
        dump(my_obj, file)
