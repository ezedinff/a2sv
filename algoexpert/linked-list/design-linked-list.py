class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index: int) -> int:
        # get item at index
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        curr = Node(val)
        curr.next = self.head
        self.head = curr
        if self.size == 0:
            self.tail = curr
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        curr = Node(val)
        if self.size == 0:
            self.head = curr
        else:
            self.tail.next = curr
        self.tail = curr
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        curr = Node(val)
        if index <= 0:
            curr.next = self.head
            self.head = curr
            if self.size == 0:
                self.tail = curr
        elif index == self.size:
            self.tail.next = curr
            self.tail = curr
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            curr.next = prev.next
            prev.next = curr
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            if index == self.size - 1:
                self.tail = prev
            prev.next = prev.next.next
        self.size -= 1
        
