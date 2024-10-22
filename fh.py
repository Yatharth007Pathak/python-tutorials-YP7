# Accessing items in a Python dictionary can be done using various techniques, depending on the specific items we want to access.


my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}


# We can access all the keys in a dictionary using the keys() method. This method returns a view object that displays a list of all the keys.
# Accessing keys
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'city'])


# We can access all the values in a dictionary using the values() method. This method returns a view object that displays a list of all the values.
# Accessing values
values = my_dict.values()
print(values)  # Output: dict_values(['Alice', 25, 'New York'])


# We can access all the key-value pairs in a dictionary using the items() method. This method returns a view object that displays a list of tuples, where each tuple contains a key and its corresponding value.
# Accessing key-value pairs
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

'''
Keys: Use my_dict.keys() to access all the keys.
Values: Use my_dict.values() to access all the values.
Key-Value Pairs: Use my_dict.items() to access all key-value pairs as tuples.
'''


# Accessing a Specific Value by Key

# Using Square Brackets
# Accessing the value associated with the key 'name'
name = my_dict["name"]
print(name)  # Output: Alice

# Using get() Method
# The get() method is safer because it doesn’t raise a KeyError if the key is not found; instead, it returns None (or a default value you specify).
# Accessing the value using get()
age = my_dict.get("age")
print(age)  # Output: 25
# Accessing a key that doesn't exist using get()
country = my_dict.get("country")  # Returns None if the key is not found
print(country)  # Output: None

# Providing a default value for a missing key
country = my_dict.get("country", "USA")
print(country)  # Output: USA