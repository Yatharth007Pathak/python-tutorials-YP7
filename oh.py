"""
Binary search is an efficient algorithm to find the position of a target value in a sorted array. 
It works by repeatedly dividing the search interval in half. If the target value is less than the middle element, 
the search continues in the left half; if it is greater, the search continues in the right half.

Steps:
Find the middle element of the array.
If the middle element equals the target, return its index.
If the target is less than the middle element, repeat the search on the left half.
If the target is greater, repeat the search on the right half.
The process continues until the target is found or the interval is empty.

Time Complexity:
Best case: O(1) (if the target is the middle element).
Worst case: O(log n) (where n is the length of the array, as the array is halved with each iteration).
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    
    return -1  # Target not found

# Example usage
arr = [1, 2, 4, 7, 9, 12, 15]
target = 7

result = binary_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

'''
Here's a breakdown of the binary search code line by line:

Function Definition (def binary_search(arr, target):): 
The function binary_search is defined with two parameters: arr (a sorted array) and target (the element to search for).

Initialize Variables (left, right = 0, len(arr) - 1): 
The variables left and right are initialized to represent the indices of the first and last elements of the array. 
left starts at 0 (the first index), and right starts at len(arr) - 1 (the last index).

While Loop (while left <= right:): A while loop runs as long as the left index is less than or equal to the right index. 
This loop will keep narrowing down the search range.

Calculate Midpoint (mid = (left + right) // 2): Inside the loop, the midpoint (mid) of the current search range is calculated. 
This is done by averaging the left and right indices and performing integer division to get an index.

Condition 1 (if arr[mid] == target:): The first condition checks if the middle element (arr[mid]) is equal to the target. 
If a match is found, the function returns the index mid.

Condition 2 (elif arr[mid] < target:): If the middle element is less than the target, it means the target is in the right half of the array. 
Therefore, the left index is updated to mid + 1 to narrow the search range to the right half.

Condition 3 (else:): If the middle element is greater than the target, the target must be in the left half of the array. 
The right index is updated to mid - 1 to narrow the search to the left half.

Return -1 (return -1): If the loop completes without finding the target (i.e., left becomes greater than right), 
the function returns -1 to indicate that the target was not found.

Example Usage (arr = [1, 2, 4, 7, 9, 12, 15]): An example sorted array arr is created with seven elements. 
The variable target is set to 7, which is the element we want to search for.

Function Call (result = binary_search(arr, target)): The binary_search function is called with arr and target as inputs. 
The result (either the index of the element or -1) is stored in the variable result.

If Condition (if result != -1:): This checks if the result is not -1. 
If the target was found, the program prints a message indicating the index of the element.

Print Statement (print(f"Element found at index {result}")): If the target is found, this line prints the index where the element was located.

Else Block (else: print("Element not found")): If the target was not found (i.e., result is -1), this block prints "Element not found".
'''