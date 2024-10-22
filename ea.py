"""
In Python, a list is a built-in data structure that allows us to store an ordered collection of items. 
Lists are mutable, meaning we can change their contents without changing their identity. 
They are very versatile and can hold a mix of different data types, including integers, floats, strings, and even other lists.
Lists allow us to store mutiple items in a single variable.

Here are some key characteristics and operations associated with lists:
Indexed: The itmes inside the list are indexed. Zero based indexing is followed in lists i.e. the index of first item is 0.
Ordered: Lists maintain the order of items as they are added. We can access items using their index, with the first item having an index of 0.
Mutable: We can modify lists by adding, removing, or changing items.
Duplicates allowed: Duplicates values are allowed in list.
Any datatype: Lists can contain items of any datatype.
Mix of different datatypes: Items of different datatypes can be stored in one list
Dynamic: Lists can grow and shrink in size as needed.

We can create a list by placing items inside square brackets [], separated by commas.

In Python, a method is a function that is defined with respect to a particular object.
Like any function, a method has zero or more parameters
The syntax is object.method(parameters)
For example, consides we have as string S, then string methods are:
S.upper()    S.lower()    S.count(substring)    S.replace(old,new)    S.find(substring)       s.index()
"""

# Creating a list of integers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "banana", "cherry"]

# Creating a mixed-type list
mixed = [1, "apple", 3.14, True]


# Print the list and their type

print(numbers)
print(type(numbers))

print(fruits)
print(type(fruits))

print(mixed)
print(type(mixed))


# Length: Get the number of items in a list using len()
print(len(fruits))  # Output: 3


# Checking if an item is present or not in the list
if "banana" in fruits:
    print("Banana is part of the list") # Output: Banana is part of the list
if "kiwi" not in fruits:
    print("Kiwi is not part of the list") # Output: Kiwi is not part of the list


# Iterating over a list
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry


# Concatenation: Combine lists using the + operator.
more_fruits = ["pineapple", "mango"]
all_fruits = fruits + more_fruits
print(all_fruits)  # Output: ['apple', 'banana', 'cherry', 'pineapple', 'mango']