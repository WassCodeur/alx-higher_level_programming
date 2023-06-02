#!/usr/bin/python3
import sys
def main(args):
    j = 0
    for i in range(1, len(args)):
        j = j + int(args[i])
    print("{}".format(j))
if __name__ == "__main__":
    main(sys.argv)
