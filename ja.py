"""
Object-Oriented Programming (OOP) in Python is a programming paradigm that uses "objects" to model real-world entities.
OOP in Python is a programming paradigm that uses objects and classes to structure and manage code.
OOP is a programming paradigm which focuses on data or objects rather than functions
Python supports OOP concepts like classes, objects, inheritance, encapsulation, and polymorphism.
OOPs helps to mimic real world entities and thier interactions.

Procedure-Oriented Programming (POP) in Python uses functions to structure and manage code.

Why use OOPs in Python?
OOPs helps to mimic real world entities and their interactions, code reusability, organisation and maintainabilty of code

OOP is powerful because it allows us to create modular, reusable, and organized code. 
By using classes and objects, we can model real-world entities in our programs, making our code easier to understand and maintain.

The key concepts and components of OOP in Python:
Classes and Objects: Define and instantiate objects.
Encapsulation: Hide data and restrict access to methods.
Inheritance: Create a hierarchy by inheriting from base classes.
Polymorphism: Use methods interchangeably with different objects.
Abstraction: Expose only necessary parts of the objects, hiding complexity.
Using these principles, Python allows for creating complex, modular, and reusable code structures.
"""

# Define the Dog class
class Dog:
    # Initialize the Dog instance with a name
    def __init__(self, name):
        self.name = name  # Instance attribute to store the dog's name

    # Method to make the dog bark
    def bark(self):
        # Print a message indicating that the dog is barking
        print(f"{self.name} says woof!")

# Create an instance of the Dog class with the name 'Buddy'
my_dog = Dog("Buddy")

# Call the bark method on the my_dog instance
my_dog.bark()  # Output: Buddy says woof!

'''
Let's break down this code line by line:

class Dog:
This line defines a new class named Dog. The purpose of this class is to represent a dog with some basic attributes and behaviors.

def __init__(self, name):
This line defines the initializer method (__init__) for the Dog class. 
It takes two parameters: self (which refers to the instance of the class) and name (the name of the dog).

self.name = name
Inside the __init__ method, this line assigns the value of the name parameter to the instance variable self.name. 
This means that each Dog object will store its name in self.name.

def bark(self):
This line defines a method named bark for the Dog class. This method simulates the dog barking by printing a message.

print(f"{self.name} says woof!")
Inside the bark method, this line uses an f-string to create a message that includes the dog's name. 
The {self.name} placeholder is replaced with the value of the self.name attribute, resulting in a message like "Buddy says woof!". 
This message is then printed to the console.

my_dog = Dog("Buddy")
This line creates an instance of the Dog class with the argument "Buddy". 
The __init__ method initializes this instance, setting self.name to "Buddy".

my_dog.bark()
This line calls the bark method on the my_dog object. The method prints "Buddy says woof!" using the name attribute of my_dog.
'''