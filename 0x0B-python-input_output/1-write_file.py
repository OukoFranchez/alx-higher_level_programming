#!/usr/bin/python3
"""Module for task 1"""


def write_file(filename="", text=""):
    """
    Writes the specified text to a file.

    Args:
        filename (str, optional): The name of the file to write to.
        If not provided, an empty string is used.
        text (str, optional): The text to write to the file.
        If not provided, an empty string is used.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        char_count = file.write(text)
    return char_count
