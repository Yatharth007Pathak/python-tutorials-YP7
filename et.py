# tuple methods: In Python, tuples have only two built-in methods: count() and index()
# The primary reason tuples have only these two methods is that they are immutable.

numbers = (1, 2, 2, 3, 4, 2)
fruits = ("apple", "banana", "cherry", "banana")


# count(): Returns the number of times a specified value occurs in the tuple.
count_of_twos = numbers.count(2)
print(count_of_twos)  # Output: 3


# index(): Returns the index of the first occurrence of a specified value. Raises a ValueError if the value is not found.
index_of_banana = fruits.index("banana")
print(index_of_banana)  # Output: 1


# Searching for "banana" starting from index 2
index_of_banana_later = fruits.index("banana", 2)
print(index_of_banana_later)  # Output: 3


# Searching for "banana" starting from index 1 and ending at index 2
index_of_banana_between = fruits.index("banana", 1, 2)
print(index_of_banana_between)  # Output: 1
