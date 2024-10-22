# Checking if a Number is Even or Odd


# POP Version:
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = check_even_odd(4)
print("The number is:", result)

'''
def check_even_odd(num):
This line defines a function named check_even_odd that takes one parameter, num.
The function is designed to determine whether the given number is even or odd.

if num % 2 == 0:
This line starts an if statement that checks whether num is divisible by 2 without a remainder. 
The expression num % 2 calculates the remainder when num is divided by 2. If the remainder is 0, it means the number is even.

return "Even"
If the condition in the if statement is true (i.e., num is even), this line returns the string "Even" to indicate that the number is even.

else:
This line begins the else block, which will be executed if the condition in the if statement is false (i.e., num is not even).

return "Odd"
If the number is not even, this line returns the string "Odd" to indicate that the number is odd.

result = check_even_odd(4)
This line calls the check_even_odd function with the argument 4. 
The function checks if 4 is even or odd and returns "Even", which is then assigned to the variable result.

print("The number is:", result)
This line prints the string "The number is:" followed by the value of the result variable. 
In this case, it outputs The number is: Even to the console, indicating that the number 4 is even.
'''


# OOP Version:
class Number:
    def __init__(self, num):
        self.num = num
    def check_even_odd(self):
        return "Even" if self.num % 2 == 0 else "Odd"
number = Number(4)
print("The number is:", number.check_even_odd())

'''
class Number:
This line defines a new class named Number. 
This class is designed to represent a number and provide functionality to check if it is even or odd.

def __init__(self, num):
This line defines the initializer method (__init__) for the Number class. 
It takes two parameters: self (which refers to the instance of the class) and num (the number to be stored in the instance).

self.num = num
Inside the __init__ method, this line assigns the value of the num parameter to the instance variable self.num. 
This means that each Number object will store its num attribute.

def check_even_odd(self):
This line defines a method named check_even_odd for the Number class. This method will determine whether the stored number is even or odd.

return "Even" if self.num % 2 == 0 else "Odd"
Inside the check_even_odd method, this line uses a ternary conditional expression to check if self.num is even or odd. 
The expression self.num % 2 == 0 checks if self.num is divisible by 2 with no remainder. 
If true, it returns "Even"; otherwise, it returns "Odd".

number = Number(4)
This line creates an instance of the Number class with the argument 4. 
The __init__ method initializes this instance with 4 stored in self.num, and assigns the instance to the variable number.

print("The number is:", number.check_even_odd())
This line calls the check_even_odd method on the number object. 
The method checks if 4 is even or odd and returns "Even". 
The print function then outputs the string "The number is:" followed by the result, so the final output is The number is: Even.
'''