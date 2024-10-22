'''
In Python, a set is an unordered collection of unique elements. 
Sets are useful when we want to store a collection of items without any duplicates and do not care about the order of the items. 
Sets are mutable, meaning we can add or remove elements, but they do not allow duplicate values.
Sets are containers used for storing multiple values in a variable.

Characteristics of Sets:
Unindexed: The itmes inside the sets are unindexed
Unordered: Elements in a set are not stored in any particular order, so they cannot be indexed or sliced like lists or tuples.
Unique: A set automatically removes duplicate values, ensuring that each element is unique.
Duplicates not allowed: Duplicates values are not allowed in sets.
Partially Mutable: We can add or remove elements from a set after it is created, but cannot update existing values.
Any datatype: Sets can contain items of any datatype.
Mix of different datatypes: Items of different datatypes can be stored in one set
Heterogeneous: A set can contain elements of different data types, such as integers, strings, floats, etc.

We can create a set by placing all the elements inside curly braces {} or by using the built-in set() function.

While the set itself is mutable, the elements within it must be immutable.
Mutable Aspects:
You can add elements to a set using the add() method.
You can remove elements from a set using methods like remove(), discard(), or pop().

Immutable Aspects:
The elements inside a set must be immutable (e.g., integers, strings, tuples).
You cannot change an existing element in the set, but you can remove it and add a new one.
'''


# Creating a set of integers using curly braces
numbers = {1, 2, 3, 4, 5, 6, 7}

# Creating a set of integers using the set() function
my_set = set([1, 2, 3, 4, 5])

# Creating a list of strings
fruits = {"apple", "banana", "cherry"}

# Creating a mixed-type list
mixed = {1, "apple", 3.14, True, 7}


# Print the list and their type

print(numbers)
print(type(numbers))

print(my_set)
print(type(my_set))

print(fruits)
print(type(fruits))

print(mixed)
print(type(mixed))


# Length: Get the number of items in a set using len()
print(len(fruits))  # Output: 3


# Checking if an item is present or not in the set
if "banana" in fruits:
    print("Banana is part of the set") # Output: Banana is part of the set
if "kiwi" not in fruits:
    print("Kiwi is not part of the set") # Output: Kiwi is not part of the set


# Iterating over a set
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry