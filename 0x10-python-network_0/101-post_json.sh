#!/bin/bash
# Script that sends a JSON POST request to a URL passed as first argument, displays body of response
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
