"""
The math module in Python provides a variety of mathematical functions and constants. 
It includes functions for mathematical operations such as exponentiation, logarithms, and trigonometry. 
Here are some commonly used functions and constants from the math module:

Common Functions
math.sqrt(x): Returns the square root of x.
math.pow(x, y): Returns x raised to the power of y.
math.log(x): Computes the natural logarithm of x.
math.log(x, base): Returns the logarithm of x to the specified base. If base is not provided, it returns the natural logarithm.
math.sin(x): Returns the sine of x (where x is in radians).
math.cos(x): Returns the cosine of x (where x is in radians).
math.tan(x): Returns the tangent of x (where x is in radians).
math.factorial(x): Returns the factorial of x (where x is a non-negative integer).
math.ceil(x): Returns the ceiling of x, the smallest integer greater than or equal to x.
math.floor(x): Returns the floor of x, the largest integer less than or equal to x.
math.fabs(x): Returns the absolute value of a number x as a floating-point number.

Common Constants
math.pi: The mathematical constant π (pi), approximately 3.14159.
math.e: The mathematical constant e, the base of natural logarithms, approximately 2.71828.
"""

import math

# Define a number
x = 16
y = 2
base = 10

# Square root
sqrt_x = math.sqrt(x)
print(f"Square root of {x}: {sqrt_x}")

# Power
pow_xy = math.pow(x, y)
print(f"{x} raised to the power of {y}: {pow_xy}")

# Logarithms
log_x = math.log(x)
log_x_base = math.log(x, base)
print(f"Natural logarithm of {x}: {log_x}")
print(f"Logarithm of {x} with base {base}: {log_x_base}")

# Trigonometric functions
angle_rad = math.pi / 4  # 45 degrees in radians
sin_angle = math.sin(angle_rad)
cos_angle = math.cos(angle_rad)
tan_angle = math.tan(angle_rad)
print(f"Sine of angle {angle_rad} radians: {sin_angle}")
print(f"Cosine of angle {angle_rad} radians: {cos_angle}")
print(f"Tangent of angle {angle_rad} radians: {tan_angle}")

# Factorial
factorial_x = math.factorial(y)
print(f"Factorial of {y}: {factorial_x}")

# Ceiling and Floor
ceil_x = math.ceil(x / 3)
floor_x = math.floor(x / 3)
print(f"Ceiling of {x}/3: {ceil_x}")
print(f"Floor of {x}/3: {floor_x}")

# Constants
pi = math.pi
e = math.e
print(f"Value of pi: {pi}")
print(f"Value of e: {e}")
