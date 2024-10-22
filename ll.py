'''
math.fabs(x): Returns the absolute value of x as a float. 
Unlike the built-in abs() function, which returns an integer if the input is an integer, math.fabs() always returns a float.
'''

import math

# Define some numbers
positive_number = 5
negative_number = -3.14

# Calculate the absolute values
abs_positive = math.fabs(positive_number)
abs_negative = math.fabs(negative_number)

print(f"Absolute value of {positive_number}: {abs_positive}")
print(f"Absolute value of {negative_number}: {abs_negative}")