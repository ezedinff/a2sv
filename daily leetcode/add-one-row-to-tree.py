# Add One Row to Tree
# https://leetcode.com/problems/add-one-row-to-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v, root)
        if d == 2:
            root.left = TreeNode(v, root.left)
            root.right = TreeNode(v, None, root.right)
            return root
        if root.left:
            self.addOneRow(root.left, v, d - 1)
        if root.right:
            self.addOneRow(root.right, v, d - 1)
        return root