#!/usr/bin/python3
""" a class that defines a square """


class Square:
    """
    a class that defines a square based on task 2-square.py instruction
    + it add a new public instance method def area(self): that returns
    the current square area
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError(" size must be >= 0")

    def area(self):
        """
        a public instance method that returns current square area
        """
        return self.__size ** 2
