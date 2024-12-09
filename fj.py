my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# We can add a new key-value pair or modify an existing one by assigning a value to a key.

# Adding a new key-value pair
my_dict["country"] = "USA"
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA'}

# Modifying an existing value
my_dict["age"] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}


# We can remove key-value pairs using the del keyword, the pop() method, or the popitem() method.

# Removing an item using del
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'country': 'USA'}

# Removing an item using pop()
age = my_dict.pop("age")
print(age)  # Output: 26
print(my_dict)  # Output: {'name': 'Alice', 'country': 'USA'}

# Removing the last inserted key-value pair using popitem() (Python 3.7+)
last_item = my_dict.popitem()
print(last_item)  # Output: ('country', 'USA')
print(my_dict)  # Output: {'name': 'Alice'}
