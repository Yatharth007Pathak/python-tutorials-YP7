'''
The split() function in Python is used to split a string into a list of substrings based on a specified delimiter (separator). 
This function is commonly used for parsing strings, especially when we want to break a string into individual components.

Syntax: str.split(separator, maxsplit)
separator (optional): The delimiter (or separator) on which to split the string. 
If not provided, the default separator is any whitespace (spaces, tabs, newlines).
maxsplit (optional): The maximum number of splits to perform. If not provided, the string is split at every occurrence of the separator.

Key Points
The split() function returns a list of substrings.
If the separator is not specified, any whitespace is used as the default separator.
The maxsplit parameter limits the number of splits. If not specified, all possible splits are performed.
The original string remains unchanged, as strings in Python are immutable.
'''



'''
Basic Splitting with Default Separator (Whitespace): The string text is split into a list of words using the default separator (whitespace). 
Each word in the string becomes an element in the list words.
'''
text = "Hello World Python"
words = text.split()
print(words)  # Output: ['Hello', 'World', 'Python']


'''
Splitting with a Specific Separator: The string text is split into a list of fruit names using a comma (,) as the separator.
'''
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']


'''
Limiting the Number of Splits (maxsplit): The string is split at the first two commas, resulting in three elements. 
The remaining part of the string after the second split is kept as is in the last element.
'''
text = "apple,banana,orange,grape"
fruits = text.split(",", 2)
print(fruits)  # Output: ['apple', 'banana', 'orange,grape']


'''
Splitting on Multiple Whitespace Characters: The string text is split into words, 
ignoring multiple spaces and treating them as a single separator.
'''
text = "   Hello   World  Python   "
words = text.split()
print(words)  # Output: ['Hello', 'World', 'Python']


'''
Splitting on a Specific Character: The string representing a date is split into year, month, and day by using the hyphen (-) as the separator.
'''
text = "2024-08-23"
date_parts = text.split("-")
print(date_parts)  # Output: ['2024', '08', '23']


'''
Splitting with No Separator Argument (Default): Since no separator is provided, the string is split using whitespace by default.
'''
text = "Python is easy to learn"
words = text.split()
print(words)  # Output: ['Python', 'is', 'easy', 'to', 'learn']