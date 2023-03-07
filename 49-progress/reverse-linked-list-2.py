# Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/
#
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # create a dummy node
        # create a prev node
        # create a curr node
        # create a next node
        # create a count
        # traverse the list
        # if count < left, move prev and curr forward
        # if count == left, set prev.next to None
        # if count > left and count <= right, reverse the list
        # if count == right + 1, set prev.next to curr
        # set prev to next
        # set curr to next
        # set count to count + 1
        # return dummy.next
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        count = 1
        while curr:
            if count < left:
                prev = curr
                curr = curr.next
            elif count == left:
                prev.next = None
            elif count > left and count <= right:
                nxt = curr.next
                curr.next = prev.next
                prev.next = curr
                curr = nxt
            elif count == right + 1:
                prev.next.next = curr
                prev.next = prev.next.next
                break
            count += 1
        return dummy.next