#!/usr/bin/python3
"""
Python function that add arguments to a Python list
"""
import sys
import os

save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

my_list = []

if not os.path.exists("./add_item.json"):
    save_json(my_list, "add_item.json")
my_list = load_json("add_item.json")

for items in sys.argv[1:]:
    my_list.append(items)
save_json(my_list, "add_item.json")
