import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, tree: TreeNode) -> int:
        self.goodNodes = 0
        self.dfs(tree, tree.val)
        return self.goodNodes

    def dfs(self, node: TreeNode, maxVal: int):
        if node:
            if node.val >= maxVal:
                self.goodNodes += 1
                maxVal = node.val
            self.dfs(node.left, maxVal)
            self.dfs(node.right, maxVal)


class TestSolution(unittest.TestCase):
    def test_goodNodes(self):
        tree = TreeNode(3, TreeNode(1, TreeNode(3), TreeNode(2)), TreeNode(4, TreeNode(1), TreeNode(5)))
        self.assertEqual(Solution().goodNodes(tree), 4)


if __name__ == '__main__':
    unittest.main()