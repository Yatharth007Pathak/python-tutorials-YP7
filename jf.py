# In Object-Oriented Programming (OOP) in Python, the dot operator (.) is used to access the attributes and methods of an object.

# When we have an instance of a class, you use the dot operator to access its instance variables (attributes).
class Person:                                              # Define a class named Person
    def __init__(self, name, age):                         # Initialize the instance with name and age
        self.name = name                                   # Set the instance variable 'name'
        self.age = age                                     # Set the instance variable 'age'
person = Person("Alice", 30)                               # Create an instance of Person with name "Alice" and age 30
# Access instance variables using the dot operator
print(person.name)                                         # print the 'name' instance variable of the 'person' object, Outputs: Alice
print(person.age)                                          # print the 'name' instance variable of the 'age' object, Outputs: 30


# The dot operator is also used to call methods on an instance of a class.
class Calculator:                                          # Define a class named Calculator
    def add(self, a, b):                                   # Method to add two numbers
        return a + b                                       # Return the sum of a and b
calc = Calculator()                                        # Create an instance of the Calculator class
result = calc.add(5, 3)                                    # Call the 'add' method of the 'calc' object with arguments 5 and 3
print(result)                                              # Print the result of the addition, Outputs: 8


# We can use the dot operator to access class-level variables and methods as well, though they are typically accessed through the class itself rather than an instance.
class Math:                                                # Define a class named Math
    pi = 3.14159                                           # Class variable representing the value of pi
    @staticmethod                                          # Static method to multiply two numbers
    def multiply(a, b):
        return a * b                                       # Return the product of a and b
print(Math.pi)                                             # Access class variable using the dot operator from the Math class, Outputs: 3.14159
result = Math.multiply(4, 5)                               # Call static method using the dot operator from the Math class with arguments 4 and 5
print(result)                                              # Print the result of the multiplication, Outputs: 20


'''
Summary
Instance Attributes: Accessed with object.attribute
Instance Methods: Called with object.method()
Class Variables: Accessed with Class.variable
Static Methods: Called with Class.method()

The dot operator is fundamental in Python for interacting with objects and their associated data and functionality.
'''