"""
In Python, the __init__ method is a special method that is used to initialize a newly created object. 
It is commonly known as the "constructor" because it allows us to set the initial state of an object by assigning values to its attributes. 
The __init__ method is called automatically when an instance of a class is created.
The __init__ method is crucial for setting up new objects. It allows for flexibility in how objects are initialized by accepting parameters.
Although __init__ is a common place to initialize attributes, it can also be used to perform any other setup needed when an object is created.

Key Points about __init__:

Automatic Invocation: The __init__ method is automatically called when we create a new instance of a class. We don't need to call it explicitly.

Self Parameter: The first parameter of __init__ is always self, which refers to the instance being created. 
It is through self that we can access and assign values to the instance's attributes.

Initialization: The main purpose of __init__ is to initialize the object's attributes with initial values.

Optional Parameters: We can define __init__ with parameters, allowing us to pass arguments when creating an object to set its initial state.
"""

# Example of __init__:

class Person:                                                            # Define the Person class
    def __init__(self, name, age):                                       # Initialize the Person instance with name and age
        self.name = name                                                 # Initialize the name attribute
        self.age = age                                                   # Initialize the age attribute

    def greet(self):                                                     # Method to greet with the person's name and age
        print(f"My name is {self.name} and I am {self.age} years old")   # Print a greeting message using the name and age attributes

# Creating an object of the Person class
person1 = Person("Alice", 30)                                            # Create an object of the Person class with the name "Alice" and age 30

# Accessing the object's attributes (name attribute and age attribute of person1)
print(person1.name)                                                      # Output: Alice
print(person1.age)                                                       # Output: 30

# Call the greet method of person1 to print the greeting message
person1.greet()                                                          # Output: My name is Alice and I am 30 years old



# Default Values in __init__:

class Person:                                                            # Define the Person class
    def __init__(self, name="Unknown", age=0):                           # Initialize the Person instance with default values for name and age
        self.name = name                                                 # Assign the provided or default name to the instance
        self.age = age                                                   # Assign the provided or default age to the instance

    def greet(self):                                                     # Method to greet with the person's name and age
        print(f"My name is {self.name} and I am {self.age} years old")   # Print a greeting message using the name and age attributes
 
# Creating objects with and without providing arguments
person1 = Person("Bob", 25)                                              # Create a Person object with specified name and age
person2 = Person()                                                       # Create a Person object with default values

# Calling the greet method to print the greeting messages
person1.greet()                                                          # Output: My name is Bob and I am 25 years old
person2.greet()                                                          # Output: My name is Unknown and I am 0 years old