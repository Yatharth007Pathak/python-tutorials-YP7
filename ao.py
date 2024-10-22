# ord() converts a character to its Unicode code point.
# chr() converts a Unicode code point to its corresponding character.

# ASCII example
print(ord('A'))  # Output: 65
print(chr(65))   # Output: A

# Unicode example
print(ord('😊'))  # Output: 128522
print(chr(128522))  # Output: 😊

'''
Let's break down each line of code for both ASCII and Unicode examples:

print(ord('A'))
ord('A'): The ord() function returns the Unicode code point (integer value) of the given character. 
For 'A', which is an ASCII character, this function returns 65 because that's the ASCII value for 'A'.
print(...): This prints the result of the ord() function to the console. In this case, it will print 65.

print(chr(65))
chr(65): The chr() function returns the character corresponding to the given Unicode code point (integer value). 
For 65, which corresponds to 'A' in ASCII, it returns the character 'A'.
print(...): This prints the result of the chr() function to the console. In this case, it will print A.

print(ord('😊'))
ord('😊'): The ord() function returns the Unicode code point of the given character. 
For '😊', this function returns 128522, which is the Unicode code point for the smiling face emoji.
print(...): This prints the result of the ord() function to the console. In this case, it will print 128522.

print(chr(128522))
chr(128522): The chr() function returns the character corresponding to the given Unicode code point. 
For 128522, this returns the '😊' emoji.
print(...): This prints the result of the chr() function to the console. In this case, it will print the emoji 😊.
'''


"""
ASCII and Unicode are character encoding standards used to represent text in computers and other devices. Here's an overview of each:

1. ASCII (American Standard Code for Information Interchange)
Definition: ASCII is a character encoding standard for electronic communication. It represents text in computers and other devices that use text.
Range: It uses 7 bits to represent characters, allowing for 128 unique characters. The ASCII values range from 0 to 127. These include:
Control characters (0-31): Non-printable characters used for text formatting, like newline (\n), tab (\t), and carriage return (\r).
non-printable control characters used for text formatting and control, such as:
NULL = 0
Start of Header = 1
Line Feed = 10
Carriage Return = 13
Printable characters (32-126): Includes letters (both uppercase and lowercase), digits, punctuation marks, and a few special symbols.
Example Characters:
Space: 32
Digits: 0 (48) to 9 (57)
Uppercase Letters: A (65) to Z (90)
Lowercase Letters: a (97) to z (122)
Punctuation Marks and Symbols: Such as ! (33), @ (64), # (35), and so on
DEL Character (127): The DEL character is a control character used to delete or remove characters.
Limitation: ASCII only supports English characters and a limited set of symbols, making it unsuitable for many languages and special symbols.

2. Unicode
Definition: Unicode is a more comprehensive encoding standard that aims to cover 
all the characters and symbols from all writing systems in the world.
Range: Unicode can use different encoding forms, such as UTF-8, UTF-16, and UTF-32, which allow for a vast range of characters 
(over 1.1 million possible code points). The most commonly used form, UTF-8, uses 1 to 4 bytes to encode characters.
Example Characters:
A = U+0041 (same as ASCII)
a = U+0061 (same as ASCII)
漢 (a Chinese character) = U+6F22
😊 (a smiley face emoji) = U+1F60A
Advantage: Unicode supports virtually every character in every language, as well as a wide range of symbols, 
including emojis, mathematical symbols, and more. This makes it the preferred standard for modern computing.

Comparison:
ASCII: Limited to 128 characters, primarily for English text and control characters.
Unicode: Extensive and universal, supporting characters from all languages, as well as symbols, emojis, and more.
"""