#!/usr/bin/python3

"""
Module check if  object is instance of, or inherited frm, specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Check if object is instance of, or inherited frm, the specified class

    Args:
    - obj: Any Python object
    - a_class: A Python class

    Returns:
    - bool: Tru if objct is instance of, inherited frm, specified class;
    othrwse Flse
    """
    return isinstance(obj, a_class)
