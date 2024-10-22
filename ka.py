# Operator overloading allows custom classes to define how standard operators (+, -, *, etc.) behave when applied to instances of those classes.

class Vector:                                                              # Define the Vector class
    def __init__(self, x, y):
        self.x = x                                                         # Initialize the vector with x and y coordinates
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)                  # Define addition for two Vector objects

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"                               # Provide a string representation of the Vector object

v1 = Vector(1, 2)                                                          # Create two Vector instances
v2 = Vector(3, 4)
v3 = v1 + v2                                                               # Add the two vectors using the overloaded __add__ method

print(v3)   # Output: Vector(4, 6)                                         # Print the result of the vector addition


# In this example, the + operator is overloaded to perform vector addition.