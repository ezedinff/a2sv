import unittest
from typing import Optional, List

# @author: Ezedin

# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [(root, 0, 0)]
        res = {}

        while queue:
            new_queue = []
            for node, row, col in queue:
                if col not in res:
                    res[col] = {}

                if row not in res[col]:
                    res[col][row] = []

                res[col][row].append(node.val)

                if node.left:
                    new_queue.append((node.left, row + 1, col - 1))

                if node.right:
                    new_queue.append((node.right, row + 1, col + 1))

            queue = new_queue

        res = [res[col] for col in sorted(res.keys())]
        res = [[val for row in sorted(col.keys()) for val in sorted(col[row])] for col in res]

        return res



class TestSolution(unittest.TestCase):
    def test_verticalTraversal(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(Solution().verticalTraversal(root), [[9], [3, 15], [20], [7]])

    def test_verticalTraversal_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(Solution().verticalTraversal(root), [[4], [2], [1, 5, 6], [3], [7]])


if __name__ == '__main__':
    unittest.main()
