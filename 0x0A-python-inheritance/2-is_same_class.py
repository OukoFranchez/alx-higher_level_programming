#!/usr/bin/python3
"""Module for task 2"""


def is_same_class(obj, a_class):
    """
    Check if an object belongs to a specific class.

    Args:
        obj: An object of any class.
        a_class: A class to compare the object against.

    Returns:
        True if the object belongs to the specified class, False otherwise.
    """
    return type(obj) is a_class
