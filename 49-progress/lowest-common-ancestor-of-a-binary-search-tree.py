'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
'''

'''
To find the lowest common ancestor of two nodes in a binary search tree, we can use the property of a binary search tree
that the nodes to the left of a node have values less than the node's value, and the nodes to the right have values
greater than the node's value.

We start at the root node of the binary search tree, and compare the values of the two nodes
we want to find the lowest common ancestor of with the value of the current node. If the values
of the two nodes are both less than the value of the current node, we move to the left child of
the current node. If the values of the two nodes are both greater than the value of the current node,
we move to the right child of the current node. If one node is less than the value of the current node
and the other is greater, we have found the lowest common ancestor, which is the current node.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root