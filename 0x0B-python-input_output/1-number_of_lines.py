#!/usr/bin/python3
'''Python Function to count number of lines in a file'''


def number_of_lines(filename=""):
    count = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            count += 1
    return count
