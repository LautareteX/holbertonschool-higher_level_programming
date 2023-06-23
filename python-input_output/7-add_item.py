#!/usr/bin/python3
"""
JSON - Interchanger
"""


import json
import sys
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

try:
    my_obj = load_from_json_file('add_item.json')
except Exception:
    my_obj = []

for i in sys.argv[1:]:
    my_obj.append(i)

save_to_json_file(my_obj, "add_item.json")
