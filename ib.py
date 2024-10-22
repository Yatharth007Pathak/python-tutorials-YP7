# Calculate the Area of a Circle

import math

def area_of_circle(radius):
    return math.pi * radius ** 2

# Example usage
try:
    r = float(input("Enter the radius of the circle: "))
    print(f"The area of the circle with radius {r} is {area_of_circle(r):.2f}.")
except ValueError:
    print("Please enter a valid number.")

'''
Here's a detailed explanation of the code:

import math imports the math module, which provides access to mathematical functions and constants, such as math.pi.

def area_of_circle(radius): defines a function named area_of_circle that takes a single parameter radius, 
which represents the radius of the circle.

return math.pi * radius ** 2 calculates and returns the area of the circle:

math.pi provides the value of π (pi).
radius ** 2 squares the radius.
math.pi * radius ** 2 computes the area using the formula 
Area = π * radius^2

try: starts a block that attempts to execute code that might raise an exception.

r = float(input("Enter the radius of the circle: ")) prompts the user to enter the radius of the circle, 
converts this input to a floating-point number, and stores it in the variable r.

print(f"The area of the circle with radius {r} is {area_of_circle(r):.2f}."):

Calls the area_of_circle function with r as the argument.
Prints the area of the circle, formatted to two decimal places using :.2f.
except ValueError: catches any ValueError that occurs if the input cannot be converted to a floating-point number.

print("Please enter a valid number.") prints an error message if the user input is not a valid number.
'''