"""
List comprehension is used when we want to make a new list from items of an existing list.
List comprehension in Python is a concise way to create lists by embedding a loop inside square brackets []. 
It allows us to generate a new list by applying an expression to each item in an existing iterable 
(like a list, tuple, or range), optionally including a condition to filter items.
List comprehension can be used to perform operations on elements of an iterable and return a new list.
List comprehension consist of brackets containing an expression followed by a for clause, and optionally, one or more for or if clauses.

Basic Syntax
[expression for item in iterable if condition]

expression: The expression that generates the items in the new list.
item: The variable that takes the value of each element in the iterable.
iterable: The collection or sequence of items to loop over.
condition: (Optional) A filter that determines whether the item should be included.
"""

# Creating a list of fruits containing 'a' using list comprehension:
fruits = ["kiwi", "orange", "guava", "mango", "strawberry", "coconut"]
new_fruits = [fruit for fruit in fruits if "a" in fruit]
print(new_fruits) # Output: ["orange", "guava", "mango", "strawberry"]

# Copy a list:
new_fruits = fruits.copy()
print(new_fruits) # Output: ["kiwi", "orange", "guava", "mango", "strawberry", "coconut"]

# Concatenation: Combine lists using the + operator.
more_fruits = ["pineapple"]
all_fruits = fruits + more_fruits
print(all_fruits)  # Output: ["kiwi", "orange", "guava", "mango", "strawberry", "coconut", 'pineapple']

# If we you want to create a list of squares for numbers from 1 to 10:
squares = [x**2 for x in range(1, 11)]
print(squares) # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# We can add an if statement to filter items. If we want to filter out only even numbers from a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens) # Output: [2, 4, 6, 8, 10]

# We can use list comprehensions to apply a function to each element in a list. For example, converting all strings in a list to uppercase:
words = ["apple", "banana", "cherry", "date"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words) # Output: ['APPLE', 'BANANA', 'CHERRY', 'DATE']

# Nested List Comprehensions for creating lists with multiple levels, like a matrix:
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix) # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# List comprehensions can be nested to work with multi-dimensional data like flattening a 2D list (matrix) into a 1D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using Conditional Logic i.e. we can include conditions in list comprehensions:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_or_even = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(odd_or_even) # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']

# Conditional Expressions in List Comprehension e.g. Replacing negative numbers with 0:
numbers = [-1, 2, -3, 4, -5]
non_negative = [x if x > 0 else 0 for x in numbers]
print(non_negative)  # Output: [0, 2, 0, 4, 0]

# Creating a List of Tuples (pairs of numbers) using list comprehension:
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# Using List Comprehension with Strings by creating a list of individual characters from strings
chars = [char for char in "hello"]
print(chars)  # Output: ['h', 'e', 'l', 'l', 'o']