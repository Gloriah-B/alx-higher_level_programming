#!/usr/bin/python3
"""
Script reads and computes metrics based on specified input format

Input format: <IP Address> - [<date>]
"GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
it prints the accumulated statistics.

Metrics include:
- Total file size: Sum of all previous file sizes.
- Number of lines by status code (sorted in ascending order).

Usage:
    ./script_name.py < input_data.txt
"""

import sys


def print_metrics(total_size, status_counts):
    """
    Print metrics based on accumulated data.

    Args:
        total_size (int): Accumulated total file size.
        status_counts (dict): Dictionary with status codes and their counts.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")


def main():
    """
    Process stdin, calculate metrics, and handle keyboard interruption
    """
    total_size = 0
    status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    lines_processed = 0

    try:
        for line in sys.stdin:
            lines_processed += 1
            ip, _, _, status_code, file_size = line.split()[:5]
            total_size += int(file_size)
            status_counts[status_code] += 1

            if lines_processed % 10 == 0:
                print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle Ctrl+C interruption
        print_metrics(total_size, status_counts)
        sys.exit(0)


if __name__ == "__main__":
    main()
