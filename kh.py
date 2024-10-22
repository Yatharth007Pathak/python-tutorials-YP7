# Finding the Maximum of Two Numbers


# POP Version:
def find_max(a, b):
    return a if a > b else b
print("Max:", find_max(10, 20))

'''
def find_max(a, b):
This line defines a function named find_max that takes two parameters, a and b. 
The purpose of this function is to determine and return the larger of the two numbers.

return a if a > b else b
This line uses a ternary conditional expression to decide which value to return. The expression a if a > b else b checks if a is greater than b. 
If it is, the function returns a; otherwise, it returns b. This is a concise way to write a simple if-else statement.

print("Max:", find_max(10, 20))
This line calls the find_max function with the arguments 10 and 20. 
The function compares these two numbers and returns the larger value, which is 20. 
The print function then outputs the string "Max:" followed by the result, so the final output is Max: 20.
'''

# OOP Version:
class Comparator:
    def find_max(self, a, b):
        return a if a > b else b
comp = Comparator()
print("Max:", comp.find_max(10, 20))

'''
class Comparator:
This line defines a new class named Comparator. 
This class is intended to provide functionality for comparing values, specifically to find the maximum of two numbers.

def find_max(self, a, b):
This line defines a method named find_max within the Comparator class. 
The method takes three parameters: self (which refers to the instance of the class), and a and b (the two numbers to compare).

return a if a > b else b
Inside the find_max method, this line uses a ternary conditional expression to determine which of the two numbers, a or b, is greater. 
If a is greater than b, it returns a; otherwise, it returns b.

comp = Comparator()
This line creates an instance of the Comparator class and assigns it to the variable comp. 
This object can now use the methods defined in the Comparator class.

print("Max:", comp.find_max(10, 20))
This line calls the find_max method on the comp object with the arguments 10 and 20. 
The find_max method compares these two numbers and returns the larger one, which is 20. 
The print function then outputs the string "Max:" followed by the result, so the final output is Max: 20.
'''