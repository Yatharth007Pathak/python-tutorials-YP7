# Python program that uses Object-Oriented Programming (OOP) principles to represent a basic Car class.

# Define the Car class
class Car:
    # Initialize the Car instance with make, model, and year
    def __init__(self, make, model, year):
        self.make = make       # Set the 'make' attribute
        self.model = model     # Set the 'model' attribute
        self.year = year       # Set the 'year' attribute

    # Method to start the car
    def start(self):
        # Print a message indicating the car is starting
        print(f"The {self.year} {self.make} {self.model} is starting.")

    # Method to stop the car
    def stop(self):
        # Print a message indicating the car is stopping
        print(f"The {self.year} {self.make} {self.model} is stopping.")

# Create an instance of the Car class with specific attributes
my_car = Car("Toyota", "Corolla", 2020)

# Call the start method on the my_car instance
my_car.start()  # Output: The 2020 Toyota Corolla is starting.

# Call the stop method on the my_car instance
my_car.stop()  # Output: The 2020 Toyota Corolla is stopping.



'''
Let's break down the code line by line:

class Car:
This line defines a new class called Car. In Python, a class is a blueprint for creating objects. 
The Car class will represent a car with specific attributes and behaviors.

def __init__(self, make, model, year):
This line defines a special method called __init__, which is the initializer or constructor method in Python. 
It is automatically called when a new instance of the Car class is created. 
The parameters make, model, and year are passed to the constructor when creating a new car object. 
The self parameter refers to the instance of the class itself.

self.make = make
This line assigns the value passed as the make parameter to the instance variable self.make. 
This means that each car object will store its make (e.g., "Toyota") in its own make attribute.

self.model = model
Similar to the previous line, this assigns the value passed as the model parameter to the instance variable self.model, 
storing the car's model (e.g., "Corolla") within the object.

self.year = year
This line assigns the value passed as the year parameter to the instance variable self.year, 
storing the year of the car (e.g., 2020) in the object.

def start(self):
This line defines a new method called start for the Car class. 
This method will perform an action (in this case, print a message) when called. 
The self parameter is again used to refer to the specific instance of the Car class on which this method is called.

print(f"The {self.year} {self.make} {self.model} is starting.")
Inside the start method, this line prints a formatted string that includes the car's year, make, and model. 
The f before the string indicates that it is an f-string, which allows embedding expressions inside string literals. 
When start() is called, it will display a message like "The 2020 Toyota Corolla is starting."

def stop(self):
This line defines another method called stop for the Car class. 
Like the start method, it will perform an action when called. The self parameter refers to the instance of the class.

print(f"The {self.year} {self.make} {self.model} is stopping.")
Inside the stop method, this line prints a formatted string similar to the start method but indicates that the car is stopping. 
For example, it would print "The 2020 Toyota Corolla is stopping."

my_car = Car("Toyota", "Corolla", 2020)
This line creates a new instance of the Car class and assigns it to the variable my_car. 
The parameters "Toyota", "Corolla", and 2020 are passed to the __init__ method, 
which initializes the make, model, and year attributes of the my_car object.

my_car.start()
This line calls the start method on the my_car object. 
It triggers the start method to execute, printing "The 2020 Toyota Corolla is starting."

my_car.stop()
This line calls the stop method on the my_car object. 
It triggers the stop method to execute, printing "The 2020 Toyota Corolla is stopping."
'''