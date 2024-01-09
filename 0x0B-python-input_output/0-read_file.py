#!/usr/bin/python3
"""
Module: file_reader

Module reads a text file and print its contents to stdout
"""


def read_file(filename=""):
    """
    Read File Function

    Opens specified text file (UTF-8 encoded) and prints to stdout

    Args:
    - filename (str): The path to the text file (default: "")

    Returns:
    - None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')


if __name__ == "__main__":
    read_file("my_file_0.txt")
