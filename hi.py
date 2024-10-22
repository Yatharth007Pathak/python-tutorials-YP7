# Remove Duplicates from a List

def remove_duplicates(lst):
    return list(set(lst))

lst = input("Enter lst: ")
print(remove_duplicates(lst))


'''
Here is an explanation of the code:

def remove_duplicates(lst): defines a function named remove_duplicates that takes a single parameter lst, which is expected to be a list.

return list(set(lst)) converts the list lst into a set using set(lst). 
This removes any duplicate elements, as sets do not allow duplicates. 
Then, list(set(lst)) converts the set back into a list, effectively giving a list with duplicates removed.

lst = input("Enter lst: ") prompts the user to enter a list. However, this input is captured as a string.

print(remove_duplicates(lst)) calls the remove_duplicates function with the user-provided lst and prints the result.
'''