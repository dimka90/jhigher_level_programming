#!/usr/bin/python3
""" a class that defines a class """


class Square:
    def __init__(self, size=0):
        """ a class that defines a square based on
        task 3-square.py task
        """
        self.__size = size

    def area(self):
        """
        a public instance that returns the current square
        area
        """
        return self.__size ** 2
    @property
    def size(self):
        """
        a size getter that retrive size
        """
        return self.__size
    @size.setter
    def size(self, value):
        """
        a value setter
        args:
            value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError(" size must be >= 0")
        else:
            self.__size = value
