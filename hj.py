# Convert Temperature from Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = int(input("Enter temp. in celsius: "))
print(celsius_to_fahrenheit(celsius))

'''
Here is a breakdown of the code:

def celsius_to_fahrenheit(celsius): defines a function named celsius_to_fahrenheit that takes a single parameter celsius, 
which represents the temperature in Celsius.

return (celsius * 9/5) + 32 converts the Celsius temperature to Fahrenheit using the formula 
(Celsius * 5/9) + 32. This formula is used to calculate the equivalent temperature in Fahrenheit.

celsius = int(input("Enter temp. in celsius: ")) prompts the user to enter a temperature in Celsius, 
converts the input to an integer, and stores it in the variable celsius.

print(celsius_to_fahrenheit(celsius)) calls the celsius_to_fahrenheit function with the 
user-provided Celsius temperature and prints the converted temperature in Fahrenheit.
'''