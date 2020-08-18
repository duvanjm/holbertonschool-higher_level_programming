#!/usr/bin/python3
"""Find a peak """


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    list_of_integers.sort()
    return list_of_integers[-1]
