'''
In Python, a string is a sequence of characters enclosed within single quotes (' '), double quotes (" "), 
or triple quotes (''' ''' or """ """). Strings are used to represent text and can include letters, numbers, symbols, and whitespace. 
They are one of the most commonly used data types in Python.
'''


# String initialization
str1 = "Hello"
str2 = 'World'
str3 = '''This is a multiline
string example.'''

print("String 1:", str1)
print("String 2:", str2)
print("String 3:", str3)

# String concatenation
concat_str = str1 + " ^ " + str2
print("\nConcatenated String:", concat_str)

# String length
length = len(concat_str)
print("Length of Concatenated String:", length)

# String indexing
first_char = str1[0]
last_char = str2[-1]
print("\nFirst character of String 1:", first_char)
print("Last character of String 2:", last_char)

# String slicing
substring1 = concat_str[0:5]     # Slicing from index 0 to 4
substring2 = concat_str[2:9]     # Slicing from index 2 to 8
substring3 = concat_str[:4]      # Slicing from start to index 3
substring4 = concat_str[2:]      # Slicing from index 2 to end
substring5 = concat_str[-3:]     # Slicing from index -3 to end
substring6 = concat_str[-7:-2]   # Slicing from index -7 to -3
substring7 = concat_str[-13:]    # Slicing from index -13 to end
substring8 = concat_str[:-13]    # Slicing from start to index -13

print("Sliced String (0:5):", substring1)
print("Sliced String (2:9):", substring2)
print("Sliced String (:4):", substring3)
print("Sliced String (2:):", substring4)
print("Sliced String (-3:):", substring5)
print("Sliced String (-7:-2):", substring6)
print("Sliced String (-13:):", substring7)
print("Sliced String (:-13):", substring8)


# String methods
upper_str = concat_str.upper()
lower_str = concat_str.lower()
replaced_str = concat_str.replace("World", "Python")

print("\nUppercase String:", upper_str)
print("Lowercase String:", lower_str)
print("Replaced String:", replaced_str)

# Checking if character/substring exists
contains_world = "World" in concat_str
print("\nDoes the concatenated string contain 'World'?", contains_world)
print(str3.find('a'))
print(str3.find('exa'))
print(str3.find(' '))
print(str3.find('z'))

# Splitting a string
split_str = concat_str.split(" ")
print("Splitted String:", split_str)

# Joining a list into a string
joined_str = "-".join(split_str)
print("Joined String with '-':", joined_str)

# String formatting
name = "Alice"
age = 30
formatted_str = f"My name is {name} and I am {age} years old."
print("\nFormatted String:", formatted_str)


'''
Explanation of the code:
String Initialization: Strings are initialized using single, double, or triple quotes.
String Concatenation: Two strings are combined using the + operator.
String Length: The len() function is used to determine the length of the string.
String Indexing: Access specific characters using their index, where the index starts from 0.
String Slicing: Extract a portion of the string using slicing ([start:end]).
String Methods:
upper() converts a string to uppercase.
lower() converts a string to lowercase.
replace(old, new) replaces a substring with another substring.
Checking Substring: Use the in operator to check if a substring exists within a string.
find() returns the index of first occurence of the character or substring and returns -1 if not found in original string.
Splitting and Joining Strings:
split(separator) splits a string into a list based on the separator.
join(list) joins a list of strings into a single string with the given separator.
String Formatting: The f-string method is used to format strings by embedding expressions inside curly braces {}.
'''