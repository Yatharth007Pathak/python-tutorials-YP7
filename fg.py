# Creating various types of dictionaries in python  


# A dictionary with strings as both keys and values:
string_dict = {
    "name": "Alice",
    "city": "New York",
    "occupation": "Engineer"
}
print(string_dict) # Output: {'name': 'Alice', 'city': 'New York', 'occupation': 'Engineer'}

# A dictionary with integers as both keys and values:
int_dict = {
    1: 100,
    2: 200,
    3: 300
}
print(int_dict) # Output: {1: 100, 2: 200, 3: 300}

# A dictionary with mixed types for keys:
mixed_keys_dict = {
    "name": "Bob",
    5: [10, 20, 30],
    (2, 3): "Tuple as key",
    True: "Boolean Key"
}
print(mixed_keys_dict) # Output: {'name': 'Bob', 5: [10, 20, 30], (2, 3): 'Tuple as key', True: 'Boolean Key'}

# A dictionary with mixed types for values:
mixed_values_dict = {
    "name": "Charlie",
    "age": 30,
    "is_student": False,
    "scores": [85, 90, 95],
    "address": {"street": "5th Avenue", "city": "Los Angeles"}
}
print(mixed_values_dict) # Output: {'name': 'Charlie', 'age': 30, 'is_student': False, 'scores': [85, 90, 95], 'address': {'street': '5th Avenue', 'city': 'Los Angeles'}}


# An empty dictionary
empty_dict = {}
print(empty_dict) # Output: {}

# A dictionary where each value is a list:
list_dict = {
    "fruits": ["apple", "banana", "cherry"],
    "vegetables": ["carrot", "spinach", "broccoli"],
    "numbers": [1, 2, 3, 4, 5]
}
print(list_dict) # Output: {'fruits': ['apple', 'banana', 'cherry'], 'vegetables': ['carrot', 'spinach', 'broccoli'], 'numbers': [1, 2, 3, 4, 5]}


# A dictionary where each value is another dictionary (nested dictionary):
nested_dict = {
    "person1": {"name": "David", "age": 25},
    "person2": {"name": "Eva", "age": 30},
    "person3": {"name": "Frank", "age": 35}
}
print(nested_dict) # Output: {'person1': {'name': 'David', 'age': 25}, 'person2': {'name': 'Eva', 'age': 30}, 'person3': {'name': 'Frank', 'age': 35}}


# A dictionary where each value is a tuple:
tuple_dict = {
    "coordinates1": (10.5, 20.5),
    "coordinates2": (30.0, 40.0),
    "coordinates3": (50.5, 60.5)
}
print(tuple_dict) # Output: {'coordinates1': (10.5, 20.5), 'coordinates2': (30.0, 40.0), 'coordinates3': (50.5, 60.5)}


# A dictionary with Boolean keys:
bool_keys_dict = {
    True: "Yes",
    False: "No"
}
print(bool_keys_dict) # Output: {True: 'Yes', False: 'No'}


# A dictionary that uses None as a key or value:
none_dict = {
    None: "No value",
    "key1": None,
    "key2": "Some value"
}
print(none_dict) # Output: {None: 'No value', 'key1': None, 'key2': 'Some value'}


# A dictionary where each value is a function:
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
func_dict = {
    "add": add,
    "subtract": subtract
}
print(func_dict) # Output: {'add': <function add at 0x000000004Ad00>, 'subtract': <function subtract at 0x00000eX00>}
# Calling functions stored in the dictionary
result1 = func_dict["add"](10, 5)
result2 = func_dict["subtract"](10, 5)
print(result1)  # Output: 15
print(result2)  # Output: 5