"""
Given a string of a number N, we need to mirror the characters from the N-th position up to the length of the strings in alphabetical order.
In mirror operation, we change 'a' to 'z', 'b' to 'y' and so on.
"""

input_string = input("Enter strings: ")
n = int(input("Enter n: "))

# Creating dictionary for mirror operation
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1]
my_dict = dict(zip(alphabets, reverse_alphabets))

# Finding the part of string on which we will do mirror operation
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

# Finding the mirror string
mirror = ""
for i in range(0, len(suffix)):
    mirror = mirror + my_dict[suffix[i]]

# Creating the final string
result = prefix + mirror
print("The result is: ", result)

'''
Here's a detailed line-by-line breakdown of the Python code:

User Input:
input_string: The user is prompted to enter a string. The entered string is stored in the variable input_string.
n: The user is prompted to enter an integer, which represents the position from where the mirroring operation will start. 
This value is stored in n.

Dictionary Creation for Mirroring:
alphabets: A string containing all lowercase letters from 'a' to 'z'.
reverse_alphabets: This is the reverse of the alphabets string, i.e., "zyxwvutsrqponmlkjihgfedcba".
my_dict: A dictionary is created using zip to pair each letter in alphabets with its corresponding mirrored letter in reverse_alphabets. 
The result is a dictionary where each letter is mapped to its opposite in the alphabet.

Splitting the String:
prefix: This extracts the part of input_string from the start up to, but not including, the (n-1)-th position (0-based index). 
This part remains unchanged.
suffix: This extracts the part of input_string from the (n-1)-th position to the end. This is the part of the string that will be mirrored.

Mirroring the Suffix:
mirror: An empty string is initialized to store the mirrored result.
A for loop iterates over each character in suffix.
my_dict[suffix[i]]: For each character in suffix, the corresponding mirrored character is fetched from my_dict.
mirror = mirror + my_dict[suffix[i]]: The mirrored character is concatenated to the mirror string.

Constructing and Printing the Final Result:
result: The final string is created by concatenating prefix with mirror.
print("The result is: ", result): The final mirrored string is printed to the console.
'''