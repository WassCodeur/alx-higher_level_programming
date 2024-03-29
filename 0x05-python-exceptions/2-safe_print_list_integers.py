#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    r_x = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            r_x += 1
        except (ValueError, TypeError):
            pass
    print()
    return (r_x)
