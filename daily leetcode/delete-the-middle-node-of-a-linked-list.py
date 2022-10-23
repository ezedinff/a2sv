# Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# algorithm: linked list
# topics: linked list

# technique: copy the value of the next node to the current node and delete the next node
# time complexity: O(1)
# space complexity: O(1)

class Solution:
    def deleteMiddle(self, head):
        if head.next is None:
            return None
        slow, fast = head, head.next.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
    # technique: two pointers
    # time complexity: O(n)
    # space complexity: O(1)
    # step 1: check if the head is the only node
    # step 2: initialize two pointers, slow and fast
    # step 3: iterate through the linked list
    # step 4: move the slow pointer one node at a time
    # step 5: move the fast pointer two nodes at a time

