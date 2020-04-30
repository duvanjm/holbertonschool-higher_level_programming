#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv) - 1
    if i == 0:
        print("{}".format("0 arguments."))
    elif i == 1:
        print("{}".format("1 argument:"))
        print("1: {}".format(argv[1]))
    else:
        print("{:d} {}".format(i, "arguments:"))
        for a in range(1, i + 1):
            print("{:d}: {}".format(a, argv[a]))
