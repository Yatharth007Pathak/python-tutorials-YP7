# Find Maximum Value in a List

def find_max(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

lst = input("Enter lst: ")
print(find_max(lst))

'''
Here's a detailed explanation of the code:

def find_max(lst): defines a function named find_max that takes a single parameter lst, which is expected to be a list.

if not lst: checks if the list lst is empty. If it is, the function returns None because there is no maximum value in an empty list.

max_val = lst[0] initializes max_val with the first element of the list. 
This value will be used to compare against other elements to find the maximum.

for num in lst: starts a loop that iterates over each element in the list.

if num > max_val: checks if the current element num is greater than the current max_val.

max_val = num updates max_val to be the current element num if it is larger.

return max_val returns the maximum value found in the list.

lst = input("Enter lst: ") prompts the user to enter a list. 
However, this will actually capture the input as a string. For the function to work correctly, the user input should be parsed into a list.

print(find_max(lst)) calls the find_max function with the user-provided lst and prints the maximum value.
'''