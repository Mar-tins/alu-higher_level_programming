#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

test_cases = [
    ([10, 0, 4], [2, 4, 0], 3),
    ([10, 0, 4], [2, 4, 0], 2),
    ([10, "0", 4], [0, 4], 3),
    ([10, 8, 4], [2, 4, 4], 3),
    ([10], [2], 1),
    ([10, 2], [2], 1),
    ([10, 2], [2], 2),
    ([10, 2], [], 2),
    ([10, "8", 4], [2, 4, 4], 3),
    ([10, "8", 4], [2, 2], 3),
    ([10, 0, 4], [2, 4, 4], 3)
]

for case in test_cases:
    mylist1, mylist2, length = case
    print(list_division(mylist1, mylist2, length))
