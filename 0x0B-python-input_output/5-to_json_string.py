#!/usr/bin/python3
"""
    Python function that returns the JSON representation of an object
"""

import json


def to_json_string(my_obj):
    return json.dumps(my_obj)
