# binary tree inorder traversal
# Source: https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        results = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            results.append(node.val)
            helper(node.right)
        helper(root)
        return results