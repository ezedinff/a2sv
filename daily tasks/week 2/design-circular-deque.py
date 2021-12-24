class MyCircularDeque:

    def __init__(self, k: int):
        self.storage = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.storage = [value] + self.storage
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.storage = self.storage + [value]
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.storage.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.storage.pop()
            return True
        return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.storage[0]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.storage[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.storage) == 0

    def isFull(self) -> bool:
        return len(self.storage) == self.k

