# Reverse a String

def reverse_string(s):
    return s[::-1]

s = input("Enter s: ")
print(reverse_string(s))

'''
Here's a detailed explanation of the code:

def reverse_string(s): defines a function named reverse_string that takes a single parameter s, which is expected to be a string.

return s[::-1] returns the reverse of the string s. 
The slicing notation [::-1] creates a new string that is the reverse of s by stepping through the string from end to start.

s = input("Enter s: ") prompts the user to enter a string and stores the input in the variable s.

print(reverse_string(s)) calls the reverse_string function with the user-provided string s and prints the reversed string.
'''