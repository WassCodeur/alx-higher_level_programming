#!/usr/bin/python3
def infinity(args):
    sum = 0
    argc = len(args)
    for i in range(1, argc):
        sum += int(args[i])
    print(sum)


if __name__ == '__main__':
    from sys import argv
    infinity(argv)
