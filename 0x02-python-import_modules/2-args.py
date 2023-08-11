#!/usr/bin/python3
import sys


def print_arguments(arguments):
    num_args = len(arguments)
    if num_args == 0:
        print("0 arguments.")
        return

    print(f"{num_args} argument{'s' if num_args > 1 else ''}:")
    for i, arg in enumerate(arguments, start=1):
        print(f"{i}: {arg}")


if __name__ == "__main__":
    print_arguments(sys.argv[1:])
