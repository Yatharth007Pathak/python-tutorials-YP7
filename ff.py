'''
In Python, a dictionary is an unordered collection of key-value pairs. Each key is unique and maps to a corresponding value. 
Dictionaries are mutable, meaning you can change, add, or remove items after the dictionary is created. 
They are one of the most commonly used data structures in Python for managing and storing data in a structured way.
Dictionary allows us to store key-value pairs

Characteristics of Dictionaries
Ordered: Dictionaries preserve the insertion order of keys.
Unindexed: The itmes inside the dictionaries are unindexed.
Key-Value Pairs: Each item in a dictionary is a pair consisting of a key and a value.
Unique Keys: Keys must be unique within a dictionary. If we attempt to assign a value to an existing key, the old value will be replaced with the new one.
Duplicates not allowed: Duplicates values are not allowed in keys
Any datatype: Key-value pairs can be of any datatype.
Mutable: We can modify the dictionary by adding, removing, or updating key-value pairs.
Heterogeneous: Keys and values in a dictionary can be of any data type (integers, strings, lists, etc.).

We can create a dictionary by enclosing a comma-separated list of key-value pairs within curly braces {} or by using the dict() function.
'''

# Creating a dictionary using curly braces
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Creating a dictionary using the dict() function
my_dicto = dict(name="Alice", age=25, city="New York")


# Print the dictionary and their type

print(my_dict)
print(type(my_dict))

print(my_dicto)
print(type(my_dicto))


# Length: Get the number of key-value pairs in a dictionary using len()
print(len(my_dict))  # Output: 3


# Checking if a Key is Present or not in the dictionary
# We can use the 'in' keyword to check if a key exists in a dictionary.
if "name" in my_dict:
    print("name is a key in the dictionary") # Output: name is a key in the dictionary
if "job" not in my_dict:
    print("job is not a key in the dictionary") # Output: job is not a key in the dictionary


# Checking if a Value is Present or not in the dictionary
# We can use the 'in' keyword with the 'values()' method to check if a value exists in a dictionary.
if 25 in my_dict.values():
    print("25 is a value in the dictionary") # Output: 25 is a value in the dictionary
if "Delhi" not in my_dict.values():
    print("Delhi is not a value in the dictionary") # Output: Delhi is not a value in the dictionary


# Checking if a Key-Value Pair is Present or not in the dictionary
# We can use the in keyword with the 'items()' method to check if a key-value pair exists in a dictionary.
if ("city", "New York")in my_dict.items():
    print("city: New York is a key value pair in the dictionary") # Output: city: New York is a key value pair in the dictionary
if ("age", 30) not in my_dict.items():
    print("age: 30 is not a key value pair in the dictionary") # Output: age: 30 is not a key value pair in the dictionary

'''
Use in to check if a key is in the dictionary.
Use in with values() to check if a value is in the dictionary.
Use in with items() to check if a key-value pair is in the dictionary.
'''


# We can iterate over the keys, values, or key-value pairs of a dictionary using a for loop.

# Iterating over keys
for key in my_dict.keys():
    print(key)
# Output:
# name
# age 
# city

# Iterating over values
for value in my_dict.values():
    print(value)
# Output:
# Alice
# 25
# New York

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 25
# city: New York


'''
We cannot concatenate dictionaries using the + operator in Python. 
The + operator is not defined for dictionaries, so attempting to use it will result in a TypeError.

However, there are several ways to merge or concatenate dictionaries in Python. Here are some methods:
Using the update() Method
Using the {**dict1, **dict2} Syntax (Python 3.5+)
Using the | Operator (Python 3.9+)
Using a Dictionary Comprehension
'''