"""
Escape characters in Python are special characters that allow us to include otherwise difficult-to-type or invisible characters within a string. 
They are introduced with a backslash (\), and they serve various purposes, 
such as inserting special characters or controlling the formatting of the string.
"""

# Newline (\n): Inserts a new line in the text.
print("Hello\nWorld")
# Output:
# Hello
# World

# Tab (\t): Inserts a horizontal tab.
print("Hello\tWorld")
# Output: Hello   World

# Backslash (\\): Inserts a literal backslash character.
print("This is a backslash: \\")
# Output: This is a backslash: \

# Single Quote (\'): Inserts a single quote within a string enclosed by single quotes.
print('It\'s a great day!')
# Output: It's a great day!

# Double Quote (\"): Inserts a double quote within a string enclosed by double quotes.
print("He said, \"Hello!\"")
# Output: He said, "Hello!"

# Carriage Return (\r): Moves the cursor to the beginning of the line without advancing to the next line.
print("Hello\rWorld")
# Output: World (It overwrites 'Hello' with 'World')

# Backspace (\b): Moves the cursor one position back, so the previous character is removed.
print("Hello\bWorld")
# Output: HellWorld (The 'o' in 'Hello' is removed)

# Form Feed (\f): Advances the cursor to the next page (used in some older printing systems).
print("Hello\fWorld")
# Output: Hello (form feed) World (Effect depends on the environment)

# Octal Value (\ooo): Represents a character using its octal value.
print("\101\102\103")
# Output: ABC (Octal values for 'A', 'B', and 'C')

# Hexadecimal Value (\xhh): Represents a character using its hexadecimal value.
print("\x41\x42\x43")
# Output: ABC (Hexadecimal values for 'A', 'B', and 'C')

# Unicode Characters (\u, \U, \N)
# \u is used for 16-bit Unicode characters.
# \U is used for 32-bit Unicode characters.
# \N is used for named Unicode characters.
print("\u00A9")  # Output: © (Unicode character for the copyright symbol)
print("\U0001F600")  # Output: 😀 (Unicode character for a smiley face)
print("\N{GREEK CAPITAL LETTER ALPHA}")  # Output: Α (Named Unicode character)


# Example Usage
message = "Hello,\nWelcome to the \"Python\" course.\n\tLet's start learning!"
print(message)
# Output:
# Hello,
# Welcome to the "Python" course.
#     Let's start learning!


# Raw Strings: If we want to prevent escape characters from being interpreted 
# (e.g., when dealing with file paths or regular expressions), we can use a raw string by prefixing the string with an r or R.
path = r"C:\Users\Name\Documents"
print(path)
# Output: C:\Users\Name\Documents
# Explanation: The r prefix tells Python to treat the backslashes as literal characters, not escape characters.