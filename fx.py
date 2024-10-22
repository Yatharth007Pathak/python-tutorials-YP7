# Examples of Using Different Types of Parameters or Arguments Together


# Positional and Keyword Parameters or Arguments:
def describe_person(name, age, city="Unknown"):
    print(f"{name} is {age} years old and lives in {city}.")
describe_person("Alice", 25)                   # Output: Alice is 25 years old and lives in Unknown.
describe_person("Bob", 30, "New York")         # Output: Bob is 30 years old and lives in New York.
describe_person(age=35, name="Charlie")        # Output: Charlie is 35 years old and lives in Unknown.


# Mixing Positional, Default, and Keyword Parameters or Arguments:
def describe_pet(animal_type, pet_name="Unknown"):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")
describe_pet("dog", "Rex")  # Output: I have a dog. My dog's name is Rex.
describe_pet("cat")         # Output: I have a cat. My cat's name is Unknown.


# Combining *args and **kwargs:
def summarize(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
summarize(1, 2, 3, name="Alice", age=25)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 25}