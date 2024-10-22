"""
In Python, the sep parameter is used in the print() function to specify the separator between multiple arguments. 
By default, print() separates each argument with a single space when printing them. 
However, we can customize this behavior by using the sep parameter to define a different string as the separator.
"""

# Default Separator (Space)
print("Hello", "World", "2024")                   # Here by default, print() separates multiple arguments with a space.


# Custom Separator
print("Hello", "World", "2024", sep="-")          # Here, sep='-' specifies that a hyphen should be used as the separator between the arguments.


# No Separator
print("Hello", "World", "2024", sep="")           # Here, sep='' causes the arguments to be concatenated directly with no space between them.


# Using a Multi-character Separator
print("Hello", "World", "2024", sep="---")        # In this case, sep='---' uses a triple hyphen as the separator.


# Combining sep with Other Print Parameters
print("Python", "is", "fun", sep=", ", end="!\n") # We can use sep in combination with other parameters like end to fully customize the output.
'''
sep=', ' specifies that each word should be separated by a comma and a space.
end='!\n' specifies that the line should end with an exclamation mark followed by a newline.
'''