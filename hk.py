# Generate a Random Password

import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

length = int(input("Enter length: "))
print(generate_password(length))

'''
Here's an explanation of the code:

import random imports the random module, which provides functions for generating random numbers and making random choices.

import string imports the string module, which contains constants for common string operations, such as letters, digits, and punctuation.

def generate_password(length): defines a function named generate_password that takes a single parameter length, 
representing the desired length of the password.

chars = string.ascii_letters + string.digits + string.punctuation creates a string chars containing all ASCII letters 
(both uppercase and lowercase), digits, and punctuation characters. 
This defines the pool of characters from which the password will be generated.

return ''.join(random.choice(chars) for _ in range(length)) generates a random password by:

Using a generator expression to repeatedly select a random character from chars.
random.choice(chars) picks a single character randomly.
for _ in range(length) ensures that this process is repeated length times.
''.join(...) combines these characters into a single string.
length = int(input("Enter length: ")) prompts the user to enter the desired length of the password, 
converts this input to an integer, and stores it in the variable length.

print(generate_password(length)) calls the generate_password function with the user-provided length and prints the generated password.
'''