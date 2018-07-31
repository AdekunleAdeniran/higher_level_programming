#!/bin/bash
# Bash script to display the size of the body of URL response
curl -sI $1 | grep 'Allow' | awk '{print $2,$3,$4}'
