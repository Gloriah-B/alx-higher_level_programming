#!/bin/bash
# Script to fetch the size of the response body from a given URL using curl


curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r'

