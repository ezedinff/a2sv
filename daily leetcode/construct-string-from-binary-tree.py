#  Construct String from Binary Tree
'''
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        if not root.left and not root.right:
            return str(root.val)
        if not root.right:
            return str(root.val) + '(' + self.tree2str(root.left) + ')'
        return str(root.val) + '(' + self.tree2str(root.left) + ')(' + self.tree2str(root.right) + ')'