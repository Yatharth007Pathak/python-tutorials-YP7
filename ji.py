"""
Write a Python class named Rectangle to represent a rectangle shape. The class should have the following functionalities:

A method named set_dimensions that takes two parameters width and height and sets the attributes of the rectangle object accordingly.
A method named area that calculates and returns the area of the rectangle
A method named perimeter that calculates and returns the perimeter of the rectangle

Use this to create objects of the class and print the width, height, area and perimeter.
"""

class Rectangle:                                               # Define the Rectangle class
    def __init__(self):                                        # Initialize the Rectangle instance with default width and height of 0
        self.width = 0                                         # Instance attribute for the width of the rectangle
        self.height = 0                                        # Instance attribute for the height of the rectangle

    def set_dimensions(self, width, height):                   # Method to set the dimensions of the rectangle
        self.width = width                                     # Set the width attribute
        self.height = height                                   # Set the height attribute
  
    def area(self):                                            # Method to calculate the area of the rectangle
        return self.width * self.height                        # Return the area (width * height)
   
    def perimeter(self):                                       # Method to calculate the perimeter of the rectangle
        return 2 * (self.width + self.height)                  # Return the perimeter (2 * (width + height))

rect1 = Rectangle()                                            # Create an instance (object) of the Rectangle class
rect1.set_dimensions(5, 10)                                    # Set the dimensions for rect1

rect2 = Rectangle()                                            # Create another instance (object) of the Rectangle class
rect2.set_dimensions(4, 8)                                     # Set the dimensions for rect2

# Print the width, height, area, and perimeter for rect1
print(f"Width: {rect1.width}")                                 # Output: Width: 5
print(f"Height: {rect1.height}")                               # Output: Height: 10
print(f"Area: {rect1.area()}")                                 # Output: Area: 50
print(f"Perimeter: {rect1.perimeter()}")                       # Output: Perimeter: 30

# Print the width, height, area, and perimeter for rect2
print("Width:", rect2.width)                                   # Output: Width: 4
print("Height:", rect2.height)                                 # Output: Height: 8
print("Area:", rect2.area())                                   # Output: Area: 32
print("Perimeter:", rect2.perimeter())                         # Output: Perimeter: 24


'''
Let's break down this code line by line:

class Rectangle:
This line defines a new class named Rectangle. This class is intended to represent a rectangle and provide functionality for 
setting dimensions, calculating the area, and calculating the perimeter.

def __init__(self):
This line defines the initializer method (__init__) for the Rectangle class. 
It takes one parameter, self, which refers to the instance of the class.
Initializes the rectangle's dimensions to 0. It ensures that each new instance of the Rectangle class starts with default values.

self.width = 0
Inside the __init__ method, this line initializes the instance variable self.width to 0. This sets the default width of the rectangle to 0.

self.height = 0
This line initializes the instance variable self.height to 0. This sets the default height of the rectangle to 0.

def set_dimensions(self, width, height):
This line defines a method named set_dimensions that takes three parameters: self, width, and height. 
This method allows setting the dimensions of the rectangle. Sets the width and height of the rectangle based on the provided parameters.

self.width = width
Inside the set_dimensions method, this line sets the instance variable self.width to the value of the width parameter.

self.height = height
This line sets the instance variable self.height to the value of the height parameter.

def area(self):
This line defines a method named area that calculates the area of the rectangle.

return self.width * self.height
Inside the area method, this line calculates the area by multiplying the width and height of the rectangle and returns the result.

def perimeter(self):
This line defines a method named perimeter that calculates the perimeter of the rectangle.

return 2 * (self.width + self.height)
Inside the perimeter method, this line calculates the perimeter by adding the width and height, multiplying the sum by 2, and returns the result.

rect1 = Rectangle()
This line creates an instance of the Rectangle class and assigns it to the variable rect1. 
The __init__ method initializes this instance with default dimensions of width 0 and height 0.

rect1.set_dimensions(5, 10)
This line calls the set_dimensions method on rect1 to set its width to 5 and its height to 10.

rect2 = Rectangle()
This line creates another instance of the Rectangle class and assigns it to the variable rect2. 
Like rect1, this instance starts with default dimensions of width 0 and height 0.

rect2.set_dimensions(4, 8)
This line calls the set_dimensions method on rect2 to set its width to 4 and its height to 8.

print(f"Width: {rect1.width}")
This line prints the width of rect1, which is 5.

print(f"Height: {rect1.height}")
This line prints the height of rect1, which is 10.

print(f"Area: {rect1.area()}")
This line calls the area method on rect1 to calculate and print its area, which is 5 * 10 = 50.

print(f"Perimeter: {rect1.perimeter()}")
This line calls the perimeter method on rect1 to calculate and print its perimeter, which is 2 * (5 + 10) = 30.

print("Width:", rect2.width)
This line prints the width of rect2, which is 4.

print("Height:", rect2.height)
This line prints the height of rect2, which is 8.

print("Area:", rect2.area())
This line calls the area method on rect2 to calculate and print its area, which is 4 * 8 = 32.

print("Perimeter:", rect2.perimeter())
This line calls the perimeter method on rect2 to calculate and print its perimeter, which is 2 * (4 + 8) = 24.
'''