#!/usr/bin/python3
"""
Module: json_parser

Module converts JSON strings into Python data structures
"""
import json


def from_json_string(my_str):
    """
    From JSON String Function

    Returns an object represented by the provided JSON string.

    Args:
        my_str (str): The JSON string representing an object

    Returns:
        object: Python data structure represented by the JSON string
    """
    return json.loads(my_str)
