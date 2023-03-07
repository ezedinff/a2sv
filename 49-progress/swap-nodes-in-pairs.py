class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp = self.swapPairs(head.next.next)
        new_head = head.next
        new_head.next = head
        head.next = temp
        return new_head
