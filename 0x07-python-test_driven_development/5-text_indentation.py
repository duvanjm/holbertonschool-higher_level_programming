#!/usr/bin/python3
"""
prints a text with 2 new lines 
after each of these characters: ., ? and :
"""


def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    text = text.replace(": ", ":\n\n")
    text = text.replace("? ", "?\n\n")
    text = text.replace(". ", ".\n\n")
    text = text.replace(":", ":\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(".", ".\n\n")
    print(text), print()
