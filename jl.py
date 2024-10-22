# protected modifier

class ABC:
    def __init__(self):
        self._protected_attribute = "Hello, World!"                # Assign a value to the protected attribute

    def _protected_function(self):
        print("This is a protected function.")                     # A simple print statement in the protected function

# Creating an object of class ABC
obj1 = ABC()

# Accessing the protected attribute
print(obj1._protected_attribute)                                   # Output: Hello, World!

# Calling the protected function
obj1._protected_function()                                         # Output: This is a protected function.

'''
Break down this code line by line:

class ABC:
This line defines a new class named ABC. The ABC class contains a protected attribute and a protected method.

def __init__(self):
This line defines the initializer method (__init__) for the ABC class. 
It takes one parameter, self, which refers to the instance of the class.

self._protected_attribute = "Hello, World!"
Inside the __init__ method, this line assigns the string "Hello, World!" to the instance variable self._protected_attribute.
The single underscore (_) before the variable name indicates that _protected_attribute is a protected attribute. 
By convention, protected attributes are meant to be accessible within the class and by subclasses, 
but they are still accessible from outside the class if needed.

def _protected_function(self):
This line defines a method named _protected_function within the ABC class. 
The single underscore before the method name indicates that _protected_function is a protected method. 
Like protected attributes, protected methods are intended to be used within the class and by subclasses, 
but they can still be called from outside the class.

print("This is a protected function.")
Inside the _protected_function method, this line prints the message "This is a protected function." to the console.

obj1 = ABC()
This line creates an instance of the ABC class and assigns it to the variable obj1. 
The __init__ method is automatically called, initializing the _protected_attribute with the value "Hello, World!".

print(obj1._protected_attribute)
This line accesses the protected attribute _protected_attribute of the obj1 object and prints its value, which is "Hello, World!". 
Even though the attribute is protected, it can still be accessed from outside the class.

obj1._protected_function()
This line calls the protected method _protected_function on the obj1 object. 
The method prints the message "This is a protected function." to the console. 
Even though the method is protected, it can still be called from outside the class.
'''