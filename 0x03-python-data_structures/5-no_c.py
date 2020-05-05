#!/bin/usr/python3
def no_c(my_string):
    string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            string += i
    return string
