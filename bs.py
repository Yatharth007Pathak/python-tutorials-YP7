'''
In Python, the range function is commonly used to generate a sequence of numbers. 
It is often used in for loops to iterate over a specific set of numbers. Let's explore how the range function works and its various parameters.

The range function can take one, two, or three arguments:

range(stop): Generates numbers from 0 to stop - 1.
range(start, stop): Generates numbers from start to stop - 1.
range(start, stop, step): Generates numbers from start to stop - 1, incrementing by step.
'''

# Generates numbers from 0 to 4
for number in range(5):
    print(number)
print("\n")

# Generates numbers from 3 to 7
for number in range(3, 8):
    print(number)
print("\n")

# Generates numbers from 2 to 10, incrementing by 2
for number in range(2, 11, 2):
    print(number)
print("\n")

# Generates numbers from 10 down to 1
for number in range(10, 0, -1):
    print(number)
print("\n")

# Create a list from a range
numbers_list = list(range(1, 6))
print(numbers_list)
print("\n")