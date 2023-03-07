from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Given the head of a linked list and a value x, partition it such that all nodes
less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
'''
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # create two lists
        # traverse the list
        # if value < x, add to first list
        # if value >= x, add to second list
        # join the two lists
        # return the first list
        if not head:
            return head
        first = ListNode()
        second = ListNode()
        first_head = first
        second_head = second
        while head:
            if head.val < x:
                first.next = head
                first = first.next
            else:
                second.next = head
                second = second.next
            head = head.next
        second.next = None
        first.next = second_head.next
        return first_head.next