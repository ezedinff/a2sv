# Delete node in a linked list
# https://leetcode.com/problems/delete-node-in-a-linked-list/
# algorithm: linked list
# topics: linked list

# technique: copy the value of the next node to the current node and delete the next node
# time complexity: O(1)
# space complexity: O(1)

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
