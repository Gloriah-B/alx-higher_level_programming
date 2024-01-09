#!/usr/bin/python3
"""
Module: json_converter

Module provides functionality to convert objects to their JSON rep
"""
import json


def to_json_string(my_obj):
    """
    To JSON String Function

    Returns the JSON representation of the provided object (string).

    Args:
        my_obj: The object to be converted to a JSON string

    Returns:
        str: JSON representation of the object
    """
    return json.dumps(my_obj)
