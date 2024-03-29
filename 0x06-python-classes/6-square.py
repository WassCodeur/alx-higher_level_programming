#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the current size of the square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """
        Public instance method:
        def area(self): that returns the current square area
    """
    def area(self):
        return (self.__size ** 2)
    """
        position getters and setters
    """
    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(el, int) for el in value) or
                all(el >= 0 for el in value)):
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print(" ")

        [print("") for _ in range(0, self.__position[1])]
        for _ in range(self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            for _ in range(self.__size):
                print("#", end="")
            print()
