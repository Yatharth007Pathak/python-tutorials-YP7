# Count Vowels in a String

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count

s = input("Enter s: ")
print(count_vowels(s))

'''
Here's a line-by-line explanation of the code:

def count_vowels(s): defines a function named count_vowels that takes a single parameter s, which is expected to be a string.

vowels = 'aeiouAEIOU' creates a string vowels containing all the lowercase and uppercase vowels. 
This string is used to check whether characters in s are vowels.

count = sum(1 for char in s if char in vowels) calculates the number of vowels in the string s. 
This line uses a generator expression to iterate through each character in s, checking if it is in the vowels string. 
For each vowel found, it yields 1. The sum() function then adds up these 1s to get the total count of vowels.

return count returns the total count of vowels from the function.

s = input("Enter s: ") prompts the user to enter a string and stores the input in the variable s.

print(count_vowels(s)) calls the count_vowels function with the user-provided string s and prints the number of vowels in the string.
'''