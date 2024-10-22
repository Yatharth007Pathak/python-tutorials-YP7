# private modifier

class ABC:
    def __init__(self):
        self.__private_attribute = "Hello, World!"                 # Assign a value to the private attribute

    def __private_function(self):
        print("This is a private function.")                       # A simple print statement in the private function

# Creating an object of class ABC
obj1 = ABC()

# Accessing the private attribute
print(obj1.__private_attribute)                                    #  AttributeError

# Calling the private function
obj1.__private_function()                                          #  AttributeError

'''
Break down this code line by line:

class ABC:
This line defines a new class named ABC. The ABC class contains a private attribute and a private method.

def __init__(self):
This line defines the initializer method (__init__) for the ABC class. 
It takes one parameter, self, which refers to the instance of the class.

self.__private_attribute = "Hello, World!"
Inside the __init__ method, this line assigns the string "Hello, World!" to the instance variable self.__private_attribute. 
The double underscore prefix (__) makes this attribute private, meaning it cannot be accessed directly from outside the class.

def __private_function(self):
This line defines a method named __private_function within the ABC class. 
The double underscore prefix (__) makes this method private, meaning it cannot be called directly from outside the class.

print("This is a private function.")
Inside the __private_function method, this line prints the message "This is a private function." to the console.

obj1 = ABC()
This line creates an instance of the ABC class and assigns it to the variable obj1. 
The __init__ method is automatically called, initializing the __private_attribute with the value "Hello, World!".

print(obj1.__private_attribute)
This line attempts to access the private attribute __private_attribute of the obj1 object.
However, because __private_attribute is a private attribute (indicated by the double underscores), this results in an AttributeError. 
The error occurs because private attributes are not meant to be accessed directly from outside the class.

obj1.__private_function()
This line attempts to call the private method __private_function on the obj1 object. 
Similarly, because __private_function is a private method, this also results in an AttributeError. 
The error occurs because private methods are not meant to be called directly from outside the class.

Key Points:

Private Attributes and Methods: In Python, a double underscore prefix (__) before an attribute or method name makes it private. 
Private attributes and methods are intended to be accessed only within the class itself and are not directly accessible from outside the class.

Accessing Private Members: Attempting to access or call private members directly from outside the class results in an AttributeError.
'''