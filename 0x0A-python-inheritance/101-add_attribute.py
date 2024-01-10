#!/usr/bin/python3

"""
Module provides a function to add a new attribute to an object if possible
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
    - obj: The object to which the attribute should be added
    - attr: The name of the attribute
    - value: The value of the attribute

    Raises:
    - TypeError: If the object cannot have new attributes
    """
    if not hasattr(obj, "__dict__") and not hasattr(type(obj), "__slots__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
