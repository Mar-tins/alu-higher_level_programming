#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list, but only integers.
    Returns the count of printed integers.
    """
    count = 0  # To track the number of integers printed
    try:
        for i in range(x):  # Loop through the first x elements
            try:
                print("{:d}".format(my_list[i]), end="")  # Print integer
                count += 1  # Increment count when successful
            except (ValueError, TypeError):
                continue  # Skip non-integer values
    except IndexError:
        pass  # If x is larger than the list, exit gracefully

    print()  # Newline after printing all integers
    return count  # Return the number of integers printed
