# Greeting a User


# POP Version:
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

'''
def greet(name):
This line defines a function named greet that takes one parameter, name. 
The purpose of this function is to generate a greeting message for the person whose name is passed as an argument.

return f"Hello, {name}!"
Inside the greet function, this line creates a formatted string using an f-string. 
The {name} placeholder inside the string is replaced with the value of the name parameter. 
The function then returns this string. For example, if name is "Alice", the function returns "Hello, Alice!".

print(greet("Alice"))
This line calls the greet function with the argument "Alice". 
The function returns the greeting "Hello, Alice!", which is then passed to the print function. 
Finally, the print function outputs this greeting to the console.
'''

# OOP Version:
class Greeter:
    def greet(self, name):
        return f"Hello, {name}!"
greeter = Greeter()
print(greeter.greet("Alice"))

'''
class Greeter:
This line defines a new class named Greeter. This class is designed to provide greeting functionality.

def greet(self, name):
This line defines a method named greet within the Greeter class. 
The method takes two parameters: self, which refers to the instance of the class, and name, which is the name of the person to greet.

return f"Hello, {name}!"
Inside the greet method, this line uses an f-string to create a greeting message. 
The {name} placeholder in the f-string is replaced with the value of the name parameter. 
The method returns a string like "Hello, Alice!" when name is "Alice".

greeter = Greeter()
This line creates an instance of the Greeter class and assigns it to the variable greeter. 
This object can now use the methods defined in the Greeter class.

print(greeter.greet("Alice"))
This line calls the greet method on the greeter object with the argument "Alice". 
The greet method returns the string "Hello, Alice!", which is then passed to the print function. 
The print function outputs "Hello, Alice!" to the console.
'''