#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Write File Function

    Writes the specified text to a file (UTF-8 encoded) and returns the number of characters written.

    Args:
    - filename (str): The name of the text file (default: "")
    - text (str): The text to be written to the file (default: "")

    Returns:
    - int: Number of characters written to the file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)


if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
