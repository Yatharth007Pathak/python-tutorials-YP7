# Public modifier

class ABC:
    def __init__(self):
        self.public_attribute = "Hello, World!"                    # Assign a value to the public attribute

    def public_function(self):
        print("This is a public function.")                        # A simple print statement in the public function

# Creating an object of class ABC
obj1 = ABC()

# Accessing the public attribute
print(obj1.public_attribute)                                       # Output: Hello, World!

# Calling the public function
obj1.public_function()                                             # Output: This is a public function.

'''
Break down this code line by line:

class ABC:
This line defines a new class named ABC. The ABC class contains a public attribute and a public method.

def __init__(self):
This line defines the initializer method (__init__) for the ABC class. 
It takes one parameter, self, which refers to the instance of the class.

self.public_attribute = "Hello, World!"
Inside the __init__ method, this line assigns the string "Hello, World!" to the instance variable self.public_attribute. 
This variable is a public attribute, meaning it can be accessed from outside the class.

def public_function(self):
This line defines a method named public_function within the ABC class. 
This method is a public function that can be called from outside the class.

print("This is a public function.")
Inside the public_function method, this line prints the message "This is a public function." to the console.

obj1 = ABC()
This line creates an instance of the ABC class and assigns it to the variable obj1. 
The __init__ method is automatically called, initializing the public_attribute with the value "Hello, World!".

print(obj1.public_attribute)
This line accesses the public_attribute of the obj1 object and prints its value, which is "Hello, World!".

obj1.public_function()
This line calls the public_function method on the obj1 object. The method prints the message "This is a public function." to the console.
'''