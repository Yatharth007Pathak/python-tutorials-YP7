# Check if a String is an Anagram

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Example usage
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if is_anagram(s1, s2):
    print(f"{s1} and {s2} are anagrams.")
else:
    print(f"{s1} and {s2} are not anagrams.")



# Two strings are anagrams if they contain the same characters in any order.

'''
Here's a detailed breakdown of the code:

def is_anagram(s1, s2): defines a function named is_anagram that takes two parameters, s1 and s2, representing the two strings to be compared.

return sorted(s1) == sorted(s2):
sorted(s1) sorts the characters of the first string s1 in ascending order and returns a list of characters.
sorted(s2) sorts the characters of the second string s2 in ascending order and returns a list of characters.
== compares the sorted lists. If the sorted lists are equal, the function returns True, 
indicating that s1 and s2 are anagrams; otherwise, it returns False.
s1 = input("Enter the first string: ") prompts the user to enter the first string and stores it in the variable s1.

s2 = input("Enter the second string: ") prompts the user to enter the second string and stores it in the variable s2.

if is_anagram(s1, s2): calls the is_anagram function with s1 and s2 as arguments and checks if the result is True.

print(f"{s1} and {s2} are anagrams.") prints a message indicating that the strings are anagrams if the condition is true.

else: handles the case where the strings are not anagrams.

print(f"{s1} and {s2} are not anagrams.") prints a message indicating that the strings are not anagrams if the condition is false.
'''