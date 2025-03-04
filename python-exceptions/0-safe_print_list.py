#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0  # Counter for printed elements
    try:
        for i in range(x):
            try:
                print(my_list[i], end="")  # Print without newline
                count += 1
            except IndexError:
                break  # Stop if index is out of range
    except Exception:
        pass  # Catch any unexpected errors

    print()  # Print a newline after printing elements
    return count  # Return the number of elements printed
