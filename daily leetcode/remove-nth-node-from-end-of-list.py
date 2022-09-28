# Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# algorithm: linked list
# topics: linked list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return None
        else:
            # find the length of the list
            length = 0
            node = head
            while node:
                length += 1
                node = node.next
            # find the node to delete
            node = head
            for i in range(length - n - 1):
                node = node.next
            if length == n:
                return head.next
            else:
                node.next = node.next.next
                return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    n = 2
    print(Solution().removeNthFromEnd(head, n))