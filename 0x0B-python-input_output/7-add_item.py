#!/usr/bin/python3
"""
Module: json_operations

Provides functionality to save and load Python objects as JSON in a file.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Save to JSON File Function

    Writes the JSON representation of the provided object to a file.

    Args:
        my_obj: The object to be serialized and saved to a JSON file
        filename (str): The name of the file to save the JSON representation

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    Load from JSON File Function

    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load

    Returns:
        object: Python data structure created from the JSON file
    """
    with open(filename, 'r') as file:
        return json.load(file)
