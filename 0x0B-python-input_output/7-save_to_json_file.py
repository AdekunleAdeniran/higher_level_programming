#!/usr/bin/python3
"""
Python Function that writs an object to a file
Using JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
