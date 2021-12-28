class MonotonicStack:
    def __init__(self):
        self.storage = []

    def isEmpty(self) -> bool:
        return len(self.storage) == 0

    def push(self, value):
        while not self.isEmpty() and self.storage[-1] < value:
            self.storage.pop()
        self.storage.append(value)
