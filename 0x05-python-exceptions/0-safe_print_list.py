#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for y in my_list[:x]:
            print("{}".format(y), end="")
            count += 1
        print()

    except:
        print("Error")

    return count
