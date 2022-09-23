# Reverse Linked List

# https://leetcode.com/problems/reverse-linked-list/

'''
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        current = head
        while current.next is not None:
            next = current.next
            current.next = next.next
            next.next = head
            head = next
        return head