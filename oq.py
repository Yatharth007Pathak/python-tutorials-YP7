"""
Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, 
and swaps them if they are in the wrong order. The process is repeated until the list is sorted.
Here's how it works:

Start at the beginning of the list.
Compare the first two elements. If the first is greater than the second, swap them.
Move to the next pair and repeat the process for each subsequent pair of elements in the list.
After completing one pass through the list, the largest element is "bubbled" to its correct position at the end.
The algorithm then repeats the process for the rest of the list (ignoring the last element each time).
This process continues until no swaps are needed, indicating that the list is sorted.

Key points:
Time Complexity: O(n²) in the worst and average case, making it inefficient for large datasets.
Space Complexity: O(1), as it sorts the array in place.
Stability: Bubble sort is a stable sorting algorithm, meaning it preserves the relative order of equal elements.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swapping happens
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, break
        if not swapped:
            break
    return arr

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)

'''
Here is a pointwise breakdown of each line of the code:

def bubble_sort(arr): 
This line defines a function named bubble_sort that takes one argument, arr, which is the array to be sorted.

n = len(arr)
The length of the array arr is calculated using the len() function and stored in the variable n.

for i in range(n):
This starts a loop that runs from i = 0 to i = n-1. This outer loop controls the number of passes required over the array.

swapped = False
A flag swapped is set to False at the beginning of each pass to track whether any elements are swapped in the current iteration.

for j in range(0, n-i-1):
This inner loop iterates over the array from the first element to n-i-2, comparing each pair of adjacent elements. 
The range decreases by 1 with each pass as the largest elements "bubble up" to the end of the array.

if arr[j] > arr[j+1]:
This condition checks if the current element (arr[j]) is greater than the next element (arr[j+1]).

arr[j], arr[j+1] = arr[j+1], arr[j]
If the above condition is true, the two adjacent elements are swapped. 
This is done using tuple unpacking to switch the positions of arr[j] and arr[j+1].

swapped = True
After a swap, the flag swapped is set to True, indicating that at least one swap has occurred during this pass.

if not swapped:
After the inner loop completes, this condition checks if no elements were swapped during the current pass (i.e., swapped is still False).

break
If no elements were swapped, the outer loop breaks early, as the array is already sorted and no further passes are needed.

return arr
The function returns the sorted array.

arr = [64, 34, 25, 12, 22, 11, 90]
An example unsorted array is defined with the elements [64, 34, 25, 12, 22, 11, 90].

sorted_arr = bubble_sort(arr)
The bubble_sort function is called with arr as the argument, and the sorted array is stored in the variable sorted_arr.

print("Sorted array:", sorted_arr)
This line prints the sorted array with the label "Sorted array:" followed by the contents of sorted_arr.
'''