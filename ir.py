"""
String formatting in Python allows you to create formatted strings by embedding variables or expressions within a string. 
Python provides several methods for string formatting, each with its own style and use cases.

Old-style (%): Simple, but less flexible.
str.format(): More powerful and versatile.
F-strings: Modern, concise, and efficient.
Template strings: Secure and simple, especially with user inputs.
"""


'''
 Old-Style String Formatting (%)
This method uses the % operator to embed values into a string.
%s is a placeholder for strings.  %d is a placeholder for integers.
'''
name = "Alice"
age = 30
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)  # Output: My name is Alice and I am 30 years old.


'''
str.format() Method
The str.format() method is more flexible and powerful than the % operator. 
It uses curly braces {} as placeholders, which can be replaced by variables or expressions.
'''
name = "Bob"
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: My name is Bob and I am 25 years old.

# Positional arguments: You can reference arguments by their position.
formatted_string = "I have {0} apples and {1} oranges.".format(3, 5)
print(formatted_string)  # Output: I have 3 apples and 5 oranges.

# Named arguments: You can use named placeholders.
formatted_string = "My name is {name} and I am {age} years old.".format(name="Charlie", age=28)
print(formatted_string)  # Output: My name is Charlie and I am 28 years old.

# Reordering placeholders: You can reorder the placeholders based on their position or name.
formatted_string = "{1} is {0} years old.".format(28, "Charlie")
print(formatted_string)  # Output: Charlie is 28 years old.


'''
Formatted String Literals (f-strings)
Introduced in Python 3.6, f-strings are the most modern and concise method for string formatting. 
They allow you to embed expressions directly within string literals by prefixing the string with f or F.
'''

# Expressions inside f-strings: You can evaluate expressions directly within the curly braces.
x = 5
y = 10
formatted_string = f"The sum of {x} and {y} is {x + y}."
print(formatted_string)  # Output: The sum of 5 and 10 is 15.

# Formatting numbers: You can format numbers for better readability.
pi = 3.14159
formatted_string = f"Pi rounded to two decimal places is {pi:.2f}."
print(formatted_string)  # Output: Pi rounded to two decimal places is 3.14.


'''
String Interpolation with Template Strings
Template strings, provided by the string module, offer another way to perform string formatting with a simpler syntax and added security, 
especially useful when dealing with user inputs.
'''
from string import Template
template = Template("My name is $name and I am $age years old.")
formatted_string = template.substitute(name="Eve", age=35)
print(formatted_string)  # Output: My name is Eve and I am 35 years old.


'''
Advanced Formatting with str.format()
'''

# Width and Alignment: You can specify the width and alignment of strings.
formatted_string = "{:<10} is my name.".format("John")
print(formatted_string)  # Output: John       is my name. (Left-aligned within 10 spaces)

# Padding and Precision: Control the precision of floating-point numbers and pad with spaces or zeros.
formatted_string = "{:0>5}".format(42)
print(formatted_string)  # Output: 00042 (Padded with zeros to be 5 characters long)