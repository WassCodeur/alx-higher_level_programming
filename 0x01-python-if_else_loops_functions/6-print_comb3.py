#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if j > i:
            if i + j == 17:
                print("{}{}".format(i, j))
            else:
                print("{}{}".format(i, j), end=", ")
