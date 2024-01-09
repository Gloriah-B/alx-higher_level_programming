#!/usr/bin/python3
"""
Module: save_to_json_file

Module provides functionality to save Python objects as JSON in a file
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
