#!/usr/bin/python3
"""This is module for task 0"""


def lookup(obj):
    """
    Returns a list of all the attributes and methods of the given object.

    Args:
        obj (object): The object for which
        to retrieve the attributes and methods.

    Returns:
        list: A list of all the attributes and methods of the input object.
    """
    return dir(obj)
