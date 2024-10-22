"""
The zip function in Python is used to combine multiple iterables (such as lists, tuples, etc.) 
into a single iterator of tuples. Each tuple contains elements from the corresponding position in each of the input iterables.

How It Works
Combining Iterables: The zip function takes two or more iterables as arguments and returns an iterator of tuples. 
Each tuple contains the elements from the corresponding position in each iterable.
Length: The length of the result is determined by the shortest input iterable. 
If the input iterables are of different lengths, the resulting iterator will be as long as the shortest input iterable.
"""

# Basic example of using zip function
# Two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
# Combining lists using zip
combined = zip(names, ages)
# Converting to a list
combined_list = list(combined)
print(combined_list) # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Two lists
l1 = ["A", "B", "C"]
l2 = [1, 2, 3]
# Combining lists using zip and type casting it to a dictionary
my_dict = dict(zip(l1, l2))
print(my_dict) # Output: {'A':1, 'B':2, 'C':3}


# handling different lengths using zip function
# Lists of different lengths
names = ["Alice", "Bob"]
ages = [25, 30, 35]
# Combining lists using zip
combined = zip(names, ages)
# Converting to a list
combined_list = list(combined)
print(combined_list) # Output: [('Alice', 25), ('Bob', 30)]
# Here, the resulting list contains tuples only for the length of the shortest input list.


# Unzipping Values: We can also unzip values using zip and unpacking:
# Combined list of tuples
combined_list = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
# Unzipping
names, ages = zip(*combined_list)
print(names)  # Output: ('Alice', 'Bob', 'Charlie')
print(ages)   # Output: (25, 30, 35)


# Using zip with Different Types of Iterables
# Combining lists and a tuple
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ("New York", "Los Angeles", "Chicago")
# Combining lists and a tuple using zip
combined = zip(names, ages, cities)
# Converting to a list
combined_list = list(combined)
print(combined_list) # Output: [('Alice', 25, 'New York'), ('Bob', 30, 'Los Angeles'), ('Charlie', 35, 'Chicago')]


'''
zip Function: Combines multiple iterables into an iterator of tuples.
Handling Different Lengths: Stops at the shortest iterable.
Unzipping: Use zip(*iterable) to separate combined values back into individual iterables.
'''