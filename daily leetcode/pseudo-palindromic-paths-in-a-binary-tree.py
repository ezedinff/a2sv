'''
Pseudo-Palindromic Paths in a Binary Tree

Given a binary tree where node values are digits from 1 to 9.
A path in the binary tree is said to be pseudo-palindromic if at least
one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0
            path ^= 1 << node.val
            if not node.left and not node.right:
                return int(path & (path - 1) == 0)
            return dfs(node.left, path) + dfs(node.right, path)
        return dfs(root, 0)

if __name__ == "__main__":
    root = [2,3,1,3,1,None,1]
    tree = TreeNode(root[0])
    tree.left = TreeNode(root[1])
    tree.right = TreeNode(root[2])
    tree.left.left = TreeNode(root[3])
    tree.left.right = TreeNode(root[4])
    tree.right.right = TreeNode(root[6])
    print(Solution().pseudoPalindromicPaths(tree))
