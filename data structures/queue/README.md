# Queue
is a data structure works in FIFO (First In First Out) order. It is a linear data structure which follows a particular order in which the operations are performed. The order may be First In First Out or Last In First Out.

## Types of Queue
There are two types of queue:
- Linear Queue
- Circular Queue

### Linear Queue
In a linear queue, the first element is removed first and the last element is removed at last. The insertion and deletion operations are performed at the two different ends of the queue. The insertion operation is performed at the rear end and the deletion operation is performed at the front end.
- simple queue implementation: [queue.py](./queue.py)
```python
class SimpleQueue:
    def __init__(self, size = 10):
        self.queue = []
        self.size = size
        self.front, self.rear = -1, -1
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return self.rear == self.size - 1
    
    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        if self.is_empty():
            self.front = 0
        self.rear += 1
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        self.front += 1
        if self.front > self.rear:
            self.front, self.rear = -1, -1
        return item
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]
    
    def __str__(self):
        return str(self.queue)
```
- priority queue (elements are sorted by priority)
- priorty queue applications:
    - scheduling jobs
    - implementing Dijkstra's algorithm
    - implementing Huffman coding
- question pattern to use priority queue are:
    - find the kth largest/smallest element
    - find the median
    - find the top k frequent elements
    - find the top k frequent words
    - find the top k frequent words with at least k characters
    - find the top k frequent words with at least k characters and no vowels
```python
import heapq
class PriorityQueue:
    def __init__(self, size = 10):
        self.queue = []
        self.size = size
        self.front, self.rear = -1, -1
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return self.rear == self.size - 1
    
    def enqueue(self, item, priority):
        if self.is_full():
            raise Exception("Queue is full")
        if self.is_empty():
            self.front = 0
        self.rear += 1
        heapq.heappush(self.queue, (priority, item))
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = heapq.heappop(self.queue)[1]
        self.front += 1
        if self.front > self.rear:
            self.front, self.rear = -1, -1
        return item
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front][1]
    
    def __str__(self):
        return str(self.queue)
```
- dequeue (double-ended queue, elements can be added and removed from both ends)
```python
from collections import deque
class DoubleEndedQueue:
    def __init__(self, size = 10):
        self.queue = deque()
        self.size = size
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == self.size
    
    def add_front(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue.appendleft(item)
    
    def add_rear(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue.append(item)
    
    def remove_front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.popleft()
    
    def remove_rear(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop()
    
    def peek_front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[0]
    
    def peek_rear(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[-1]
    
    def __str__(self):
        return str(self.queue)
```

### Circular Queue
In a circular queue, the last position is connected back to the first position to make a circle. It is also called ‘Ring Buffer’. In a circular queue, we can not insert the next element if the queue is full. For example, the queue size is 5, and we have inserted 5 elements in it, then when we try to insert the next element, the queue gets full. Here, an exception occurs.
- circular queue
```python
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        if self.is_full():
            print("Queue is Full")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def display(self):
        if (self.front == -1):
            print("Queue is Empty")
        elif (self.rear >= self.front):
            print("Elements in the circular queue are:",
                  end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            print("Elements in Circular Queue are:",
                  end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full")
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    def peek(self):
        return self.queue[self.front]
    
    def __str__(self):
        return str(self.queue)
```

## Applications
- CPU Scheduling
- Disk Scheduling
- Handling of interrupts in real-time systems
- Call Center phone systems use Queues to hold people calling them in an order, until a service representative is free.
- Handling of multiple requests at a single point, for example, a single printer, CPU task scheduling etc.

## [Priority Queue](priority-queue.py)
- a queue where each element has a priority
- the element with the highest priority is dequeued first
- if two elements have the same priority, they are dequeued according to their order in the queue

## [Circular Queue](circular-queue.py)
- a queue where the last position is connected back to the first position to make a circle
- it is also called ‘Ring Buffer’

## Questions
- [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
- [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
- [Design Circular Deque](https://leetcode.com/problems/design-circular-deque/)
- [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
- [Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/)


## Amazon Interview Questions
- [Amazon Interview Questions](https://www.geeksforgeeks.org/amazon-interview-experience-set-1-campus/)
    - 1. Given a string, find the first non-repeating character in it and return it’s index. If it doesn’t exist, return -1. 
    - 2. Given a string, find the length of the longest substring without repeating characters.
    - 3. Given a string, find the length of the longest substring T that contains at most k distinct characters.
    - 4. Given a string, find the length of the longest substring without repeating characters.