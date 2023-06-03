#!/usr/bin/python3
def main(args):
    argc = len(args)
    print("{} arguments.".format((argc - 1)))
    for i in range(1, argc):
        print("{}: {}".format(i, args[i]))


if __name__ == '__main__':
    from sys import argv
    main(argv)
