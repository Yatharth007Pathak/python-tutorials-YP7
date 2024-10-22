# Key Features of Strings in Python:

'''
Immutable: Once a string is created, its content cannot be changed. Operations that seem to modify a string actually create a new string.
However, we can associate the old string name with the new object

Indexed: Each character in a string is indexed, starting from 0 for the first character. 
This allows us to access individual characters using their index.
'''
my_string = "Hello"
print(my_string[0])   # Output: H
print(my_string[-1])  # Output: o


'''
Slicing: We can extract a substring by using slicing, which specifies a range of indices.
'''
my_string = "Hello, World!"
print(my_string[0:5])  # Output: Hello

'''
Concatenation: Strings can be concatenated (joined together) using the + operator.
'''
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

'''
Repetition: Strings can be repeated using the * operator.
'''
word = "Hi"
repeated_word = word * 3
print(repeated_word)  # Output: HiHiHi

'''
Multiline Strings: Using triple quotes, we can create strings that span multiple lines.
'''
multiline_string = """This is a 
multiline string"""
print(multiline_string)

'''
String Methods: Python provides various built-in methods for string manipulation, such as lower(), upper(), replace(), find(), split(), and more.
'''
my_string = "Hello, World!"
print(my_string.lower())  # Output: hello, world!
print(my_string.upper())  # Output: HELLO, WORLD!

'''
strip() method: Used for stripping or removing any trailing whitespaces
'''
str = "       hello world!       "
print(str)
print(str.strip())

'''
Formatted Strings: We can embed expressions inside string literals using formatted string literals (f-strings) or the format() method.
'''
name = "Alice"
age = 30
print(f"{name} is {age} years old.")  # Output: Alice is 30 years old.