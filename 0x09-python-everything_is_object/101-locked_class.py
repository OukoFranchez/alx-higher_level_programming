#!/usr/bin/python3
"""
module for task 30
"""


class LockedClass:
    """prohibits dynamic creation of new instances
    """
    __slots__ = ['first_name']
