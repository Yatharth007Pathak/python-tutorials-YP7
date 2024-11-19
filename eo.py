# Accessing items in a Python tuple can be done using various techniques, depending on the specific items we want to access.

fruits = ("apple", "banana", "cherry", "date")


# Accessing Elements by Index i.e positive indexing
# Each element in a tuple is associated with an index, starting from 0 for the first element. We can use these indices to access specific elements.
print("first_fruit =", fruits[0])  # "apple"
print("second_fruit =", fruits[1])  # "banana"
print("last_fruit =", fruits[3])  # "date"


# Accessing Elements Using Negative Indices i.e negative indexing
# Negative indices allow us to access elements from the end of the tuple. The last element has an index of -1, the 2nd last element has an index of -2, and so on.
print("last_fruit =", fruits[-1])  # Output: date
print("second_last_fruit =", fruits[-2])  # Output: cherry


# Accessing a Range of Elements (Slicing) i.e range indexing
# Slicing is used to access a range of elements in a tuple. The syntax for slicing is tuple[start:end], which returns a new tuple containing elements from the start index up to, but not including, the end index.
print("some_fruits =", fruits[1:3])  # Output: ['banana', 'cherry']
print("all_fruits =", fruits[:])  # Output: ['apple', 'banana', 'cherry', 'date']
print("fruits_from_second =", fruits[1:])  # Output: ['banana', 'cherry', 'date']
print("fruits_up_to_third =", fruits[:3])  # Output: ['apple', 'banana', 'cherry']


# Slicing with Step
# We can also specify a step value in slicing to skip elements. The syntax for this is tuple[start:end:step].
print("every_second_fruit =", fruits[::2])  # Output: ['apple', 'cherry']
print("reverse_fruits =", fruits[::-1])  # Output: ['date', 'cherry', 'banana', 'apple']


# Slicing using range of negative indexes i.e negative range indexing
print("some_fruits =", fruits[-3:-1]) # Output: ['banana', 'cherry']
print("some_fruits =", fruits[-4::2]) # Output: ['apple', 'cherry']


# We can iterate over the elements of a tuple using a for loop, which is useful for accessing each item without needing an index.
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
# date


# If we need both the index and the value during iteration, you can use the enumerate() function
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry
# 3 date
