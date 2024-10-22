# Accessing Values in Nested Dictionaries
# If a dictionary contains another dictionary (a nested dictionary), we can access the values by chaining the keys.
# For nested dictionaries, chain square brackets to access nested keys.

# Nested dictionary
nested_dict = {
    "person1": {"name": "Bob", "age": 30},
    "person2": {"name": "Charlie", "age": 25}
}

# Accessing the value of a key in a nested dictionary
person1_name = nested_dict["person1"]["name"]
print(person1_name)  # Output: Bob


# Nested dictionary
nested_dicto = {
    "person": {
        "name": "Bob",
        "age": 30,
        "address": {
            "city": "Los Angeles",
            "state": "California"
        }
    }
}

# Accessing the values of nested dictionary keys
city = nested_dicto["person"]["address"]["city"]
print(city)  # Output: Los Angeles