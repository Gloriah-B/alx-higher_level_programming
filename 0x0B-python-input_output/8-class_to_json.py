#!/usr/bin/python3

"""Module to convert class attributes to a JSON serializable dictionary."""


def class_to_json(obj):
    """
    Convert attributes of an object to a JSON serializable dictionary.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary containing serializable attributes of the object.
    """
    # Check if obj is an instance of a class
    if not isinstance(obj, type):
        return obj.__dict__
    else:
        # If obj is a class, return its attributes
        return {k: v for k, v in obj.__dict__.items() if not callable(v)}
