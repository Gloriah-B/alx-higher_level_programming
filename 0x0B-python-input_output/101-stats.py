#!/usr/bin/python3
"""
Script reads stdin line by line, computes metrics, and prints statistics.
"""


import sys


def print_metrics(total_size, status_code_counts):
    """
    Prints the computed metrics.

    Args:
        total_size (int): Total file size.
        status_code_counts (dict): Dictionary with counts each status code
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_code_counts.keys()):
        print("{}: {}".format(code, status_code_counts[code]))


def main():
    """
    Main function to read stdin, compute metrics, and print statistics.
    """
    total_size = 0
    status_code_counts =
    {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            tokens = line.split()
            if len(tokens) >= 8:
                status_code = int(tokens[-2])
                file_size = int(tokens[-1])
                total_size += file_size

                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_code_counts)

    except KeyboardInterrupt:
        # Handle CTRL + C
        print_metrics(total_size, status_code_counts)
        sys.exit(0)


if __name__ == "__main__":
    main()
