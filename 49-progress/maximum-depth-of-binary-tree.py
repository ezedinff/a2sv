from typing import Optional
'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        # Recursive case
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))