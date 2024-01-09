#!/usr/bin/python3
"""
Module: json_file_loader

This module loads Python data structures from JSON files.
"""
import json


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
