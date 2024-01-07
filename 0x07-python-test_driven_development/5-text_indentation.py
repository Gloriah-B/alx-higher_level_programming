#!/usr/bin/python3
"""Prints text with 2 new lines after ., ? and : characters."""


def text_indentation(text):
    """Prints text with 2 new lines after ., ? and : characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = {'.', '?', ':'}
    lines = []
    line = ''

    for char in text:
        line += char
        if char in punctuation:
            lines.append(line.strip())
            lines.append('')
            line = ''

    if line:
        lines.append(line.strip())

    for line in lines:
        print(line)
