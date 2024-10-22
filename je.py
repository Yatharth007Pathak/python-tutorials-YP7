"""
Methods are functions defined within a class that operate on instances of that class. 
They define the behavior of the objects and can modify the object's state or perform actions.
They can be instance methods (operate on object data), class methods (operate on class data), 
or static methods (do not operate on object or class data).
"""

# Instance Methods take self as their first parameter, which refers to the instance on which the method is called.
class Circle:                                   # Define the Circle class
    def __init__(self, radius):                 # Initialize the Circle instance with a radius
        self.radius = radius                    # Instance attribute to store the radius

    def area(self):                             # Method to calculate the area of the circle
        return 3.14 * (self.radius ** 2)        # Instance method to Calculate the area using the formula π * r^2

circle = Circle(5)                              # Create an instance of the Circle class with a radius of 5
print(circle.area())                            # Call the area method on the circle instance and print the result, Output: 78.5


# Class Methods are defined using the @classmethod decorator and take cls as their first parameter, which refers to the class itself rather than an instance.
class MathOperations:                           # Define the MathOperations class
    @classmethod                                # Define a class method to add two numbers
    def add(cls, a, b):
        return a + b                            # Return the sum of a and b

print(MathOperations.add(3, 5))                 # Call the class method add on the MathOperations class and print the result, Output: 8


# Static Methods are defined using the @staticmethod decorator and do not take self or cls as their first parameter. They do not depend on class or instance data.
class Utility:                                  # Define the Utility class
    @staticmethod                               # Define a static method to multiply two numbers
    def multiply(a, b):
        return a * b                            # Return the product of a and b

print(Utility.multiply(4, 5))                   # Call the static method multiply on the Utility class and print the result, Output: 20