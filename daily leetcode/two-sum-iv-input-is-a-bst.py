# Two sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
#

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def dfs(root, k, seen):
            if not root:
                return False
            if k - root.val in seen:
                return True
            seen.add(root.val)
            return dfs(root.left, k, seen) or dfs(root.right, k, seen)
        return dfs(root, k, set())