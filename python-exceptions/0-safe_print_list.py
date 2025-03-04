#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0  # Counter for printed elements
    try:
        for i in range(x):  # Loop x times
            print(my_list[i], end="")  # Print without newline
            count += 1  # Increase count
    except IndexError:  # If we go out of bounds, do nothing
        pass
    print()  # Print newline after printing elements
    return count  # Return number of elements printed
