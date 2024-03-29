#!/usr/bin/python3

"""
This module checks if an object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
    - obj: Any Python object
    - a_class: A Python class

    Returns:
    - bool: True if the object is an instance of class tht inherited
    (directly or indirectly) from the specified class; otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
