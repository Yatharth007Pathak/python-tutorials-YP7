'''
Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. 
If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

Example:
Vehicle Fare: 5000
Bus Fare: 5500.0
'''

class Vehicle:                                                        # Define the Vehicle class
    def __init__(self, seating_capacity):                             # Initialize the Vehicle with seating capacity
        self.seating_capacity = seating_capacity

    def get_fare(self):                                               # Method to calculate the fare based on seating capacity
        return self.seating_capacity * 100
     
class Bus(Vehicle):                                                   # Define the Bus class that inherits from Vehicle
    def __init__(self, seating_capacity):                             # Initialize the Bus with seating capacity
        super().__init__(seating_capacity)                            # Call the parent class's __init__ method

    def get_fare(self):                                               # Override the get_fare method to include maintenance costs
        vehicle_fare = super().get_fare()                             # Call the parent class's get_fare method
        maintenance_fare = 0.1 * vehicle_fare                         # Calculate maintenance fare
        total_fare = vehicle_fare + maintenance_fare                  # Total fare including maintenance
        return total_fare

vehicle1 = Vehicle(50)                                                # Create an instance of Vehicle
print("vehicle fare:", vehicle1.get_fare())                           # Outputs: Vehicle fare: 5000

bus1 = Bus(50)                                                        # Create an instance of Bus
print("Bus fare:", bus1.get_fare())                                   # Outputs: Bus fare: 5500


'''
Let's break down the code to understand how inheritance and method overriding work in this example:

class Vehicle:
This defines a base class named Vehicle. It provides common functionality related to vehicles.

def __init__(self, seating_capacity):
This is the constructor method for the Vehicle class. It initializes the seating_capacity attribute when an instance of Vehicle is created.

self.seating_capacity = seating_capacity
This line sets the instance variable seating_capacity to the value passed when creating a Vehicle instance.

def get_fare(self):
This method calculates the fare based on the seating capacity of the vehicle.

return self.seating_capacity * 100
This line returns the fare, calculated as seating_capacity multiplied by 100. This is the base fare calculation for the Vehicle class.

class Bus(Vehicle):
This defines a class named Bus that inherits from the Vehicle class. This means Bus will have all the methods and attributes of Vehicle.

def __init__(self, seating_capacity):
This is the constructor method for the Bus class. It calls the parent class's constructor to initialize the seating_capacity.

super().__init__(seating_capacity)
This line calls the __init__ method of the parent Vehicle class to initialize the seating_capacity attribute. 
super() is used to refer to the parent class.

def get_fare(self):
This method overrides the get_fare method from the Vehicle class to provide a custom fare calculation for the Bus class.

vehicle_fare = super().get_fare()
This line calls the get_fare method of the parent Vehicle class to get the base fare. 
The super() function is used to access the parent class's method.

maintenance_fare = 0.1 * vehicle_fare
This line calculates the maintenance fare as 10% of the base fare.

total_fare = vehicle_fare + maintenance_fare
This line calculates the total fare by adding the maintenance fare to the base fare.

return total_fare
This line returns the total fare, which includes both the base fare and the maintenance fare.

vehicle1 = Vehicle(50)
This line creates an instance of the Vehicle class with a seating capacity of 50 and assigns it to the variable vehicle1.

print("vehicle fare:", vehicle1.get_fare())
This line calls the get_fare method on the vehicle1 instance and prints the result. 
It will use the Vehicle class's get_fare method, which calculates the fare as 50 * 100 = 5000.

bus1 = Bus(50)
This line creates an instance of the Bus class with a seating capacity of 50 and assigns it to the variable bus1.

print("Bus fare:", bus1.get_fare())
This line calls the get_fare method on the bus1 instance and prints the result. 
It uses the overridden get_fare method in the Bus class, which includes an additional maintenance fare. 
The total fare is calculated as follows:
Base fare: 50 * 100 = 5000
Maintenance fare: 0.1 * 5000 = 500
Total fare: 5000 + 500 = 5500
'''