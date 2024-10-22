tuple1 = (1, 2, 3)


# Max/Min: Find the maximum or minimum value in a tuple.
max_value = max(tuple1)  # Output: 3
min_value = min(tuple1)  # Output: 1
print(max_value)
print(min_value)

# Membership Test: Check if an element exists in a tuple using the in keyword.
is_in_tuple = 2 in tuple1  # Output: True
print(is_in_tuple)

# Length: Get the number of items in a tuple using len().
length = len(tuple1)  # Output: 3
print(length)

# Slicing: Access a portion of the tuple using slicing.
result = tuple1[1:3]  # Output: (2, 3)
print(result)

# Repetition: Repeat elements in a tuple using the * operator.
result = tuple1 * 2  # Output: (1, 2, 3, 1, 2, 3)
print(result)