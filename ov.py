"""
In a Binary Search Tree (BST), the leftmost and rightmost nodes are defined by the following properties:

Leftmost Node:
The leftmost node is the node that has no left child and is reached by continuously traversing left from the root.
This node contains the minimum value in the BST.

Rightmost Node:
The rightmost node is the node that has no right child and is reached by continuously traversing right from the root.
This node contains the maximum value in the BST.
"""

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    # Function to find the minimum element (leftmost node) in the given BST.
    def minValue(self, root):
        if root is None:
            return None  # In case the tree is empty
        
        current = root
        while current.left is not None:
            current = current.left
        
        return current.data  # Return the value of the leftmost node
    
    # Function to find the maximum element (rightmost node) in the given BST.
    def maxValue(self, root):
        if root is None:
            return None  # In case the tree is empty
        
        current = root
        while current.right is not None:
            current = current.right
        
        return current.data  # Return the value of the rightmost node

# Example usage
# Creating a BST
root = Node(5)
root.left = Node(4)
root.right = Node(6)
root.left.left = Node(3)
root.left.left.left = Node(1)
root.right.right = Node(7)

sol = Solution()

# Finding the minimum value (leftmost node)
min_value = sol.minValue(root)
print(f"Minimum Value (Leftmost Node): {min_value}")  # Output: 1

# Finding the maximum value (rightmost node)
max_value = sol.maxValue(root)
print(f"Maximum Value (Rightmost Node): {max_value}")  # Output: 7


'''
Explanation:
minValue: This function traverses the left child nodes until it finds the leftmost node and returns its value.
maxValue: This function traverses the right child nodes until it finds the rightmost node and returns its value.

Example Outputs:
For the given BST, the leftmost node's value will be 1 (minimum value), and the rightmost node's value will be 7 (maximum value).
'''