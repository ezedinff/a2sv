from typing import List
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            if root.val == targetSum:
                return [[root.val]]
            else:
                return []
        left = self.pathSum(root.left, targetSum - root.val)
        right = self.pathSum(root.right, targetSum - root.val)
        return [[root.val] + path for path in left + right]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_pathSum(self):
        s = self.s
        root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
        targetSum = 22
        result = s.pathSum(root, targetSum)
        expected = [[5, 4, 11, 2], [5, 8, 4, 5]]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()