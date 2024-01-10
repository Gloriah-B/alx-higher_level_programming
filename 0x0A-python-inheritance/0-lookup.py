#!/usr/bin/python3

"""
Module provides functn to look up avlble attributes and method of object
"""


def lookup(obj):
    """
    Return list containing available attributes and method of given object

    Args:
    - obj: Any Python object

    Returns:
    - List: A list containing attributes and methods of the object.
    """
    return dir(obj)
