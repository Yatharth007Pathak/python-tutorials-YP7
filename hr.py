'''
Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. 
It is much less efficient on large lists than more advanced algorithms like quicksort, heapsort, or merge sort. 
However, it has the advantage of being more efficient for small lists or when adding a few elements to a mostly sorted list.
'''

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
# Example usage
print(insertion_sort([64, 34, 25, 12, 22, 11, 90]))  # Output: [11, 12, 22, 25, 34, 64, 90]

'''
Here's a detailed explanation of the bubble sort algorithm code:

def bubble_sort(arr): defines a function named bubble_sort that takes a single parameter arr, which is a list of numbers to be sorted.

n = len(arr) calculates the length of the list arr and stores it in the variable n.

for i in range(n): starts a loop that iterates n times. Each iteration represents a pass through the list, 
ensuring that the largest unsorted element "bubbles up" to its correct position.

for j in range(0, n-i-1): starts a nested loop that iterates through the unsorted portion of the list. 
The range is 0 to n-i-1 because after each pass, the last i elements are already sorted.

if arr[j] > arr[j+1]: checks if the current element arr[j] is greater than the next element arr[j+1]. 
If so, the elements are out of order and need to be swapped.

arr[j], arr[j+1] = arr[j+1], arr[j] swaps the elements arr[j] and arr[j+1] to put the larger element further down the list.

return arr returns the sorted list after all passes are complete.

print(bubble_sort([64, 34, 25, 12, 22, 11, 90])) calls the bubble_sort function with a sample list and prints the sorted result. 
The output will be [11, 12, 22, 25, 34, 64, 90].
'''