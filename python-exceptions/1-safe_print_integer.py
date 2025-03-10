#!/usr/bin/python3


def safe_print_integer(value):
    """
    Prints an integer using '{:d}'.format() and returns True if successful.
    """
    try:
        print("{:d}".format(value))  # Format and print as an integer
        return True
    except (ValueError, TypeError):
        return False
