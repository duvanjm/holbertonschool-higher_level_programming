#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for y in my_list[:x]:
        try:
            print("{:d}".format(my_list[y]), end="")
            count += 1
        except ValueError:
            pass

        print()
        return count        