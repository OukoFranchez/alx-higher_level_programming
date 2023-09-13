#!/usr/bin/python3
"""Module for task 2"""


def append_write(filename="", text=""):
    """
    Appends text to a file and returns the number of characters written.

    Args:
        filename (str, optional): The name of the file to write to.
        If not provided, an empty string will be used.
        text (str, optional): The text to append to the file.
        If not provided, an empty string will be used.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        char_count = file.write(text)
    return char_count
