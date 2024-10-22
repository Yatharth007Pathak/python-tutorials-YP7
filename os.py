"""
Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. 
It is much like sorting playing cards in your hand - you pick one card and insert it in the right position relative to the already sorted cards.

Steps:
Start with the second element (as the first element is considered sorted).
Compare the current element with the elements in the sorted section (to the left).
Shift all larger elements one position to the right to make room for the current element.
Insert the current element in its correct position.
Repeat the process for all remaining elements.

Key Points:
Time Complexity: O(n²) in the worst and average cases (when the array is sorted in reverse). 
However, in the best case (when the array is already sorted), it performs only O(n) operations.
Space Complexity: O(1), as it sorts the array in place.
Stability: Insertion sort is a stable sorting algorithm, meaning it preserves the relative order of equal elements.
Best Use Cases:
Insertion sort is efficient for small datasets or partially sorted datasets.
"""

def insertion_sort(arr):
    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be positioned
        j = i - 1
        # Move elements that are greater than key to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert key at the right position
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)

'''
Here is a pointwise breakdown of each line in the insertion_sort function:

def insertion_sort(arr):
This defines a function called insertion_sort that takes one argument arr, which is the array to be sorted.

for i in range(1, len(arr)):
This loop starts at the second element (i = 1) and iterates over the array until the last element. It moves from left to right, 
placing each element in its correct position relative to the sorted part of the array (the part to the left of the current element).

key = arr[i]
The current element at index i is stored in variable key. This is the element that needs to be inserted into the sorted portion of the array.

j = i - 1
The variable j is initialized to the index just before i, representing the last element in the already sorted part of the array.

while j >= 0 and key < arr[j]:
This while loop continues as long as j is greater than or equal to 0 and the key is smaller than arr[j]. 
It checks whether the key needs to be moved back further to find the correct position in the sorted part.

arr[j + 1] = arr[j]
Inside the while loop, if the current element (arr[j]) is greater than key, it is shifted one position to the right (i.e., arr[j + 1]).

j -= 1
The index j is decremented to continue checking the previous element in the sorted part of the array.

arr[j + 1] = key
Once the correct position is found, the key is placed at the position j + 1, ensuring that the sorted portion of the array is maintained.

return arr
The function returns the sorted array.

arr = [12, 11, 13, 5, 6]
An example unsorted array is defined with the elements [12, 11, 13, 5, 6].

sorted_arr = insertion_sort(arr)
The insertion_sort function is called with arr as the argument, and the sorted array is stored in the variable sorted_arr.

print("Sorted array:", sorted_arr)
This line prints the sorted array with the label "Sorted array:" followed by the contents of sorted_arr.
'''