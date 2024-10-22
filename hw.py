# Count Words in a String

def count_words(s):
    return len(s.split())

# Example usage
s = input("Enter a string: ")
print(f"The number of words in the string is {count_words(s)}.")

'''
Here's a line-by-line explanation of the code:

def count_words(s): defines a function named count_words that takes a single parameter s, which is expected to be a string.

return len(s.split()):

s.split() splits the string s into a list of words based on whitespace (spaces, tabs, newlines).
len(...) calculates the number of items in this list, which corresponds to the number of words in the string.
The function returns this count.
s = input("Enter a string: ") prompts the user to enter a string and stores the input in the variable s.

print(f"The number of words in the string is {count_words(s)}."):

Calls the count_words function with s as the argument.
Prints a message showing the number of words in the string, which is the result returned by count_words.
'''