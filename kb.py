"""
Abstraction allows us to focus on the 'what of' an object rather than 'how' of the object
Abstraction involves hiding complex implementation details and showing only the essential features of the object. 
In Python, abstraction can be achieved using abstract classes and methods (with the abc module).
An abstract class may contain abstract methods, which must be implemented by its concrete subclasses.
"""

from abc import ABC, abstractmethod

class Shape(ABC):                                                # Define an abstract base class Shape
    @abstractmethod
    def area(self):
        pass                                                     # Abstract method that must be implemented by any subclass

class Circle(Shape):                                             # Define a concrete class Circle that inherits from Shape
    def __init__(self, radius):
        self.radius = radius                                     # Initialize the Circle with a radius

    def area(self):
        return 3.14 * self.radius * self.radius                  # Implement the area method for a circle

circle = Circle(5)                                               # Create an instance of Circle
print(circle.area())   # Output: 78.5                            # Call the area method and print the result


'''
The provided code demonstrates the use of abstract base classes (ABCs) and method overriding in Python. Here's a detailed breakdown:

from abc import ABC, abstractmethod
This line imports the ABC class and the abstractmethod decorator from the abc module. 
ABC is used to define abstract base classes, and abstractmethod is used to declare abstract methods that must be implemented by subclasses.

class Shape(ABC):
This defines an abstract base class named Shape that inherits from ABC. 
Since Shape is an abstract class, it cannot be instantiated directly and is meant to be subclassed.

@abstractmethod
This decorator is used to declare a method as abstract. 
Abstract methods are placeholders that define a method signature but do not provide an implementation. 
Subclasses of Shape must override this method.

def area(self):
This method is declared as abstract. It does not provide any implementation in the Shape class. 
Subclasses must provide their own implementation of this method.

pass
This line is a placeholder in the abstract method and does nothing. 
It signifies that the area method is abstract and does not yet have an implementation.

class Circle(Shape):
This defines a class named Circle that inherits from Shape. 
It provides a concrete implementation of the abstract methods defined in the Shape class.

def __init__(self, radius):
This is the constructor method for the Circle class. It initializes the radius attribute when creating an instance of Circle.

self.radius = radius
This line sets the radius instance variable to the value provided when creating a Circle instance.

def area(self):
This method provides a concrete implementation of the abstract area method from the Shape class. It calculates the area of the circle.

return 3.14 * self.radius * self.radius
This line calculates the area of the circle using the formula pi * r^2. Here, π is approximated as 3.14.

circle = Circle(5)
This line creates an instance of the Circle class with a radius of 5 and assigns it to the variable circle.

print(circle.area())
This line calls the area method on the circle instance. The area method in the Circle class calculates the area as 3.14 * 5^2 = 78.5 
and prints the result.

Summary:
Abstract Base Class (ABC): The Shape class is an abstract base class that defines an interface for shapes but does not provide concrete implementations.
Abstract Method: The area method in Shape is abstract and must be implemented by subclasses.
Concrete Implementation: The Circle class inherits from Shape and provides a specific implementation of the area method.
Instantiation and Usage: An instance of Circle is created, and the area method is called to compute and print the area of the circle.
'''
