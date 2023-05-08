# https://leetcode.com/problems/maximum-width-of-binary-tree/
from typing import Optional
from data_structures import TreeNode

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [(root, 0)]
        ans = 1
        while queue:
            ans = max(ans, queue[-1][1] - queue[0][1] + 1)
            new_queue = []
            for node, index in queue:
                for i, child in enumerate((node.left, node.right)):
                    if child:
                        new_queue.append((child, index * 2 + i))
            queue = new_queue
        return ans