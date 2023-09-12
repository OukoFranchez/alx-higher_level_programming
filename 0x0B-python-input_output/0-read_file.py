#!/usr/bin/python3
"""Module for task 1"""


def read_file(filename=""):
    """
    Reads the contents of a file and prints each line to the console.

    Args:
        filename (str, optional): The name of the file to be read.
        If no filename is provided, an empty string is used.

    Returns:
        None
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        pass
