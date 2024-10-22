def say(message, times = 1):
    print(message * times)
say('Hello')
say('World', 5)

'''
Let's analyze the given code step by step:

def say(message, times = 1)::
This defines a function named say that takes two parameters:
message: A string that the function will print.
times: An optional parameter with a default value of 1. This parameter determines how many times the message will be repeated when printed.

print(message * times):
Inside the say function, the print statement multiplies the message string by the value of times.
In Python, multiplying a string by an integer repeats the string that many times.
The result is then printed.

say('Hello'):
This calls the say function with 'Hello' as the message and uses the default value of times (which is 1).
The function prints 'Hello' once.

say('World', 5):
This calls the say function with 'World' as the message and 5 as the value of times.
The function prints 'World' five times in a row, resulting in 'WorldWorldWorldWorldWorld'.

The output of the code will be:
Hello
WorldWorldWorldWorldWorld

Key Concepts
Default Parameter Values: The times parameter has a default value (1), 
so if it's not provided when the function is called, the function uses the default.
String Multiplication: Multiplying a string by an integer repeats the string that many times.
'''