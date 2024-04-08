#!/bin/bash
# This script takes a URL as input, sends a GET request to the URL using curl, and displays the body of the response if the status code is 200.
response=$(curl -s -o /dev/null -w "%{http_code}" "$1"); if [[ $response == 200 ]]; then curl -s "$1"; fi

