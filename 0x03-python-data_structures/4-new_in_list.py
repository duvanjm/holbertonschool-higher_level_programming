#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = my_list[:]
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        a[idx] = element
        return a
