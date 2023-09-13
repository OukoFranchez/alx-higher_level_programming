#!/usr/bin/python3
"""Module for task 4"""

from json import loads


def from_json_string(my_str):
    """
    Convert a string into a JSON object.

    Args:
        my_str (str): A string representing a JSON object.

    Returns:
        str: A string representing the JSON object.

    Example:
        >>> my_str = '{"name": "John", "age": 30}'
        >>> json_string = to_json_string(my_str)
        >>> print(json_string)
        {"name": "John", "age": 30}
    """

    return loads(my_str)
