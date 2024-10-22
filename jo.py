"""
Inheritance is the property of OOP where one class inherit properties (attributes and methods) from another class
Inheritance allows a class to inherit attributes and methods from another class. 
The class that is inherited from is called the parent or base class, and the class that inherits is called the child or derived class.
This promotes code reuse and establishes a natural hierarchy.
When working with inheritance, super() function calls the constructor of the base class.

Syntax:
class SuperClass:
    # Attributes and meethods of superclass go here

class SubClass(SuperClass)
    # Additional attributes and methods of subclass go here
"""

class Parent:                                               # Define the Parent class
    def __init__(self):                                     # Initialize the Parent class
        print("This is a parent class")                     # Print a message indicating this is the Parent class


class Child(Parent):                                        # Define the Child class that inherits from the Parent class
    def __init__(self):                                     # Initialize the Child class
        super().__init__()                                  # Call the __init__ method of the Parent class using super()
        print("This is a child class")                      # Print a message indicating this is the Child class

# Create an instance of the Child class
child1 = Child()                                            # This will trigger the initialization of both the Parent and Child classes


'''
Let's break down this code step by step, focusing on the concept of inheritance and the use of super():

class Parent:
This line defines a new class named Parent. This class will serve as the base class for another class.

def __init__(self):
This line defines the initializer method (__init__) for the Parent class. 
It takes one parameter, self, which refers to the instance of the class.

print("This is a parent class")
Inside the __init__ method of the Parent class, this line prints the message "This is a parent class" 
to the console when an instance of the Parent class (or a subclass) is created.

class Child(Parent):
This line defines a new class named Child, which inherits from the Parent class. 
The Child class is a subclass of Parent, meaning it inherits the properties and methods of the Parent class.

def __init__(self):
This line defines the initializer method (__init__) for the Child class. 
It takes one parameter, self, which refers to the instance of the class.

super().__init__()
Inside the __init__ method of the Child class, this line calls the __init__ method of the parent class (Parent). 
The super() function returns a temporary object of the parent class, allowing you to call its methods. 
In this case, it ensures that the parent class's initialization code is executed, which prints "This is a parent class".

print("This is a child class")
After calling the parent class's __init__ method, this line prints the message "This is a child class" 
to the console when an instance of the Child class is created.

child1 = Child()
This line creates an instance of the Child class and assigns it to the variable child1. 
When this instance is created, the following happens:

The __init__ method of the Child class is called.
Inside the Child class's __init__ method, super().__init__() is executed, 
which calls the __init__ method of the Parent class, printing "This is a parent class".
After that, the print("This is a child class") statement is executed, printing "This is a child class".

When the Child class instance child1 is created, it first calls the parent class's initializer through super().__init__(), 
which prints "This is a parent class". Then, it prints "This is a child class" from the child class's initializer. 
This demonstrates how the child class inherits behavior from the parent class and can extend or modify it.
'''


'''
Class Definition:
Parent Class: The Parent class is defined with an __init__ method that prints a message when an instance is created.
Child Class: The Child class is defined to inherit from the Parent class. It also has its own __init__ method.

Inheritance:
super().__init__(): In the Child class's __init__ method, super().__init__() is used to call the __init__ method of the Parent class. 
This ensures that the parent class's initialization code is executed when a Child object is created.

Instance Creation: When child1 is created, the following happens:
The __init__ method of the Parent class is called, printing "This is a parent class".
The __init__ method of the Child class continues, printing "This is a child class".
'''