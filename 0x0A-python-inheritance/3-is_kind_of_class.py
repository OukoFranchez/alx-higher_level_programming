#!/usr/bin/python3
"""Module for task 3"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a given class/subclass.

    Args:
        obj (any): The object to be checked.
        a_class (class): The class to check against.

    Returns:
        bool: True if the object is an instance of the given class,
        False otherwise.
    """
    return isinstance(obj, a_class)
