#!/usr/bin/python3

"""
Module checks if object is exactly an instance of specified class
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
    - obj: Any Python object
    - a_class: A Python class

    Returns:
    - bool: Tr if object is exactly instance of specified class; othrwse F
    """
    return type(obj) is a_class
