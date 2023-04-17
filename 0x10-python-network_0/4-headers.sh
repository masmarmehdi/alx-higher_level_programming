#!/bin/bash
# Takes a URL, send a GET request to the URL and displays the body response
curl -sH "X-School-User-Id: 98" "${1}"
