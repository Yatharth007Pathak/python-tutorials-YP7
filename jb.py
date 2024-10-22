"""      
In Object-Oriented Programming (OOP), self is a special keyword used in class methods to refer to the instance of the class.
In essence, self is a way to ensure that each instance of a class has its own unique set of attributes and methods.
Here's what we need to know about self:

Instance Reference: self refers to the current instance of the class. 
It is used to access instance variables and methods from within class methods.

Initialization: When you create an instance of a class, 
self allows the methods within the class to access and modify the attributes of that specific instance.

Usage:
In Methods: self is used as the first parameter in instance methods. 
It helps to distinguish between instance attributes and local variables within methods.
Not a Keyword: self is not a reserved keyword in Python. 
It's just a convention. You could use any name, but self is the widely accepted and recommended name.
"""


class Car:
    # Constructor method
    def __init__(self, make, model):
        self.make = make   # Instance variable
        self.model = model # Instance variable

    # Method to display car details
    def display_info(self):
        return f"{self.make} {self.model}"

# Create an instance of Car
my_car = Car("Toyota", "Corolla")

# Call the display_info method
print(my_car.display_info())


'''
class Car:
This line defines a new class named Car. The Car class will represent a car with some basic attributes and functionality.

def __init__(self, make, model):
This line defines the initializer method (__init__) for the Car class. It takes three parameters: 
self (which refers to the instance of the class), make (the manufacturer of the car), and model (the model of the car).

self.make = make
Inside the __init__ method, this line assigns the value of the make parameter to the instance variable self.make. 
This means that each Car object will store its make in self.make.

self.model = model
This line assigns the value of the model parameter to the instance variable self.model. 
This means that each Car object will store its model in self.model.

def display_info(self):
This line defines a method named display_info for the Car class. This method returns a string that displays the car's make and model.

return f"{self.make} {self.model}"
Inside the display_info method, this line uses an f-string to create a formatted string that includes the car's make and model.
The placeholders {self.make} and {self.model} are replaced with the values of the corresponding instance variables, 
resulting in a string like "Toyota Corolla".

my_car = Car("Toyota", "Corolla")
This line creates an instance of the Car class with the arguments "Toyota" and "Corolla". 
The __init__ method initializes this instance, setting self.make to "Toyota" and self.model to "Corolla".

print(my_car.display_info())
This line calls the display_info method on the my_car object. 
The method returns the string "Toyota Corolla", which is then passed to the print function. 
The print function outputs "Toyota Corolla" to the console, displaying the car's make and model.
'''

'''
__init__ Method: The __init__ method initializes the instance with make and model. 
self allows us to assign these values to the instance variables self.make and self.model.

display_info Method: This method uses self to access the instance variables self.make and self.model 
and returns a string with the car's information.
'''