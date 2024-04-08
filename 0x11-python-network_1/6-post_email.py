#!/usr/bin/python3
"""
Script takes in URL and an email address, sends a POST request to
passed URL with the email as parameter, then displays body of response."""


if __name__ == '__main__':
    from sys import argv
    from requests import post

    url = argv[1]
    email = argv[2]
    res = post(url, {'email': email})
    print(res.text)
