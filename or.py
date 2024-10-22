"""
Selection sort is another simple comparison-based sorting algorithm. The basic idea is to divide the list into two parts: 
a sorted section and an unsorted section. The algorithm repeatedly selects the smallest 
(or largest, depending on the sorting order) element from the unsorted section and swaps it with the first element of the unsorted section. 
This process is repeated until the entire list is sorted.

Steps:
Start with the first element in the list.
Find the smallest element in the unsorted section of the list.
Swap the smallest element with the first element of the unsorted section.
Move the boundary between the sorted and unsorted sections one element to the right.
Repeat the process for the remaining unsorted section of the list.

Key Points:
Time Complexity: O(n²) for all cases (best, average, and worst), as it always iterates through the unsorted part to find the minimum element.
Space Complexity: O(1) because it performs the sort in place.
Stability: Selection sort is not stable. It can change the relative order of elements with equal values.
Although simple, selection sort is less efficient for large datasets compared to more advanced algorithms like merge sort or quicksort.
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the first element of the unsorted part is the smallest
        min_idx = i
        # Find the minimum element in the remaining unsorted array
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage:
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)

'''
Here is a detailed pointwise breakdown of each line in the selection_sort function:

def selection_sort(arr):
This defines a function named selection_sort that takes one argument arr, representing the array to be sorted.

n = len(arr)
The length of the array arr is calculated using the len() function and stored in the variable n.

for i in range(n):
A loop is initiated from i = 0 to i = n-1, where i represents the index of the element currently being placed in its correct sorted position.

min_idx = i
The variable min_idx is set to i, assuming that the element at index i is the smallest in the unsorted portion of the array.

for j in range(i+1, n):
This inner loop runs from i+1 to n-1, iterating through the unsorted part of the array to find the smallest element.

if arr[j] < arr[min_idx]:
A condition checks if the element at index j is smaller than the current smallest element (arr[min_idx]).

min_idx = j
If the condition is true, min_idx is updated to j, indicating that the element at index j is 
now considered the smallest in the unsorted part of the array.

arr[i], arr[min_idx] = arr[min_idx], arr[i]
After the inner loop completes, the smallest element found is swapped with the element at index i. 
This ensures that the smallest element is placed in the correct position in the sorted part of the array.

return arr
The function returns the sorted array.

arr = [64, 25, 12, 22, 11]
An example unsorted array is defined with the elements [64, 25, 12, 22, 11].

sorted_arr = selection_sort(arr)
The selection_sort function is called with arr as the argument, and the sorted array is stored in the variable sorted_arr.

print("Sorted array:", sorted_arr)
This line prints the sorted array with the label "Sorted array:" followed by the contents of sorted_arr.
'''