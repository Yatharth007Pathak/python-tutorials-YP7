"""
Linear search is a simple algorithm used to find the position of a target value within an array or list. 
It checks each element in the list one by one until the target value is found or the list ends.

Time Complexity:
Best case: O(1) (if the target is found at the first position).
Worst case: O(n) (if the target is not found or at the last position, where n is the length of the array).
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage
arr = [4, 2, 7, 1, 9]
target = 7

result = linear_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

'''
Here's a breakdown of the code:

Function Definition (def linear_search(arr, target):): The function linear_search is defined, 
taking two arguments: arr (the array to search) and target (the element to find in the array).

For Loop (for i in range(len(arr)):): A for loop is initiated that iterates through the array arr. 
The variable i acts as an index, and the loop will run from 0 to the length of the array minus one.

Condition Check (if arr[i] == target:): Inside the loop, it checks if the current element (arr[i]) is equal to the target. 
If a match is found, the block under this condition will execute.

Return Index (return i): If the target element is found, the function returns the index i of the element where the match occurred. 
This effectively exits the function.

Return -1 (return -1): If the loop completes without finding the target, 
the function returns -1 to indicate that the element was not found in the array.

Example Usage (arr = [4, 2, 7, 1, 9]): A sample array arr is created, containing five integer elements. 
The variable target is set to 7, which is the element we want to search for.

Function Call (result = linear_search(arr, target)): The linear_search function is called with arr and target as inputs. 
The result of the search (either the index of the element or -1) is stored in the variable result.

If Condition (if result != -1:): This checks if the result is not equal to -1. 
If the target was found, the program proceeds to print a message stating the element was found along with its index.

Print Statement (print(f"Element found at index {result}")): 
If the target is found, this line prints a formatted message showing the index at which the element was located.

Else Block (else: print("Element not found")): If the target was not found (i.e., the result is -1), this block prints "Element not found".
'''