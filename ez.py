# creating various types of sets in Python

# Set of Integers
numbers = {10, 20, 30, 40, 50}
print(numbers)  # Output: {10, 20, 30, 40, 50}

# Set of Strings
fruits = {"apple", "banana", "cherry", "date"}
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'date'}

# Mixed-Type Set
mixed = {1, "apple", 3.14, True}
print(mixed)  # Output: {1, 'apple', 3.14, True}

# Empty Set
empty_set = set() # Note: {} creates an empty dictionary, not a set
print(empty_set)  # Output: set()

# Set Created Using range()
range_set = set(range(1, 11))
print(range_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Set of Boolean Values
booleans = {True, False, True, True, False}
print(booleans)  # Output: {False, True}

# Set of Tuples
coordinates = {(0, 0), (1, 1), (2, 2)}
print(coordinates)  # Output: {(0, 0), (1, 1), (2, 2)}

# Set Using Set Comprehension
squares = {x**2 for x in range(1, 11)}
print(squares)  # Output: {1, 4, 9, 16, 25, 36, 49, 64, 81, 100}

# Set of Characters from a String
characters = set("hello")
print(characters)  # Output: {'h', 'e', 'l', 'o'}