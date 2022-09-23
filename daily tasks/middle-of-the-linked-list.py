class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        current = head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        current = head
        for i in range(length // 2):
            current = current.next
        return current


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = Solution().middleNode(head)
    printList = []
    expected = [3,4,5]
    while result is not None:
        printList.append(result.val)
        result = result.next
    
    assert printList == expected, (printList, expected)