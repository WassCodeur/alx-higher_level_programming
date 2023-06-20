#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
print(Square.__doc__)
print(Square.__name__)
print(Square.__module__)
print(my_square.__class__)
