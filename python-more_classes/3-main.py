#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
area = my_rectangle.area()
perimeter = my_rectangle.perimeter()
print("Area: {} - Perimeter: {}".format(area, perimeter))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))
