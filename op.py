# O(n!) - Factorial Time

from itertools import permutations

def generate_permutations(arr):
    return list(permutations(arr))

# Test
arr = [1, 2, 3]
print(list(generate_permutations(arr)))
# Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]