class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # create a list
        # traverse the list
        # add values to the list
        # compare the list to the reversed list
        # return True if they are the same
        # return False if they are not
        if not head:
            return True
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst == lst[::-1]
    
    # other solution
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     # find the middle of the list
    #     # reverse the second half of the list
    #     # compare the first half of the list to the second half of the list
    #     # return True if they are the same
    #     # return False if they are not
    #     if not head:
    #         return True
    #     slow = head
    #     fast = head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #     prev = None
    #     while slow:
    #         nxt = slow.next
    #         slow.next = prev
    #         prev = slow
    #         slow = nxt
    #     while prev:
    #         if prev.val != head.val:
    #             return False
    #         prev = prev.next
    #         head = head.next
    #     return True