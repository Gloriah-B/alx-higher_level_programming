#!/bin/bash
# This script takes a URL as input, sends a request to that URL using curl, and
#displays the size of the response body

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to the URL using curl and store the response body
content_length=$(curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')

# Display the size of the body of the response in bytes
echo "Size of the response body: $content_length bytes"
