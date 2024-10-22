# Simple Temperature Conversion (Celsius to Fahrenheit)


# POP Version:
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print("Fahrenheit:", celsius_to_fahrenheit(25))

'''
def celsius_to_fahrenheit(celsius):
This line defines a function named celsius_to_fahrenheit that takes one parameter, celsius. 
The purpose of this function is to convert a temperature from Celsius to Fahrenheit.

return (celsius * 9/5) + 32
Inside the celsius_to_fahrenheit function, this line performs the temperature conversion. 
The formula (celsius * 9/5) + 32 converts the temperature from Celsius to Fahrenheit. 
Specifically, it multiplies the Celsius temperature by 9/5 (which is equivalent to 1.8) 
and then adds 32 to shift the result into the Fahrenheit scale. The function returns the calculated Fahrenheit temperature.

print("Fahrenheit:", celsius_to_fahrenheit(25))
This line calls the celsius_to_fahrenheit function with the argument 25. 
The function converts 25 degrees Celsius to Fahrenheit, returning the result 77.0. 
The print function then outputs the string "Fahrenheit:" followed by the converted temperature, so the final output is Fahrenheit: 77.0.
'''

# OOP Version:
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
temp = Temperature(25)
print("Fahrenheit:", temp.to_fahrenheit())

'''
class Temperature:
This line defines a new class named Temperature. 
The purpose of this class is to handle temperature conversions, specifically from Celsius to Fahrenheit.

def __init__(self, celsius):
This line defines the initializer method (__init__) for the Temperature class. 
It takes two parameters: self (which refers to the instance of the class) and celsius (the temperature in Celsius to be stored).

self.celsius = celsius
Inside the __init__ method, this line assigns the value of the celsius parameter to the instance variable self.celsius. 
This means that each Temperature object will store its Celsius temperature in self.celsius.

def to_fahrenheit(self):
This line defines a method named to_fahrenheit for the Temperature class. 
This method converts the temperature stored in self.celsius from Celsius to Fahrenheit.

return (self.celsius * 9/5) + 32
Inside the to_fahrenheit method, this line uses the formula (self.celsius * 9/5) + 32 to convert the Celsius temperature to Fahrenheit. 
It calculates the Fahrenheit equivalent of self.celsius and returns the result.

temp = Temperature(25)
This line creates an instance of the Temperature class with the argument 25. 
The __init__ method initializes this instance, setting self.celsius to 25.

print("Fahrenheit:", temp.to_fahrenheit())
This line calls the to_fahrenheit method on the temp object. The method converts 25 degrees Celsius to Fahrenheit, resulting in 77.0. 
The print function then outputs the string "Fahrenheit:" followed by the converted temperature, so the final output is Fahrenheit: 77.0.
'''