#!/bin/bash
# This takes URL as input, sends GET request to URL using curl, displays body response
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
