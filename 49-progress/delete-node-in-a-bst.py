from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # to delete a node from a BST, we need to find the node first
        # then we need to find the node's successor (the smallest node in the right subtree)
        # then we need to replace the node with the successor
        # then we need to delete the successor
        # the successor can be found by finding the smallest node in the right subtree
        # the successor can also be found by finding the largest node in the left subtree

        if not root:
            return None
        
        if root.val == key:
            # if the node is a leaf node, just delete it
            if not root.left and not root.right:
                return None
            # if the node has only one child, return the child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # if the node has two children, find the successor
            # the successor can be found by finding the smallest node in the right subtree
            # the successor can also be found by finding the largest node in the left subtree
            # here we use the smallest node in the right subtree
            successor = root.right
            while successor.left:
                successor = successor.left
            # replace the node with the successor
            root.val = successor.val
            # delete the successor
            root.right = self.deleteNode(root.right, successor.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root