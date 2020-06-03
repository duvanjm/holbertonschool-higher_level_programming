#!/usr/bin/python3
"""add save load"""


from sysy import argv
save_to_json_file = __import__ ('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    lista = load_from_json_file(filename)
except:
    lista = []

save_to_json_file(filename, lista)
