#!/usr/bin/python3
"""Module for task 3"""


def inherits_from(obj, a_class):
    """
    Check if an object inherits from a specific class.

    Args:
        obj (object): The object to check if it inherits from a class.
        a_class (class): The class to check if the object inherits from.

    Returns:
        bool: True if the object inherits from the specified class
        and is not an instance of the class itself, False otherwise.
    """
    return issubclass(type(obj), a_class) and (type(obj) != a_class)
