#!/usr/bin/python3
import sys

def main(args):
    if len(args) == 0:
        print("{} arguments.".format(len(args)))
    elif len(args) != 0:
        print("{} arguments: ".format(len(args) - 1))
        for i in range(1, len(args)):
            print("{}: {}".format(i , args[i]))
            
if __name__ == "__main__":
    main(sys.argv)
