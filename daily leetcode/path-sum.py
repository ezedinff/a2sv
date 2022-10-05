# Path Sum
# https://leetcode.com/problems/path-sum/

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

if __name__ == "__main__":
    s = "()"
    solution = Solution()
    print(solution.isValid(s))