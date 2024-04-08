#!/bin/bash
# Sends a GET request to the URL with a custom header X-HolbertonSchool-User-Id: 98, and displays the body of the response
curl -sH "X-School-User-Id: 98" "${1}"
