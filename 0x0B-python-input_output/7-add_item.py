#!/usr/bin/python3

"""Script to add command-line arguments to list and save to JSON file."""

import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_items_to_list_and_save():
    """Add command-line arguments to a list and save it to a JSON file."""
    try:
        try:
            # Load existing items from the file if it exists
            items_list = load_from_json_file('add_item.json')
        except FileNotFoundError:
            items_list = []

        # Add new items from command-line arguments to the list
        items_list.extend(sys.argv[1:])

        # Save the updated list to add_item.json
        save_to_json_file(items_list, 'add_item.json')
        print("Items added and saved successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    add_items_to_list_and_save()
