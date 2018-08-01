#!/bin/bash
# Bash script to display the size of the body of URL response
curl -sX POST "$1" -d @"$2" "Content-Type: application/json"
