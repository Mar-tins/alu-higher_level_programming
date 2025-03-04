#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Divides two integers and prints the result inside a finally block.
    Returns the result or None if division is not possible.
    """
    result = None
    try:
        result = a / b  # Perform division
    except ZeroDivisionError:
        result = None  # Handle division by zero
    finally:
        print("Inside result: {}".format(result))  # Always print result
    return result  # Return the division result (or None)
