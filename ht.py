# Palindrome check

def is_palindrome(s):
 
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Get input from the user
s = input("Enter a string: ")
if is_palindrome(s):
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")

'''

Here's a breakdown of the code:

def is_palindrome(s): defines a function named is_palindrome that takes a single parameter s, which is expected to be a string.

return s == s[::-1] checks if the string s is equal to its reverse. The slicing notation [::-1] creates a reversed version of the string. 
If s is the same forwards and backwards, the function returns True, indicating that s is a palindrome.

s = input("Enter a string: ") prompts the user to enter a string and stores this input in the variable s.

if is_palindrome(s): calls the is_palindrome function with the user-provided string s and checks if the result is True.

print(f"{s} is a palindrome.") prints a message indicating that the string is a palindrome if the condition is true.

else: handles the case where the string is not a palindrome.

print(f"{s} is not a palindrome.") prints a message indicating that the string is not a palindrome if the condition is false.
'''