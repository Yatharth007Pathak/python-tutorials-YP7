"""
In Python, a deque (pronounced "deck") is a data structure from the collections module that stands for double-ended queue. 
Unlike regular lists, deques allow us to add and remove elements from both ends (left and right) efficiently.

Key features of a deque:
Fast appends and pops: O(1) time complexity for operations at both ends, unlike lists which have O(n) complexity for operations at the beginning.
Optimized for both ends: We can append or pop from either end of the deque (left or right).
Thread-safe: Deques support thread-safe, memory-efficient appends and pops.

Common Operations:
Appending elements:
append(x): Add x to the right end.
appendleft(x): Add x to the left end.
Removing elements: 
pop(): Remove and return the element from the right end.
popleft(): Remove and return the element from the left end.
Accessing elements: 
We can access elements by indexing, but this is slower (O(n)).
Rotation: 
rotate(n): Rotate the deque n steps to the right. If n is negative, rotate left.
"""

from collections import deque

# Create a deque
dq = deque([1, 2, 3])

# Append to the right
dq.append(4)  # deque([1, 2, 3, 4])

# Append to the left
dq.appendleft(0)  # deque([0, 1, 2, 3, 4])

# Pop from the right
dq.pop()  # deque([0, 1, 2, 3])

# Pop from the left
dq.popleft()  # deque([1, 2, 3])

# Rotate
dq.rotate(1)  # deque([3, 1, 2])

# Print final state of deque
print(dq)  # Output: deque([3, 1, 2])

'''
Here's what the output of the final state of the deque will look like: deque([3, 1, 2])

Explanation:
The initial deque starts as [1, 2, 3].
After dq.append(4), it becomes [1, 2, 3, 4].
After dq.appendleft(0), it becomes [0, 1, 2, 3, 4].
After dq.pop(), the last element (4) is removed, resulting in [0, 1, 2, 3].
After dq.popleft(), the first element (0) is removed, resulting in [1, 2, 3].
After dq.rotate(1), the deque is rotated right by one step, so it becomes [3, 1, 2].
'''