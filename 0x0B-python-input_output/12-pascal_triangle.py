#!/usr/bin/python3

"""
Module: pascal_triangle
This module contains a function to generate Pascal's Triangle.
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the given number of rows.

    Args:
    - n (int): Number of rows to generate for Pascal's Triangle.

    Returns:
    - list of lists: Pascal's Triangle as a list of lists of integers.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        new_row = [1]  # First element of each row is always 1

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # Last element of each row is always 1
        triangle.append(new_row)

    return triangle


def print_triangle(triangle):
    """
    Print the provided triangle in a formatted manner.

    Args:
    - triangle (list of lists): Pascal's Triangle to print.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
