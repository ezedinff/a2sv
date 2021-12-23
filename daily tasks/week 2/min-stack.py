class MinStack:

    def __init__(self):
        self.storage = []

    def push(self, val: int) -> None:
        self.storage.append(val)

    def pop(self) -> None:
        if len(self.storage):
            self.storage.pop()

    def top(self) -> int:
        return self.storage[-1]

    def getMin(self) -> int:
        return min(self.storage)
