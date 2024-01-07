#!/usr/bin/python3
"""Prints a name."""


def say_my_name(first_name, last_name=""):
    """Prints the name in a specified format.

    Args:
        first_name (str): First name.
        last_name (str): Last name (optional).

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    full_name = "My name is {} {}".format(first_name, last_name) if last_name else "My name is {}".format(first_name)
    print(full_name)
