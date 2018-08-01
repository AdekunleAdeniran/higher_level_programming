#!/bin/bash
# Bash script to display the size of the body of URL response
curl -s POST -d "Content-Type: application/json" "$1" @"$2"
