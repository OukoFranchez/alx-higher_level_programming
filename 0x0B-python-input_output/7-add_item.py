#!/usr/bin/python3
"""
Contains the "save_to_json_file" function
"""

from json import dump


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file in JSON format.

    Args:
        my_obj: The object to be written to the file.
        filename: The name of the file to write the object to.

    Returns:
        None. The object is written to the file specified by `filename`.

    Example:
        save_to_json_file(my_obj, "output.json")

    This function opens the file specified by `filename` in
    write mode with UTF-8 encoding.
    It uses the `dump` function from the `json` module
    to write the JSON representation of `my_obj` to the file.
    """
    # Open the file in write mode with UTF-8 encoding
    with open(filename, 'w', encoding='utf-8') as f:
        dump(my_obj, f)
