from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in order traversal
        def backtrack(node, prev):
            if not node:
                return True
            if not backtrack(node.left, prev):
                return False
            if prev[0] and node.val <= prev[0].val:
                return False
            prev[0] = node
            return backtrack(node.right, prev)
        return backtrack(root, [None])