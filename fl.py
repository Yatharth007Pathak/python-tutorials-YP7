# Ways to merge or concatenate dictionaries in Python

# The update() method merges another dictionary into the current dictionary. This modifies the original dictionary.
# Two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# Using update() to merge dict2 into dict1
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# Using the {**dict1, **dict2} Syntax, to creates a new dictionary by unpacking the key-value pairs from the original dictionaries. (Python 3.5+)
# Two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# Using dictionary unpacking to merge
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# Using the | Operator for merging dictionaries, which creates a new dictionary without modifying the originals. (Python 3.9+)
# Two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# Using the | operator to merge
merged_dict = dict1 | dict2
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# We can also merge dictionaries using a dictionary comprehension.
# Two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# Using a dictionary comprehension to merge
merged_dict = {key: value for d in (dict1, dict2) for key, value in d.items()}
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}