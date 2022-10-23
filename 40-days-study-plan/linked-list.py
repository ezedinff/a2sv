class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# remove duplicates from an unsorted linked list

class Solution:
    def removeDuplicates(self, head):
        if head is None:
            return None
        current = head
        while current is not None:
            runner = current
            while runner.next is not None:
                if runner.next.val == current.val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
        return head
    # technique: two pointers
    # time complexity: O(n^2)
    # space complexity: O(1)
    # step 1: check if the head is None
    # step 2: initialize a current pointer
    # step 3: iterate through the linked list
    # step 4: initialize a runner pointer
    # step 5: iterate through the linked list
    # step 6: check if the next node's value is the same as the current node's value
    # step 7: if it is, delete the next node
    # step 8: if it is not, move the runner pointer to the next node
    # step 9: move the current pointer to the next node

# using a hash table
class Solution:
    def removeDuplicates(self, head):
        if head is None:
            return None
        current = head
        seen = set()
        seen.add(current.val)
        while current.next is not None:
            if current.next.val in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.val)
                current = current.next
        return head
    # technique: hash table
    # time complexity: O(n)
    # space complexity: O(n)
    # step 1: check if the head is None
    # step 2: initialize a current pointer
    # step 3: initialize a hash table
    # step 4: add the current node's value to the hash table
    # step 5: iterate through the linked list
    # step 6: check if the next node's value is in the hash table
    # step 7: if it is, delete the next node
    # step 8: if it is not, add the next node's value to the hash table
    # step 9: move the current pointer to the next node


# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
class Solution:
    def kthToLast(self, head, k):
        if head is None:
            return None
        current = head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        current = head
        for i in range(length - k):
            current = current.next
        return current.val
    # technique: two pointers
    # time complexity: O(n)
    # space complexity: O(1)
    # step 1: check if the head is None
    # step 2: initialize a current pointer
    # step 3: initialize a length variable
    # step 4: iterate through the linked list
    # step 5: increment the length variable
    # step 6: move the current pointer to the next node
    # step 7: initialize a current pointer
    # step 8: iterate through the linked list
    # step 9: move the current pointer to the next node
    # step 10: return the current node's value

# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
class Solution:
    def deleteMiddle(self, head):
        if head.next is None:
            return None
        slow, fast = head, head.next.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
    # technique: two pointers
    # time complexity: O(n)
    # space complexity: O(1)
    # step 1: check if the head is the only node
    # step 2: initialize two pointers, slow and fast
    # step 3: iterate through the linked list
    # step 4: move the slow pointer one node at a time
    # step 5: move the fast pointer two nodes at a time
    # step 6: delete the next node
    # step 7: return the head


# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
class Solution:
    def partition(self, head, x):
        if head is None:
            return None
        current = head
        left = []
        right = []
        while current is not None:
            if current.val < x:
                left.append(current.val)
            else:
                right.append(current.val)
            current = current.next
        current = head
        for val in left + right:
            current.val = val
            current = current.next
        return head
    # technique: two arrays
    # time complexity: O(n)
    # space complexity: O(n)
    # step 1: check if the head is None
    # step 2: initialize a current pointer
    # step 3: initialize two arrays, left and right
    # step 4: iterate through the linked list
    # step 5: if the current node's value is less than x, append it to the left array
    # step 6: if the current node's value is greater than or equal to x, append it to the right array
    # step 7: move the current pointer to the next node
    # step 8: initialize a current pointer
    # step 9: iterate through the linked list
    # step 10: set the current node's value to the left array and right array
    # step 11: move the current pointer to the next node
    # step 12: return the head

# Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
class Solution:
    def sumLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        current1 = l1
        current2 = l2
        carry = 0
        head = ListNode(0)
        current = head
        while current1 is not None or current2 is not None:
            if current1 is None:
                current1 = ListNode(0)
            if current2 is None:
                current2 = ListNode(0)
            sum = current1.val + current2.val + carry
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            current1 = current1.next
            current2 = current2.next
        if carry > 0:
            current.next = ListNode(carry)
        return head.next
    # technique: two pointers
    # time complexity: O(n)
    # space complexity: O(1)
    # step 1: check if l1 is None
    # step 2: check if l2 is None
    # step 3: initialize two current pointers
    # step 4: initialize a carry variable
    # step 5: initialize a head node
    # step 6: initialize a current pointer
    # step 7: iterate through the linked lists
    # step 8: check if l1 is None
    # step 9: if it is, set it to a node with a value of 0
    # step 10: check if l2 is None
    # step 11: if it is, set it to a node with a value of 0
    # step 12: initialize a sum variable
    # step 13: set the sum variable to the sum of the current nodes' values and the carry variable
    # step 14: set the carry variable to the sum divided by 10
    # step 15: set the next node to a node with a value of the sum modulus 10
    # step 16: move the current pointer to the next node
    # step 17: move the l1 pointer to the next node
    # step 18: move the l2 pointer to the next node
    # step 19: check if the carry variable is greater than

# Palindrome: Implement a function to check if a linked list is a palindrome.
class Solution:
    def isPalindrome(self, head):
        if head is None:
            return True
        current = head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        current = head
        for i in range(length // 2):
            current = current.next
        if length % 2 == 1:
            current = current.next
        stack = []
        while current is not None:
            stack.append(current.val)
            current = current.next
        current = head
        for i in range(length // 2):
            if current.val != stack.pop():
                return False
            current = current.next
        return True
    # technique: two pointers and a stack
    # time complexity: O(n)
    # space complexity: O(n)
    # step 1: check if the head is None
    # step 2: initialize a current pointer
    # step 3: initialize a length variable
    # step 4: iterate through the linked list
    # step 5: increment the length variable
    # step 6: move the current pointer to the next node
    # step 7: initialize a current pointer
    # step 8: iterate through the linked list
    # step 9: move the current pointer to the next node
    # step 10: initialize a stack
    # step 11: iterate through the linked list
    # step 12: append the current node's value to the stack
    # step 13: move the current pointer to the next node
    # step 14: initialize a current pointer
    # step 15: iterate through the linked list
    # step 16: check if the current node's value is not equal to the stack's pop
    # step 17: move the current pointer to the next node
    # step 18: return True