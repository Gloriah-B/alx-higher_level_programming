#!/usr/bin/python3
"""
Script to add command line arguments to a list and save them to a JSON file
"""


import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_items_to_list_and_save(arguments):
    """
    Add command line arguments to a list and save them to a JSON file

    :param arguments: List of command line arguments
    """
    try:
        # Load existing items from the file
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty list
        items = []

    # Add new items from command line arguments
    items.extend(arguments)

    # Save the updated list to the file
    save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    # Exclude the script name from the arguments
    arguments = sys.argv[1:]

    # Add items to the list and save to the file
    add_items_to_list_and_save(arguments)
