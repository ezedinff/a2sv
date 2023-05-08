from typing import List, Optional

'''
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        paths = []
        def backtrack(node, path):
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                backtrack(node.left, f'{path}->{node.left.val}')
            if node.right:
                backtrack(node.right, f'{path}->{node.right.val}')
        backtrack(root, str(root.val))
        return paths
