"""
In Python, a tuple is a built-in data structure that allows you to store an ordered collection of items. 
Tuple is an immutable, ordered collection of elements. 
Tuples are similar to lists, but unlike lists, tuples cannot be modified after their creation (i.e., they are immutable). 
This immutability makes tuples useful in situations where you need a fixed collection of items that should not be altered.
Tuples allow us to store mutiple items in a single variable.

Key Characteristics of Tuples:
Ordered: The elements in a tuple have a defined order, and that order will not change.
Immutable: Once a tuple is created, we cannot modify its elements (no adding, removing, or changing elements).
Duplicates allowed: Duplicates values are allowed in tuple.
Heterogeneous: Tuples can contain elements of different data types, such as integers, floats, strings, or even other tuples.
Indexed: We can access elements in a tuple using indices (starting from 0), just like with lists.

We can create a tuple by placing items inside parentheses (), separated by commas.

Tuples are typically used when you want to create a collection of items that should not be changed throughout the program. 
For example, tuples are often used to represent fixed collections like coordinates (x, y), RGB color values, or database records.

When to Use Tuples:
Fixed Data: Use tuples when you have a collection of items that should not change.
Heterogeneous Data: Tuples are often used to store heterogeneous data (data of different types), like records or database rows.
Dictionary Keys: Tuples can be used as keys in dictionaries because they are immutable.
Return Multiple Values: Functions often return tuples to send back multiple values.

Tuple vs Lists
Iterating through a tuple is faster than in a list.
Lists are mutable whereas tuples are immutable.
Tuples that contain immutable elements can be used as a key for a dictionary.
"""


# Creating a tuple of integers
numbers = (1, 2, 3, 4, 5)

# Creating a tuple of string
fruits = ("apple", "banana", "cherry")

# creating a tuple of mixed data types
mixed = (1, "Hello", 3.14, [5, 6, 7])

# A tuple with a single element (note the trailing comma)
single_element_tuple = (5,)


# Print the tuple and their type

print(numbers)
print(type(numbers))

print(fruits)
print(type(fruits))

print(mixed)
print(type(mixed))

print(single_element_tuple)
print(type(single_element_tuple))


# Length: Get the number of items in a tuple using len().
print(len(fruits))  # Output: 3


# Checking if an item is present or not in the tuple
if "banana" in fruits:
    print("Banana is part of the tuple") # Output: Banana is part of the tuple
if "kiwi" not in fruits:
    print("Kiwi is not part of the tuple") # Output: Kiwi is not part of the tuple


# Iterating over a tuple
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry


# Concatenation: Combine tuples using the + operator.
more_fruits = ("pineapple", "mango")
all_fruits = fruits + more_fruits
print(all_fruits)  # Output: ('apple', 'banana', 'cherry', 'pineapple', 'mango')

# Unpacking a tuple: Assign tuple elements to variables in a single statement.
fruit1, fruit2, fruit3 = fruits
print(fruit1, fruit2, fruit3)

# Repetition: Repeat the elements in a tuple using the * operator.
print(fruits * 2)  # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')