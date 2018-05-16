#!/usr/bin/python3
'''Python Function to write text to file and
   returns number of characters written
'''


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
