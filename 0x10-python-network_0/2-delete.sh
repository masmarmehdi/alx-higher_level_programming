#!/bin/bash
# Sends a DELETE request to the URL passed as 1st argument and display body
curl -sX DELETE "$1"
