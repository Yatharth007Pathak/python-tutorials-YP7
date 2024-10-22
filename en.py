# Creating various types of tuples in python

# tuple of Integers
numbers = (10, 20, 30, 40, 50)
print(numbers)  # Output: (10, 20, 30, 40, 50)

# Tuple of Strings
fruits = ("apple", "banana", "cherry", "date")
print(fruits)  # Output: ('apple', 'banana', 'cherry', 'date')

# Mixed-Type Tuple
mixed = (1, "apple", 3.14, True)
print(mixed)  # Output: (1, 'apple', 3.14, True)

# Nested Tuple (2D Tuple)
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(matrix)
# Output: 
# (
#   (1, 2, 3),
#   (4, 5, 6),
#   (7, 8, 9)
# )

# Empty Tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()

# Tuple Created Using range()
range_tuple = tuple(range(1, 11))
print(range_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Tuple of Boolean Values
booleans = (True, False, True, True, False)
print(booleans)  # Output: (True, False, True, True, False)

# Tuple of Tuples
coordinates = ((0, 0), (1, 1), (2, 2))
print(coordinates)  # Output: ((0, 0), (1, 1), (2, 2))
9
# Tuple of lists
Tuple_of_lists = ([1, 2], [3, 4], [5, 6])
print(Tuple_of_lists)  # Output: ([1, 2], [3, 4], [5, 6])

# Tuple Using Tuple Comprehension
squares = (x**2 for x in range(1, 11))
print(squares)  # Output: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# Tuple of Characters from a String
characters = tuple("hello")
print(characters)  # Output: ('h', 'e', 'l', 'l', 'o')

# Creating a tuple without parentheses (optional)
another_tuple = 10, 20, 30
print(another_tuple) # Output: (10, 20, 30)

# Creating a tuple with a single element (note the trailing comma)
single_element_tuple = (42,)
print(single_element_tuple) # Output: (42,)