from typing import Optional
from data_structures import TreeNode
'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = True
        if p and q:
            ans = p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif p or q:
            ans = False
        return ans