#!/usr/bin/bash
# Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -so /dev/null -w '%response_code' "$1"
