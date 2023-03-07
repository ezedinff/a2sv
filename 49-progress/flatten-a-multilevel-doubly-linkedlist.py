class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        curr = head
        while curr:
            if curr.child:
                next = curr.next
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
                while curr.next:
                    curr = curr.next
                curr.next = next
                if next:
                    next.prev = curr
            curr = curr.next
        return head
    
    # using stack
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        stack = [head]
        prev = None
        while stack:
            curr = stack.pop()
            if prev:
                prev.next = curr
                curr.prev = prev
            prev = curr
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
        return head