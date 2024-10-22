"""
Attributes are variables that belong to an object or class. They represent the state or properties of the object. In Python, 
attributes are often defined within the __init__ method of a class, but they can also be added or modified outside of the class definition.
They can be instance-specific (created with self) or shared across all instances (class attributes).
The 'init' method is automatically called when an object is created and allows us to iniitialize its attributes.

Instance attributes are specific to a particular instance/object

Class attributes are defined inside class. All object instances will have these attributes
"""

# Instance Attributes are attributes specific to an instance of a class. They are defined within the __init__ method and are accessed using self.
class Person:                                        # Define the Person class
    def __init__(self, name, age):                   # Initialize the Person instance with name and age
        self.name = name                             # Instance attribute, Set the 'name' attribute
        self.age = age                               # Instance attribute, Set the 'age' attribute

person = Person("Alice", 30)                         # Create an instance of the Person class with specific attributes
print(person.name)                                   # Print the 'name' attribute of the person instance, Output: Alice
print(person.age)                                    # Print the 'age' attribute of the person instance, Output: 30


# Class Attributes are attributes shared by all object instances of a class. They are defined directly within the class body.
class Dog:                                           # Define the Dog class
    species = "Canis familiaris"                     # Class attribute shared by all instances
 
    def __init__(self, name, age):                   # Initialize the Dog instance with name and age
        self.name = name                             # Instance attribute for the dog's name
        self.age = age                               # Instance attribute for the dog's age

dog1 = Dog("Buddy", 4)                               # Create an instance of the Dog class named 'dog1'
dog2 = Dog("Max", 5)                                 # Create another instance of the Dog class named 'dog2'
print(dog1.species)                                  #  Print the 'species' attribute for dog1, Output: Canis familiaris
print(dog2.species)                                  #  Print the 'species' attribute for dog1, Output: Canis familiaris