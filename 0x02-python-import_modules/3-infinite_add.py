#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv)
    sum = 0
    for a in range(1, i):
        sum += int(argv[a])
    print("{:d}".format(sum))
