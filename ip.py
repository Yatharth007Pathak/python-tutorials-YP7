'''
The replace() function in Python is used to replace occurrences of a specified substring with another substring within a string. 
This function returns a new string with the specified replacements, 
leaving the original string unchanged (because strings in Python are immutable).

Syntax: str.replace(old, new, count)
old: The substring you want to replace.
new: The substring that will replace the old substring.
count (optional): The maximum number of occurrences to replace. If omitted, all occurrences of old will be replaced.

Key Points
The replace() function does not modify the original string but returns a new string with the replacements.
The function is case-sensitive, so it distinguishes between uppercase and lowercase characters.
We can use count to limit the number of replacements, which can be useful when you don't want to replace all occurrences of the substring.
'''


# Basic Replacement: The word "World" in the string text is replaced with "Universe"
text = "Hello, World!"
new_text = text.replace("World", "Universe")
print(new_text)  # Output: Hello, Universe!


# Replacing Multiple Occurrences: All occurrences of the word "apple" are replaced with "banana".
text = "apple apple orange apple"
new_text = text.replace("apple", "banana")
print(new_text)  # Output: banana banana orange banana


# Limiting the Number of Replacements: Only the first two occurrences of "apple" are replaced with "banana". The third occurrence remains unchanged because of the count argument set to 2.
text = "apple apple orange apple"
new_text = text.replace("apple", "banana", 2)
print(new_text)  # Output: banana banana orange apple


# Replacing Characters: Every occurrence of the character "s" in the string is replaced with "z".
text = "mississippi"
new_text = text.replace("s", "z")
print(new_text)  # Output: mizzizzippi


# Replacing with an Empty String: The word "World" is removed from the string by replacing it with an empty string.
text = "Hello, World!"
new_text = text.replace("World", "")
print(new_text)  # Output: Hello, !


# Case Sensitivity: The replace() function is case-sensitive. Only the exact matches of "Hello" are replaced with "Hi", while "hello" remains unchanged.
text = "Hello, World! hello, world!"
new_text = text.replace("Hello", "Hi")
print(new_text)  # Output: Hi, World! hello, world!