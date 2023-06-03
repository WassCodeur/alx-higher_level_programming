#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def calculator(av):
    argc = len(av)
    ops = ['+', '-', '*', '/']
    if argc != 4:
        print("USAGE: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        op = av[2]
        if op not in ops:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(av[1])
            b = int(av[3])
            if op == '+':
                result = add(a, b)
            elif op == '/':
                result = div(a, b)
            elif op == '-':
                result = sub(a, b)
            else:
                result = mul(a, b)
            print("{} {} {} = {}".format(a, op, b, result))


if __name__ == '__main__':
    from sys import argv
    calculator(argv)
