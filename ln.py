'''
pow function is a built-in function in Python and not part of the math module.
The pow function in Python can be used in two different forms:
pow(x, y): Returns x raised to the power of y (x**y).
pow(x, y, z): Returns (x**y) % z. This computes the power of x raised to y, then takes the modulus with z.

While the math module provides functions like math.pow(x, y) for raising x to the power of y, it does not include the modulus operation. 
The math.pow(x, y) function always returns a float and does not support the modulus operation.
'''

# Built-in pow(x, y) and pow(x, y, z):
x = 2
y = 3
result1 = pow(x, y)        # 2 raised to the power of 3
print(f"{x} raised to the power of {y} is {result1}")
z = 5
result2 = pow(x, y, z)     # (2**3) % 5
print(f"({x} raised to the power of {y}) modulo {z} is {result2}")

# math.pow(x, y):
import math
result = math.pow(2, 3)    # 2 raised to the power of 3, returns float
print("2 raised to power 3 is", result)