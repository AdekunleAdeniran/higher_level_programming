#!/usr/bin/python3
"""
Python function that returns an object from JSON
"""


import json


def from_json_string(my_str):
    return json.loads(my_str)
