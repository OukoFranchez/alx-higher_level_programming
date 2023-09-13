#!/usr/bin/python3
"""Module for task 3"""
import json


def to_json_string(my_obj):
    """
    Convert an object to a JSON string representation.

    Args:
        my_obj: The object to be converted.

    Returns:
        A JSON string representation of the input object.
    """
    return json.dumps(my_obj)
