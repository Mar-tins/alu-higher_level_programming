#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list safely.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print.

    Returns:
        int: The actual number of elements printed.
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")  # Print element without newline
            count += 1
    except IndexError:
        pass  # If index is out of range, ignore and continue
    print()  # Print a new line at the end
    return count  # Return number of elements successfully printed
