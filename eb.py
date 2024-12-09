# creating various types of lists in Python

# List of Integers
numbers = [10, 20, 30, 40, 50]
print(numbers)  # Output: [10, 20, 30, 40, 50]

# List of Strings
fruits = ["apple", "banana", "cherry", "date"]
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# Mixed-Type List
mixed = [1, "apple", 3.14, True]
print(mixed)  # Output: [1, 'apple', 3.14, True]

# Nested List (2D List)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
# Output: 
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# Empty List
empty_list = []
print(empty_list)  # Output: []

# List Created Using range()
range_list = list(range(1, 11))
print(range_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List of Boolean Values
booleans = [True, False, True, True, False]
print(booleans)  # Output: [True, False, True, True, False]

# List of Tuples
coordinates = [(0, 0), (1, 1), (2, 2)]
print(coordinates)  # Output: [(0, 0), (1, 1), (2, 2)]

# List of Lists
list_of_lists = [[1, 2], [3, 4], [5, 6]]
print(list_of_lists)  # Output: [[1, 2], [3, 4], [5, 6]]

# List Using List Comprehension
squares = [x**2 for x in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# List of Characters from a String
characters = list("hello")
print(characters)  # Output: ['h', 'e', 'l', 'l', 'o']
