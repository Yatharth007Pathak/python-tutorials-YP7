"""
Inheritance is a key feature of Object-Oriented Programming (OOP) that allows a class to inherit attributes and methods from another class.

Single Inheritance: Inherits from one base class.
Multiple Inheritance: Inherits from more than one base class.
Multilevel Inheritance: Inherits from a derived class, creating a chain.
Hierarchical Inheritance: Multiple classes inherit from the same base class.
Hybrid Inheritance: A combination of different types of inheritance.
"""


# Show how a child class (Car) can inherit properties and methods from a parent class (Vehicle)

class Vehicle:                                                       # Define the Vehicle class
    def __init__(self, make, model):                                 # Initialize the Vehicle instance with make and model
        self.make = make                                             # Assign the make (manufacturer) to the instance
        self.model = model                                           # Assign the model to the instance

    def start(self):                                                 # Method to start the vehicle
        print(f"{self.make} {self.model} is starting.")              # Print a message indicating the vehicle is starting

class Car(Vehicle):                                                  # Define the Car class that inherits from the Vehicle class
    def __init__(self, make, model, year):                           # Initialize the Car instance with make, model, and year
        super().__init__(make, model)                                # Call the parent class's __init__ method to set make and model
        self.year = year                                             # Assign the year to the instance

    def display_info(self):                                          # Method to display the car's information
        print(f"{self.year} {self.make} {self.model}")               # Print the car's year, make, and model

my_car = Car("Toyota", "Corolla", 2020)                              # Create an instance of the Car class
my_car.start()             # Output: Toyota Corolla is starting.     # Call the start method inherited from the Vehicle class
my_car.display_info()      # Output: 2020 Toyota Corolla             # Call the display_info method from the Car class



'''
Let's break down this code step by step, focusing on inheritance, method overriding, and the use of super():

class Vehicle:
This line defines a new class named Vehicle. The Vehicle class will serve as the base class for other classes like Car.

def __init__(self, make, model):
This line defines the initializer method (__init__) for the Vehicle class. It takes three parameters: self, make, and model. 
self refers to the instance of the class, while make and model are used to initialize the vehicle's make and model.

self.make = make
Inside the __init__ method, this line assigns the value of make to the instance variable self.make.

self.model = model
Similarly, this line assigns the value of model to the instance variable self.model.

def start(self):
This line defines a method named start within the Vehicle class. This method will be inherited by any subclass of Vehicle.

print(f"{self.make} {self.model} is starting.")
Inside the start method, this line prints a message indicating that the vehicle (with its make and model) is starting.

class Car(Vehicle):
This line defines a new class named Car, which inherits from the Vehicle class. 
The Car class is a subclass of Vehicle, meaning it inherits all the properties and methods of the Vehicle class.

def __init__(self, make, model, year):
This line defines the initializer method (__init__) for the Car class. 
It takes four parameters: self, make, model, and year. The Car class introduces an additional attribute, year.

super().__init__(make, model)
Inside the __init__ method of the Car class, this line calls the __init__ method of the parent class (Vehicle) using super(). 
This initializes the make and model attributes by passing them to the parent class's initializer.

self.year = year
This line assigns the value of year to the instance variable self.year. 
This attribute is unique to the Car class and not part of the Vehicle class.

def display_info(self):
This line defines a method named display_info within the Car class. 
This method displays the full information about the car, including the year, make, and model.

print(f"{self.year} {self.make} {self.model}")
Inside the display_info method, this line prints a message displaying the car's year, make, and model.

my_car = Car("Toyota", "Corolla", 2020)
This line creates an instance of the Car class, passing "Toyota" as the make, "Corolla" as the model, and 2020 as the year. 
The __init__ method of the Car class is called, which in turn calls the __init__ method of the Vehicle class via super().

my_car.start()
This line calls the start method on the my_car object. 
Since Car inherits from Vehicle, the start method is executed, and it prints "Toyota Corolla is starting.".

my_car.display_info()
This line calls the display_info method on the my_car object. 
The method prints "2020 Toyota Corolla", displaying the full information about the car.
'''