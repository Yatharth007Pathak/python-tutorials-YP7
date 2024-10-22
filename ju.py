# Hybrid inheritance: Combination of two or more types of inheritance. 
# It involves complex structures of inheritance like combining multilevel and multiple inheritance.

class Vehicle:                                            # Define the Vehicle class
    def move(self):                                       # Method to describe movement
        return "Moving"

class Car(Vehicle):                                       # Define the Car class that inherits from Vehicle
    def drive(self):                                      # Method specific to Car for driving
        return "Driving a car"

class Boat(Vehicle):                                      # Define the Boat class that inherits from Vehicle
    def sail(self):                                       # Method specific to Boat for sailing   
        return "Sailing a boat" 

class AmphibiousVehicle(Car, Boat):                       # Define the AmphibiousVehicle class that inherits from both Car and Boat, which in turn inherit from Vehicle
    pass                                                  # Inherits all methods from Car and Boat without additional methods or attributes

amphibious = AmphibiousVehicle()                          # Create an instance of the AmphibiousVehicle class
print(amphibious.move())  # Outputs: Moving               # Call the move method inherited from the Vehicle class
print(amphibious.drive()) # Outputs: Driving a car        # Call the drive method inherited from the Car class
print(amphibious.sail())  # Outputs: Sailing a boat       # Call the sail method inherited from the Boat class
 


'''
Let's break down the code to understand the use of multiple inheritance and how methods are accessed in the AmphibiousVehicle class:

class Vehicle:
This defines a base class named Vehicle. It provides common functionality for all types of vehicles.

def move(self):
This method is defined within the Vehicle class. It takes self as a parameter.

return "Moving"
This line returns the string "Moving". It represents a generic movement behavior for vehicles.

class Car(Vehicle):
This defines a class named Car, which inherits from the Vehicle class. This means Car inherits the move method from Vehicle.

def drive(self):
This method is defined within the Car class. It takes self as a parameter.

return "Driving a car"
This line returns the string "Driving a car". It represents a specific behavior for cars.

class Boat(Vehicle):
This defines a class named Boat, which also inherits from the Vehicle class. This means Boat inherits the move method from Vehicle.

def sail(self):
This method is defined within the Boat class. It takes self as a parameter.

return "Sailing a boat"
This line returns the string "Sailing a boat". It represents a specific behavior for boats.

class AmphibiousVehicle(Car, Boat):
This defines a class named AmphibiousVehicle that inherits from both Car and Boat. 
This is an example of multiple inheritance, where AmphibiousVehicle inherits methods and attributes from both parent classes (Car and Boat).

pass
The pass statement indicates that the AmphibiousVehicle class does not add any new methods or attributes beyond those inherited from Car and Boat.

amphibious = AmphibiousVehicle()
This line creates an instance of the AmphibiousVehicle class and assigns it to the variable amphibious. 
This instance has access to methods from both Car and Boat, as well as Vehicle.

print(amphibious.move())
This line calls the move method on the amphibious instance. 
Since AmphibiousVehicle inherits from both Car and Boat, and both inherit from Vehicle, it uses the move method from the Vehicle class. 
This prints "Moving".

print(amphibious.drive())
This line calls the drive method on the amphibious instance. The drive method is defined in the Car class, so it prints "Driving a car".

print(amphibious.sail())
This line calls the sail method on the amphibious instance. The sail method is defined in the Boat class, so it prints "Sailing a boat".

Summary:
Multiple Inheritance: The AmphibiousVehicle class inherits from both Car and Boat, 
demonstrating how multiple inheritance allows a class to combine features from multiple parent classes.
Method Resolution: The AmphibiousVehicle instance can access:
move from Vehicle
drive from Car
sail from Boat
Combined Functionality: The AmphibiousVehicle class effectively combines the behaviors of both cars and boats, 
while still retaining the basic movement functionality provided by the Vehicle class.
'''