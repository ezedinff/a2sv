# Linked List
A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers as shown in the below image:

![Linked List](./linked-list.png)

## Types of Linked List
There are two types of linked list:
- Singly Linked List
- Doubly Linked List

### Singly Linked List
In a singly linked list, each node contains a data field and a reference(link) to the next node in the list. The last node contains a link to null. It is a data structure consisting of a group of nodes which together represent a sequence. Under the simplest form, each node is composed of data and a reference (in other words, a link) to the next node in the sequence. This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration. More complex variants add additional links, allowing more efficient insertion or removal of nodes at arbitrary positions. A drawback of linked lists is that access time is linear (and difficult to pipeline). Faster access, such as random access, is not feasible. Arrays have better cache locality as compared to linked lists.
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def delete(self, data):
        current = self.head
        if current.data == data:
            self.head = current.next
            return
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def sort(self):
        current = self.head
        index = None
        if current is None:
            return
        else:
            while current is not None:
                index = current.next
                while index is not None:
                    if current.data > index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next