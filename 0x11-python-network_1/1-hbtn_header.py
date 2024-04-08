#!/usr/bin/python3
"""
Script takes in a URL, sends request and displays
the value of X-Request-Id variable found in the header
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
