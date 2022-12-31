from typing import Optional

class ListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class Solution:
    def pair_sum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        res = 0
        while slow:
            res = max(res, slow.val + stack.pop())
            slow = slow.next
        return res

# explaination
# defiine two pointers, slow and fast
# slow moves one step at a time, fast moves two steps at a time
# when fast reaches the end, slow is at the middle
# push the values of the first half of the linked list into a stack
# if the length of the linked list is odd, skip the middle node
# pop the values from the stack and compare with the second half of the linked list
# return the maximum sum of the two values