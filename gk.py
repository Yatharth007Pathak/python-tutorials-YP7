'''
Here's a Python program that demonstrates the use of various built-in functions. 
These functions cover different categories, such as mathematical operations, type conversions, and string manipulations.
'''

# Demonstrating various built-in functions in Python

# abs(): Returns the absolute value of a number
print("Absolute value of -7:", abs(-7))  # Output: 7

# all(): Returns True if all elements in an iterable are true
print("All elements are true:", all([True, 1, 3, "hello"]))  # Output: True
print("All elements are true:", all([True, 1, 0, "hello"]))  # Output: False

# any(): Returns True if any element in an iterable is true
print("Any element is true:", any([False, 0, 0, ""]))  # Output: False
print("Any element is true:", any([False, 0, 0, "hello"]))  # Output: True

# bin(): Converts an integer to a binary string
print("Binary representation of 10:", bin(10))  # Output: 0b1010

# bool(): Converts a value to a Boolean
print("Boolean value of 0:", bool(0))  # Output: False
print("Boolean value of 1:", bool(1))  # Output: True

# chr(): Returns a string representing a character from its Unicode code
print("Character for Unicode 97:", chr(97))  # Output: a

# divmod(): Returns the quotient and remainder of division
print("Quotient and remainder of 10 divided by 3:", divmod(10, 3))  # Output: (3, 1)

# enumerate(): Adds a counter to an iterable and returns it
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Fruit {index}: {fruit}")
# Output:
# Fruit 0: apple
# Fruit 1: banana
# Fruit 2: cherry

# eval(): Evaluates a string as a Python expression
expression = "3 * 5 + 2"
print("Evaluation of expression '3 * 5 + 2':", eval(expression))  # Output: 17

# float(): Converts a value to a floating-point number
print("Float representation of '3.14':", float("3.14"))  # Output: 3.14

# int(): Converts a value to an integer
print("Integer representation of '100':", int("100"))  # Output: 100

# len(): Returns the length of an object
print("Length of the list [1, 2, 3, 4]:", len([1, 2, 3, 4]))  # Output: 4

# max(): Returns the largest item in an iterable or the largest of two or more arguments
print("Maximum value in the list [1, 4, 7, 2]:", max([1, 4, 7, 2]))  # Output: 7

# min(): Returns the smallest item in an iterable or the smallest of two or more arguments
print("Minimum value in the list [1, 4, 7, 2]:", min([1, 4, 7, 2]))  # Output: 1

# pow(): Returns the value of x raised to the power y
print("2 to the power 3:", pow(2, 3))  # Output: 8

# range(): Returns a sequence of numbers
print("Range from 0 to 5:", list(range(6)))  # Output: [0, 1, 2, 3, 4, 5]

# round(): Rounds a number to a given precision
print("Rounding 3.14159 to 2 decimal places:", round(3.14159, 2))  # Output: 3.14

# sorted(): Returns a sorted list from the elements of any iterable
unsorted_list = [3, 1, 4, 1, 5, 9]
print("Sorted list:", sorted(unsorted_list))  # Output: [1, 1, 3, 4, 5, 9]

# sum(): Sums the items of an iterable
print("Sum of the list [1, 2, 3, 4]:", sum([1, 2, 3, 4]))  # Output: 10

# type(): Returns the type of an object
print("Type of 'hello':", type("hello"))  # Output: <class 'str'>

# zip(): Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print("Zipped list:", list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

'''
Mathematical Operations: abs(), divmod(), pow(), round(), sum().
Type Conversion: bin(), bool(), chr(), float(), int(), str().
String Operations: len(), sorted(), type().
Iterables and Iteration: all(), any(), enumerate(), zip().
Evaluation: eval().
'''