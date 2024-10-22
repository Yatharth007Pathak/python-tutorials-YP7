"""
Python does not support traditional method overloading (having multiple methods with the same name but different signatures) 
as seen in some other languages. 
However, we can achieve similar functionality by using default arguments or variable-length argument lists
"""

# Example with Default Arguments:

class Greeter:                                                        # Define the Greeter class
    def greet(self, name=None):                                       # Method to return a greeting
        if name is not None:
            return f"Hello, {name}!"                                  # Return a personalized greeting
        else:
            return "Hello!"                                           # Return a generic greeting

greeter = Greeter()                                                   # Create an instance of the Greeter class

print(greeter.greet())          # Output: Hello!                      # Call the greet method with no arguments
print(greeter.greet("Alice"))   # Output: Hello, Alice!               # Call the greet method with a name argument


# Example with Variable-Length Arguments:

class Calculator:                                                     # Define the Calculator class
    def add(self, *args):                                             # Method to add any number of arguments
        return sum(args)                                              # Sum up all the arguments provided
    
calc = Calculator()                                                   # Create an instance of the Calculator class

# Call the add method with different numbers of arguments
print(calc.add(1, 2))          # Output: 3
print(calc.add(1, 2, 3, 4))    # Output: 10



# In these examples, greet and add can handle different numbers of arguments, providing flexibility similar to method overloading.