class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        current = head
        while current is not None:
            next = current.next
            prev = dummy
            while prev.next is not None and prev.next.val < current.val:
                prev = prev.next
            current.next = prev.next
            prev.next = current
            current = next
        return dummy.next

    def print_list(self, head: ListNode) -> None:
        current = head
        while current is not None:
            print(current.val, end=' ')
            current = current.next
        print()

if __name__ == "__main__":
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    result = Solution().insertionSortList(head)
    printList = []
    expected = [1,2,3,4]
    while result is not None:
        printList.append(result.val)
        result = result.next
    
    assert printList == expected, (printList, expected)
