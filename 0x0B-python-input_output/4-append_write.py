#!/usr/bin/python3
"""Python Function to append string to a file"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
