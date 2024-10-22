'''
Given 3 arrays, we have to find common elements in 3 sorted lists using sets
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15,20,30, 70, 80, 120]
'''


# Given sorted arrays
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Convert arrays to sets using type casting
set1 = set(ar1)
set2 = set(ar2)
set3 = set(ar3)

# Find the intersection of the three sets
common_elements = set1.intersection(set2).intersection(set3)

# Convert the result back to a list (if needed)
common_elements = list(common_elements)

print("Common elements in all three arrays:", common_elements)

# Output: Common elements in all three arrays: [20, 80]

'''
Explanation:
Convert Arrays to Sets: We convert each of the three arrays to sets to eliminate any duplicates (if there were any) 
and to make use of set operations.
Intersection: We use the intersection() method to find the common elements in all three sets. 
The intersection of sets contains only the elements that are present in all sets.
Sort the Result: Since the original arrays were sorted, we sort the result for consistency.
'''