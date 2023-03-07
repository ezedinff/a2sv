# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        if k == 1:
            return head
        current = head
        for i in range(k):
            if current is None:
                return head
            current = current.next
        current = head
        for i in range(k - 1):
            next = current.next
            current.next = next.next
            next.next = head
            head = next
        current.next = self.reverseKGroup(current.next, k)
        return head