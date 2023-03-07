class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # create a set
        # traverse headA
        # add each node to the set
        # traverse headB
        # if node in set, return node
        # return None
        nodes = set()
        while headA:
            nodes.add(headA)
            headA = headA.next
        while headB:
            if headB in nodes:
                return headB
            headB = headB.next
        return None
    
    # using o(1) space
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # create a currA node
        # create a currB node
        # traverse headA
        # traverse headB
        # if currA == currB, return currA
        # if currA is None, set currA to headB
        # if currB is None, set cur rB to headA
        # return None
        currA = headA
        currB = headB
        while currA != currB:
            if currA is None:
                currA = headB
            else:
                currA = currA.next
            if currB is None:
                currB = headA
            else:
                currB = currB.next
        return currA