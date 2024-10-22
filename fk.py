# Dictionary Methods: Dictionaries come with several built-in methods for various operations:

my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(my_dict)

# keys(): Returns a view object of all the keys in the dictionary.
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'city'])

# values(): Returns a view object of all the values in the dictionary.
values = my_dict.values()
print(values)  # Output: dict_values(['Alice', 25, 'New York'])

# items(): Returns a view object of all the key-value pairs in the dictionary.
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# update(): Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.
my_dict.update({"age": 26, "city": "Los Angeles"})
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'Los Angeles'}

# clear(): Removes all items from the dictionary.
my_dict.clear()
print(my_dict)  # Output: {}