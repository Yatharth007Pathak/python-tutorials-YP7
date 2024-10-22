# Sum of Two Numbers


# POP Version:
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 7)
print("Sum:", result)

'''
def add_numbers(a, b):
This line defines a function named add_numbers that takes two parameters, a and b. 
A function in Python is a block of reusable code that performs a specific task. In this case, the task is to add two numbers together.

return a + b
Inside the add_numbers function, this line calculates the sum of a and b and returns the result. 
The return statement sends the result back to the caller of the function, allowing it to be used elsewhere in the code.

result = add_numbers(5, 7)
This line calls the add_numbers function with the arguments 5 and 7. 
The function adds these two numbers together, returning the result (12), which is then assigned to the variable result.

print("Sum:", result)
This line prints the string "Sum:" followed by the value of the result variable. In this case, it outputs Sum: 12 to the console.
'''


# OOP Version:
class Calculator:
    def add(self, a, b):
        return a + b
calc = Calculator()
result = calc.add(5, 7)
print("Sum:", result)

'''
class Calculator:
This line defines a new class named Calculator. A class in Python is a blueprint for creating objects, and in this case,
Calculator is intended to represent a calculator that can perform various operations.

def add(self, a, b):
This line defines a method named add within the Calculator class. The add method takes three parameters: self, a, and b. 
self refers to the instance of the class, while a and b are the two numbers to be added.

return a + b
Inside the add method, this line calculates the sum of a and b and returns the result. 
This allows the method to provide the sum of the two numbers when called.

calc = Calculator()
This line creates a new instance of the Calculator class and assigns it to the variable calc. 
This object calc can now use the methods defined in the Calculator class.

result = calc.add(5, 7)
This line calls the add method on the calc object with the arguments 5 and 7. 
The add method computes the sum (which is 12) and returns it. The result is then stored in the variable result.

print("Sum:", result)
This line prints the string "Sum:" followed by the value of the result variable. 
In this case, it outputs Sum: 12, indicating the result of adding 5 and 7.
'''