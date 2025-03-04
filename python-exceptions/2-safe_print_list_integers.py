#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list, but only integers.
    Returns the count of printed integers.
    """
    count = 0  # Track the number of printed integers

    for i in range(x):  # Loop through the first x elements
        try:
            print("{:d}".format(my_list[i]), end="")  # Print integer
            count += 1  # Increment count when successful
        except (ValueError, TypeError):
            continue  # Skip non-integer values

    print()  # Newline after printing all integers
    return count  # Return the number of printed integers
