"""
Given a string of a number N, we need to mirror the characters from the N-th position up to the length of the strings in alphabetical order.
In mirror operation, we change 'a' to 'z', 'b' to 'y' and so on.
"""

def mirror_string(input_str, n):
    # Extract unchanged part of the string
    unchanged_part = input_str[:n - 1]  # N-th position is 1-based index

    # Extract the part of the string to be mirrored
    mirror_part = input_str[n - 1:]
    
    # Initialize an empty string for the mirrored part
    mirrored_part = ""
    
    # Manually mirror each character in the mirror_part
    for char in mirror_part:
        if 'a' <= char <= 'z':  # For lowercase letters
            # Calculate mirrored character
            mirrored_char = chr(ord('a') + ord('z') - ord(char))
            mirrored_part += mirrored_char
        elif 'A' <= char <= 'Z':  # For uppercase letters
            # Calculate mirrored character
            mirrored_char = chr(ord('A') + ord('Z') - ord(char))
            mirrored_part += mirrored_char
        else:
            # If not a letter, just add the character as is
            mirrored_part += char
    
    # Concatenate unchanged part with mirrored part
    result = unchanged_part + mirrored_part
    return result

# Example usage
input_str = "abcdefgh"
n = 3
mirrored_result = mirror_string(input_str, n)
print(mirrored_result)  # Output: "abzyxwvu"


'''
The mirror_string function is designed to mirror the characters in a string from a 
specified position while keeping the part before that position unchanged. 
Here's a step-by-step breakdown:

Function Definition: mirror_string takes two arguments:
input_str: the string to be processed.
n: the position from which mirroring starts (1-based index).

Unchanged Part Extraction:
input_str[:n - 1] slices the string from the beginning up to (but not including) the (n-1)-th position (0-based index). 
This part of the string remains unchanged.

Mirror Part Extraction:
input_str[n - 1:] slices the string from the (n-1)-th position to the end. This part will be mirrored.

Initialize Mirrored Part:
mirrored_part is an empty string that will be used to store the result of mirroring.

Mirroring Logic:
Iterate over each character char in mirror_part.
Lowercase Letters:
If char is a lowercase letter (between 'a' and 'z'), calculate its mirrored character.
This is done by finding the ASCII value of 'a' plus the ASCII value of 'z', minus the ASCII value of char. 
This formula effectively mirrors the character around the midpoint of the alphabet.
Uppercase Letters:
Similarly, if char is an uppercase letter (between 'A' and 'Z'), use the same formula for mirroring.
Non-Letters:
If char is neither lowercase nor uppercase, it is added to mirrored_part without modification.

Result Construction:
Concatenate unchanged_part with mirrored_part to form the final result. Return the concatenated result.
'''