"""
Object-Oriented Programming (OOP) and Procedure-Oriented Programming (POP) are two fundamental programming paradigms, 
each with distinct approaches to writing and organizing code. Here's a breakdown of the differences:

1. Basic Concept
Object-Oriented Programming (OOP):
Focuses on creating objects, which are instances of classes that represent real-world entities.
Emphasizes the use of classes and objects, encapsulating data and behavior (methods) together.
Example languages: Python, Java, C++, C#.

Procedure-Oriented Programming (POP):
Focuses on writing procedures or functions, which operate on data.
Emphasizes a sequence of tasks or instructions to be executed.
Example languages: C, Pascal, Fortran.

2. Structure
OOP:
Code is organized around objects, which are instances of classes.
Methods (functions) are defined within classes, and these methods operate on data attributes within the class.
Promotes modular and reusable code through inheritance and polymorphism.

POP:
Code is organized around functions, and data is often passed between these functions.
Functions operate on global or local variables and are typically called in a sequence.
Code reuse is achieved through functions and procedures, but without the advanced features of OOP like inheritance.

3. Data Handling
OOP:
Encapsulation allows data to be hidden within objects, providing control over access and modification.
Data is protected and managed within the class, reducing the risk of unintended interference.

POP:
Data is often global, making it accessible to all functions. This can lead to a higher risk of accidental modification.
Less emphasis on data protection, and managing the scope of variables can be challenging in larger programs.

4. Abstraction
OOP:
Supports abstraction through classes and objects. You can model complex systems by abstracting details and focusing on higher-level design.
Abstract classes and interfaces allow the definition of common behavior that can be shared by multiple subclasses.

POP:
Abstraction is achieved through functions, but it is more challenging to represent real-world entities in a natural way.
The focus is more on the process rather than the entities involved in the process.

5. Modularity
OOP:
Promotes high modularity, as classes can be developed and tested independently.
Code is often easier to maintain, modify, and extend due to the modular structure.

POP:
Modularity is achieved through functions, but interdependencies between functions can make the codebase more difficult to maintain.
Modifying one function might require changes in others, especially in large programs.

6. Reusability
OOP:
Encourages code reusability through inheritance and polymorphism.
Classes can be extended or reused in different parts of the program or even in other programs.

POP:
Functions can be reused, but there is no concept of inheritance, making it less flexible for extending functionality.
Reusability is more manual and less systematic compared to OOP.

7. Complexity
OOP:
May have a steeper learning curve due to its abstraction and concepts like inheritance and polymorphism.
Better suited for complex, large-scale applications where modeling real-world entities is important.

POP:
Simpler and more straightforward, making it easier to learn and use for small to medium-sized programs.
May become cumbersome as the program size and complexity increase.

Summary
OOP is ideal for applications where real-world entities and relationships need to be modeled, 
offering benefits in terms of modularity, reusability, and maintainability.
POP is suited for simpler, sequential tasks where the focus is on the sequence of actions or procedures to be performed, 
making it easier to implement but less flexible as complexity grows.
"""

# Procedure-Oriented Programming (POP) Example

# Function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width

# Function to display the area
def display_area(length, width, area):
    print(f"The area of the rectangle with length {length} and width {width} is {area}")

# Main procedure
def main():
    length = 5
    width = 3
    area = calculate_area(length, width)
    display_area(length, width, area)

# Run the main procedure
main()


# Object-Oriented Programming (OOP) Example

# Define a Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def display_area(self):
        area = self.calculate_area()
        print(f"The area of the rectangle with length {self.length} and width {self.width} is {area}")

# Create an object of the Rectangle class
my_rectangle = Rectangle(5, 3)

# Call the method to display the area
my_rectangle.display_area()

'''
POP Example:
The program uses functions to perform tasks.
It follows a step-by-step approach where each function performs a specific task.
There is no concept of objects or classes.

OOP Example:
The program defines a Rectangle class with attributes (length and width) and methods (calculate_area and display_area).
An object (my_rectangle) is created from the Rectangle class, and methods are called on this object.
This approach encapsulates data (length and width) and behavior (calculating and displaying the area) together.
'''