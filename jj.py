"""
Access modifiers are used to control the visibility or access of class attributes and functions
The three main types of access modifiers in Python are:
Public (no underscore): Accessible from anywhere.
Protected (single underscore _): Intended to be used within the class and subclasses. Accessible from outside, but it's not recommended.
Private (double underscore __): Accessible only within the class. Name mangling makes it harder to access from outside.
"""

'''
Public (public):
Attributes and methods with no underscores before their names are considered public.
They can be accessed from anywhere—inside the class, outside the class, or in derived classes.
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width   # Public attribute
        self.height = height # Public attribute

    def area(self):
        return self.width * self.height  # Public method

rect = Rectangle(5, 10)
print(rect.width)   # Accessing public attribute
print(rect.area())  # Accessing public method

print()

'''
Protected (protected):
Attributes and methods with a single underscore _ before their names are considered protected.
They are intended to be accessed only within the class and its subclasses, 
but they can still be accessed from outside if needed (Python does not enforce strict access restrictions).
'''
class Rectangle:
    def __init__(self, width, height):
        self._width = width   # Protected attribute
        self._height = height # Protected attribute

    def _area(self):           # Protected method
        return self._width * self._height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def display_area(self):
        print(f"Area: {self._area()}")  # Accessing protected method from subclass

square = Square(5)
square.display_area()  # Correct usage of protected attribute/method

print(square._width)   # Accessing protected attribute (not recommended)

print()

'''
Private (private):
Attributes and methods with a double underscore __ before their names are considered private.
They are intended to be accessed only within the class where they are defined. 
Python "name mangles" these attributes/methods to make them harder to access from outside the class, though it is still possible.
'''
class Rectangle:
    def __init__(self, width, height):
        self.__width = width   # Private attribute
        self.__height = height # Private attribute

    def __area(self):           # Private method
        return self.__width * self.__height

    def display_area(self):
        print(f"Area: {self.__area()}")  # Accessing private method within class

rect = Rectangle(5, 10)
rect.display_area()              # Correct usage of private attribute/method

# print(rect.__width)            # Error: can't access private attribute directly
# print(rect.__area())           # Error: can't access private method directly

# Accessing private attribute/method using name mangling (not recommended)
print(rect._Rectangle__width)    # Access private attribute using name mangling
print(rect._Rectangle__area())   # Access private method using name mangling