"""
In programming, an instance is a single occurrence of a class or object, and is a fundamental concept in object-oriented programming. 
An instance is a copy of an object that can be interacted with independently from other instances.
When we create an instance, the process is called instantisation.
During program execution, if a variable changes its value from one instance to another, it's called an instance variable

Here's a breakdown:

Object-Oriented Programming (OOP): In OOP, a class is like a blueprint or template for creating objects. 
An instance is a concrete realization of this class. 
For example, if we have a class Car, an instance of this class would be a specific car, like a red Toyota Corolla with a specific license plate.

Creating an Instance: We create an instance by calling a class as if it were a function. 
For instance, if Car is a class, we might create an instance with my_car = Car().

Instance Variables: Each instance of a class can have its own set of values for variables defined in the class. 
For example, each Car instance might have different values for color, model, and year.

Instance Methods: Instances can also use methods defined in the class. 
For example, the Car class might have a method drive() that you can call on my_car.

For example, if we define a class called "River", we can create instances of that class, such as "Volga", "Seine", and "Nile". 
An instance is built from a class blueprint, which is essentially a program code that acts as a template to create objects. 
An instance carries detailed information about the object, and can take the form of an element or document type.
"""

# basic example of creating and using instances in Python

# Define a basic class named 'Person'
class Person:
    # Constructor method to initialize the instance variable
    def __init__(self, name):
        self.name = name
# Create an instance of the Person class
person = Person("Alice")
# Print the name of the person
print(person.name)


'''
Explanation:
Class Definition: Person is a class with an __init__ method to initialize the name attribute.
Instance Creation: person is an instance of the Person class, created with the name "Alice."
Accessing Instance Variable: person.name accesses the name attribute of the instance and prints it.
'''